---
name: tracker
description: >-
  Own issue-tracker mechanics behind one contract, dispatching to the configured adapter
  (Jira or GitHub Projects): hierarchy, lifecycle, dependencies, comments, machine logs,
  attachments, and decomposition. Workflow skills own decisions; this skill owns durable
  representation and mutation.
argument-hint: "[tracker operation or issue key]"
---

Own tracker mechanics behind the contract in `${CLAUDE_PLUGIN_ROOT}/skills/tracker/CONTRACT.md`. Workflow skills (`/sy:plan`, `/sy:spec`, `/sy:ship`, `/sy:spike`) decide *what* the lifecycle should do in canonical terms; this skill turns that into concrete calls against the selected tracker.

$ARGUMENTS

## Select the adapter

Resolve the tracker with the standard precedence — env var, then project settings, then default:

```text
SY_TRACKER = jira | github        # default: jira
```

Then load exactly two files and use nothing else for tracker mechanics:

1. `${CLAUDE_PLUGIN_ROOT}/skills/tracker/CONTRACT.md` — the canonical verbs, statuses, and types.
2. `${CLAUDE_PLUGIN_ROOT}/skills/tracker/${SY_TRACKER}/ADAPTER.md` — the native implementation.

This is the **single point** where tracker selection happens. No other skill or agent branches on the tracker. Fail fast before any work when:

- `SY_TRACKER` is set to anything other than `jira` or `github`;
- any required column-name env var is unset — `SY_BACKLOG_COLNAME`, `SY_READY_COLNAME`, `SY_IN_PROGRESS_COLNAME`, `SY_IN_REVIEW_COLNAME`, `SY_DONE_COLNAME` (read from the repo's `.claude/settings.json` `env`; shared by every adapter);
- the selected adapter's required configuration is absent (each adapter lists it and self-checks).

Report the actionable error and stop; never fall through to a default that silently writes to the wrong system.

## What core may ask for

Core speaks only the contract: canonical verbs (`create-issue`, `create-child`, `get-issue`, `update-issue`, `find-issues`, `set-status`, `assign`, `link-parent`, `add-dependency`, `add-label`, `post-comment`, `post-log`, `attach-artifact`, `link-pr`), canonical statuses (`backlog`, `ready`, `in-progress`, `in-review`, `done`), and canonical types (`epic`, `task`, `bug`). Issue IDs are opaque; bodies and comments are Markdown. The adapter maps all of it.

## Conventions that live here, not in an adapter

- **Standalone machine logs.** `post-log` output (`# Claude Code usage`, `# Claude Code ship metrics`) is its own comment, never merged into prose. Generate usage from the transcript tree with `${CLAUDE_PLUGIN_ROOT}/scripts/session_usage.py`.
- **Exactly one ACTIVE plan** per task/bug; supersede explicitly and re-read to confirm.
- **Closure is not delivery.** Merged/delivered closure satisfies a dependency; decomposed or superseded closure does not — follow replacement links until delivered capability is reached.
- **Canonical decomposition** when replacing one task with smaller ones:
  1. create/approve replacements as direct children of the same epic;
  2. record replacement dependencies with `add-dependency`;
  3. `post-comment` a `# Decomposition` note with reason and replacement IDs;
  4. `add-label` the old task `decomposed` (labels preserved);
  5. `set-status` the old task `done`;
  6. ensure the old and replacement work are never simultaneously actionable;
  7. represent the old task as a conceptual parent branch in the epic roadmap.

## Durable comment types

- `# Execution Plan vN` — human-readable plan plus explicit ACTIVE/SUPERSEDED status.
- `# SEAMS` — oversized-leaf evidence for `/sy:plan`.
- `# Decomposition` — replacement IDs and terminal reason.
- `# Ship retrospective` — human-readable shipped-vs-plan lessons.
- `# Claude Code usage` — standalone JSON usage log (`post-log`).
- `# Claude Code ship metrics` — standalone JSON outcome log (`post-log`).
- Epic decision logs ending in a `Plan checkpoint` footer.

## Loop mapping

- `/sy:plan` ↔ epic roadmap + direct executable children created in `backlog`, max 4 active.
- `/sy:spec` ↔ task/bug + sole ACTIVE versioned plan; the approved plan moves the task to `ready`.
- `/sy:ship` ↔ `in-progress` on build, `in-review` at a reviewable gated PR, `done` after merge;
  retrospective, standalone logs, and transcript live on the task.
- `/sy:spike` ↔ task under the selected experiment epic; `in-progress` during, `done` at verdict.
- dependencies ↔ `add-dependency` plus the closure semantics above.

## References: load only when needed

- `${SY_TRACKER}/references/*` — adapter-specific cookbooks and setup.
