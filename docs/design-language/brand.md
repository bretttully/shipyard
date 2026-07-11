# Brand identity

Who Shipyard is, how it sounds, and the shared visual vocabulary every image draws from. Colours, type, and the image-generation playbooks live in the sibling files ([`colour-and-type.md`](colour-and-type.md), [`prompts-backgrounds.md`](prompts-backgrounds.md), [`prompts-diagrams.md`](prompts-diagrams.md), [`prompts-logo.md`](prompts-logo.md)).

## 1. Brand essence and personality

Shipyard is a **working dry dock for software**. It takes an objective from *we should build this* to a merged, independently reviewed pull request, and it does so at **two tempos**: `/sy:plan` lays down a **living roadmap** up front and re-plots it as work ships, while beneath it a fast per-task loop — `/sy:spec`, `/sy:ship`, merge — repeats for each unit of work. Planning is not rerun for every task, but it is not a one-shot either: shipped evidence feeds the next planning round, the plotted route adapts, and only the north-star objective stays fixed. Claude builds and reviews; the human approves the plan and authorises the merge.

Three convictions give it its character, and every visual choice descends from them:

- **The immutable gate.** A separate `sy:gate` agent reviews the *exact commits* you are about to merge, in its own read-only checkout pinned to the pushed SHA, and every suspected bug must survive an attempt to refute it before it is reported. The PR head, the CI-green commit, and the reviewed commit must be the *same commit* before anything hands off or merges. You never review one thing and merge another.
- **Briefs, not transcripts.** Reading fifty files to answer one question happens inside a disposable agent; what comes back is a short brief of pointers backed by checkable evidence. The orchestrator stays clear-headed because it holds compact briefs, not everything it read.
- **A disciplined fleet with a full paper trail.** A crew of specialist subagents (`sweep`, `seam`, `trace`, `slice`, `hunt`, `gate`, and the `ship-*` workers) does the heavy lifting in sealed bays, each in its own context and model. The whole trail — plan, retrospective, token and outcome logs, transcript — is recorded on the tracker, so the *why* survives long after the diff is gone.

**Personality:** Disciplined · Exacting · Trustworthy · Industrial-nautical · Evidence-first.

**Voice:** Speaks like a master shipwright — calm and exacting, skeptical by design. It states what it verified, names the evidence, and lets nothing leave the dock unchecked. It is never breathless, never decorative; confidence comes from precision, not volume.

**Feeling the imagery should evoke:** a shipyard at night. Deep water, low key light, one warm beacon burning, instruments glowing on a dark bridge. Order and calm under load. Not sci-fi neon, not startup gradient optimism, not distressed grunge — considered, seaworthy, built to last.

## 2. Naming and wordmark

**Names.** The product is **Shipyard**; the plugin and CLI namespace is **`sy`**, surfaced in the command family `/sy:plan → /sy:spec → /sy:ship` (plus `/sy:spike`, `/sy:pr`, `/sy:ci`). "Shipyard" is the noun you say; `sy:` is the prefix you type. Both are part of the verbal identity — favour the real command strings in copy, set in mono.

**Wordmark.** "Shipyard" set in **Space Grotesk**, medium-to-bold weight, tight tracking (about `-0.02em`). Deep-hull black on light grounds, moonlit white on dark. Keep it plain; if a single accent is wanted, tint only the dot of the `i` or a trailing period in beacon coral — one spark, never the whole word. The lowercase short-mark **`sy`** (Space Grotesk, tightly set) is the compact identity for the plugin, the CLI, and cramped contexts.

**Mark direction.** The favicon / avatar is a rounded square on an **abyssal-midnight** ground (`#071A1C`), monoline in **harbor-light teal** with a single **beacon-coral** spark. Two candidate marks — a *harbour gate* with a coral keystone dot (the pinned commit passing the immutable gate) and a *beacon-over-waterline* with one coral dot and a faint sonar arc. The `sy` monogram is the safe fallback. Whichever is chosen, the rule holds: **abyssal ground, teal structure, exactly one coral spark.** Production prompts and output specs for all of these live in [`prompts-logo.md`](prompts-logo.md).

## 3. Iconography system

Icons are **precision instruments**, drawn to match Space Grotesk: geometric, constructed, calm. They are the counterpart to the atmospheric imagery — where hero art is for mood, icons are for exactness. This is also the icon vocabulary the [README diagrams](prompts-diagrams.md) draw one glyph per node from.

**Grid.** 24×24 canvas, 20×20 live area (2px padding all round). Favicon / 16px variants simplify to **at most two shapes** and drop interior detail.

**Stroke and geometry.** Consistent 2px stroke at the 24 grid. Square-cut caps, 2px outer corner radius (near-sharp, instrument-precise — not pill-rounded, not knife-sharp). Angles snap to 15° / 45° / 90°; arcs are true circular arcs struck from a visible centre (compass-and-dividers construction). One optical weight across the whole set; never mix filled and stroked icons in the same context.

**Two-tone rule.** Monoline in **harbor-light teal** (or slate on light) by default; the single *active / attention* element within an icon is coral — **at most one coral detail per icon**: **deep signal coral `#A83A22`** on light grounds, bright `#FF7F5E` on dark, so the spark clears the 3:1 non-text threshold either way. A contact sheet of several icon studies therefore shows one spark each, which is intended as long as the sheet does not read as coral-heavy. Filled variants use abyssal-teal fills with a coral spark.

**Domain motif vocabulary** — the shared kit of shapes, each with a suggested icon:

| Motif | Suggested icon | Attaches to |
|---|---|---|
| shipyard | gantry-and-slipway silhouette | the product mark, "the yard" |
| dock / dry-dock | a hull cradled in a basin (waterline + cradle) | the working context |
| crane / gantry | a gantry crane arm | build / in-progress |
| hull | a hull cross-section or prow | the artifact being built (the PR) |
| container | a shipping container | a compact brief, a unit of work |
| gate | two posts + lintel with a bar across; locked = keystone dot | the immutable gate, review |
| compass | compass rose / north star | `/sy:plan`, the roadmap's North Star |
| ledger / paper-trail | a bound logbook / stamped page | the tracker record |
| fleet | three chevron wakes / three hulls in formation | the agent fleet |
| beacon / lighthouse | a beacon with one arc of light | signals, the review verdict |
| sonar / ping | concentric arcs from a point | verification, detection, spikes |
| anchor | an anchor | backlog / anchored work |
| knot / shackle | a shackle or knotted line | a dependency (blocked-by) |

**Suggested icon per key concept:**

- `/sy:plan` → compass rose over a plotted chart course with a north star.
- `/sy:spec` → a stamped plan sheet with a wax-seal check.
- `/sy:ship` → a hull clearing the dock gate.
- `/sy:spike` → a sounding line / depth probe into the deep.
- immutable gate → the gate glyph with three short arrows converging on one coral keystone dot.
- agent fleet → three identical hull-chevrons in formation, one lamp lit.
- briefs-not-transcripts → a sealed container beside a crossed-out unspooled scroll.
- verification obligations → a checklist tag tied to a sonar ping.
- tracker seam → a shackle/coupling joining two different rails into one track.
- ship-states → a signal mast with flags, or five moored slips.

## 4. Concept → metaphor vocabulary

The atmospheric way to depict each idea (painterly-illustrative, not diagrammatic). These feed the hero and section art in [`prompts-backgrounds.md`](prompts-backgrounds.md). **Precise, labelled relationships are diagrams, not scenes** — those belong in [`prompts-diagrams.md`](prompts-diagrams.md), and the two must not be mixed (§3 there).

| Concept | Atmospheric image idea |
|---|---|
| The delivery model (`/sy:plan` once, then repeating `/sy:spec → /sy:ship`) | Two tempos in one frame, **not** a plan→spec→ship→plan conveyor. A persistent nautical chart on a raised table is the fixed centre — plotted once and re-plotted only when voyages report back. Vessels are drawn *from* the chart into a small two-berth dock — fit-out then launch past the gate — a cycle that repeats per vessel in the foreground. Faint sounding-lines run from returning vessels back to the chart; the north star above the table never moves. |
| The immutable gate | One sealed lock gate at the harbour mouth. Three thin beams of light converge to a single glowing coral point on the gate: HEAD, CI-green, and reviewed collapsing to one commit. |
| Briefs, not transcripts | A courier vessel carrying one sealed dispatch container across dark water, while a tangle of discarded paper is left behind on the dock. Compression made physical. |
| The agent fleet | A disciplined formation of small identical vessels crossing deep water at night, each with one lit lamp, all converging on a single harbour. |
| Verification obligations | An inspector on a gantry lowering a sonar / depth gauge against a hull below the waterline; a faint checklist glowing on the hull. |
| The roadmap | A nautical chart on a chart table under a low lamp: a plotted course with waypoints, a compass rose and north star, dividers and parallel rules. |
| Ship-states | A harbour status board or a signal mast; five moored positions from an anchored slip to open sea, one of them lit coral. |
| The tracker seam | A single modular coupling / shackle joining two different rail systems into one continuous track — the one pluggable part. |

Let the model paint the world, not annotate it: keep these scenes wordless and overlay any real labels yourself.
