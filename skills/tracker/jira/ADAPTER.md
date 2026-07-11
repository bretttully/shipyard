# Jira adapter

Implements the tracker contract (`../CONTRACT.md`) against Jira via the Atlassian `acli`, with a small REST helper for operations where `acli` is ambiguous or inverted. This is the default tracker (`SY_TRACKER=jira`).

## Configuration (self-check before any work)

Required env: `ACLI_EMAIL`, `ACLI_TOKEN`, `ACLI_SITE`, `ACLI_PROJECT`. Never put tokens in command arguments. `acli jira auth status` proves only local credential presence; validate with a real work-item read. If any required value is missing, fail fast with the missing name. Build JQL with `${ACLI_PROJECT:?}`, never a hard-coded project.

## Type mapping

| Canonical | Jira type |
|---|---|
| `epic` | Epic |
| `task` | Task |
| `bug` | Bug |

Execution is flat: one tracking Epic, every executable Task/Bug directly beneath it; conceptual hierarchy lives in the Epic body/comments.

## Status mapping

Each canonical status maps to the Jira status/transition named by the shared, required per-repo column env var (the Jira workflow must have statuses with those names):

| Canonical | Jira status (transition target) |
|---|---|
| `backlog` | `$SY_BACKLOG_COLNAME` |
| `ready` | `$SY_READY_COLNAME` |
| `in-progress` | `$SY_IN_PROGRESS_COLNAME` |
| `in-review` | `$SY_IN_REVIEW_COLNAME` |
| `done` | `$SY_DONE_COLNAME` |

`set-status` transitions to the resolved name:

```bash
acli jira workitem transition --key <ID> --status "$SY_IN_REVIEW_COLNAME" --yes
```

(`--yes` only where the installed command supports it). Inspect the closure reason before treating a `done` issue as delivered — decomposed/superseded closure is not delivery.

## Rich text: Markdown → ADF

Jira comments and descriptions are ADF. Stage the Markdown, convert, then write:

```bash
python "${CLAUDE_PLUGIN_ROOT}/skills/tracker/jira/md_to_adf.py" .scratch/body.md > .scratch/body.adf.json
```

Load `references/adf.md` for converter setup/verification.

## Verb implementations

```bash
# create-issue  (epic)
acli jira workitem create --project "${ACLI_PROJECT:?}" --type Epic \
  --summary "<title>" --description-file .scratch/epic.adf.json

# create-child  (task/bug under a parent)
acli jira workitem create --project "${ACLI_PROJECT:?}" --type Task \
  --parent <PARENT_ID> --summary "<title>" --description-file .scratch/task.adf.json

# get-issue
acli jira workitem view <ID> --fields '*all'
acli jira workitem comment list --key <ID>

# update-issue  (replace body)
acli jira workitem edit --key <ID> --description-file .scratch/body.adf.json

# find-issues  (JQL against the configured project)
acli jira workitem search --jql "project = ${ACLI_PROJECT:?} AND status = 'In Progress'"

# assign
acli jira workitem assign --key <ID> --assignee @me

# post-comment / post-log  (both are comments; post-log carries only fenced JSON)
acli jira workitem comment create --key <ID> --body-file .scratch/comment.adf.json

# link-pr  (Jira dev-panel link is driven from the commit/PR; record the URL in a comment too)
#   PRs surface in the Jira development panel when the branch/commit names the key.
#   Post the PR URL as a comment so it is durable regardless of dev-panel wiring.
```

### `add-dependency` (X blocked by Y) — use the REST helper

`acli`'s `link --out`/`--in` flags are inverted relative to Jira's model (empirically `--in` is the blocker), so it silently creates the reverse link. The helper sets direction via the REST model and verifies it:

```bash
# ID_Y blocks ID_X  (ID_X is blocked by ID_Y)
python "${CLAUDE_PLUGIN_ROOT}/skills/tracker/jira/jira_rest.py" link --blocker <ID_Y> --blocked <ID_X>
```

Deleting a link is unambiguous on `acli`: `acli jira workitem link delete --id <id> --yes`.

### `add-label` — use the REST helper

`acli` append-vs-replace label semantics are ambiguous. The helper reads the current set and writes it back plus the requested label:

```bash
python "${CLAUDE_PLUGIN_ROOT}/skills/tracker/jira/jira_rest.py" add-label <ID> decomposed
```

### `link-parent` — use the REST helper

```bash
python "${CLAUDE_PLUGIN_ROOT}/skills/tracker/jira/jira_rest.py" set-parent <ID> <PARENT_ID>
```

Ask before crossing into another project or portfolio hierarchy.

### `attach-artifact`

Jira supports native work-item attachments. Scan first (secrets), then upload with the helper so credentials never appear in argv. Load `references/attachments.md` for the render/scan/upload/verify flow:

```bash
python "${CLAUDE_PLUGIN_ROOT}/skills/tracker/jira/jira_rest.py" attach <ID> .scratch/<ID>-ship-transcript.txt
```

## References

- `references/adf.md` — Markdown→ADF converter setup/verification.
- `references/attachments.md` — transcript render/scan/redact/upload/verify.
- `references/accounting.md` — usage/metrics JSON shapes and standalone-comment rules.
- `references/acli-cookbook.md` — extended commands and REST parent updates.
- `references/migration.md` — GitHub-issue → Jira migration (separate workflow, not used in the loop).
