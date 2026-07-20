# Proposer/adversary debate

Some plan and spec decisions have two comparably strong candidates and no amount of further reading resolves which is right — the fork is genuinely contested, not merely unresearched. For exactly that case, `/sy:plan` and `/sy:spec` can pressure-test the contested premise or approach with `sy:debate`, which runs a bounded proposer/adversary exchange and returns only the synthesized disagreement — never the raw rounds — for the user to steer (see `${CLAUDE_PLUGIN_ROOT}/skills/shared/references/user-interaction.md`, Question mode). Like `sy:sweep`, `sy:seam`, and `sy:img-inspector`, the raw work stays inside the delegate; only a compressed lead comes back.

## When to run it

After the normal research pass (sweep/seam/trace as applicable), check whether a genuine fork remains: two or more approaches that are each individually defensible, where picking wrong is expensive to reverse once the roadmap or plan commits to it. Skip it for routine roadmap updates, a case where research already produced a clearly dominant option, or a small, reversible, low-stakes call — those get decided directly or, if they turn on something only the user can weigh, go straight to a `Question`. This bar is a starting calibration, not a fixed ceiling — loosen or tighten it based on how the debate's findings land in practice.

## Dispatch it

```text
DEBATE_MODEL=${SY_DEBATE_MODEL:-opus}
```

Dispatch `sy:debate` once, foreground, with the explicit `model` override `DEBATE_MODEL` (an `Agent` call does not inherit the parent's model) plus, in the prompt itself:

- the contested premise or approach as a single neutral sentence, not pre-weighted toward either side;
- the seed evidence already gathered — paths, findings, anchors — so it isn't rediscovered;
- the literal `DEBATE_MODEL` string, for `sy:debate` to forward to its own nested dispatches.

Raise `DEBATE_MODEL` (e.g. to the frontier tier, `${SY_FRONTIER_MODEL:-fable}`) for a fork whose blast radius justifies the extra cost; the default floor is opus because this is a judgment task, not a lookup.

## Hand it back

`sy:debate` returns `AGREE` / `CONTESTED` / `READ` (see `${CLAUDE_PLUGIN_ROOT}/agents/debate.md`). Present it as a status update, then close with a single `AskUserQuestion` naming the real candidate options from `CONTESTED` — never a summary that quietly picks a winner; this is a `Question`-mode fork per `user-interaction.md`, not a status update with a question folded in. Record the outcome durably on whichever surface the caller already writes decisions to: `/sy:plan` folds it into the roadmap decision-log delta; `/sy:spec` folds the adversary's strongest objection into the plan's "strongest rejected alternative and why" and any resulting risk into "risks/edge cases." The debate transcript itself is never attached — only `sy:debate`'s synthesis and the user's steer are durable.
