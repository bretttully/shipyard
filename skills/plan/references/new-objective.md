# NEW objective procedure

1. Light scope scan: direct read for a small surface; otherwise use `sy:sweep` enough to ask sharp questions.
2. Interview backwards from destination: objective/why, done-at-the-top, hard constraints, priorities. One shape-changing question at a time, via `AskUserQuestion` (`${CLAUDE_PLUGIN_ROOT}/skills/shared/references/user-interaction.md`).
3. Once nameable, suggest as a single optional aside (not a gate) that the user run `/rename plan: <objective-slug>`.
4. Draft the Epic body with:
   - North Star — objective, why, done-at-the-top;
   - Context / constraints;
   - Out of scope.
5. Show the draft, then close with `AskUserQuestion` (create as-is / revise / other); create only on that explicit approval. Use the `tracker` skill (`/sy:tracker`); new Epic starts `backlog`. If a portfolio parent exists, use the tracker's re-parent operation.
6. Continue with `roadmap-shaping.md`.
