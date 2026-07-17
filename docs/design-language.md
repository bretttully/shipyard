# Shipyard design language

Shipyard's identity: a shipyard at night — deep water, low-key teal light, one warm coral beacon breaking through. Disciplined, exacting, industrial-nautical, evidence-first. `docs/img/background_*.png` and the README's diagram images are working reference output — attach one alongside this file when prompting an image model for anything new, rather than a long written brief.

## Colour palette — Deep Fleet

Teal is the workhorse; coral is the one warm signal — exactly one coral focal point per image, never a second accent. Sonar-green is a sparing highlight, not a second accent either.

| Role | Prose name | Light hex | Dark hex |
|---|---|---|---|
| Primary | abyssal fleet teal / harbor-light teal | `#0F5B5E` | `#4FB8B0` |
| Accent | deep signal coral / lit beacon coral | `#A83A22` | `#FF7F5E` |
| Orchestration | periscope indigo | `#5B6BC7` | `#8A98F0` |
| Success / done | delivered-wake green | `#2FB37A` | `#4DE8A6` |
| Background | sea-mist grey / abyssal midnight | `#EEF2F1` | `#071A1C` |
| Text | deep-hull black / moonlit white | `#0C1B1C` | `#E8F1EF` |

Prefer dark, low-key grounds for atmospheric art; light sea-mist for documentation read at length. For image prompts, lead with the prose name — models reproduce hex poorly — and pass the hex only as a secondary hint.

## Type

**Space Grotesk** for headings/wordmark, **Inter** for body, **JetBrains Mono** for code/commands/SHAs — all SIL OFL 1.1.
