# Existing Epic re-entry

Reconstruct the delta, not total history:

1. read current Epic body;
2. read decision-log comments since the last `Plan checkpoint`;
3. list child Tasks/Bugs and read retrospectives plus standalone usage logs from items `done` since that checkpoint;
4. inspect current non-terminal leaves, statuses, and blockers;
5. open older PRs/comments only when a current shape decision cannot be settled from durable summaries.

Use `sy:sweep` for large tails; direct-read small cohesive ticket text. Suggest, as a single optional aside (not a gate), that the user run `/rename plan <epic> <slug>` once loaded.

## Reconcile leaves

Classify every non-terminal leaf: `active`, `still valid`, `blocked`, or `superseded`.

For superseded/decomposed work: draft replacements under the same Epic, obtain approval via `AskUserQuestion`, then follow the tracker's canonical decomposition (see the `tracker` skill). Represent the old Task as a conceptual parent branch over replacements. Never leave old and replacement work simultaneously actionable.

Continue with `roadmap-shaping.md`.
