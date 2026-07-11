# Shipyard visual language

The identity for Shipyard and the `sy` plugin, and the source of truth for generating on-brand documentation imagery. Chosen direction: the **Deep Fleet** palette with the **Space Grotesk / Inter / JetBrains Mono** type pairing — a calm, oceanic ground lit by a single warm beacon, set in exacting, developer-native type. The night bridge, read by precision instruments.

This document is the *language*, not the pictures. It exists so that a human, or an image model like ChatGPT, can produce covers, hero art, textures, and icon studies that all look like they came from the same yard. It intentionally does not depend on any imagery currently in `docs/img/`.

---

## 1. Brand essence and personality

Shipyard is a **working dry dock for software**. It takes an objective from *we should build this* to a merged, independently reviewed pull request, and it does so at **two tempos**: `/sy:plan` lays down a **living roadmap** up front and re-plots it as work ships, while beneath it a fast per-task loop — `/sy:spec`, `/sy:ship`, merge — repeats for each unit of work. Planning is not rerun for every task, but it is not a one-shot either: shipped evidence feeds the next planning round, the plotted route adapts, and only the north-star objective stays fixed. Claude builds and reviews; the human approves the plan and authorises the merge.

Three convictions give it its character, and every visual choice below descends from them:

- **The immutable gate.** A separate `sy:gate` agent reviews the *exact commits* you are about to merge, in its own read-only checkout pinned to the pushed SHA, and every suspected bug must survive an attempt to refute it before it is reported. The PR head, the CI-green commit, and the reviewed commit must be the *same commit* before anything hands off or merges. You never review one thing and merge another.
- **Briefs, not transcripts.** Reading fifty files to answer one question happens inside a disposable agent; what comes back is a short brief of pointers backed by checkable evidence. The orchestrator stays clear-headed because it holds compact briefs, not everything it read.
- **A disciplined fleet with a full paper trail.** A crew of specialist subagents (`sweep`, `seam`, `trace`, `slice`, `hunt`, `gate`, and the `ship-*` workers) does the heavy lifting in sealed bays, each in its own context and model. The whole trail — plan, retrospective, token and outcome logs, transcript — is recorded on the tracker, so the *why* survives long after the diff is gone.

**Personality:** Disciplined · Exacting · Trustworthy · Industrial-nautical · Evidence-first.

**Voice:** Speaks like a master shipwright — calm and exacting, skeptical by design. It states what it verified, names the evidence, and lets nothing leave the dock unchecked. It is never breathless, never decorative; confidence comes from precision, not volume.

**Feeling the imagery should evoke:** a shipyard at night. Deep water, low key light, one warm beacon burning, instruments glowing on a dark bridge. Order and calm under load. Not sci-fi neon, not startup gradient optimism, not distressed grunge — considered, seaworthy, built to last.

---

## 2. Naming, wordmark, favicon, avatar

**Names.** The product is **Shipyard**; the plugin and CLI namespace is **`sy`**, surfaced in the command family `/sy:plan → /sy:spec → /sy:ship` (plus `/sy:spike`, `/sy:pr`, `/sy:ci`). "Shipyard" is the noun you say; `sy:` is the prefix you type. Both are part of the verbal identity — favour the real command strings in copy, set in mono.

**Wordmark.** "Shipyard" set in **Space Grotesk**, medium-to-bold weight, tight tracking (about `-0.02em`). Deep-hull black on light grounds, moonlit white on dark. Keep it plain; if a single accent is wanted, tint only the dot of the `i` or a trailing period in beacon coral — one spark, never the whole word. The lowercase short-mark **`sy`** (Space Grotesk, tightly set) is the compact identity for the plugin, the CLI, and cramped contexts.

**Favicon / avatar direction (to be produced later, described here in words).** A rounded square on an **abyssal-midnight** ground (`#071A1C`). Two candidate marks, both constructed on the icon grid in §5, both monoline in **harbor-light teal** with a single **beacon-coral** spark:

- *Gate mark* — two vertical posts and a lintel (a harbour gate), with a single coral dot at the keystone: the pinned commit passing the immutable gate. Reads at 16px as "a gate with one lit point."
- *Beacon-over-waterline mark* — a low teal waterline with a single coral beacon dot and one faint sonar arc rising from it: the fleet's one warm signal on dark water.

The `sy` monogram is the safe fallback favicon. Whichever is chosen, the rule holds: **abyssal ground, teal structure, exactly one coral spark.**

---

## 3. Colour palette — Deep Fleet

Cool teal is the workhorse; the warm **coral** accent is the point of attention, applied with a discipline that scales by medium (§3.5) — a single focal point in a picture, at most one detail per icon, functional repeats only in UI and docs. Sonar phosphor-green is a sparing highlight, not a second accent. All ratios below are measured against WCAG; treat them as binding.

Image models *can* accept hex, but they do not reproduce exact colour values reliably. So every colour also carries a plain-English name: steer image prompts with the prose names as the primary mechanism (use them verbatim, §8), pass hex only as a secondary hint, and correct any critical colour during composition or post-processing. For code and design tokens the hex is authoritative.

### 3.1 Core and neutrals

| Role | Prose name (use in prompts) | Light hex | Dark hex | Notes |
|---|---|---|---|---|
| Primary | abyssal fleet teal / harbor-light teal (dark) | `#0F5B5E` | `#4FB8B0` | Headings, primary fills, instrument glow. Light 6.9:1, dark 7.5:1 on ground. |
| Accent — functional | deep signal coral (light) / lit beacon coral (dark) | `#A83A22` | `#FF7F5E` | The one warm signal for text, links, icon sparks, focus rings, borders, status dots. Clears AA with margin: light 5.65:1 (6.4:1 on white), dark 7.2:1. |
| Accent — glow | beacon coral | `#EE6C4D` | `#FF7F5E` | The beacon *light itself*: imagery, hero art, and large fills where text sits on top. Not for small text/icons on light (2.7:1). |
| Highlight | sonar phosphor-green | `#2FB37A` | `#4DE8A6` | Sparing — success, "delivered", a detection ping. Never a second accent. |
| Background | sea-mist grey / abyssal midnight (dark) | `#EEF2F1` | `#071A1C` | Page/canvas ground. |
| Surface | spume white / deep-water panel (dark) | `#FFFFFF` | `#0E2A2C` | Cards, raised panels. |
| Border | tide line / bioluminescent line (dark) | `#CBD8D6` | `#1C4143` | Hairlines, dividers. |
| Muted text | slate teal / seafoam grey (dark) | `#4E6462` | `#8FA8A5` | Secondary text. Light 5.6:1, dark 7.1:1. |
| Text | deep-hull black / moonlit white (dark) | `#0C1B1C` | `#E8F1EF` | Body text. 15.6:1 on ground; 17.7:1 (light) / 13.2:1 (dark) on surface. |

**The accent is one signal with two values, chosen by job — not one hex forced across both themes.** On dark, `#FF7F5E` does everything (7.2:1). On light, use **deep signal coral `#A83A22`** for anything functional — text, links, icon sparks, focus rings, borders, status dots — and reserve bright **beacon coral `#EE6C4D`** for large fills and atmospheric washes where legibility rides on the foreground, not the background. Generated imagery is *always* the bright glow (§8) — it lives on dark grounds where the glow is the point; the deep value is a screen-and-print concern, not a picture concern.

### 3.2 Lifecycle columns

The five tracker columns, mapped to a vessel's progress from the hard to open sea. Each maps to a canonical status token in the [tracker contract](../skills/tracker/CONTRACT.md); the names are Shipyard's, the board labels are per-repo.

| Column | Prose name | Light hex | Dark hex | Meaning |
|---|---|---|---|---|
| backlog | anchored slate | `#5B7377` | `#7E9A9C` | queued on the hard, not yet specced |
| ready | harbor teal | `#1F9E9E` | `#3FC4C4` | specced, provisioned, ready to build |
| in-progress | underway coral | `#A83A22` | `#FF7F5E` | active build — the vessel is underway (the coral accent; work-in-progress *is* the warm signal). Large fills may use the bright glow `#EE6C4D`. |
| in-review | periscope indigo | `#5B6BC7` | `#8A98F0` | a reviewable gated PR exists, under inspection |
| done | delivered-wake green | `#2FB37A` | `#4DE8A6` | merged, terminal — the wake left behind |

### 3.3 Semantic

| Role | Prose name | Light hex | Dark hex |
|---|---|---|---|
| success | delivered-wake green | `#2FB37A` | `#4DE8A6` |
| warning | signal amber | `#E8A33D` | `#F6BB57` |
| danger | distress red | `#E24C4B` | `#FF6B69` |

Success shares its hue with `done` (delivery *is* success) and in-progress shares its hue with the accent (work underway *is* the warm signal) — both overlaps are intentional and meaningful, not collisions. Warning and danger are distinct hues reserved for genuine alarm; do not use them decoratively.

### 3.4 The palette is truest on dark

Deep Fleet is a dark-first identity. On the abyssal-midnight ground the teal instruments and the coral beacon both clear 7:1 and the whole thing sings — prefer dark grounds for hero and atmospheric imagery. Use the light sea-mist ground for documentation body and anything a reader must scan for a long time. In light, reach for **deep signal coral `#A83A22`** wherever coral must be legible (text, icons, focus, borders — 5.65:1) and keep bright **beacon coral `#EE6C4D`** for large fills and washes; the bright glow is the value used in all generated imagery, which lives on dark grounds.

### 3.5 Coral discipline (scales by medium)

The warm coral is the identity's one deliberate risk, and how strictly "one" is enforced depends on the medium:

- **Atmospheric hero art, covers, conceptual illustrations** — exactly **one** warm coral focal point in the entire composition; everything else is teal and neutral. A lone beacon does the most work.
- **Individual icons and marks** — at most **one** coral detail per icon (the single active/attention element). A contact sheet of many icon studies therefore shows several sparks, one per icon — intended, provided the sheet as a whole does not read as coral-heavy.
- **UI, documentation, and precise diagrams** — coral may **repeat** where it carries functional meaning (links, active states, status dots, the in-progress column, a call-to-action), but only one element should be visually dominant at a time, and teal stays the workhorse. If a screen starts to feel coral-heavy, demote the least-important coral back to teal.

Across all three, teal is the constant and coral is the exception that earns attention. Bright beacon coral is the *glow* (atmospheric and large fills); deep signal coral is the *ink* (functional, on light grounds) — see §3.1.

---

## 4. Typography

Open-license throughout (SIL OFL 1.1). The pairing reads as *precise instruments on a calm bridge*: a geometric grotesk for structure, a neutral humanist for reading, a developer mono that carries the machinery — SHAs, `sy:` commands, CI and tracker output.

| Role | Typeface | License | Used for |
|---|---|---|---|
| Display / headings | **Space Grotesk** | SIL OFL 1.1 | H1–H3, wordmark, big numerals. Weights 500 / 700. Tight tracking at large sizes. |
| Body | **Inter** | SIL OFL 1.1 | Running text, UI. Weights 400 / 600. ~65-character measure, 1.6 line-height. |
| Mono | **JetBrains Mono** | SIL OFL 1.1 | Code, SHAs, command strings, tracker/CI logs, uppercase micro-labels. Weights 400 / 700. |

**Font stacks (for any web surface):**

```css
--font-head: "Space Grotesk", ui-sans-serif, system-ui, sans-serif;
--font-body: "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
--font-mono: "JetBrains Mono", ui-monospace, "SF Mono", Menlo, Consolas, monospace;
```

**Type scale** (base 16px, modular):

| Role | Size | Line-height | Setting |
|---|---|---|---|
| Display | 48px / 3rem | 1.05 | Space Grotesk 700, `-0.02em` |
| H1 | 34px / 2.125rem | 1.1 | Space Grotesk 700, `-0.015em` |
| H2 | 24px / 1.5rem | 1.2 | Space Grotesk 500–700 |
| H3 | 19px / 1.1875rem | 1.3 | Space Grotesk 500 |
| Body | 17px / 1.0625rem | 1.6 | Inter 400 |
| Small | 14px / 0.875rem | 1.5 | Inter 400 |
| Label | 12px / 0.75rem | 1.4 | JetBrains Mono 500, uppercase, `+0.1em` |
| Code | 15px / 0.9375rem | 1.6 | JetBrains Mono 400 |

**Rules.** Stay on the scale — do not freestyle sizes. Uppercase mono micro-labels (eyebrows, column headers, metadata) are a signature; give them the `+0.1em` tracking. Set all commands, SHAs, and log output in mono, never in body. Give headings `text-wrap: balance`.

**Embedding note.** The style board embeds these faces as base64 `@font-face` data URIs so it needs no network. Reuse that technique for any self-contained HTML artifact (the Artifact CSP blocks external font hosts); the woff2 files come from the `@fontsource` packages for each family.

---

## 5. Iconography system

Icons are **precision instruments**, drawn to match Space Grotesk: geometric, constructed, calm. They are the counterpart to the atmospheric imagery — where photos and hero art are for mood, icons are for exactness.

**Grid.** 24×24 canvas, 20×20 live area (2px padding all round). Favicon/16px variants simplify to **at most two shapes** and drop interior detail.

**Stroke and geometry.** Consistent 2px stroke at the 24 grid. Square-cut caps, 2px outer corner radius (near-sharp, instrument-precise — not pill-rounded, not knife-sharp). Angles snap to 15° / 45° / 90°; arcs are true circular arcs struck from a visible centre (compass-and-dividers construction). One optical weight across the whole set; never mix filled and stroked icons in the same context.

**Two-tone rule.** Monoline in **harbor-light teal** (or slate on light) by default; the single *active / attention* element within an icon is coral — **at most one coral detail per icon** (§3.5): **deep signal coral `#A83A22`** on light grounds, bright `#FF7F5E` on dark, so the spark clears the 3:1 non-text threshold either way. A contact sheet of several icon studies therefore shows one spark each, which is intended as long as the sheet does not read as coral-heavy. Filled variants use abyssal-teal fills with a coral spark.

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

---

## 6. Visual metaphors — concept → image idea

For hero and atmospheric art (photographic-illustrative or painterly, not diagrammatic). These are the compositions to reach for; §8 turns them into prompts.

| Concept | Image idea |
|---|---|
| The delivery model (`/sy:plan` once, then repeating `/sy:spec → /sy:ship`) | Two tempos in one frame, **not** a plan→spec→ship→plan conveyor. A persistent nautical chart on a raised table is the fixed centre — plotted once by `/sy:plan` and re-plotted only when voyages report back. Vessels are drawn *from* the chart into a small two-berth dock — fit-out (`/sy:spec`) then launch past the gate (`/sy:ship`) — a cycle that repeats per vessel in the foreground. Faint sounding-lines run from returning vessels back to the chart, occasionally redrawing the course; the north star above the table never moves. |
| The immutable gate | One sealed lock gate at the harbour mouth. Three thin beams of light — labelled in your own overlay, not by the model — converge to a single glowing coral point on the gate: HEAD, CI-green, and reviewed collapsing to one commit. |
| Briefs, not transcripts | A courier vessel carrying one sealed dispatch container across dark water, while a tangle of discarded paper is left behind on the dock. Compression made physical. |
| The agent fleet | A disciplined formation of small identical vessels crossing deep water at night, each with one lit lamp, all converging on a single harbour. |
| Verification obligations | An inspector on a gantry lowering a sonar / depth gauge against a hull below the waterline; a faint checklist glowing on the hull. |
| The roadmap | A nautical chart on a chart table under a low lamp: a plotted course with waypoints, a compass rose and north star, dividers and parallel rules. |
| Ship-states | A harbour status board or a signal mast; five moored positions from an anchored slip to open sea, one of them lit coral. |
| The tracker seam | A single modular coupling / shackle joining two different rail systems into one continuous track — the one pluggable part. |

Overlay any real labels, arrows, or exact relationships yourself (see §8); let the model paint the world, not annotate it.

---

## 7. Layout rules and do's / don'ts

**Grounds.** Dark abyssal-midnight for hero, cover, and atmospheric surfaces; light sea-mist for documentation body and anything read at length. Both themes are first-class — design and check both (the board demonstrates the token pattern).

**Colour discipline.** Teal is the constant workhorse; coral is the warm signal, disciplined by medium (§3.5) — one focal coral point in an atmospheric composition, at most one coral detail per icon, and functional coral (links, active states, status, the in-progress column) allowed to repeat in UI and docs only while a single element stays dominant and the frame never turns coral-heavy. Sonar-green is an occasional highlight. If coral starts to fight itself, demote the least-important instance back to teal.

**Space and rhythm.** Generous negative space (deep water, night sky). 8px spacing rhythm. Moderate radii (8–16px). 1px tide-line borders. Instrument-precise alignment — nothing casually placed.

**Type.** Space Grotesk headings, tight; Inter body at 16–17px on a ~65ch measure; JetBrains Mono for every command, SHA, and log line and for uppercase micro-labels.

**Do**

- lean into deep, dark, low-key grounds for atmosphere;
- apply coral by medium (§3.5): one focal point in atmospheric art, one detail per icon, functional repeats only in UI and docs;
- use the nautical-instrument motif kit (chart, compass, sonar, gate, beacon) with restraint;
- keep type crisp, technical, and on the scale;
- design and verify light and dark.

**Don't**

- reach for the purple-to-blue gradient hero, neon cyberpunk, or lens-flare clutter;
- centre everything or round every corner into pills;
- set small text or icons in the *bright* beacon coral (`#EE6C4D`) on a light ground — use deep signal coral (`#A83A22`) there;
- let coral compete with itself or stand in for teal as the workhorse;
- hand ChatGPT a precise labelled diagram and expect legible, correct labels (see §8).

---

## 8. ChatGPT image playbook

**What it is good for:** atmospheric hero and cover art; section mood images; textures and backdrops (deep water, dry dock at night, chart paper, brushed steel); conceptual illustration of the §6 metaphors; **icon *style* exploration** — mood and shape language, not final production icons.

**What it is bad at, and what to use instead:**

- **Precise labelled diagrams** — the labelled delivery-model or ship-states diagram, the tracker-seam architecture, state machines, any box-and-arrow relationship. Expect garbled text, invented labels, and inconsistent geometry. Use **Mermaid**, **hand-drawn**, or **SVG** for these, and use ChatGPT only for the atmospheric backdrop you then overlay real vectors/text onto.
- **Any legible in-image text** — do not require words in the image. If a word is essential, plan to composite it in afterwards in Space Grotesk / JetBrains Mono.
- **Hex is a hint, not a spec** — image models accept hex but do not reproduce it reliably, so colour drifts. Steer with the *prose* names first, pass hex as a secondary hint, and correct any critical colour in composition or post-processing.
- **Character / style consistency across images** — the model will not remember. Keep the **style block below verbatim** and prepend it to every prompt so a set hangs together.

### Reusable prompt templates

Copy-paste and fill the `<…>` slots. Always begin with the style block.

**Template 0 — Deep Fleet style block (prepend to everything):**

```
Style: deep, calm, nautical-industrial. Setting is a shipyard at night. Palette: an abyssal
midnight teal-black background (deep blue-green, near #071A1C), deep-water teal panels, cool
harbor-light teal instrument glow (#4FB8B0), lit by a SINGLE warm beacon-coral light source
(#FF7F5E), with faint sonar phosphor-green highlights (#4DE8A6) used sparingly; moonlit off-white
for any light shapes. Cool teal dominates the frame; exactly one warm coral focal point in the whole composition. Low-key
cinematic lighting, generous negative space, matte finish, subtle film grain. Precise,
engineered, seaworthy — not neon, not cyberpunk, not distressed.
Negative: no text, no words, no letters or numbers, no logos or watermarks, no UI screenshots,
no garbled typography; avoid purple-to-blue gradients, avoid neon glow overload, avoid lens-flare
clutter; keep to one warm accent only.
```

**Template 1 — Atmospheric hero:**

```
<style block>
Scene: <one metaphor from §6, described concretely>. Wide cinematic composition, low horizon /
waterline, deep water and night sky filling the negative space, the single coral beacon as the
focal point. Painterly-photographic illustration. Aspect ratio <16:9 | 21:9>.
```

**Template 2 — Conceptual metaphor illustration:**

```
<style block>
Illustrate this idea without any labels: <concept, e.g. "three light beams converging to one point
on a sealed harbour gate">. Isometric or 3/4 view, clean geometric forms, instrument-like
precision, one coral spark at the convergence point. Leave clear negative space for text overlay.
Aspect ratio <3:2 | 16:9>.
```

**Template 3 — Icon / mark style exploration (mood, not final assets):**

```
Do NOT prepend the atmospheric style block — this is a flat icon sheet, not a night scene.
A contact sheet of monoline icons on an abyssal-midnight ground (#071A1C); harbor-light teal
(#4FB8B0) strokes at an even 2px weight, square-cut caps, geometric construction on a 24px grid.
Coral rule (§3.5): at most one small coral detail per icon — a sheet of several icons therefore
shows several sparks, one each, and must not become coral-heavy overall. Motifs:
<pick from §5, e.g. "harbour gate, compass rose, gantry crane, shipping container">. Flat, no
shading, no background scene, even optical weight. Style exploration only — final icons are
hand-authored SVG. Aspect ratio 1:1.
```

**Template 4 — Texture / backdrop:**

```
<style block>
A seamless-feeling background texture: <e.g. "dark rippled deep water under a single coral
beacon" | "a weathered nautical chart in cool teal ink" | "brushed gunmetal panel">. Very low
contrast, no focal subject, room for text on top. Aspect ratio <16:9 | 1.91:1 for social>.
```

### Two worked examples

**Example A — README hero: the immutable gate**

```
Style: deep, calm, nautical-industrial. Setting is a shipyard at night. Palette: an abyssal
midnight teal-black background (near #071A1C), deep-water teal, cool harbor-light teal instrument
glow (#4FB8B0), lit by a SINGLE warm beacon-coral light source (#FF7F5E), faint sonar
phosphor-green highlights used sparingly, moonlit off-white for light shapes. Cool teal dominates;
exactly one warm coral accent. Low-key cinematic lighting, generous negative space, matte finish,
subtle film grain. Precise, engineered, seaworthy — not neon, not cyberpunk.
Negative: no text, no words, no letters or numbers, no logos or watermarks, no garbled typography;
avoid purple-to-blue gradients, avoid neon overload, avoid lens-flare clutter; one warm accent only.
Scene: a single massive sealed lock gate at the mouth of a dark harbour, seen straight-on and low.
Three thin parallel beams of cool teal light travel across the water toward the gate and converge
to one small glowing coral point at its centre — three things becoming one commit. Still black
water, wide cinematic frame, the coral point as the sole focus, lots of empty night sky above for
a title overlay. Painterly-photographic. Aspect ratio 21:9.
```

Then set the title in Space Grotesk and the command in JetBrains Mono over the empty sky yourself — do not ask the model for the text.

**Example B — the agent fleet section image**

```
Style: deep, calm, nautical-industrial. Setting is a shipyard at night. Palette: abyssal midnight
teal-black background, deep-water teal, harbor-light teal glow (#4FB8B0), a SINGLE warm
beacon-coral accent (#FF7F5E), sparing sonar phosphor-green; moonlit off-white highlights. Cool
teal dominates; one warm accent. Low-key cinematic light, generous negative space, matte, subtle
grain. Precise and seaworthy — not neon, not cyberpunk.
Negative: no text, no words, no letters or numbers, no logos, no garbled typography; avoid
purple-to-blue gradients, avoid neon overload; one warm accent only.
Scene: a disciplined formation of several small identical vessels crossing deep dark water at
night, all heading the same way toward one distant harbour marked by a single coral beacon on the
horizon. Each vessel carries one small cool-teal lamp; the only warm light in the frame is the far
beacon. 3/4 aerial view, calm wake lines, lots of open water as negative space. Painterly-
photographic. Aspect ratio 16:9.
```

### Docs-site asset checklist

Every purely-illustrative asset the docs site needs, with its **source**, a ready-to-paste prompt for the generated ones, and an exact **output spec**. The boundary is firm: **anything carrying a label, a box-and-arrow relationship, or exact text is authored by hand / Mermaid / SVG — never ChatGPT** (see "what it is bad at"). Those diagrams are the last row, called out explicitly.

| Asset | Source | Output spec (dimensions · format · background · themes) |
|---|---|---|
| Wordmark | Author — set in Space Grotesk (§2), export | SVG master + PNG 960×240 (@2×); **transparent**; two colour cuts: deep-hull `#0C1B1C` for light grounds, moonlit `#E8F1EF` for dark |
| Logo / avatar mark | Author — SVG from §5 (ChatGPT for *style exploration* only, Template 3) | SVG + PNG 512×512 and 1024×1024; **filled** abyssal `#071A1C` square; teal mark + one coral spark; one design serves both themes |
| Favicon | Author — SVG → ICO/PNG | `favicon.ico` (16/32/48) + `icon.svg` + apple-touch 180×180 + maskable 512×512; **filled** abyssal ground (favicons need a solid ground); single design works in both themes |
| Social / OG card | ChatGPT background + author overlays text | 1200×630 PNG; **filled** abyssal bg; **one (dark) variant**; wordmark + tagline set by the author in Space Grotesk / JetBrains Mono, never model-rendered |
| Landing hero | ChatGPT (Template 1 / Worked Example A) | 2560×1280 WebP + PNG master (downscale for mobile); **filled** bg; dark primary, optional light variant; keep a clear safe-zone for the overlaid H1 |
| Spot / section illustrations | ChatGPT (Template 2) | 1600×1200 WebP; **filled** bg; one coral focal point each; see the dark/light note below |
| Texture / backdrop | ChatGPT (Template 4) | 1920×1080 WebP; **filled**, very low contrast; dark + light; leaves room for text on top |
| Architecture diagrams — delivery model, immutable gate (labelled), ship-states, tracker seam | **Author — Mermaid or SVG, NOT ChatGPT** | inline SVG using `currentColor` + the CSS variables from §9 (one file, both themes) or Mermaid with a theme init; real labels in Space Grotesk / JetBrains Mono |

**Dark/light variants for atmospheric art.** A shipyard-at-night scene is inherently dark, so a naive "light version" fights the concept. For light-theme pages, either place the dark illustration inside a dark-inset card, or commission a genuinely lighter-key companion ("dawn at the dry dock") that keeps teal structure and a single coral point — do not simply invert. Favicon, logo mark, and OG card intentionally ship as **one** filled-ground design that reads on both themes.

**Suggested spot-illustration set** (each an atmospheric §6 metaphor, one coral focal point): the delivery model (persistent chart + repeating dock cycle), briefs-not-transcripts, the agent fleet, verification obligations, and the tracker seam. The immutable gate is already covered by the hero (Worked Example A).

**Ready-to-paste prompts for the generated assets:**

*Social / OG card background — 1200×630 (author overlays the wordmark + tagline after):*

```
<Template 0 style block>
Scene: a calm wide harbour at night seen from just above the waterline, deep still water and a low
band of sky, a single small coral beacon low on the right third. The whole left and lower area is
open, uncluttered dark water and sky — deliberately empty for a title and logo to be placed later.
No focal subject in the centre. Painterly-photographic. Aspect ratio 1200:630.
```

*Spot illustration — briefs, not transcripts (Template 2 filled in):*

```
<Template 0 style block>
Illustrate this idea without any labels: a small courier vessel crossing dark water carrying one
neat sealed container lit by a single coral lamp, while a loose tangle of pale discarded paper is
left behind on the dark dock. Calm, low, 3/4 view, generous empty water, one coral focal point.
Aspect ratio 4:3.
```

The **landing hero** uses Worked Example A (the immutable gate) or Template 1 with a §6 metaphor, exported at the 2560×1280 master. For the remaining spot illustrations, fill Template 2 with the matching §6 image idea, always keeping the single coral focal point.

---

## 9. Docusaurus integration

The palette and type as a paste-able `src/css/custom.css` for a Docusaurus (classic preset) site, mapping the chosen tokens onto Infima's variables — primary and its shade ramp, base/heading/monospace font families, grounds, links, and code — with a light default and a `[data-theme='dark']` block.

**Fonts.** All three families are SIL OFL 1.1 and available as woff2 from the `@fontsource` packages (`@fontsource/space-grotesk`, `@fontsource/inter`, `@fontsource/jetbrains-mono` on npm — or each project's GitHub release). Drop the six files named in the `@font-face` rules into `static/fonts/`; Docusaurus serves `static/` at the site root, so they resolve at `/fonts/…`. Reference this file from `docusaurus.config.js` (`presets → theme → customCss: './src/css/custom.css'`).

```css
/**
 * Shipyard — Deep Fleet theme for Docusaurus (Infima overrides).
 * Fonts: SIL OFL 1.1, from @fontsource (space-grotesk / inter / jetbrains-mono).
 * Copy the six woff2 files into static/fonts/ to match the @font-face srcs below.
 */

/* ---- self-hosted fonts (static/fonts/) ---- */
@font-face { font-family: "Space Grotesk"; font-style: normal; font-weight: 500; font-display: swap; src: url("/fonts/space-grotesk-500.woff2") format("woff2"); }
@font-face { font-family: "Space Grotesk"; font-style: normal; font-weight: 700; font-display: swap; src: url("/fonts/space-grotesk-700.woff2") format("woff2"); }
@font-face { font-family: "Inter"; font-style: normal; font-weight: 400; font-display: swap; src: url("/fonts/inter-400.woff2") format("woff2"); }
@font-face { font-family: "Inter"; font-style: normal; font-weight: 600; font-display: swap; src: url("/fonts/inter-600.woff2") format("woff2"); }
@font-face { font-family: "JetBrains Mono"; font-style: normal; font-weight: 400; font-display: swap; src: url("/fonts/jetbrains-mono-400.woff2") format("woff2"); }
@font-face { font-family: "JetBrains Mono"; font-style: normal; font-weight: 700; font-display: swap; src: url("/fonts/jetbrains-mono-700.woff2") format("woff2"); }

/* ---- LIGHT (default) ---- */
:root {
  /* brand primary — abyssal fleet teal + Infima shade ramp */
  --ifm-color-primary: #0F5B5E;
  --ifm-color-primary-dark: #0C4A4C;
  --ifm-color-primary-darker: #0A3D3F;
  --ifm-color-primary-darkest: #062425;
  --ifm-color-primary-light: #126C70;
  --ifm-color-primary-lighter: #14797D;
  --ifm-color-primary-lightest: #189297;

  /* type */
  --ifm-font-family-base: "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --ifm-heading-font-family: "Space Grotesk", var(--ifm-font-family-base);
  --ifm-font-family-monospace: "JetBrains Mono", ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  --ifm-heading-font-weight: 700;

  /* grounds & text */
  --ifm-background-color: #EEF2F1;             /* sea-mist grey */
  --ifm-background-surface-color: #FFFFFF;     /* spume white */
  --ifm-font-color-base: #0C1B1C;              /* deep-hull black */
  --ifm-heading-color: #0C1B1C;
  --ifm-color-content-secondary: #4E6462;      /* slate teal (muted) */

  /* links — teal workhorse (see §3.5); coral is reserved for CTAs/active/status */
  --ifm-link-color: #0F5B5E;
  --ifm-link-hover-color: #0A3D3F;
  --sy-accent: #A83A22;                        /* deep signal coral — functional accent */
  --sy-accent-glow: #EE6C4D;                   /* bright beacon coral — large fills only */

  /* code */
  --ifm-code-background: #E3EBEA;              /* faint tide tint */
  --ifm-code-color: #0C1B1C;
  --docusaurus-highlighted-code-line-bg: #DCE6E4;

  /* admonitions / semantic */
  --ifm-color-success: #2FB37A;
  --ifm-color-info: #1F9E9E;
  --ifm-color-warning: #E8A33D;
  --ifm-color-danger: #E24C4B;
}

/* ---- DARK ---- */
[data-theme='dark'] {
  --ifm-color-primary: #4FB8B0;                /* harbor-light teal */
  --ifm-color-primary-dark: #46ADA5;
  --ifm-color-primary-darker: #41A29B;
  --ifm-color-primary-darkest: #398C86;
  --ifm-color-primary-light: #5EBEB7;
  --ifm-color-primary-lighter: #68C2BB;
  --ifm-color-primary-lightest: #7ECBC5;

  --ifm-background-color: #071A1C;             /* abyssal midnight */
  --ifm-background-surface-color: #0E2A2C;     /* deep-water panel */
  --ifm-font-color-base: #E8F1EF;              /* moonlit white */
  --ifm-heading-color: #E8F1EF;
  --ifm-color-content-secondary: #8FA8A5;      /* seafoam grey */

  --ifm-link-color: #4FB8B0;
  --ifm-link-hover-color: #7ECBC5;
  --sy-accent: #FF7F5E;                        /* lit beacon coral — legible on dark */
  --sy-accent-glow: #FF7F5E;

  --ifm-code-background: #0E2A2C;
  --ifm-code-color: #E8F1EF;
  --docusaurus-highlighted-code-line-bg: #13383A;

  --ifm-color-success: #4DE8A6;
  --ifm-color-info: #3FC4C4;
  --ifm-color-warning: #F6BB57;
  --ifm-color-danger: #FF6B69;
}

/* wordmark treatment + optional coral call-to-action, kept off body links so pages don't turn coral-heavy */
.navbar__title { font-family: var(--ifm-heading-font-family); letter-spacing: -0.02em; }
.button.button--primary { background: var(--sy-accent); border-color: var(--sy-accent); color: #FFFFFF; }
```

Link colour is teal on purpose (teal is the workhorse; coral for every link would breach the §3.5 "not coral-heavy" rule). Coral lives on `--sy-accent` for calls-to-action, active states, and status dots — the one primary button rule above shows the pattern.
