# Colour and typography

The Deep Fleet palette, the type system, the layout rules, and the paste-able web theme tokens. For code and design tokens the hex is authoritative. For image prompts the *prose* colour names are primary — image models accept hex but do not reproduce exact values reliably, so steer with the plain-English name and pass hex only as a secondary hint (the prompt files already do this).

## 1. Colour palette — Deep Fleet

Cool teal is the workhorse; the warm **coral** accent is the point of attention, applied with a discipline that scales by medium (§1.5). Sonar phosphor-green is a sparing highlight, not a second accent. All ratios below are measured against WCAG; treat them as binding.

### 1.1 Core and neutrals

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

**The accent is one signal with two values, chosen by job — not one hex forced across both themes.** On dark, `#FF7F5E` does everything (7.2:1). On light, use **deep signal coral `#A83A22`** for anything functional — text, links, icon sparks, focus rings, borders, status dots — and reserve bright **beacon coral `#EE6C4D`** for large fills and atmospheric washes where legibility rides on the foreground. Generated imagery is *always* the bright glow — it lives on dark grounds where the glow is the point; the deep value is a screen-and-print concern, not a picture concern.

### 1.2 Lifecycle columns

The five tracker columns, mapped to a vessel's progress from the hard to open sea. Each maps to a canonical status token in the [tracker contract](../../skills/tracker/CONTRACT.md); the names are Shipyard's, the board labels are per-repo.

| Column | Prose name | Light hex | Dark hex | Meaning |
|---|---|---|---|---|
| backlog | anchored slate | `#5B7377` | `#7E9A9C` | queued on the hard, not yet specced |
| ready | harbor teal | `#1F9E9E` | `#3FC4C4` | specced, provisioned, ready to build |
| in-progress | underway coral | `#A83A22` | `#FF7F5E` | active build — the vessel is underway (the coral accent; work-in-progress *is* the warm signal). Large fills may use the bright glow `#EE6C4D`. |
| in-review | periscope indigo | `#5B6BC7` | `#8A98F0` | a reviewable gated PR exists, under inspection |
| done | delivered-wake green | `#2FB37A` | `#4DE8A6` | merged, terminal — the wake left behind |

### 1.3 Semantic

| Role | Prose name | Light hex | Dark hex |
|---|---|---|---|
| success | delivered-wake green | `#2FB37A` | `#4DE8A6` |
| warning | signal amber | `#E8A33D` | `#F6BB57` |
| danger | distress red | `#E24C4B` | `#FF6B69` |

Success shares its hue with `done`, and in-progress shares its hue with the accent — both overlaps are intentional and meaningful, not collisions. Warning and danger are distinct hues reserved for genuine alarm; do not use them decoratively.

### 1.4 The palette is truest on dark

Deep Fleet is a dark-first identity. On the abyssal-midnight ground the teal instruments and the coral beacon both clear 7:1 and the whole thing sings — prefer dark grounds for hero and atmospheric imagery. Use the light sea-mist ground for documentation body and anything a reader must scan for a long time. In light, reach for **deep signal coral `#A83A22`** wherever coral must be legible and keep bright **beacon coral `#EE6C4D`** for large fills and washes.

### 1.5 Coral discipline (scales by medium)

The warm coral is the identity's one deliberate risk, and how strictly "one" is enforced depends on the medium:

- **Atmospheric hero art, covers, conceptual illustrations** — exactly **one** warm coral focal point in the entire composition; everything else is teal and neutral. A lone beacon does the most work.
- **Individual icons and marks** — at most **one** coral detail per icon. A contact sheet of many icon studies therefore shows several sparks, one per icon — intended, provided the sheet as a whole does not read as coral-heavy.
- **UI, documentation, and precise diagrams** — coral marks the **one exceptional or gated action** (the immutable gate, the merge, a bail-out); functional coral (links, active states, status dots, the in-progress column) may repeat, but only one element is visually dominant at a time, and teal stays the workhorse. If a screen starts to feel coral-heavy, demote the least-important coral back to teal.

Across all three, teal is the constant and coral is the exception that earns attention. Bright beacon coral is the *glow* (atmospheric and large fills); deep signal coral is the *ink* (functional, on light grounds).

### 1.6 Diagram colour roles

The README diagrams encode structure, so they use more than teal + coral — but **only** from the documented palette above, never a stray fourth hue. Four roles, four tokens:

| Role in a diagram | Token | Light hex | Dark hex |
|---|---|---|---|
| Specialist agents, build substance, generic structure | abyssal fleet teal / harbor-light teal | `#0F5B5E` | `#4FB8B0` |
| Orchestration / command layer — the `/sy:` commands, the dispatcher, handoff, the workflow spine | periscope indigo | `#5B6BC7` | `#8A98F0` |
| The one gated or exceptional action — the immutable gate, the merge, a bail-out | deep signal coral / lit beacon coral | `#A83A22` | `#FF7F5E` |
| Done / success / delivered | delivered-wake green | `#2FB37A` | `#4DE8A6` |

Teal is still the default and the most-used; indigo is reserved for the orchestration spine so it reads as a distinct layer; coral appears **once** per diagram on the gated action; green marks terminal success. Do not introduce a brighter, more saturated "tech blue" — the orchestration colour is periscope indigo, the same token the tracker uses for `in-review`.

## 2. Typography

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

**Rules.** Stay on the scale — do not freestyle sizes. Uppercase mono micro-labels (eyebrows, column headers, metadata) are a signature; give them the `+0.1em` tracking. Set all commands, SHAs, and log output in mono, never in body. Give headings `text-wrap: balance`. This type system is also the one to composite any label onto generated imagery in — Space Grotesk for titles, JetBrains Mono for commands and SHAs.

## 3. Layout rules and do's / don'ts

**Grounds.** Dark abyssal-midnight for hero, cover, and atmospheric surfaces; light sea-mist for documentation body and anything read at length. Both themes are first-class — design and check both.

**Colour discipline.** Teal is the constant workhorse; coral is the warm signal, disciplined by medium (§1.5). Sonar-green is an occasional highlight. If coral starts to fight itself, demote the least-important instance back to teal.

**Space and rhythm.** Generous negative space (deep water, night sky). 8px spacing rhythm. Moderate radii (8–16px). 1px tide-line borders. Instrument-precise alignment — nothing casually placed.

**Type.** Space Grotesk headings, tight; Inter body at 16–17px on a ~65ch measure; JetBrains Mono for every command, SHA, and log line and for uppercase micro-labels.

**Do**

- lean into deep, dark, low-key grounds for atmosphere;
- apply coral by medium (§1.5): one focal point in atmospheric art, one detail per icon, one gated action in a diagram;
- use the nautical-instrument motif kit (chart, compass, sonar, gate, beacon) with restraint;
- keep type crisp, technical, and on the scale;
- design and verify light and dark.

**Don't**

- reach for the purple-to-blue gradient hero, neon cyberpunk, or lens-flare clutter;
- centre everything or round every corner into pills;
- set small text or icons in the *bright* beacon coral (`#EE6C4D`) on a light ground — use deep signal coral (`#A83A22`) there;
- let coral compete with itself or stand in for teal as the workhorse;
- introduce a bright royal "tech blue" — the orchestration colour is periscope indigo (§1.6).

## 4. Web theme tokens

The palette and type as generator-neutral CSS custom properties — a light default plus a dark block — consumed directly by the Astro site. The `--sy-*` values are the site's source of truth; any component (or a framework, if one is ever added) maps its own variables onto them.

**Fonts.** All three families are SIL OFL 1.1 and available as woff2 from the `@fontsource` packages (`@fontsource/space-grotesk`, `@fontsource/inter`, `@fontsource/jetbrains-mono`). Self-host the six woff2 files (the site must not depend on an external font host) and reference them from the `@font-face` rules below.

**Theme switching.** Light is the default under `:root`; dark applies under `:root[data-theme='dark']`. The site sets `data-theme` before first paint from the reader's saved choice, falling back to `prefers-color-scheme` — so there is no flash of the wrong theme and no need to duplicate the tokens inside a media query.

```css
/**
 * Shipyard — Deep Fleet web theme (light default + dark). Generator-neutral --sy-* tokens.
 * Fonts: SIL OFL 1.1, self-hosted from @fontsource (space-grotesk / inter / jetbrains-mono).
 */

/* ---- self-hosted fonts ---- */
@font-face { font-family: "Space Grotesk"; font-style: normal; font-weight: 500; font-display: swap; src: url("/fonts/space-grotesk-500.woff2") format("woff2"); }
@font-face { font-family: "Space Grotesk"; font-style: normal; font-weight: 700; font-display: swap; src: url("/fonts/space-grotesk-700.woff2") format("woff2"); }
@font-face { font-family: "Inter"; font-style: normal; font-weight: 400; font-display: swap; src: url("/fonts/inter-400.woff2") format("woff2"); }
@font-face { font-family: "Inter"; font-style: normal; font-weight: 600; font-display: swap; src: url("/fonts/inter-600.woff2") format("woff2"); }
@font-face { font-family: "JetBrains Mono"; font-style: normal; font-weight: 400; font-display: swap; src: url("/fonts/jetbrains-mono-400.woff2") format("woff2"); }
@font-face { font-family: "JetBrains Mono"; font-style: normal; font-weight: 700; font-display: swap; src: url("/fonts/jetbrains-mono-700.woff2") format("woff2"); }

/* ---- design tokens: LIGHT (default) ---- */
:root {
  /* type */
  --sy-font-head: "Space Grotesk", ui-sans-serif, system-ui, sans-serif;
  --sy-font-body: "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --sy-font-mono: "JetBrains Mono", ui-monospace, "SF Mono", Menlo, Consolas, monospace;

  /* brand */
  --sy-primary: #0F5B5E;          /* abyssal fleet teal — headings, primary fills */
  --sy-accent: #A83A22;           /* deep signal coral — functional accent (CTAs, active, status) */
  --sy-accent-glow: #EE6C4D;      /* beacon coral — large fills/washes only, never small text on light */
  --sy-indigo: #5B6BC7;           /* periscope indigo — orchestration spine, in-review */
  --sy-highlight: #2FB37A;        /* sonar phosphor-green — sparing highlight */

  /* grounds & text */
  --sy-bg: #EEF2F1;               /* sea-mist grey */
  --sy-surface: #FFFFFF;          /* spume white */
  --sy-border: #CBD8D6;           /* tide line */
  --sy-text: #0C1B1C;             /* deep-hull black */
  --sy-text-muted: #4E6462;       /* slate teal */
  --sy-link: #0F5B5E;             /* teal is the workhorse; coral is reserved (§1.5) */
  --sy-link-hover: #0A3D3F;

  /* code */
  --sy-code-bg: #E3EBEA;          /* faint tide tint */
  --sy-code-text: #0C1B1C;
  --sy-code-line-highlight: #DCE6E4;

  /* lifecycle columns (§1.2) */
  --sy-col-backlog: #5B7377;
  --sy-col-ready: #1F9E9E;
  --sy-col-in-progress: #A83A22;
  --sy-col-in-review: #5B6BC7;
  --sy-col-done: #2FB37A;

  /* semantic (§1.3) */
  --sy-success: #2FB37A;
  --sy-info: #1F9E9E;
  --sy-warning: #E8A33D;
  --sy-danger: #E24C4B;
}

/* ---- DARK ---- */
:root[data-theme='dark'] {
  --sy-primary: #4FB8B0;          /* harbor-light teal */
  --sy-accent: #FF7F5E;           /* lit beacon coral — legible on dark */
  --sy-accent-glow: #FF7F5E;
  --sy-indigo: #8A98F0;
  --sy-highlight: #4DE8A6;

  --sy-bg: #071A1C;               /* abyssal midnight */
  --sy-surface: #0E2A2C;          /* deep-water panel */
  --sy-border: #1C4143;           /* bioluminescent line */
  --sy-text: #E8F1EF;             /* moonlit white */
  --sy-text-muted: #8FA8A5;       /* seafoam grey */
  --sy-link: #4FB8B0;
  --sy-link-hover: #7ECBC5;

  --sy-code-bg: #0E2A2C;
  --sy-code-text: #E8F1EF;
  --sy-code-line-highlight: #13383A;

  --sy-col-backlog: #7E9A9C;
  --sy-col-ready: #3FC4C4;
  --sy-col-in-progress: #FF7F5E;
  --sy-col-in-review: #8A98F0;
  --sy-col-done: #4DE8A6;

  --sy-success: #4DE8A6;
  --sy-info: #3FC4C4;
  --sy-warning: #F6BB57;
  --sy-danger: #FF6B69;
}
```

Apply the tokens through the site's own components: the wordmark and headings use `var(--sy-font-head)` (tight, `-0.02em` at large sizes), body uses `var(--sy-font-body)`, and every command / SHA / log line uses `var(--sy-font-mono)`. Links are teal (`--sy-link`) on purpose — coral for every link would breach the §1.5 "not coral-heavy" rule. Coral lives on `--sy-accent` for calls-to-action, active states, and status dots; periscope indigo lives on `--sy-indigo` for the orchestration accent and the `in-review` state.
