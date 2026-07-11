# Start or resume

This phase runs as the `sy:ship-start` worker: it initializes or resumes ownership, delegates standards resolution and large Epic/plan reads, and returns the state brief per the worker contract.

1. Read Task body/comments and select the sole ACTIVE execution plan.
2. Read parent Epic only enough for sibling interfaces/blockers; use `sy:sweep` for a large tail.
3. Ship profile (model / effort / process tier) is a parent precondition verified before dispatch; if the running profile is below plan the parent stops for a user decision. The profile floors worker models (may raise, never lower, so BUILD keeps its opus tier) and sets worker effort to match the work; it never lowers review effort (`sy:gate` stays max). Do not prompt the user from the worker.
4. Resolve standards in a delegate (subagent running `/sy:standards resolve <task scope>`, added to `agents_used`) that returns only the retained contract — authority, implementation contract, primitives, risk lenses; rule-file reads stay out of the ship context.
5. Load `.scratch/<task>-ship-state.yaml` from main checkout if present.

Classify:

- no owned branch/PR/worktree record → fresh;
- owned branch, no PR → resume only when ownership matches;
- draft PR → resume build/gate cycle;
- ready PR → inspect coverage freshness;
- merged PR → set the task `done` if needed via the `tracker` skill and clean only recorded paths.

Suggest the user run `/rename ship <task> <slug>` once loaded.

## Fresh run

1. fetch origin;
2. check plan-base freshness: diff the plan's `PLAN_BASE_SHA` against fresh `origin/main`. Unrelated drift → continue. Drift touching plan anchors/dependencies → inspect those changes before building. Material contract or architecture drift → stop and return to `/sy:spec`;
3. branch from fresh `origin/main`;
4. create the dedicated build worktree in the sibling `<repo>-worktrees/` directory beside the repo (never inside it) and record its absolute path;
5. write local resume state:

```yaml
task: TASK-123
branch: task-123-example
worktree: /abs/path
plan_base_sha: <from ACTIVE plan>
ship_base_sha: <fresh origin/main>
process_tier: full
pr: null
head_sha: null
ci_green_sha: null
review_base_sha: null
reviewed_sha: null
target_sha: null
review_model_requested: null
review_model_observed: null
review_effort: max
accepted_deviations: []
phase_checkpoint: null
ship_session_id: <current session id if available>
ship_session_started_at: <timestamp>
agents_used: []
```

6. set the Task `in-progress` via the `tracker` skill, self-assign, and ensure the parent Epic is `in-progress`.

The state file is local resume state, not shared truth. Never prune unrelated worktrees or paths. `phase_checkpoint` is the active worker's idempotent resume anchor (e.g. a slice manifest with per-slice status), passed to any continuation worker.

Return `done` with the state brief; the parent dispatches BUILD.
