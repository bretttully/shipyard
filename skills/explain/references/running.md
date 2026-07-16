# Running an explainer session

One layer per turn, in the doc's own order. Never paste the whole doc, and never dump remaining
layers even when asked to "just continue" twice — acknowledge faster instead.

## The checkpoint

End every layer with an `AskUserQuestion` call
(`${CLAUDE_PLUGIN_ROOT}/skills/shared/references/user-interaction.md`) — never a prose question
mark, which gets missed inside a longer turn. Offer:

- **Continue** — move to the next layer.
- **I have a question** — answer it in place, then re-offer the checkpoint before moving on.
- **Challenge this** — see below.
- **Skip ahead** — name which later layer answers it and let the choice of jumping stay theirs.

## A challenge is the most valuable event in the session

When the explainee pushes back ("I'm not satisfied by your WHY", "isn't this really about Z?"):
stop asserting, design the *discriminating* experiment — the one whose outcome differs between the
doc's claim and theirs — and run it live. If the evidence contradicts the doc, say so plainly
("your correction stands; my gloss was wrong"), fix the ground truth in the doc, and continue from
the corrected ground. Doc-defensiveness destroys the session; a visible correction is what makes
the rest of the doc credible.

## The explainee's own ideas are first-class hypotheses

When they propose a fix or reframing mid-session, test it live with the same rigor as the doc's own
options before comparing it to them. Two disciplines when it wins:

- enumerate the full requirement set before declaring it proven — write the requirements down and
  check each one; a passing demo of six cases says nothing about the seventh (read paths, write
  paths, bypass paths, isolation, ordering);
- say clearly which parts of the doc it obsoletes.

## Closing

Restate the decision made (or explicitly left open) and what happens next. Never read or write the
tracker — nothing about this session belongs on the ticket.
