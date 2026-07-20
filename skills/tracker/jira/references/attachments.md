# Jira attachments and transcript handling

Use for large durable artifacts, especially session transcripts. Attachments belong on the work item, not in comment bodies or PR comments.

## Render a session transcript

Render the whole transcript tree (main plus every nested subagent) from the on-disk JSONL rather than running `/export` by hand:

```bash
python ${CLAUDE_PLUGIN_ROOT}/scripts/session_usage.py export \
  --session-id "$SESSION_ID" \
  --task "$KEY" \
  --output .scratch/$KEY-$KIND-transcript-$(date -u +%Y%m%d%H%M).txt
```

`$SESSION_ID` is the current session id; `$KIND` is `ship`, `spec`, or `plan`. The renderer truncates bulky tool output and strips raw-JSONL noise, so the file stays audit-readable. Prefer running the render, scan, and upload from a delegate so the rendered text never enters the caller's context; when that delegation is denied under auto-mode, running them inline via direct Bash is a permitted fallback, provided the rendered transcript is still never read back into the caller's context. Run it as late as the session allows so the captured tail is maximal. `/ship` attaches on the `full` process tier; `/spec` and `/plan` attach every run, to the Task and the Epic respectively.

## Secret scan before upload

1. Run deterministic scanning first:

```bash
gitleaks dir .scratch/PROJ-123-ship-session.txt --redact --report-format json --report-path .scratch/gitleaks-report.json
```

2. Inspect the report and the transcript for organisation-specific secrets, bearer tokens, API keys, `.env` values, credentials, private signed URLs, and contextual secrets scanners may miss.
3. Redact and rescan.
4. If safe redaction is uncertain, stop rather than publishing.

A zero-result scanner run is evidence, not proof of safety.

## Upload

Use the helper so credentials never appear in argv:

```bash
python ${CLAUDE_PLUGIN_ROOT}/skills/tracker/jira/jira_rest.py attach \
  PROJ-123 .scratch/PROJ-123-ship-session.txt
```

The helper reads `ACLI_EMAIL`, `ACLI_TOKEN`, and optional `ACLI_SITE` from the environment. It prints created attachment metadata. Treat HTTP errors, empty results, or filename mismatch as failure.

Rules:

- name artifacts `<task>-<kind>.<ext>`;
- if site size limits reject a transcript, split into numbered parts and verify every part;
- reference attachment filename from the accounting comment;
- never claim an attachment exists without response evidence.
