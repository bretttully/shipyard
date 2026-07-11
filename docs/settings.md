# Configuration

Shipyard is configured **per repository**, through the `env` block of that repo's `.claude/settings.json`. Claude Code sets those variables for any session run in the repo, and every Shipyard skill, agent, and helper reads them from the environment. Because the config lives in the repo, different repos on one machine can use different trackers, boards, column names, and reviewer models with no global state — the same machine can drive a Jira repo and a GitHub repo side by side.

This page is the complete reference for every knob. For the one-time GitHub Projects board and field setup that the GitHub variables point at, see [`github-setup.md`](github-setup.md).

## Every setting

| Variable | Tracker | Required | Default | What it does |
|---|---|---|---|---|
| `SY_TRACKER` | both | no | `jira` | Selects the tracker adapter: `jira` or `github`. This is the single point where the tracker is chosen. |
| `SY_FRONTIER_MODEL` | both | no | `fable` | The model `sy:gate` uses for the independent review. A quality floor, not a cost dial — set it to your strongest available model. |
| `SY_FRONTIER_FALLBACK` | both | no | `opus` | The model the reviewer falls back to once if the frontier model cannot run (spend cap, rate limit, or a refusal). If the fallback also fails, ship returns `blocked` rather than promoting an unreviewed commit. |
| `SY_BACKLOG_COLNAME` | both | **yes** | — | Your board/workflow name for the `backlog` column (queued, not yet specced). |
| `SY_READY_COLNAME` | both | **yes** | — | Your name for the `ready` column (specced, plan approved). |
| `SY_IN_PROGRESS_COLNAME` | both | **yes** | — | Your name for the `in-progress` column (active build). |
| `SY_IN_REVIEW_COLNAME` | both | **yes** | — | Your name for the `in-review` column (a reviewable gated PR exists). |
| `SY_DONE_COLNAME` | both | **yes** | — | Your name for the `done` column (terminal). |
| `SY_GH_PROJECT` | github | **yes** (github) | — | The Projects v2 board, `<owner>/<number>` — `@me/<n>` (or `<username>/<n>`) for a user board, `<org>/<n>` for an org board. |
| `SY_GH_REPO` | github | no | current repo | Where issues live, `<owner>/<repo>`. Set it when issues live in a different repo than the one you run Claude in. |
| `ACLI_EMAIL` | jira | **yes** (jira) | — | Atlassian account email for `acli`. |
| `ACLI_TOKEN` | jira | **yes** (jira) | — | Atlassian API token. **Secret** — see below. |
| `ACLI_SITE` | jira | **yes** (jira) | — | Your Atlassian site (e.g. `your-org.atlassian.net`). |
| `ACLI_PROJECT` | jira | **yes** (jira) | — | The Jira project key new issues are created in and queries are scoped to. |

Missing required values fail fast with the name of the missing variable, rather than silently writing to the wrong place.

### The five column names

Shipyard is opinionated about the **number and role** of the lifecycle columns — five: `backlog → ready → in-progress → in-review → done` — but not their names. The five `SY_*_COLNAME` variables map each canonical role to whatever your board actually calls it (matching is case-insensitive). They are tracker-neutral: the Jira adapter reads them as workflow transition targets and the GitHub adapter reads them as `Status` field options, so one repo config drives whichever tracker the repo uses. `blocked` is deliberately not a column — a block is a dependency relationship the tracker surfaces natively.

## Example: a Jira repo

`.claude/settings.json` in the repo:

```json
{
  "env": {
    "SY_TRACKER": "jira",
    "SY_FRONTIER_MODEL": "fable",
    "ACLI_EMAIL": "you@example.com",
    "ACLI_SITE": "your-org.atlassian.net",
    "ACLI_PROJECT": "PROJ",
    "SY_BACKLOG_COLNAME": "To Do",
    "SY_READY_COLNAME": "Ready",
    "SY_IN_PROGRESS_COLNAME": "In Progress",
    "SY_IN_REVIEW_COLNAME": "In Review",
    "SY_DONE_COLNAME": "Done"
  }
}
```

`ACLI_TOKEN` is intentionally absent here — keep it out of shared config (see [Secrets](#secrets)). The five column names must match statuses that exist in the Jira project's workflow.

## Example: a GitHub repo

`.claude/settings.json` in the repo:

```json
{
  "env": {
    "SY_TRACKER": "github",
    "SY_FRONTIER_MODEL": "fable",
    "SY_GH_PROJECT": "@me/3",
    "SY_GH_REPO": "your-name/your-repo",
    "SY_BACKLOG_COLNAME": "Backlog",
    "SY_READY_COLNAME": "Ready",
    "SY_IN_PROGRESS_COLNAME": "In progress",
    "SY_IN_REVIEW_COLNAME": "In review",
    "SY_DONE_COLNAME": "Done"
  }
}
```

The board this points at needs a `Status` single-select with one option per column name above, and a `Type` single-select with options `Epic`/`Task`/`Bug`. [`github-setup.md`](github-setup.md) walks through creating them and verifying the config resolves.

## Secrets

`ACLI_TOKEN` is a credential and must not be committed. Put it in the repo's `.claude/settings.local.json` (which Claude Code treats as personal and is gitignored) or export it in your shell environment; keep only non-secret config in the shared `.claude/settings.json`. `settings.local.json` uses the same `env` shape:

```json
{ "env": { "ACLI_TOKEN": "your-atlassian-api-token" } }
```

Shipyard never passes tokens as command-line arguments.

## Model routing

Leave `CLAUDE_CODE_SUBAGENT_MODEL` **unset**. It overrides model routing for every subagent and takes precedence over `SY_FRONTIER_MODEL`, so setting it would silently reroute the independent reviewer off its intended model. `./install.sh` warns if it is set.
