# Shipyard design language

The identity for Shipyard and the `sy` plugin, and the source of truth for generating on-brand documentation imagery. Chosen direction: the **Deep Fleet** palette with the **Space Grotesk / Inter / JetBrains Mono** type pairing — a calm, oceanic ground lit by a single warm beacon, set in exacting, developer-native type. The night bridge, read by precision instruments.

This is the *language*, not the pictures. It exists so that a human, or an image model like ChatGPT, can produce covers, hero art, textures, diagrams, and a logo that all look like they came from the same yard.

**Personality:** Disciplined · Exacting · Trustworthy · Industrial-nautical · Evidence-first.

## Where this is going

The end product is a **themeable documentation site on GitHub Pages, built and deployed by GitHub Actions**, composed from the prose in `docs/` and the imagery in `docs/img/`. Nothing here builds that site yet — but every asset is specified so it drops straight into one: web-ready dimensions and formats, **first-class light *and* dark variants** (the site is theme-aware), clear safe-zones for text the site overlays rather than bakes in, and colour/type expressed as CSS tokens the site consumes directly. Generate assets to these specs and the site is an assembly job, not a re-shoot.

## The files

| File | What it holds | Who reads it |
|---|---|---|
| [`brand.md`](brand.md) | Brand essence, voice, naming and wordmark, the iconography system, and the concept→metaphor vocabulary | humans; prompt authors |
| [`colour-and-type.md`](colour-and-type.md) | The Deep Fleet palette (with disciplined diagram colour roles), typography, layout rules, and paste-able web theme tokens | humans; the site's CSS |
| [`prompts-backgrounds.md`](prompts-backgrounds.md) | A copy-whole ChatGPT prompt for the atmospheric hero / section / texture art — **dark and light** | anyone regenerating `docs/img/background_*` |
| [`prompts-diagrams.md`](prompts-diagrams.md) | A copy-whole ChatGPT prompt for the README diagrams — carries the authoritative **diagram simplicity rules** | anyone regenerating the labelled diagrams in `docs/img/` |
| [`prompts-logo.md`](prompts-logo.md) | A copy-whole ChatGPT prompt for the logo mark, wordmark, and favicon set | anyone producing the marks |

## Generating assets

The three `prompts-*.md` files are **operational prompts, not documentation** — each is written to be copied *whole* into ChatGPT as your first message, alongside these attachments: `brand.md`, `colour-and-type.md`, `README.md` (the product README), and, where noted, one example image. The prompt tells the model exactly what to attach.

Each prompt runs a **two-phase, look-book-first workflow**: the model returns **three variations of one representative image** and stops for you to choose; once you pick a direction, it produces the rest of the set in that locked style. Backgrounds and diagrams each render in both light and dark. This keeps a whole set visually consistent instead of drifting image to image.

## Two principles that override everything

**1. The prose carries the nuance; the diagram carries the skeleton.** Do not turn every rule, exception, or invariant into a visible element. The README sentences beside an image already carry the detail — a diagram that tries to restate them becomes a dense systems infographic and stops being read. One idea per image. See [`prompts-diagrams.md`](prompts-diagrams.md), which is authoritative for every README diagram.

**2. Teal is the constant; coral is the one exception that earns attention.** Cool teal is the workhorse across every medium; the warm coral accent marks the single focal or gated thing and nothing else. Diagrams may add **periscope indigo** for the orchestration layer and **delivered-wake green** for "done" — but only from the documented palette, never a stray fourth hue. See [`colour-and-type.md`](colour-and-type.md).
