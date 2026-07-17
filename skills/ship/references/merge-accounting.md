# Explicit merge path

Load only after the user directly authorizes merge. The authorization is the informed go-ahead front-loaded in the handoff `## Action needed` block, which named the follow-on mutations: this path will merge the verified head, attach the scanned transcript, and set the task done. Execute exactly those three and no more; a mutation the consent point did not name is not covered by this authorization.

## Revalidate

1. reread PR head and required checks;
2. verify current head equals `CI_GREEN_SHA` and `REV_REVIEWED_SHA`;
3. fetch and compare the current target branch against recorded `TARGET_SHA`. If the target moved: disjoint, uncoupled drift → proceed and note it in the handoff; overlapping or plausibly coupled drift → refresh CI against the current merge result and open a new immutable review scope when reviewed files interact. Target drift never silently downgrades coverage;
4. verify recorded `REVIEW_BASE_SHA`, requested review model, standalone usage comment, standalone ship-metrics comment, and transcript attachment (full tier);
5. inspect the usage JSON's `by_agent` entry for `sy:gate` and record the transcript-observed gate model in local state/handoff. If the observed model conflicts with the requested model, stop and investigate rather than claiming the requested reviewer ran;
6. if the same ship session is active and substantial post-handoff agent work occurred, regenerate full-tree usage JSON and post a new standalone `# Claude Code usage` comment rather than editing it into another comment;
7. refresh/rescan the transcript attachment when appropriate (full tier). If merge runs in another session, preserve the original ship transcript and record merge execution separately.

Follow the `tracker` skill's attachment flow for the deterministic `gitleaks` scan, contextual review, redaction, upload, and verification.

## Merge

Merge atomically against the verified head:

```bash
gh pr merge <pr> --match-head-commit "$VERIFIED_HEAD_SHA" <chosen strategy flags>
```

Then verify merged state, set the task `done` via the `tracker` skill, and remove only build/slice/review worktrees and branches recorded by this run.

Explicit merge authorization never waives stale CI or review coverage.
