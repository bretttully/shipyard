# Shipyard Agent Guide

## What Shipyard is

Shipyard is a Claude Code plugin that runs a `plan → spec → ship` delivery loop against an issue tracker (Jira or GitHub Projects). It turns an objective into a merged, independently reviewed pull request, with the plan, an adversarial review, and a paper trail recorded on the ticket. The user approves the plan and authorizes every merge; Shipyard does the building and the reviewing.

## Concept model

- **Tracker**: the pluggable backend — Jira or GitHub Projects — selected by `SY_TRACKER`. Core skills never speak tracker-native vocabulary; only `skills/tracker/<name>/` does.
- **Five lifecycle columns**: `backlog → ready → in-progress → in-review → done`, mapped to whatever the user's board actually calls them via `SY_*_COLNAME` variables. `blocked` is not a column — it's a tracker-native dependency relationship.
- **Plan**: a living roadmap on one Epic, produced by `/sy:plan`. At most four child tasks are active at once.
- **Spec**: a single ACTIVE execution plan per task, produced by `/sy:spec <task>` and approved by the user before anything is built. It's stamped with the commit it was planned against. Not every spec ends in a plan — when research shows the premise is already delivered, invalidated, or superseded, spec shelves the task with evidence instead.
- **Ship**: `/sy:ship <task>` builds the plan in its own worktree, gets CI green, and runs `sy:gate` — an independent reviewer on a frontier model, in an isolated read-only checkout, that must refute-test every bug candidate before reporting it. Head, CI-green, and reviewed commits must converge before it stops.
- **Merge**: never automatic. The user's explicit word is required every time.
- **Cross-session memory**: a small, user-global store (`scripts/sy_memory.py`, `SY_MEMORY_DIR`) of durable lessons — a CLI flag with inverted semantics, a silent model fallback — that outlive any one ticket or repo. `/sy:plan` and `/sy:spec` read it early; `/sy:ship` writes to it at the retrospective.

## Installing

Two ways to load the plugin — pick based on whether this is a one-off trial or a persistent setup:

```bash
# one session only, from a local checkout
claude --plugin-dir /path/to/shipyard

# persistent, straight from GitHub (no clone needed)
claude plugin marketplace add bretttully/shipyard
claude plugin install sy@shipyard
```

`./install.sh` (run from a local checkout) validates the plugin's structure and runs a tracker-aware preflight against the current environment — do this after cloning:

```bash
cd /path/to/shipyard && ./install.sh
```

Required tools: Claude Code (plugin-capable), Python 3.10+ on PATH as `python`, `gh` ≥ 2.94.0 authenticated (every tracker uses it for PRs/CI), and `gitleaks` (scans transcripts before they're attached/gisted). Jira additionally needs `acli`.

## Configuring a repo

Configuration is per-repo, in `.claude/settings.json`'s `env` block. Required for every repo:

- `SY_BACKLOG_COLNAME`, `SY_READY_COLNAME`, `SY_IN_PROGRESS_COLNAME`, `SY_IN_REVIEW_COLNAME`, `SY_DONE_COLNAME` — the five lifecycle columns, matched case-insensitively to the user's actual board.
- `SY_TRACKER` — `jira` (default) or `github`.

Then, tracker-specific:

- **Jira**: `ACLI_EMAIL`, `ACLI_SITE`, `ACLI_PROJECT` required; `ACLI_TOKEN` is a secret — put it in `.claude/settings.local.json`, never the shared file.
- **GitHub**: `SY_GH_PROJECT` (`<owner>/<number>`, e.g. `@me/3`) required; `SY_GH_REPO` only if issues live in a different repo than the one Claude runs in. The board needs a `Status` single-select (one option per column) and a `Type` single-select (`Epic`/`Task`/`Bug`) — see the repo's `docs/github-setup.md` to create them.

Optional knobs worth knowing: `SY_FRONTIER_MODEL` (default `fable`) is the `sy:gate` reviewer's model — a quality floor, set it to the strongest available model, not a cost dial. `SY_WORKTREE_ROOT` defaults to a sibling `<repo>-worktrees/` directory beside the repo. `SY_MEMORY_DIR` (default `~/.claude/shipyard/memory`) relocates the cross-session memory store — it's user-global and cross-repo, so most setups never need to touch it.

## First-run walkthrough

1. Load the plugin (session or persistent, above).
2. Fill in `.claude/settings.json` for this repo — the five column names plus the chosen tracker's required variables.
3. Put any secret (`ACLI_TOKEN`) in `.claude/settings.local.json`, not the shared file.
4. Name a session and start the loop: `claude -n "plan <objective>" "/sy:plan <objective>"`.
5. Answer `/sy:plan`'s interview questions; it writes the roadmap to one Epic.
6. Per task: `/sy:spec <task>` (review and approve the plan it proposes), then `/sy:ship <task>` (builds, gets CI green, gets gated).
7. When ship reports head/CI-green/reviewed convergence, authorize the merge explicitly — Shipyard never does this on its own.

## Diagnosis recipes

- `/sy:ship` refuses to build: the plan's base commit has drifted from `origin/main` — re-run `/sy:spec` to refresh it.
- The reviewer seems to be running the wrong model: check `CLAUDE_CODE_SUBAGENT_MODEL` isn't set — it silently overrides `SY_FRONTIER_MODEL`/`SY_IMAGE_MODEL`. `./install.sh` warns about this.
- A tracker verb is missing or behaves oddly: it belongs in `skills/tracker/<name>/ADAPTER.md` — never in a core skill or agent.
- Ship stops before attaching a transcript: `gitleaks` isn't installed — it's a hard gate, not a warning.
- The GitHub tracker preflight fails on a missing `gh`: hard error for `SY_TRACKER=github` (soft warning for `jira`).

## Key rules for guidance

- Don't invent `SY_*` variable names, column values, or tracker fields — the authoritative list is `docs/settings.md`; read it rather than guessing.
- Never suggest merging on the user's behalf or imply a merge happened automatically — nothing merges without their explicit word, by design.
- Keep tracker vocabulary (`jira`, `acli`, `gh issue`, ADF, …) out of anything described as core when discussing the codebase — that seam is enforced by `scripts/validate.py`.
- Task/issue IDs (`PROJ-123`, `#123`) pass straight through to the tracker — don't reformat or reinterpret them.
- Exactly one execution plan is ACTIVE per task at a time — flag that a new `/sy:spec` run supersedes an existing unshipped plan rather than stacking silently.
- This is a Claude Code plugin: install it with `claude plugin` / `--plugin-dir`, never by copying or symlinking files into `~/.claude`.
