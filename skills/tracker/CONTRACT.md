# Tracker contract

The single vocabulary the toolbox uses to talk to an issue tracker. Core skills and agents (everything outside `skills/tracker/`) reference **only** the verbs, statuses, and types below. Each adapter (`jira/ADAPTER.md`, `github/ADAPTER.md`) maps them to its native system. The code host (GitHub PRs and CI) is a separate concern owned by `/sy:pr` and `/sy:ci`; it is not the tracker and never varies.

## Issue IDs are opaque

An issue ID is an opaque string that round-trips untouched: `PROJ-123` and `#123` both pass through core without being parsed, split, or constructed. Only an adapter may interpret an ID's shape.

## Rich text is Markdown

Every body and comment the toolbox produces is **Markdown**. The adapter renders it to the native format (Jira: ADF; GitHub: Markdown passthrough). Core never emits tracker-native markup.

## Issue types

| Canonical | Meaning |
|---|---|
| `epic` | The living roadmap container. One per objective. |
| `task` | One executable unit ≈ one coherent PR. Direct child of an epic. |
| `bug` | Same lifecycle as `task`; a defect fix rather than new work. |

## Statuses (the kanban columns)

Shipyard is opinionated about the **five** lifecycle columns and their workflow mapping — not their names. Core uses only these canonical tokens; each adapter maps a token to the tracker's actual column via a **required per-repo env var**. Matching is case-insensitive.

| Canonical | Column env var | Set when | Meaning |
|---|---|---|---|
| `backlog` | `SY_BACKLOG_COLNAME` | `/sy:plan` creates the item | queued, not yet specced |
| `ready` | `SY_READY_COLNAME` | `/sy:spec` plan approved | specced, ready to build |
| `in-progress` | `SY_IN_PROGRESS_COLNAME` | `/sy:ship` builds | active build |
| `in-review` | `SY_IN_REVIEW_COLNAME` | gate on a reviewable PR | reviewable gated PR exists |
| `done` | `SY_DONE_COLNAME` | merge | terminal (inspect closure reason — see below) |

The column-name env vars are **required** and read from the repo's `.claude/settings.json` `env`, so different repos on one machine can use different board labels while every adapter reads the same vars — the same config drives whichever tracker the repo uses.

**`blocked` is not a status.** A blocking relationship is expressed with `add-dependency`; the tracker surfaces it natively (Jira link / GitHub blocked indicator).

**Closure semantics.** `done` is not automatically *delivered*. Merged/delivered closure satisfies a dependency; decomposed/superseded closure does not. Follow replacement links until delivered capability is reached. `/sy:ship` resolves this chain before branching.

## Verbs

The complete set of tracker operations. An adapter must implement every verb.

| Verb | Semantics |
|---|---|
| `create-issue` | Create an issue with `type`, `title`, Markdown `body`. Returns an opaque issue ID. |
| `create-child` | Create an issue of `type` parented to a given issue. Returns an opaque ID. |
| `get-issue` | Fetch title, body, canonical status, type, parent, children, labels, dependencies, linked PRs. |
| `update-issue` | Replace an issue's Markdown body. |
| `find-issues` | Query by status / type / parent / free text within the configured project. |
| `set-status` | Move an issue to a canonical status. |
| `assign` | Assign an issue (self-assign is the default caller need). |
| `link-parent` | Re-parent an existing issue under another. |
| `add-dependency` | Record that issue X is blocked by issue Y. |
| `add-label` | Add a label, preserving existing labels. |
| `post-comment` | Post a Markdown comment. The TL;DR-first convention applies here, in core. |
| `post-log` | Post a **standalone** machine log comment (fenced JSON). Never combined with prose — see below. |
| `attach-artifact` | Attach a durable file (the session transcript) to the issue. |
| `link-pr` | Associate a PR with an issue. |

### Machine logs are standalone (`post-log`)

Usage and metrics logs are small, machine-readable, and posted as their own comments — never appended to a retrospective, plan, decomposition, or checkpoint comment. Schemas:

- `# Claude Code usage` → `{"schema": "shipyard.claude_usage.v1", ...}`
- `# Claude Code ship metrics` → `{"schema": "shipyard.ship_metrics.v1", ...}`

Generate usage from the on-disk transcript tree with `${CLAUDE_PLUGIN_ROOT}/scripts/session_usage.py` (tracker-agnostic). The adapter only posts the resulting JSON.

### Attachments may degrade to a link

`attach-artifact` uploads a file where the tracker supports it (Jira work-item attachments). Where it does not (GitHub issues have no CLI-scriptable attachment), the adapter substitutes an equivalent durable artifact (a private gist) and links it from a comment. Either way the artifact is secret-scanned before it leaves the machine, and the log comment references it by name/URL. This asymmetry is documented per adapter and in the deliberate-asymmetries section of the README.

## Exactly one ACTIVE plan

A `task`/`bug` carries at most one execution plan whose status is ACTIVE. Superseding is explicit: mark the old plan comment SUPERSEDED and the new one ACTIVE, then re-read to confirm exactly one ACTIVE. Never use a "latest-looking comment wins" heuristic. This is a core convention; the adapter only provides `post-comment`/`get-issue`.

## Configuration

- `SY_TRACKER` = `jira` | `github` (default `jira`). Selects the adapter.
- **Required column names** (all trackers), from the repo's `.claude/settings.json` `env`: `SY_BACKLOG_COLNAME`, `SY_READY_COLNAME`, `SY_IN_PROGRESS_COLNAME`, `SY_IN_REVIEW_COLNAME`, `SY_DONE_COLNAME`. Missing values fail fast.
- Each adapter declares its own additional configuration and fails fast when it is missing.
