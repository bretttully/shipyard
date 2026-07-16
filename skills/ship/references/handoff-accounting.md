# Retrospective, token accounting, transcript, and handoff

This phase runs mostly as a worker for the records and accounting. The readable transcript is rendered from the on-disk session tree by a delegate, so no manual `/export` is ever run.

Create the durable records for the plan's process tier, each as its own tracker comment, never combined: `full` = all four below; `light` = records 1–3 only, with `transcript_attachment: null` in the metrics JSON. The tier never changes CI/review coverage.

## 1. Human retrospective comment

Post `# Ship retrospective` as clear prose:

- shipped vs plan;
- divergences and mid-ship decisions — accepted deviations and any parent-resolved `needs-decision` — and why;
- what the plan missed;
- lessons for next `/sy:plan`;
- follow-ups;
- PR URL and gate coverage.

Do **not** embed token or metrics JSON in this comment.

## 2. Standalone token-usage JSON comment

Token accounting must include the parent ship session and every nested subagent transcript (`sy:slice`, `sy:gate`, nested `sy:hunt`, `sy:sweep`, fallbacks, etc.). Claude stores subagent transcripts separately, so do not derive totals from parent export text alone.

Generate the report from the full transcript tree. This example assumes `sy:slice` was used; repeat/remove `--require-agent` flags to match local `agents_used`:

```bash
python ${CLAUDE_PLUGIN_ROOT}/scripts/session_usage.py summarize \
  --session-id "$SHIP_SESSION_ID" \
  --phase ship \
  --task "$TASK_KEY" \
  --require-agent gate \
  --require-agent slice \
  --output .scratch/claude-usage-$TASK_KEY.json
```

Inspect the JSON before posting:

- `scope` must be `main_plus_subagents`;
- `transcripts.subagents` must be consistent with the agents actually used;
- run with one `--require-agent` per directly used agent in `agents_used`; the command must fail if any is absent;
- `by_agent` must include nested agents when present;
- totals must not be manually reconstructed or inferred.

Post one small tracker comment containing only:

````text
# Claude Code usage

```json
<contents of .scratch/claude-usage-$TASK_KEY.json>
```
````

Post via the `tracker` skill (it renders Markdown to the tracker's native format). This usage log is standalone; never append it to the retrospective, execution plan, or decomposition comment.

## 3. Standalone ship-metrics JSON comment

Post a second small comment containing only a JSON object under `# Claude Code ship metrics`:

```json
{
  "schema": "shipyard.ship_metrics.v1",
  "task": "TASK-123",
  "pr_url": "...",
  "plan_divergence_count": 0,
  "ci_fix_rounds": 0,
  "review_findings_accepted": 0,
  "review_findings_rejected": 0,
  "human_review_defects": 0,
  "post_merge_defect": null,
  "rollback": null,
  "lead_time_seconds": null,
  "transcript_attachment": "ship-session-....txt"
}
```

Use `null` for unknown values. Never infer metrics.

## 4. Transcript attachment (full tier only)

A HANDOFF delegate (subagent, added to `agents_used`) renders and uploads the transcript straight from the on-disk session tree, so nothing session-bound and no by-hand `/export` is involved. It renders the whole tree — main plus every nested subagent — into one readable file:

```bash
python ${CLAUDE_PLUGIN_ROOT}/scripts/session_usage.py export \
  --session-id "$SHIP_SESSION_ID" \
  --task "$TASK_KEY" \
  --output .scratch/$TASK_KEY-ship-transcript.txt
```

The renderer truncates bulky tool output and strips raw-JSONL noise, so the result is an audit-readable transcript, not a machine dump; token accounting still comes from `session_usage.py summarize`. The delegate then runs the deterministic `gitleaks` scan, contextual review, and redaction, uploads exactly one attachment, and verifies it, per `${CLAUDE_PLUGIN_ROOT}/skills/ship/references/merge-accounting.md` and the `tracker` skill's attachment flow. Run it as late as possible (after an authorized merge) so the captured tail is maximal; because it reads on-disk transcripts it can also run on a resumed session. The rendered transcript is never read back into the ship context.

Subagent delegation is the primary path. When it is denied under auto-mode — the delegation itself is refused rather than the attachment — the identical operation may run inline as an explicit permitted fallback: execute the same `session_usage.py export` above, then the deterministic `gitleaks` scan and redaction, then upload the single attachment through the `tracker` skill's attachment flow, all directly in the caller. This is the authorized-alternate-route case of the denied-write boundary in `${CLAUDE_PLUGIN_ROOT}/skills/shared/references/write-integrity.md`: it is the same documented render-and-attach, not a reroute to force a write the operator blocked. The invariant is unchanged — the rendered transcript file is written, scanned, and uploaded by path only, and its text is never read back into the caller context. The fallback's scan is deterministic-only — it drops the contextual-review step of the primary path, since reading the transcript to review it would defeat the isolation invariant it exists to preserve — so treat a clean result here as evidence, not proof, per the `tracker` skill's attachment flow. If neither path can complete, surface it loudly (do not silently skip the attachment) per the same boundary.

## Handoff

Task stays `in-review` until merge. Report PR URL, tracker status, acceptance state, coverage SHAs/requested+observed gate models, usage/metrics comment status, transcript attachment status, and owned-worktree status as a status update, then close the turn with an isolated `## Action needed` block (per `${CLAUDE_PLUGIN_ROOT}/skills/shared/references/user-interaction.md`) stating the PR is ready and merge awaits your explicit authorization — never let that wait get lost among the status facts above it. Front-load the follow-on mutations in that same block so consent is informed and no later write is a surprise: name that on your go-ahead the run will merge the verified head, attach the scanned transcript, and set the task done. Under auto-mode this is the one consent point covering all three mutations, so it must enumerate them rather than authorize a bare "merge".
