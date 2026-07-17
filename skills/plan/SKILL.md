---
name: plan
description: >-
  Turn a large objective or existing Epic into a living roadmap with at most four
  active /sy:spec-ready Tasks, real seams, dependency order, and flat tracker execution.
argument-hint: "[large objective or existing epic key (<epic>)]"
disable-model-invocation: true
effort: high
---

Build or revise one **living Epic roadmap**. The Epic body owns conceptual depth; executable Tasks/Bugs remain direct children. End at the roadmap and `/sy:spec` handoffs. Never implement or spec leaves.

Plan against fresh `origin/main` unless the user names another base. Work code read-only. Tracker writes use the `tracker` skill (`/sy:tracker`).

$ARGUMENTS

## Invariants

- Work backwards: North Star → capabilities → dependency order → near executable leaves.
- At most **4** leaves may be active `/sy:spec`-ready/in-spec/in-ship/in-review at once.
- One Task/Bug ≈ one coherent PR. Keep far work conceptual until evidence justifies decomposition.
- Not every issue surfaced mid-ship earns its own leaf: a small, adjacent, low-risk fix folds into the current PR as a recorded scope extension, and a follow-up must justify itself against that (see `${CLAUDE_PLUGIN_ROOT}/skills/shared/references/scope-discipline.md`).
- Objective is stable; path is provisional and should adapt to shipped evidence.
- Flat tracker execution, fractal conceptual map.
- Ask one question at a time, via `AskUserQuestion`, only when the answer changes seam, sequence, blocker, or outcome — see `${CLAUDE_PLUGIN_ROOT}/skills/shared/references/user-interaction.md`. At an approval point that authorizes tracker writes, name the mutations the go-ahead covers — create/edit the Epic, create/edit its children, and post the plan checkpoint — so auto-mode consent is informed rather than a bare "proceed".

## Scope and delegation

Read small cohesive evidence directly. Use `sy:sweep` for large code/ticket/PR/docs surfaces and `sy:seam` only for one unresolved boundary that changes roadmap shape. At most 3 depth agents in flight. Agent returns are compressed leads; verify decisive spans and own the cut.

Seed every agent prompt with known anchors — paths, symbols, entry points, keys — and name ground already covered; agents must not rediscover what the caller knows.

Machine-facing agent briefs stay pointer-dense. Human-facing Epic maps and decision logs remain clear prose.

## State router

Classify before loading detailed procedure:

```text
NEW       objective, no Epic yet        → references/new-objective.md
REENTRY   existing Epic                 → references/reentry.md
SHAPING   evidence gathered             → references/roadmap-shaping.md
CAPTURE   roadmap decisions settled     → references/checkpoint-handoff.md
```

Load only the reference for the current state. Do not preload mutually exclusive procedures.

## Completion bar

The Epic body must show North Star, conceptual horizon ladder, completed branches, current active set (≤4) with keys/kickoffs, queued conceptual work, critical path, blockers, and parallel-safe set. Every planning run that changes the tracker adds one decision-log delta ending in a `Plan checkpoint` footer, and delegates a subagent to render this session's transcript and attach it to the Epic, following the `tracker` skill's attachment flow (`$KIND=plan`). A roadmap entry or checkpoint that shipped evidence later overrules is corrected on its own surface, not left stale — the retroactive-honesty invariant in `${CLAUDE_PLUGIN_ROOT}/skills/shared/references/write-integrity.md`; and when the transcript-attach delegation is denied under auto-mode, the identical render-and-attach may run inline as that reference's authorized-alternate-route fallback, the rendered text handled by path only — deterministic scan only, no contextual review, so treat a clean result as evidence, not proof, per the `tracker` skill's attachment flow.

When every horizon is delivered and every child is `done` for delivered reasons, set the Epic `done`.
