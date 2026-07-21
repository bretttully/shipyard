---
name: init-repo
description: >-
  Get this repo's Shipyard config from zero (or partially done) to genuinely usable: write
  `.claude/settings.json` (shared, tracked) and `.claude/settings.local.json` (personal,
  gitignored), then prove it live with the same preflight check every other command runs.
  Asks only for what is actually missing, so a teammate joining an already-configured repo
  is a short exchange, not a full interview.
argument-hint: "[optional SY_TRACKER override]"
disable-model-invocation: true
---

Turn an unconfigured or partially-configured repo into one where `/sy:plan`, `/sy:spec`,
`/sy:ship`, and `/sy:spike` all pass preflight (`${CLAUDE_PLUGIN_ROOT}/skills/shared/references/preflight.md`)
on the first real try. Never writes code; never touches the tracker's actual issues.

$ARGUMENTS

## 1. Read what already exists

Read `.claude/settings.json`'s `env` block (if the file exists) and the current process
environment. Anything already set there is **shared, committed config** — never re-ask for
it, never overwrite it without saying so first. This is what makes the common case fast: a
teammate joining a repo someone already configured has almost everything already answered,
and this run is short.

## 2. Resolve the tracker

If `SY_TRACKER` is already set (settings.json or env) or `$ARGUMENTS` names one, use it. Otherwise
ask via `AskUserQuestion` which supported tracker this repo uses (the options and their meaning
are `${CLAUDE_PLUGIN_ROOT}/skills/tracker/CONTRACT.md`'s to name, not this file's) — a genuine
fork with no reasonable default (`${CLAUDE_PLUGIN_ROOT}/skills/shared/references/user-interaction.md`).

Load `${CLAUDE_PLUGIN_ROOT}/skills/tracker/${SY_TRACKER}/ADAPTER.md`'s configuration/preflight
section to learn, for the chosen tracker only: its required env vars, which of them are secrets,
and the one-time CLI login it needs outside those vars. This file stays tracker-agnostic in its
own prose — the concrete var names and meanings live only in the adapter, exactly per
`CONTRIBUTING.md`'s seam rule.

## 3. Check the one-time CLI login first

Before asking for anything else, check the adapter's one-time login **live**, not by presence:
the loaded `ADAPTER.md` names the check (e.g. an auth-status command) and the login command that
fixes it. This step cannot be automated — it is an interactive, per-person login this skill has
no business running on the user's behalf — so a missing login stops the run right here with a
single `## Action needed` block naming the exact command to run, then re-run `/sy:init-repo`.
Continuing the interview before this is fixed only produces config that still cannot pass
preflight.

## 4. Interview only for what is missing

For each of the adapter's required vars, and the five canonical column names
(`SY_BACKLOG_COLNAME`, `SY_READY_COLNAME`, `SY_IN_PROGRESS_COLNAME`, `SY_IN_REVIEW_COLNAME`,
`SY_DONE_COLNAME` — shared across trackers, matching the real names on this tracker's board or
workflow) not already resolved in step 1, ask directly in conversation — this is data entry, not
a multiple-choice fork, so plain prompts, not `AskUserQuestion`. State plainly which values are
shared (safe to commit) and which are secret (never committed) before asking, so the user is not
surprised later by where an answer lands.

The user may not recall a board's exact column spelling. Once the identifiers that only they know
(project/board key or number) are answered, discover the board's actual lifecycle values via a
subagent scoped to exactly that tracker and project/board — never run open-ended discovery queries
in this session — and present the discovered names for the user to confirm rather than asking them
to type a spelling from memory.

## 5. Write, split by secrecy

- Shared, non-secret values (`SY_TRACKER`, the five column names, and every adapter var the
  loaded `ADAPTER.md` does not call out as a credential) merge into `.claude/settings.json`'s
  `env` block. Create the file if absent; preserve every existing key (including
  `enabledPlugins`/`extraKnownMarketplaces` if already there) and merge rather than overwrite.
- Secret values (a personal API token) merge into `.claude/settings.local.json`'s `env` block —
  **never** the shared file — matching the Secrets convention in `docs/settings.md`.
- If `.claude/settings.json` has no `enabledPlugins` entry for this plugin yet, this is the very
  first setup for the repo, not a teammate joining one already configured: mention, as a single
  optional aside, the project-scope install path in `docs/installation.md` so the rest of the
  team gets it for free on clone — never run a plugin-install command silently on the user's
  behalf, the same boundary `docs/installation.md` already states.

## 6. Prove it live

Run the adapter's real preflight read directly (skip the cache check — the config just changed,
so a hit would be stale by construction), then record success so the very next command gets the
cached fast path:

```bash
<adapter's live-check command, from its ADAPTER.md>
python "${CLAUDE_PLUGIN_ROOT}/scripts/sy_preflight.py" record --tracker "$SY_TRACKER" --vars <adapter's var list>
```

A failure here is the same `## Action needed` shape as step 3 — name the exact thing that is
still wrong (per the adapter's own error text) and stop; do not report success on unverified
config.

## 7. Report

Close with a status update: which file(s) were written, the tracker confirmed live, and — as a
single optional aside, never a gate — a nudge toward `/sy:plan` or `/sy:spec` next.
