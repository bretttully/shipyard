# ChatGPT prompt — Shipyard logo, wordmark, favicon

> **How to use:** attach `brand.md`, `colour-and-type.md`, and `README.md`, then paste **everything below the line** as your first message to ChatGPT. No example image is needed (none exists yet). The model returns a 3-option look book of logo marks first; you pick one; it then produces the favicon set and lockups from the chosen mark.

---

You are designing the **logo mark** for Shipyard, a Claude Code plugin, plus the favicon and lockups derived from it. This is a flat vector mark, **not** an atmospheric scene and **not** a diagram.

I have attached:

- **`brand.md`** — the identity, the two candidate mark ideas (§2), and the monoline icon construction rules (§3);
- **`colour-and-type.md`** — the Deep Fleet palette and type;
- **`README.md`** — what Shipyard is.

Read them before drawing.

## Work in two phases

**Phase 1 — look book. Do this first, then stop.**
Produce **three logo-mark options**, presented together as 1, 2, and 3. Base them on the two candidate marks from `brand.md` §2 — option 1 the **harbour gate** (two posts + a lintel, one coral dot at the keystone), option 2 the **beacon over a waterline** (a low waterline + an upright beacon whose light is one coral dot, with one faint teal arc), option 3 your strongest alternative built from the same vocabulary. All three on a rounded-square abyssal-midnight ground. Then **stop and ask me to choose. Do not produce the favicon set or lockups yet.**

**Phase 2 — the derived set. Only after I pick an option.**
When I reply with the chosen option number, produce, from that one mark:

- the mark at **512×512 and 1024×1024** on the filled abyssal rounded square;
- a **favicon study** simplified to **at most two shapes** so it still reads at 16px, shown at 16 / 32 / 48px;
- a **horizontal lockup**: the mark beside the "Shipyard" wordmark on one baseline (see the wordmark note below);
- a note on how the single filled-ground design reads on both light and dark web pages.

## The rules (firm)

- **Flat vector only** — no shading, no gradient, no 3D, no background scene, no photographic texture.
- Monoline **harbor-light teal** (`#4FB8B0`) at an even 2px-style weight, geometric and precise, constructed on a 24px grid.
- **Exactly one coral spark** (`#FF7F5E`) per mark — everything else teal. This is the whole identity: *abyssal ground, teal structure, one coral spark.*
- Filled **abyssal-midnight** (`#071A1C`) rounded-square ground, so one design serves both light and dark pages.
- **No text or letters inside the mark** (the wordmark is separate, set in type).
- Crisp, engineered, instrument-like — think precision nautical instrument, not a cute app blob.

## The look, in words

A single flat vector app-icon on a rounded-square abyssal-midnight ground (deep teal-black, near `#071A1C`). The mark is clean monoline harbor-light teal (`#4FB8B0`), geometric, generously padded and centred, with exactly one small warm coral dot (`#FF7F5E`) as the single point of attention. No shading, no gradient, no scenery, no text.

## The wordmark (set in type — do not render it as an image)

"Shipyard" is **set**, not generated: Space Grotesk, medium-to-bold, tight tracking (about `-0.02em`), deep-hull black (`#0C1B1C`) on light grounds and moonlit white (`#E8F1EF`) on dark. If a single accent is wanted, tint only the dot of the `i` or a trailing period in beacon coral — one spark, never the whole word. For the lockup in Phase 2, place the chosen mark to the left of this wordmark on a shared baseline; deliver it as a clean flat composition. Do not try to draw the letterforms freehand — the type must be exact.

## Output

- Phase 1: the three options side by side, 1:1, on the abyssal rounded square.
- Phase 2: the mark at 512×512 and 1024×1024; the favicon study at 16 / 32 / 48px (≤ two shapes); the horizontal lockup.
- For pin-sharp favicon use, the chosen mark should ultimately be traced to crisp SVG and rebuilt on the 24px grid — flag this, since image renders blur at 16px.
