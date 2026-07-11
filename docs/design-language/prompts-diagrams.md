# ChatGPT prompt — Shipyard README diagrams

> **How to use:** attach `brand.md`, `colour-and-type.md`, `README.md`, and `docs/img/agent-fleet.png` (a *density/layout* reference only — its colours and fonts are deliberately not the target), then paste **everything below the line** as your first message to ChatGPT. The model returns a 3-option look book first; you pick one; it then produces the whole set in the chosen style.

---

You are producing the labelled **diagrams** for Shipyard, a Claude Code plugin. These are the flat, technical, card-and-arrow images embedded beside the README prose — not atmospheric scenes.

I have attached:

- **`brand.md`** — the brand identity and the monoline icon vocabulary;
- **`colour-and-type.md`** — the Deep Fleet palette (see §1.6 "Diagram colour roles") and the type system;
- **`README.md`** — what Shipyard is and what each diagram depicts;
- **`agent-fleet.png`** — an example of the target **structure, density, and label legibility only**: flat cards of consistent size, one monoline icon per card, short legible labels, sparse arrows, generous whitespace. **Copy its layout and density — do NOT copy its colours or fonts.** That example uses a bright royal blue and its own typeface; ignore both. Take every colour from the "Colour roles" section below and all type direction from the attached `colour-and-type.md`. (Correcting that royal blue to periscope indigo is one of the reasons for this redraw, so matching the example's colour would defeat the purpose.)

Read all four attachments before drawing anything.

## Work in two phases

**Phase 1 — look book. Do this first, then stop.**
Produce **three variations of a single diagram — the `delivery-loop`** (spec below), presented together as options 1, 2, and 3. Between the three, vary only the *presentation*: card corner radius, border weight, icon treatment (pure stroke vs. a hairline-filled panel), label placement, arrow style, and ground tint. Keep the palette and the four colour roles **identical** in all three. Then **stop and ask me to choose. Do not draw any other diagram yet.**

**Phase 2 — the full set. Only after I pick an option.**
When I reply with the chosen option number, lock that exact card system — same radius, borders, icons, type, spacing, arrows — and reproduce it across **every diagram in "The diagrams" section below**. They must look like one consistent set. Deliver each as its own image.

## The rules (apply to every diagram — these are firm)

**The prose carries the nuance; the diagram carries the skeleton.** The README sentence beside each image already carries the detail. Each diagram shows the *one* relationship that sentence is about — do not restate every rule, exception, or invariant as a visible element, and do not visualise every sentence.

Every diagram **must**:

- carry **one primary idea**;
- use **5–7 major nodes maximum**;
- give each node **one simple monoline icon** from the attached icon vocabulary;
- use **short labels only** — one to three words, or a real command / token in monospace;
- follow a **single reading path**, left-to-right or top-to-bottom, with **minimal branching**;
- leave **generous whitespace**;
- use **flat cards of consistent size** — white on a light sea-mist ground (or deep-water teal panels on an abyssal ground for a dark variant) — with **thin borders in the node's role colour**;
- use **coral for exactly one thing**: the single gated or exceptional action.

Every diagram **must not**:

- combine workflow, architecture, state transitions, evidence flow, and exception handling in one image;
- carry explanatory captions *inside* the frame (one short caption *beneath* the whole image is fine);
- contain decorative nautical scenery — no water, docks, beacons, fleets, gradients, or grain (that is atmospheric art, not a diagram);
- nest cards inside cards, or stack multiple footer bands / metadata regions;
- add concepts implied by the prose but not needed to understand the one idea.

If a diagram cannot be reduced to the ceiling above, **split it into two images** rather than cramming it.

## Colour roles (from `colour-and-type.md` §1.6 — use only these tokens)

- **teal** (`#0F5B5E` light / `#4FB8B0` dark) — specialist agents, build substance, generic structure. This is the default and most-used.
- **periscope indigo** (`#5B6BC7` light / `#8A98F0` dark) — the orchestration / command layer: the `/sy:` commands, the dispatcher, handoff.
- **coral** (`#A83A22` light / `#FF7F5E` dark) — the **one** gated or exceptional action per diagram (a gate, a merge, a bail-out).
- **delivered-wake green** (`#2FB37A`) — done / success / merged.

Do not use a bright royal "tech blue" — the orchestration colour is periscope indigo. Steer by these names; treat the hex as a secondary hint and correct any drift.

## The look, in words

A flat, precise technical diagram — a compositional system of identical cards, **not** an illustration or a scene. Clean vector look on a plain light sea-mist ground (near `#EEF2F1`), or a plain abyssal ground (`#071A1C`) for the dark variant. Cards are flat white (deep-water teal panels on dark) with a thin ~2px border and a small rounded radius; all cards share the same dimensions. Monoline icons at an even 2px weight, geometric, one per card. Short labels only, clean sans-serif, with commands and tokens in monospace. Sparse thin arrows, one reading direction. Generous whitespace. No scenery, no gradients, no grain, no shading, no nested cards, no captions inside the frame, no garbled or long text.

## The diagrams

### `delivery-loop` — *(this is the Phase 1 look-book subject)*

One idea: plan once, then repeat the per-task loop. An indigo card **`/sy:plan`** (compass icon) sits above a left-to-right row of indigo cards **`/sy:spec`** (stamped sheet) → **`/sy:ship`** (hull) ending in one **coral** card **`merge`** (gate icon). A single thin arrow loops from `merge` back to the start of the row to show it repeats per task. Four cards on the loop plus the plan card. No roadmap internals, no spike feeder, no evidence-feedback details.

### `immutable-gate`

One idea: three inputs collapse to one commit, which then hands off and merges. Three small **teal** cards on the left — `PR HEAD`, `CI-GREEN`, `REVIEWED` (mono labels) — with thin arrows converging on one **coral** card `gate` (shield icon). From the gate, one arrow to an **indigo** `handoff` card (two-figures icon), then one arrow to a **coral** `merge` card (key icon). Six cards, left-to-right, one convergence. No worktree bands, no fix-cycle loop, no prohibition symbol, no `TARGET_SHA` panel.

### `compression-boundary`

One idea: many files go in, one brief comes out. On the left, one **teal** card holding a small simple grid of file glyphs labelled `many files`. One arrow into a **teal** card `disposable worker` (layers icon). One arrow out to a small card `compact brief` (container icon). One arrow to an **indigo** `parent` card. Four cards, strictly left-to-right, one path. No `SPLIT_REQUIRED` exception card, no scattered file-web, no "caller verifies" panel.

### `jira-roadmap`

One idea: an Epic holds a few active tasks; everything further out is one muted block. One **indigo** `Epic` card at the top labelled `living roadmap`. Below it, a row of up to four identical **teal** `Task` cards (checklist icon) under a small bracket labelled `≤ 4 active`. To their right, **one** muted grey block labelled `future work` standing in for everything not yet specced. A single thin line joins the Epic to the active tasks. No "conceptual" row, no crossed-out decomposed card, no extra task columns.

### `verification-obligations`

One idea: each obligation is a claim, its evidence, and the check. Two or three identical horizontal rows, each with three small cards left-to-right: a **teal** `claim` card (document icon) → a **teal** `evidence` card (ledger icon) → a **green** `check` card (shield-check icon), joined by thin arrows. The rows are stacked and identical. One short caption beneath: `undischarged = finding`. No per-command band, no risk-lens card.

### `ship-states`

One idea: the dispatcher runs three workers, then hands off and merges, with a few exception states. An **indigo** `/ship` dispatcher card on the left → a grouped row of three **teal** worker cards `ship-start`, `ship-build`, `ship-gate` (flag / code / shield icons) → an **indigo** `handoff` card → a **coral** `merge` card (key icon). Below the row, three or four small exception-state cards on thin dashed arrows — `done` (green), `needs-decision`, `blocked`, and one **coral** `bail-to-spec`. One short caption beneath: `parent holds briefs, not history`. Keep it exactly this sparse.

### `agent-fleet`

One idea: the specialist fleet plus the grouped `/sy:ship` workers. **Match the attached `agent-fleet.png` for layout and density** — same card grid, same spacing — but apply the colours and type from this brief, not the example's (its blue becomes periscope indigo). A top row of six identical **teal** specialist cards — `sweep`, `seam`, `trace`, `slice`, `hunt`, `gate` — each with one icon, one role word (breadth / boundary / path / build / bugs / verdict), one monospace `model / effort` line, and a small budget chip. Below, an **indigo** `/ship` card with an arrow into a dashed group of three worker cards `ship-start`, `ship-build`, `ship-gate` in the same format. The `gate` card carries the one **coral** spark on its shield.

## Output

- Deliver each diagram as its own image at roughly 1600×900 (a 16:9-ish frame), consistent across the set.
- Keep labels to 1–3 words; if any label comes out garbled, redo that image rather than leaving drift — the text must be legible.
- If you can, also render each on a **transparent** ground (or a dark `#071A1C` variant) so the diagrams can sit on a theme-aware web page without a white box around them.
