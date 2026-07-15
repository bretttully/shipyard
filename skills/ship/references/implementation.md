# Implement and integrate

Follow ordered plan decisions. Resolve small details consistent with plan intent yourself and record them in `accepted_deviations`. A decision you cannot ground in plan/standards/code but that does not invalidate the plan returns `needs-decision` with an updated checkpoint; a new load-bearing fork or an invalidated contract returns `bail-to-spec`. Never prompt the user. Use `sy:sweep` for broad reconnaissance.

## Delegated slice protocol

Delegate only bounded, low-design-ambiguity slices:

1. create and record the dedicated slice branch/worktree from the integration base, in the sibling `<repo>-worktrees/` directory (never inside the repo);
2. prompt `sy:slice` with plan step, anchors, acceptance criteria, sibling interfaces, and relevant standards contract;
3. add `sy:slice` to local `agents_used` accounting state;
4. receive committed SHA and compact evidence brief;
5. inspect diff and decisive spans;
6. cherry-pick into build branch;
7. run integration-relevant tests;
8. remove only the exact recorded slice worktree/branch after successful integration.

Track build progress as a slice manifest in `phase_checkpoint` (per slice: `pending|committed|integrated`, with SHAs), updated after each integration, so a `needs-decision` return resumes at the next pending slice and re-does no integrated work.

After integration, run acceptance tests and standards-required formatter/linter/type checks; route verbose runs (full suite, linters, type checks) through `.scratch/` logs and read back only failures and summary lines, keeping raw output out of the ship context. Discharge every verification obligation with its named evidence; an undischargeable obligation returns to `/sy:spec`. Where acceptance criteria describe observable behaviour, execute the behaviour (a `.scratch/` runner is fine) and capture the output as acceptance evidence — tests alone discharge only test-shaped criteria.

When a plan step produces, regenerates, or selects among images (figures, screenshots, plots, marketing visuals), inspect them by fanning out to `sy:img-inspector` per `${CLAUDE_PLUGIN_ROOT}/skills/shared/references/image-inspection.md`: resolve `IMAGE_MODEL=${SY_IMAGE_MODEL:-sonnet}`, dispatch the inspector with the path(s) and the inspection task, add it to `agents_used`, and record the returned text verdicts as the figure's acceptance evidence. Never `Read` a raw image into the build context; the text verdicts drive accept / regenerate / reselect.

Every load-bearing claim the brief will assert — diff scope, invariants preserved, "nothing else affected", lockfile/dependency effects, verification outcomes — carries a checkable pointer (the command run and where its output lives), never a bare assertion; a claim you cannot back is not `done`. Verify a claim about a generated or dependency artifact (lockfile hash, `depends`/`run_exports`, package moves) against the artifact itself, not against intent.

Then commit/push and open a draft PR through `/sy:pr draft`; Task remains `in-progress`. Return `done` with the updated state brief; the parent dispatches GATE.
