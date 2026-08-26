# KaizenCommerce Design System
version: 4.1 — Updated 2026-05-31

Reference file for the `kaizen-commerce-expert` skill system. Loaded on demand by every skill
that produces styled output: website direction, PDFs, Google Docs, slide decks, LinkedIn
carousels, proposals, Blueprint reports, health checks, and sales collateral.

## Source Of Truth

`reference/kaizen-ds-v2.html` is the canonical visual design system. This markdown file is the
portable interpretation for agents and renderers. `reference/kaizen-design-tokens.json` is the
machine-readable enforcement layer. If this file, a generated dummy artifact, a copied example, or
old boilerplate conflicts with `kaizen-ds-v2.html`, the HTML spec wins.

The supplied examples remain calibration artifacts:
- `../examples/kaizen-pitch-deck-example.pptx`
- `../examples/kaizen-blueprint-advisory-example.pdf`

The reusable PPTX template and DS v2 acceptance deck is:
- `../assets/templates/kaizen-pitch-deck-template.pptx`

The reusable PDF templates and acceptance assets are:
- `../assets/templates/kaizen-proposal-template.pdf`
- `../assets/templates/kaizen-sow-template.html`
- `../assets/templates/kaizen-sow-template.pdf`

Use them for rhythm, pacing, and content structure, but reconcile them to DS v2 before generating
new work. Do not let the examples reintroduce old ramps, rounded cards, shadows, or non-system
colors.

Note: `kaizen-ds-v2.html` contains a few internal preview-interface colors for the version tabs and
Do/Don't demonstration scaffolding. Those are not export tokens. New client-facing artifacts use
the displayed DS v2 swatches plus alpha black/white by default.

## Version History

| Version | Date | Changes |
|---|---|---|
| 4.1 | 2026-05-31 | Added machine-readable token enforcement and governed supporting ramps for cases where they improve dense document readability or reference-artifact fidelity. |
| 4.0 | 2026-05-31 | Promoted `kaizen-ds-v2.html` to the visual source of truth; closed the palette to DS v2 tokens and alpha variants; restored EB Garamond editorial body usage; removed artifact-over-DS precedence. |
| 3.0 | 2026-05-31 | Superseded. Calibrated to examples but allowed extra grey, steel, red-tint, and panel-fill ramps. |
| 2.0 | 2026-05-31 | Superseded. Initial EB Garamond + Hanken adoption. |
| 1.0 | 2026-03 | Initial design system. |

## Core Principle

Editorial, flat, and grid-led. The brand should feel like a precise commerce operations system:
black-dominant, serif authority, compact Hanken labels, hard-edged bento cells, and color used
only for meaning. There are no decorative effects.

**Non-negotiable rules:**
- `reference/kaizen-ds-v2.html` wins over all examples and generated boilerplate.
- DS v2 swatches are the default. Governed ramps may be used only for documented support roles in
  `kaizen-design-tokens.json`.
- No shadows, gradients, glow, blur, atmospheric orbs, HUD rails, decorative brackets, or faux depth.
- No border radius anywhere: cells, buttons, inputs, badges, images, and tables are square.
- No nested cards. Use bento cells, text, and lines.
- Red means problem or action. One red zone per page/slide/section maximum.
- Navy means process, trust, Blueprint, and featured Gold tier.
- Ice Blue is text-only on Navy. Never use Ice Blue as a fill and never use it on Black.
- White is a signal, not a generic field. It is allowed as page/canvas paper and high-contrast CTA
  fill, but avoid full white "card sections" inside compositions.

## Color Tokens

DS v2 labels this a "Four-color palette. No exceptions." The implemented swatch set has six
operational core tokens: Black, Mid Black, Deep Navy, Red, White, and Ice Blue. These are the
default solid hex values for new styled outputs.

| Token | Hex | Usage |
|---|---|---|
| `--black` | `#0e0e0e` | Primary surface, default brand field, heading ink, authority. 60-70% visual weight. |
| `--mid` | `#181818` | Secondary cells against Black only. |
| `--navy` | `#0D1B2A` | Process, trust, Blueprint moments, featured Gold tier, method context. |
| `--red` | `#a8201a` | Problem framing, urgency, primary action, risk/action emphasis. |
| `--white` | `#F5F7F9` | Paper/canvas, text on dark, max-contrast CTA fill, rare emphasis cell. |
| `--ice-blue` | `#aaccdb` | Text accent on Navy only. Never a fill. Never on Black. |

### Alpha Utility

Use alpha variants instead of inventing grey ramps:
- Light-surface body text: `rgba(14,14,14,0.55-0.72)`.
- Light-surface muted labels/rules: `rgba(14,14,14,0.08-0.45)`.
- Dark-surface body text: `rgba(245,247,249,0.50-0.75)`.
- Dark-surface labels/rules: `rgba(245,247,249,0.08-0.45)`.
- Red-surface body text: `rgba(245,247,249,0.55-0.75)`.

### Governed Supporting Ramps

The old grey, steel-blue, red-tint, and light-panel ramps are not banned outright. They are
allowed only when they make the output more readable, more faithful to a reference artifact, or
more robust in formats that cannot represent alpha transparency consistently.

- **Grey ramp:** dense PDF/table body text, footers, metadata, or exported surfaces where alpha
  black is unreliable.
- **Steel-blue ramp:** quiet operational accents, small labels on dark/navy, sub-list markers, or
  reference-artifact calibration where Ice Blue is too bright.
- **Red tints:** secondary risk/severity states and body text on Red panels where full Red would
  overpower the composition.
- **Light panel fills:** print/PDF table fills, first-column emphasis, or quiet document panels
  where alpha fills are unavailable or unreliable.
- **Reference dark variants:** canonical PPTX template reproduction where the source deck uses
  near-black or deep-navy export variants in stacked dark panels.

Do not use these ramps as decoration, website card themes, Gold-tier fills, primary CTAs, or
replacement brand colors. Exact values and audit policy live in
`reference/kaizen-design-tokens.json`.

## Typography

Two typefaces, one purpose each.

| Token | Typeface | Spec | Use |
|---|---|---|---|
| Display | EB Garamond 500 | `clamp(52px, 6.5vw, 96px)`, line-height 1.0, letter-spacing `-0.02em` | Hero headlines, document titles, major narrative statements. |
| Display SM | EB Garamond 500 | `clamp(32px, 4vw, 56px)`, line-height 1.06, letter-spacing `-0.015em` | Section leads and secondary display moments. |
| Stat | EB Garamond 500 | `clamp(44px, 5vw, 72px)`, line-height 1.0, letter-spacing `-0.02em` | Numbers and quantified proof. |
| Body Serif | EB Garamond 400 | 18-22px, line-height 1.5 | Editorial/narrative copy where authority and pacing matter. |
| Eyebrow | Hanken Grotesk 800 | 10px, uppercase, letter-spacing `0.14em` | Section labels, small caps, bento labels. |
| UI Label | Hanken Grotesk 700 | 13-14px, letter-spacing `-0.01em` | Controls, buttons, compact labels. |
| Body Sans | Hanken Grotesk 400 | 13-15px, line-height 1.65-1.75 | Functional copy, UI text, explanations, tables. |
| Ghost Input | EB Garamond 400 italic | 24-26px, bottom-border only | Email/input prompts in designed artifacts. |

**Font roles:** EB Garamond carries authority, editorial weight, and numbers. Hanken Grotesk
carries UI, labels, tables, and functional copy. Never use Inter, Space Grotesk, Geist, IBM Plex
Mono, Bebas Neue, or Calibri as a brand choice.

**Font loading:**
```html
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400;1,500&family=Hanken+Grotesk:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

## Grid And Spacing

The layout system is a single flat bento grid. Hierarchy comes from background fills and type
scale, not elevation.

| Token | Value | Usage |
|---|---|---|
| Base unit | 8px | All spacing derives from this unit. |
| Grid gap | 1px | The gap between bento cells; wrapper background creates the line. |
| Page margin | 40px | Outer margin for bento wrappers in web/social layouts. |
| Cell padding | 56px top/bottom, 60px left/right | Default full cell padding. |
| Compact pad | 44px | Stat cells and secondary cells. |

Rules:
- Bento wrappers have borders; cells do not.
- Set wrapper background to an alpha line color and `gap: 1px`.
- Adjacent bento sections share a border; remove duplicate top borders after the first section.
- Use `border-radius: 0` everywhere.

## Components

### Buttons

Square, Hanken Grotesk 800, uppercase, `0.1em` tracking.
- On dark: White fill with Black text.
- On light: Black fill with White text.
- Ghost action: bottom border only with muted alpha text.

### Ghost Inputs

EB Garamond italic, 24-26px, bottom border only. No boxed inputs unless the platform requires a
native input field.

### Bento Cells

Cells are flat surfaces in Black, Mid Black, Navy, Red, or rare White emphasis. Use text alignment,
scale, and one-pixel gaps to create hierarchy. Do not use card shadows, rounded containers, or
nested panels.

### Tables And Dense Data

Use Hanken Grotesk for all functional data. Prefer black, navy, or red header surfaces with white
text. Use alpha row separators instead of fixed grey lines. First-column emphasis may use bold Black
text, not a separate fill color unless the whole table is a bento cell.

### Severity

Render severity as plain bold text, never as pills or badges.
- Critical / blocking: Red.
- Important / watch: Red at lower emphasis or Black with red section context.
- OK / informational: Navy or alpha-muted Black.
- Done / healthy: Black or Navy. Do not add a green success color.

## Document And Deck Guidance

### PDFs / Proposals / Blueprint Reports

- Use DS v2 paper/canvas (`#F5F7F9`) for readable document pages, but do not treat White as a
  decorative card fill.
- Dark covers and closing pages use Black with no top bar, gradient, grid, or bracket effects.
- Section headers: Hanken eyebrow, EB Garamond section heading, alpha hairline.
- Body may be EB Garamond editorial copy for narrative sections or Hanken Grotesk for functional
  sections. Choose deliberately by role.
- Callouts are bento cells or line-led blocks, not rounded alert boxes.
- Footers use Hanken Grotesk with alpha-muted text and alpha hairline.

### PPTX / Carousels

- Widescreen decks use 13.333 x 7.5 in.
- Social carousels use 1080 x 1080.
- Use two-panel or bento-grid compositions with 1px/hairline gaps.
- Slide/page surfaces must come from the six DS v2 tokens only.
- Featured Gold tier is Navy, not steel.
- Ice Blue only labels text on Navy.
- Do not use light-blue cards, grey cards, steel cards, red-tint panels, glows, or gradients.

## Verification Checklist

Before delivering any styled Kaizen output:

- [ ] `reference/kaizen-ds-v2.html` was treated as visual source of truth.
- [ ] Core DS v2 tokens carry the composition; any governed ramp token has a clear readability,
  print/PDF, or reference-fidelity reason.
- [ ] Red marks a problem/action and appears as one zone maximum.
- [ ] Navy marks process/trust/Blueprint/Gold.
- [ ] Ice Blue appears only as text on Navy.
- [ ] EB Garamond and Hanken Grotesk roles match DS v2.
- [ ] Layout uses bento cells, 1px/hairline gaps, and flat primitives.
- [ ] No rounded cards, nested cards, shadows, gradients, or extra decorative geometry.
- [ ] Text fits without overflow on desktop, slide, print, and mobile targets.

**Footer string for formal documents:** `KaizenCommerce | Confidential` + page number.
