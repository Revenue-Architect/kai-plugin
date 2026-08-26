# KaizenCommerce PPTX Design System and Boilerplate

Moved from `skills/kaizen-publish.md` to keep the publish router lean without compressing or deleting guidance. The section now points to the canonical PPTX template asset where template geometry supersedes older prose. Load this file for PPTX, slide deck, pitch deck, proposal deck, or presentation work.

## McKinsey Structural Principles

These principles govern every deck. Apply them before writing a single slide.

### 1. Action Titles (Non-negotiable)
Every slide title must be a **complete sentence that states the key insight** — not a topic label.

| Bad (topic label) | Good (action title) |
|---|---|
| "POS Migration Challenges" | "Most POS migrations fail because teams underestimate data complexity, not the migration itself" |
| "Our Solution" | "KaizenCommerce eliminates migration risk with a structured Blueprint before a single line moves" |
| "Before / After" | "Retailers who migrate with us eliminate sync lag, transfer chaos, and blind replenishment in 90 days" |

Rule: If the reader can understand the slide's point from the title alone without looking at the body, the title is correct.

### 2. Pyramid Principle — Lead with the Conclusion
- **State the recommendation first**, then support it
- Never bury the insight at the end
- Executive readers should be able to read only titles and get the full story

### 3. SCR Storyline Framework
Structure every deck as: **Situation --> Complication --> Resolution**

- **Situation:** Where the client is now (factual, agreed-upon context)
- **Complication:** What makes the status quo untenable (the real problem)
- **Resolution:** The specific action that resolves the complication (the Blueprint)

The SCR arc should be readable from slide titles alone.

### 4. One Message Per Slide
- Every element on the slide must support the action title
- If something doesn't prove the title's claim, remove it
- No decoration for decoration's sake — orbs and design elements should not compete with data

### 5. MECE Structure
Supporting points must be **Mutually Exclusive, Collectively Exhaustive** — no overlaps, no gaps.

### 6. Executive Summary Slide (Slide 2)
Every client-facing deck needs a slide 2 "At a Glance" that:
- Summarizes the full SCR arc in 3-5 bullets
- Lets a busy executive skip the body and still understand the recommendation
- Uses the same action-title logic at bullet level

### 7. Source Citations
- Any data point, stat, or external claim gets a citation
- Bottom-left corner, 9pt muted text: `Source: [Name], [Year]`
- Internal estimates labeled: `KaizenCommerce analysis`

### 8. Slide Anatomy (Three Required Parts)
Every body slide must have:
- **(a) Action title** — the insight (full sentence, top of slide)
- **(b) Subheading** — what data/evidence you're presenting to prove it (optional but preferred)
- **(c) Body** — the evidence (chart, table, bullets, diagram)

### 9. Elevator Test
Before finalizing: can you explain the deck's recommendation in 30 seconds? If not, the storyline needs tightening.

## PPTX Design System

The deck follows the visual source of truth in `../reference/kaizen-ds-v2.html` and the token
allowlist in `../reference/kaizen-design-tokens.json`. PPTX-specific ownership here is limited to
split-panel composition, slide sizing, PptxGenJS implementation patterns, and reference-deck
calibration.

### Calibration to the reference deck (READ FIRST — avoids the "AI-generated" look)

The canonical visual artifact is `../reference/kaizen-ds-v2.html`; `../assets/templates/kaizen-pitch-deck-template.pptx` is the reusable PPTX template and DS v2 acceptance deck; `../examples/kaizen-pitch-deck-example.pptx` is the byte-identical calibration artifact; and `../examples/kaizen-pitch-deck-example.md` is the inspection guide. Match DS v2 first, then preserve the deck's rhythm. The following are the specific tells that make a generated deck read as AI-made instead of like KaizenCommerce — never do the left column, always do the right:

| ✗ AI-generated tell | ✓ KaizenCommerce example |
|---|---|
| Random italic/roman switching | **Use the template's EB Garamond display treatment deliberately.** The reference deck uses an italic display cut for major titles/stats; do not force a different style or mix arbitrary italics. |
| Centered eyebrows + centered headlines | **Left-aligned, edge-anchored.** Eyebrow sits top-left of its panel; headline left-aligned beneath. `align:"left"` everywhere except numeric stat values. |
| Hero stats as a horizontal row of boxed cells | **Hero stats stacked vertically** on the navy panel: number (EB Garamond, left) + label (Hanken caps, right-aligned on the same baseline), separated by alpha hairlines. No boxes. |
| One marker shape reused everywhere | **Marker geometry is context-specific.** White/problem panels use wide Red horizontal rules (`8.958" × 0.040"`). Dark differentiator panels use tall Ice vertical rules (`0.040" × 1.300"`). |
| Eyebrow placed below the title | **Eyebrow always above the title.** |
| Gold tier rendered as a non-system color | **Gold tier is the featured Navy card**, sitting between Mid Black Silver and Black Diamond. |
| Arrow glyphs (`→`/`->`) as list bullets | No glyph bullets in the deck. Use the tick mark + label. |
| Drop shadows, rounded cards, gradient panels | Flat `RECTANGLE` fills only, square corners, no shadow. |

Eyebrows, titles, body, and stat labels are all **left-aligned**. The only centered text is inside the CTA button. Keep generous left padding (~0.6–0.7") so content reads as editorial, not poster-like.

Before delivering a PPTX, compare against DS v2 plus the extracted notes: split-panel geometry, flat rectangles, template-matched EB Garamond display treatment, Hanken functional copy, stacked hero stats, red/problem slide treatment, Navy featured Gold tier, and dark CTA close. Do not deliver a dummy-deck aesthetic.

### Color Palette (PptxGenJS constants, no `#`)

```javascript
const C = {
  BLACK:"0E0E0E", MID:"181818", NAVY:"0D1B2A", RED:"A8201A", WHITE:"F5F7F9", ICE:"AACCDB",
};
```

| Group | Tokens | Usage |
|---|---|---|
| Surfaces | `BLACK` `MID` `NAVY` `RED` `WHITE` | Full-bleed panel fills (the split) |
| Alpha utility | black/white transparency | Muted text, hairlines, quiet fills |
| Ice Blue | `ICE` | Text labels on Navy only |
| Governed ramps | See `kaizen-design-tokens.json` | Use only when a dense deck/table/reference calibration needs them |

**Rules:**
- Each slide is **2 panels** (or top band + body). Pick a surface pair: Black+Navy (hero/who-we-are), Red+White (problem), Navy-band+White (method/tiers), Black+Red-bar (deliverable), Red+Navy (CTA).
- Eyebrow labels: `ICE` on Navy, `WHITE`/alpha White on Black, `WHITE` on Red, alpha Black on White.
- Body text: Black/alpha Black on White, White/alpha White on Black or Red, Ice Blue only on Navy.
- One Red accent per slide (panel, stat bar, or CTA). No cyan, teal, purple, gradients, or orbs.

### Typography

**Fonts for PPTX:**
- **Display / Stats:** `EB Garamond` weight 500 (specify `"EB Garamond"` in fontFace; fallback: `"Georgia"`)
- **Eyebrows / Labels / Buttons:** `Hanken Grotesk` weight 700–800 (specify `"Hanken Grotesk"`; fallback: `"Calibri"`)
- **Body / functional copy:** `Hanken Grotesk` weight 400 (fallback: `"Calibri"`)
- Note: PptxGenJS uses whatever fontFace name is specified — if the font is installed on the target machine, it renders; otherwise falls back. Ensure fonts are installed or specify the fallback explicitly.

| Element | Size (pt) | Weight | Font | Color |
|---|---|---|---|---|
| Eyebrow label | 10 | 800, ALL CAPS, charSpacing:5 | Hanken Grotesk | `F5F7F9` or `aaccdb` on Navy |
| Slide title — line 1 | 36-44 | 500 | EB Garamond | `F5F7F9` |
| Slide title — line 2 (problem/CTA) | 36-44 | 500 | EB Garamond | `a8201a` Red |
| Slide title — line 3 | 36-44 | 500 | EB Garamond | `F5F7F9` |
| Section subhead | 18-20 | 700 | Hanken Grotesk | `F5F7F9` |
| Card label | 14 | 700 | Hanken Grotesk | `F5F7F9` or `aaccdb` |
| Card body | 13 | 400 | Hanken Grotesk | `F5F7F9` |
| Bullet label | 14 | 700 | Hanken Grotesk | `F5F7F9` |
| Bullet body | 13 | 400 | Hanken Grotesk | `aaccdb` |
| Table header | 12 | 700 | Hanken Grotesk | `F5F7F9` |
| Table row text | 12 | 400 | Hanken Grotesk | `F5F7F9` or `aaccdb` |
| Footer / source | 10 | 400 | Hanken Grotesk | `aaccdb` |
| CTA label | 11 | 800, ALL CAPS, charSpacing:4 | Hanken Grotesk | `F5F7F9` |
| CTA headline | 28-32 | 500 | EB Garamond | `F5F7F9` |
| CTA button text | 14 | 800 | Hanken Grotesk | `0e0e0e` (dark on White fill) |
| Stat callout — number | 48-56 | 500 | EB Garamond | `F5F7F9` |
| Stat callout — label | 13 | 400 | Hanken Grotesk | `aaccdb` |

### Layout & Dimensions

- **Slide format:** widescreen **13.333" x 7.5"** — define a custom layout, do NOT use `LAYOUT_16x9` (10×5.625):
  ```javascript
  pres.defineLayout({ name: "W", width: 13.333, height: 7.5 });
  pres.layout = "W";
  ```
- **Margins:** ~0.7" content inset from panel edges.
- **Wordmark:** "KaizenCommerce" in EB Garamond ~20pt on slide 1 (top-left); positioning line beneath in Hanken 9pt alpha-muted White/Black depending on surface.
- **Slide number:** bottom-right, zero-padded (`01`), Hanken 8pt alpha Black/White depending on surface.

### Background Treatment — Split Panels (NOT flat single-color)

Lay down two full-bleed rectangles, then place content on each panel. No `slide.background`, no orbs, no gradients.

```javascript
const W = 13.333, H = 7.5;
const box = (s,o)=>s.addShape(pres.shapes.RECTANGLE, o);

// Hero: black left (62%) + navy right (38%)
box(slide,{ x:0,       y:0, w:W*0.62, h:H, fill:{color:C.BLACK}, line:{type:"none"} });
box(slide,{ x:W*0.62,  y:0, w:W*0.38, h:H, fill:{color:C.NAVY},  line:{type:"none"} });
```

**Panel pairings by slide role:**

| Slide role | Left / top panel | Right / body panel |
|---|---|---|
| Hero | Black (62%) | Navy (38%) — holds "why it matters" + Mid Black stat cells |
| Problem / cost | Red `4.20"` panel — big serif stat + White copy | White panel from `x:4.255"` — failure modes with wide Red horizontal rules |
| Who we are | Navy `4.60"` panel | Black panel from `x:4.655"` — differentiators with tall `ICE` vertical rules |
| Method | Navy band (top, full width) | White body — 4 DS v2 bento cells, navy step numbers |
| Deliverable | Black + Mid top band | 3 dark columns (`NAVY`/`MID`) + full-width Red stat bar |
| Tiers | Navy band (top) | White paper — 3 bento cells: `MID` (Silver) / `NAVY` (Gold, featured) / `BLACK` (Diamond) |
| CTA | Red (45%) — headline + white button | Navy (55%) — "how it works" steps, `ICE` labels |

Titles are EB Garamond (white on dark, `NAVY` on light cards). Eyebrows, labels, body, and bullets are Hanken Grotesk. Use flat `RECTANGLE` only — never `ROUNDED_RECTANGLE`.

## PPTX Layout Patterns

### Pattern A — Title / Hero Hook

Use for: Slide 1 (cover), section dividers.

```javascript
// Eyebrow — LEFT-aligned, top of panel (never centered; centered titles are the AI-tell)
slide.addText("THE MIGRATION PROBLEM", {
  x: 0.7, y: 0.85, w: 7.5, h: 0.3,
  fontSize: 10, fontFace: "Hanken Grotesk", bold: true,
  color: "F5F7F9", align: "left", charSpacing: 5
});

// Headline (rich text array — line 2 in Red for problem framing). Match the template's EB Garamond display treatment.
slide.addText([
  { text: "Your stores are running.", options: { color: "F5F7F9", breakLine: true } },
  { text: "Your systems aren't.", options: { color: "a8201a" } }
], {
  x: 0.7, y: 2.2, w: 7.5, h: 2.0,
  fontSize: 40, fontFace: "EB Garamond", bold: false, italic: true, align: "left",
  lineSpacingMultiple: 1.05
});

// Sub-statement — left-aligned beneath
slide.addText("Scope first. Cutover second.", {
  x: 0.72, y: 4.5, w: 7, h: 0.5,
  fontSize: 11, fontFace: "Hanken Grotesk", color: "909396", align: "left"
});
```

### Pattern B — Bullet List

Use for: Problem depth, failure modes, key observations.

```javascript
const bullets = [
  { label: "Data integrity", body: "Products and variants that looked fine in staging don't survive the format conversion." },
  { label: "Workflow gaps", body: "Gift cards, loyalty, B2B accounts, and staff permissions live outside the standard export." },
  { label: "Timeline compression", body: "IT locks the cutover window. Issues surface when the floor is open, not in testing." },
];

bullets.forEach((b, i) => {
  const y = 2.0 + i * 0.85;
  // Navy accent bar marker — no border-radius
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0.5, y: y + 0.05, w: 0.06, h: 0.25,
    fill: { color: "0D1B2A" }, line: { color: "0D1B2A", transparency: 100 }
  });
  // Label
  slide.addText(b.label, {
    x: 0.68, y: y, w: 8.5, h: 0.3,
    fontSize: 14, fontFace: "Hanken Grotesk", bold: true, color: "F5F7F9"
  });
  // Body
  slide.addText(b.body, {
    x: 0.68, y: y + 0.3, w: 8.5, h: 0.45,
    fontSize: 13, fontFace: "Hanken Grotesk", color: "aaccdb"
  });
});
```

### Pattern C — Card List (Bordered)

Use for: Root cause analysis, solution pillars, service breakdown.

```javascript
const cards = [
  { label: "Scope-first methodology", body: "A scoped lane decision before technical work begins: Blueprint/advisory or full implementation." },
  { label: "Retail-native validation", body: "140+ retail-specific scenarios: gift cards, loyalty, staff permissions, B2B pricing, reporting parity." },
  { label: "Credited toward full engagement", body: "The [BLUEPRINT_FEE] blueprint fee applies in full to any Gold or Diamond engagement." },
];

const cardW = 2.8, cardH = 1.8, cardGap = 0.2;
const startX = (10 - (cardW * 3 + cardGap * 2)) / 2;

cards.forEach((card, i) => {
  const x = startX + i * (cardW + cardGap);
  const y = 2.5;
  // Card fill — Navy bento cell, flat (no border-radius), subtle hairline border
  slide.addShape(pres.shapes.RECTANGLE, {
    x, y, w: cardW, h: cardH,
    fill: { color: C.NAVY },
    line: { color: C.WHITE, transparency: 90, width: 1 }
  });
  // Label — Ice Blue on Navy
  slide.addText(card.label, {
    x: x + 0.18, y: y + 0.18, w: cardW - 0.36, h: 0.35,
    fontSize: 13, fontFace: "Hanken Grotesk", bold: true, color: "aaccdb"
  });
  // Body
  slide.addText(card.body, {
    x: x + 0.18, y: y + 0.56, w: cardW - 0.36, h: 1.0,
    fontSize: 12, fontFace: "Hanken Grotesk", color: "F5F7F9"
  });
});
```

### Pattern D — Two-Column Comparison (Before / After)

Use for: Before vs. after migration, old ops vs. new ops.

```javascript
const rows = [
  { before: "Manual PO receipts in Excel", after: "Digital receiving in AnyDB" },
  { before: "Inventory sync every 4 hours", after: "Real-time sync across all locations" },
  { before: "Transfer confirmation by text", after: "Transfer lifecycle tracked end-to-end" },
  { before: "Blind reorder decisions", after: "Replenishment triggered by sell-through data" },
];

const colW = 4.0, startX = 0.9, headerY = 2.1, rowH = 0.55;

// Headers — Before bar = Mid Black (red label), After bar = Navy (white label)
slide.addShape(pres.shapes.RECTANGLE, { x: startX, y: headerY, w: colW, h: 0.4, fill: { color: C.MID }, line: { type: "none" } });
slide.addText("BEFORE", { x: startX + 0.1, y: headerY + 0.05, w: colW - 0.2, h: 0.3, fontSize: 11, fontFace: "Hanken Grotesk", bold: true, color: C.RED });

slide.addShape(pres.shapes.RECTANGLE, { x: startX + colW + 0.1, y: headerY, w: colW, h: 0.4, fill: { color: C.NAVY }, line: { type: "none" } });
slide.addText("AFTER", { x: startX + colW + 0.2, y: headerY + 0.05, w: colW - 0.2, h: 0.3, fontSize: 11, fontFace: "Hanken Grotesk", bold: true, color: C.WHITE });

rows.forEach((row, i) => {
  const y = headerY + 0.4 + i * rowH;
  const leftFill = i % 2 === 0 ? C.MID : "0e0e0e";
  const rightFill = i % 2 === 0 ? C.NAVY : "0e0e0e";
  slide.addShape(pres.shapes.RECTANGLE, { x: startX, y, w: colW, h: rowH - 0.04, fill: { color: leftFill }, line: { color: leftFill, transparency: 100 } });
  slide.addText(row.before, { x: startX + 0.15, y: y + 0.1, w: colW - 0.3, h: rowH - 0.2, fontSize: 12, fontFace: "Hanken Grotesk", color: "aaccdb" });
  slide.addShape(pres.shapes.RECTANGLE, { x: startX + colW + 0.1, y, w: colW, h: rowH - 0.04, fill: { color: rightFill }, line: { color: rightFill, transparency: 100 } });
  slide.addText(row.after, { x: startX + colW + 0.25, y: y + 0.1, w: colW - 0.3, h: rowH - 0.2, fontSize: 12, fontFace: "Hanken Grotesk", color: "F5F7F9" });
});
```

### Pattern E — System Boundary / Architecture Diagram

Use for: How the two-system architecture works, integration overview.

```javascript
const boxY = 2.2, boxH = 2.3, boxW = 3.8;

// Left box — Navy fill, flat (no border-radius)
slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: boxY, w: boxW, h: boxH, fill: { color: "0D1B2A" }, line: { color: "F5F7F9", transparency: 90, width: 1 } });
slide.addText("SHOPIFY POS", { x: 0.65, y: boxY + 0.15, w: boxW - 0.3, h: 0.3, fontSize: 11, fontFace: "Hanken Grotesk", bold: true, color: "aaccdb", charSpacing: 4 });
["→ All transactions", "→ Inventory master", "→ Customer profiles", "→ Channel sync"].forEach((item, i) => {
  slide.addText(item, { x: 0.72, y: boxY + 0.55 + i * 0.4, w: boxW - 0.44, h: 0.36, fontSize: 12, fontFace: "Hanken Grotesk", color: "F5F7F9" });
});

// Arrow divider
slide.addText("→", { x: 4.5, y: boxY + boxH / 2 - 0.2, w: 0.9, h: 0.4, fontSize: 28, fontFace: "Hanken Grotesk", bold: true, color: "F5F7F9", align: "center" });

// Right box — Mid Black fill to distinguish from left Navy box
slide.addShape(pres.shapes.RECTANGLE, { x: 5.7, y: boxY, w: boxW, h: boxH, fill: { color: "181818" }, line: { color: "F5F7F9", transparency: 90, width: 1 } });
slide.addText("ANYDB OPS", { x: 5.85, y: boxY + 0.15, w: boxW - 0.3, h: 0.3, fontSize: 11, fontFace: "Hanken Grotesk", bold: true, color: "aaccdb", charSpacing: 4 });
["→ Purchase orders", "→ Receiving workflow", "→ Vendor reconciliation", "→ Custom automations"].forEach((item, i) => {
  slide.addText(item, { x: 5.92, y: boxY + 0.55 + i * 0.4, w: boxW - 0.44, h: 0.36, fontSize: 12, fontFace: "Hanken Grotesk", color: "F5F7F9" });
});
```

### Pattern F — Stat Callouts / Data Row

Use for: Scale indicators, risk data, urgency amplifiers.

```javascript
const stats = [
  { number: "3x", label: "More transfer errors per location added" },
  { number: "68%", label: "Of oversell incidents traced to sync lag" },
  { number: "14 days", label: "Average time to full diagnostic clarity" },
];

stats.forEach((stat, i) => {
  const x = 0.5 + i * 3.1;
  // Stat number — EB Garamond, White
  slide.addText(stat.number, {
    x, y: 2.3, w: 3.0, h: 1.1,
    fontSize: 52, fontFace: "EB Garamond", bold: false, color: "F5F7F9", align: "center"
  });
  // Stat label — Hanken Grotesk, Ice Blue
  slide.addText(stat.label, {
    x, y: 3.4, w: 3.0, h: 0.7,
    fontSize: 13, fontFace: "Hanken Grotesk", color: "aaccdb", align: "center"
  });
});
```

### Pattern G — CTA / Closing Slide

Use for: Final slide. Always the Blueprint offer.

```javascript
// Eyebrow — left-aligned, edge anchored
slide.addText("NEXT STEP", {
  x: 0.7, y: 1.15, w: 7.8, h: 0.3,
  fontSize: 10, fontFace: "Hanken Grotesk", bold: true,
  color: "F5F7F9", align: "left", charSpacing: 5
});

// Headline — EB Garamond, line 2 in Red for urgency
slide.addText([
  { text: "Book a 30-minute scoping call.", options: { color: "F5F7F9", breakLine: true } },
  { text: "No obligation.", options: { color: "a8201a" } }
], { x: 0.7, y: 1.5, w: 8.2, h: 1.0, fontSize: 32, fontFace: "EB Garamond", bold: false, align: "left" });

// Callout box — Navy fill, flat rectangle (no border-radius)
slide.addShape(pres.shapes.RECTANGLE, {
  x: 2.0, y: 2.65, w: 6.0, h: 1.65,
  fill: { color: "0D1B2A" }, line: { color: "F5F7F9", transparency: 90, width: 1 }
});

const ctaBullets = [
  "→  7-day Blueprint — full system map, risk register, rollout path",
  "→  [Value prop from this deck's problem space]",
  "→  [BLUEPRINT_FEE] — credited 100% toward Gold or Diamond",
];
ctaBullets.forEach((line, i) => {
  slide.addText(line, {
    x: 2.2, y: 2.82 + i * 0.44, w: 5.6, h: 0.38,
    fontSize: 12, fontFace: "Hanken Grotesk", color: "aaccdb"
  });
});

// CTA button — White fill, Black text, flat rectangle (no border-radius, no ROUNDED_RECTANGLE)
slide.addShape(pres.shapes.RECTANGLE, {
  x: 3.5, y: 4.45, w: 3.0, h: 0.5,
  fill: { color: "F5F7F9" }, line: { color: "F5F7F9", transparency: 100 }
});
slide.addText("BOOK THE BLUEPRINT →", {
  x: 3.5, y: 4.45, w: 3.0, h: 0.5,
  fontSize: 13, fontFace: "Hanken Grotesk", bold: true, color: "0e0e0e", align: "center"
});
```

## Deck Structure Rules

### Deck Types

**Client Proposal / Pitch Deck** (8-12 slides)
1. Cover — Pattern A
2. Executive Summary — Pattern B (3-5 action-title bullets summarizing SCR arc)
3. The Problem — Pattern B or C
4. Why It Compounds — Pattern F (stats) or B
5. Root Cause — Pattern C
6. Our Solution — Pattern E (architecture) or D
7. The Migration Process — Pattern B (numbered steps)
8. Before / After — Pattern D
9. Why KaizenCommerce — Pattern C (3 pillars: ex-Shopify experience, controlled cutover discipline, Blueprint/advisory)
10. Timeline / Investment — Pattern B or F
11. CTA — Pattern G

**Discovery / Workshop Deck** (6-8 slides)
1. Cover — Pattern A
2. Agenda — Pattern B (simple list)
3. Context slides (2-3) — Pattern B or C
4. Workshop prompts — Pattern B or E
5. Next Steps — Pattern B
6. CTA — Pattern G

**Leave-Behind / One-Pager Deck** (4-5 slides)
1. Cover — Pattern A
2. The Problem — Pattern B
3. Our Solution — Pattern C or E
4. CTA — Pattern G

**LinkedIn Carousel --> Deck Expansion**
Mirror the carousel structure but expand each slide to a full narrative slide using Pattern B or C, then add a Process slide (Pattern E) and a Why KaizenCommerce slide (Pattern C) before the CTA.

## Full PptxGenJS Boilerplate Script (structural fallback)

Use `../assets/templates/kaizen-pitch-deck-template.pptx` first when a PPTX can be cloned or edited. This runnable 7-slide script is a structural fallback for environments where the template cannot be used directly. It preserves the house deck structure while enforcing DS v2: 13.33×7.5, split-panel color blocking, EB Garamond display + Hanken Grotesk, closed palette, flat rectangles only. Adapt copy per topic; keep the panel structure and palette.

```javascript
// KaizenCommerce Pitch Deck — faithful to the brand deck:
// 13.33x7.5, split-panel color-blocked layouts, EB Garamond display + Hanken Grotesk,
// DS v2 closed palette. Do not add legacy ramps or non-system aliases.
const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.defineLayout({ name: "W", width: 13.333, height: 7.5 });
p.layout = "W";

const C = {
  BLACK:"0E0E0E", MID:"181818", NAVY:"0D1B2A", RED:"A8201A", WHITE:"F5F7F9", ICE:"AACCDB",
};
const F = { D:"EB Garamond", U:"Hanken Grotesk" };
const W = 13.333, H = 7.5;
const box = (s,o)=>s.addShape(p.shapes.RECTANGLE,o);
const t   = (s,txt,o)=>s.addText(txt,o);
const pageNo=(s,n)=>t(s,String(n).padStart(2,"0"),{x:W-0.8,y:H-0.5,w:0.5,h:0.3,fontSize:8,fontFace:F.U,color:C.WHITE,transparency:45,align:"right"});

// ── 1 — Hero (split: black left / navy right) ──
let s=p.addSlide();
box(s,{x:0,y:0,w:W*0.62,h:H,fill:{color:C.BLACK},line:{type:"none"}});
box(s,{x:W*0.62,y:0,w:W*0.38,h:H,fill:{color:C.NAVY},line:{type:"none"}});
t(s,"KaizenCommerce",{x:0.7,y:0.6,w:5,h:0.5,fontFace:F.D,fontSize:20,color:C.WHITE,bold:true});
t(s,"Shopify POS Migration Specialists",{x:0.72,y:1.05,w:6,h:0.3,fontFace:F.U,fontSize:9,color:C.WHITE,transparency:35});
t(s,[{text:"Your stores are running.",options:{color:C.WHITE,breakLine:true}},
     {text:"Your systems aren't.",options:{color:C.RED}}],
  {x:0.7,y:2.4,w:7.2,h:2.0,fontFace:F.D,fontSize:40,lineSpacingMultiple:1.05});
box(s,{x:0.72,y:4.5,w:0.5,h:0.03,fill:{color:C.RED},line:{type:"none"}});
t(s,"Scope first. Cutover second.",{x:0.72,y:4.7,w:6,h:0.3,fontFace:F.U,fontSize:11,color:C.WHITE,transparency:35});
t(s,"WHY IT MATTERS",{x:W*0.62+0.5,y:0.8,w:4,h:0.3,fontFace:F.U,fontSize:8,bold:true,color:C.ICE,charSpacing:3});
t(s,[{text:"Every gap your pre-migration checklist missed shows up on go-live day. ",options:{color:C.WHITE}},
     {text:"We prevent that.",options:{color:C.ICE,bold:true}},
     {text:"\n\nLed by ex-Shopify retail operators who've seen it from the inside.",options:{color:C.WHITE}}],
  {x:W*0.62+0.5,y:1.25,w:4.2,h:2.4,fontFace:F.U,fontSize:11,lineSpacingMultiple:1.2});
// Stats stacked as hairline-divided rows (NOT filled boxes — matches the reference deck).
[["200+","migrations led"],["< 1%","go-live failures"],["7 days","to blueprint"]].forEach((d,i)=>{
  const y=3.95+i*0.92;
  box(s,{x:W*0.62+0.5,y,w:4.2,h:0.0075,fill:{color:C.NAVY,transparency:35},line:{type:"none"}}); // 0.75pt hairline
  t(s,d[0],{x:W*0.62+0.5,y:y+0.16,w:2.2,h:0.55,fontFace:F.D,fontSize:26,color:C.WHITE,italic:true});
  t(s,d[1],{x:W*0.62+2.2,y:y+0.34,w:2.5,h:0.4,fontFace:F.U,fontSize:9.5,color:C.ICE,align:"right"});
});
pageNo(s,1);

// ── 2 — Problem/Cost (split: red left / white right) ──
s=p.addSlide();
const problemLeftW=4.2;
const problemRightX=4.255;
box(s,{x:0,y:0,w:problemLeftW,h:H,fill:{color:C.RED},line:{type:"none"}});
box(s,{x:problemRightX,y:0,w:W-problemRightX,h:H,fill:{color:C.WHITE},line:{type:"none"}});
t(s,"THE COST OF A BAD MIGRATION",{x:0.7,y:0.8,w:4.5,h:0.3,fontFace:F.U,fontSize:8,bold:true,color:C.WHITE,charSpacing:3});
t(s,"$30K–$80K",{x:0.7,y:2.4,w:4.5,h:1.2,fontFace:F.D,fontSize:52,color:C.WHITE});
t(s,"average recovery cost per botched retail POS migration",{x:0.72,y:3.7,w:4,h:0.6,fontFace:F.U,fontSize:11,color:C.WHITE});
t(s,"Downtime. Manual workarounds. Angry store staff. Inventory frozen for days. Leadership asking if you can roll back. You can't.",
  {x:0.72,y:4.6,w:4,h:1.5,fontFace:F.U,fontSize:10,color:C.WHITE,transparency:20,lineSpacingMultiple:1.3});
t(s,"WHERE MIGRATIONS FAIL",{x:4.575,y:0.8,w:5,h:0.3,fontFace:F.U,fontSize:8,bold:true,color:C.BLACK,transparency:40,charSpacing:3});
[["Data integrity","Products and variants that looked fine in staging don't survive the format conversion."],
 ["Workflow gaps","Gift cards, loyalty points, B2B accounts, and staff permissions live outside the standard export."],
 ["Timeline compression","IT locks the cutover window. Go-live pressure forces teams to skip validation steps."]].forEach((d,i)=>{
  const y=1.18+i*1.56;
  // Reference deck uses wide Red horizontal rules on white panels.
  box(s,{x:4.575,y:y,w:8.958,h:0.04,fill:{color:C.RED},line:{type:"none"}});
  t(s,d[0],{x:4.575,y:y+0.18,w:6,h:0.4,fontFace:F.U,fontSize:13,bold:true,color:C.BLACK});
  t(s,d[1],{x:4.575,y:y+0.63,w:6.2,h:0.9,fontFace:F.U,fontSize:10,color:C.BLACK,transparency:25,lineSpacingMultiple:1.25});
});
pageNo(s,2);

// ── 3 — Who We Are (split: navy left / black right) ──
s=p.addSlide();
const whoLeftW=4.6;
const whoRightX=4.655;
box(s,{x:0,y:0,w:whoLeftW,h:H,fill:{color:C.NAVY},line:{type:"none"}});
box(s,{x:whoRightX,y:0,w:W-whoRightX,h:H,fill:{color:C.BLACK},line:{type:"none"}});
t(s,"WHO WE ARE",{x:0.7,y:0.8,w:4,h:0.3,fontFace:F.U,fontSize:8,bold:true,color:C.ICE,charSpacing:3});
t(s,[{text:"Ex-Shopify",options:{color:C.WHITE,breakLine:true}},{text:"Retail Operators.",options:{color:C.WHITE}}],
  {x:0.7,y:2.3,w:5,h:1.6,fontFace:F.D,fontSize:34,lineSpacingMultiple:1.05});
t(s,[{text:"We built and managed retail operations on Shopify before we advised on them.\n\n",options:{color:C.WHITE}},
     {text:"No generalist IT consultants. No offshore dev shops.",options:{color:C.ICE}}],
  {x:0.72,y:4.2,w:4.8,h:2,fontFace:F.U,fontSize:11,lineSpacingMultiple:1.25});
t(s,"WHAT SETS US APART",{x:4.975,y:0.8,w:5,h:0.3,fontFace:F.U,fontSize:8,bold:true,color:C.WHITE,transparency:35,charSpacing:3});
[["Scope-first methodology","We confirm the lane before technical work begins: advisory or full implementation."],
 ["Retail-native validation","Our QA checklist covers 140+ retail-specific scenarios."],
 ["Credited toward full engagement","The [BLUEPRINT_FEE] blueprint fee applies in full to any Gold or Diamond engagement."]].forEach((d,i)=>{
  const y=1.16+i*1.52;
  // Reference deck uses tall ICE vertical rules on dark panels.
  box(s,{x:4.975,y:y,w:0.04,h:1.3,fill:{color:C.ICE},line:{type:"none"}});
  t(s,d[0],{x:5.25,y:y+0.15,w:6,h:0.4,fontFace:F.U,fontSize:13,bold:true,color:C.ICE});
  t(s,d[1],{x:5.25,y:y+0.6,w:6,h:0.8,fontFace:F.U,fontSize:10,color:C.WHITE,transparency:30,lineSpacingMultiple:1.25});
});
pageNo(s,3);

// ── 4 — Methodology (navy top band + DS v2 bento cells) ──
s=p.addSlide();
box(s,{x:0,y:0,w:W,h:H,fill:{color:C.WHITE},line:{type:"none"}});
box(s,{x:0,y:0,w:W,h:1.7,fill:{color:C.NAVY},line:{type:"none"}});
t(s,"THE KAIZENCOMMERCE METHOD",{x:0.7,y:0.45,w:6,h:0.3,fontFace:F.U,fontSize:8,bold:true,color:C.ICE,charSpacing:3});
t(s,"Scope first. Cutover second.",{x:0.7,y:0.8,w:9,h:0.7,fontFace:F.D,fontSize:26,color:C.WHITE});
const steps=[["01","DIAGNOSE","Structured discovery across your current POS, catalogue, inventory, integrations, and workflows.",["Current system audit","Data schema mapping","Integration inventory","Staff workflow review"]],
 ["02","ARCHITECT","We design the target-state Shopify configuration and write the full migration blueprint.",["Target-state design","Risk register","Rollback plan","Go/No-go criteria"]],
 ["03","VALIDATE","Parallel environment testing against 140+ retail scenarios before cutover.",["140+ scenario QA","Register walkthroughs","Gift card & loyalty","Reporting parity"]],
 ["04","SCALE","Post-cutover stabilisation, staff training, and hypercare support.",["Go-live oversight","Floor-hour support","Staff certification","30-day hypercare"]]];
const cw=2.85, gap=0.3, x0=0.7;
steps.forEach((st,i)=>{
  const x=x0+i*(cw+gap);
  const fill = i % 2 ? C.NAVY : C.MID;
  const text = fill === C.NAVY ? C.ICE : C.WHITE;
  box(s,{x,y:2.2,w:cw,h:4.6,fill:{color:fill},line:{type:"none"}});
  box(s,{x,y:2.2,w:cw,h:0.08,fill:{color:C.RED},line:{type:"none"}});
  t(s,st[0],{x:x+0.25,y:2.45,w:1.5,h:0.7,fontFace:F.D,fontSize:24,color:text});
  t(s,st[1],{x:x+0.25,y:3.2,w:cw-0.5,h:0.35,fontFace:F.U,fontSize:11,bold:true,color:text,charSpacing:2});
  t(s,st[2],{x:x+0.25,y:3.6,w:cw-0.5,h:1.4,fontFace:F.U,fontSize:9,color:C.WHITE,lineSpacingMultiple:1.2,transparency:18});
  t(s,st[3].map((d,j)=>({text:"–  "+d,options:{breakLine:true,color:text}})),
    {x:x+0.25,y:5.2,w:cw-0.5,h:1.5,fontFace:F.U,fontSize:9,lineSpacingMultiple:1.3});
});
pageNo(s,4);

// ── 5 — Blueprint Deliverable (dark, 3 columns + red stat bar) ──
s=p.addSlide();
box(s,{x:0,y:0,w:W,h:H,fill:{color:C.BLACK},line:{type:"none"}});
box(s,{x:0,y:0,w:W,h:1.6,fill:{color:C.MID},line:{type:"none"}});
t(s,"WHAT YOU RECEIVE IN 7 BUSINESS DAYS",{x:0.7,y:0.4,w:7,h:0.3,fontFace:F.U,fontSize:8,bold:true,color:C.WHITE,transparency:35,charSpacing:3});
t(s,"The Blueprint Deliverable",{x:0.7,y:0.75,w:9,h:0.7,fontFace:F.D,fontSize:26,color:C.WHITE});
const cols=[["System Map","A full technical map of your current POS environment.",["Product & variant schema","Inventory location matrix","Integration dependencies","Data gap analysis"],C.NAVY],
 ["Risk Register","Every migration risk, ranked by severity, with mitigation.",["Risk severity ranking","Mitigation recommendations","Effort estimates","Go/No-go checklist"],C.MID],
 ["Rollout Path","A sequenced cutover plan with validation checkpoints.",["Phased cutover sequence","Staff role assignments","Validation checkpoints","Tested rollback plan"],C.NAVY]];
const c5w=3.9;
cols.forEach((c,i)=>{
  const x=0.7+i*(c5w+0.25);
  box(s,{x,y:2.0,w:c5w,h:3.4,fill:{color:c[3]},line:{type:"none"}});
  t(s,c[0],{x:x+0.3,y:2.25,w:c5w-0.6,h:0.5,fontFace:F.D,fontSize:20,color:C.WHITE});
  t(s,c[1],{x:x+0.3,y:2.85,w:c5w-0.6,h:0.7,fontFace:F.U,fontSize:9,color:C.WHITE,transparency:28,lineSpacingMultiple:1.2});
  t(s,c[2].map(d=>({text:"–  "+d,options:{breakLine:true,color:C.WHITE}})),
    {x:x+0.3,y:3.7,w:c5w-0.6,h:1.6,fontFace:F.U,fontSize:9,lineSpacingMultiple:1.35});
});
box(s,{x:0.7,y:5.7,w:W-1.4,h:1.1,fill:{color:C.RED},line:{type:"none"}});
[["[BLUEPRINT_FEE]","fixed fee"],["7 days","turnaround"],["Written report","PDF + working files"],["Credited 100%","toward Gold or Diamond"]].forEach((d,i)=>{
  const x=1.0+i*2.95;
  t(s,d[0],{x,y:5.85,w:2.8,h:0.5,fontFace:F.D,fontSize:22,color:C.WHITE});
  t(s,d[1],{x,y:6.4,w:2.8,h:0.3,fontFace:F.U,fontSize:9,color:C.WHITE});
});
pageNo(s,5);

// ── 6 — Tiers (light paper, 3 DS v2 cells: mid / navy featured / black) ──
s=p.addSlide();
box(s,{x:0,y:0,w:W,h:H,fill:{color:C.WHITE},line:{type:"none"}});
box(s,{x:0,y:0,w:W,h:1.6,fill:{color:C.NAVY},line:{type:"none"}});
t(s,"CHOOSE THE DEPTH YOUR MIGRATION REQUIRES",{x:0.7,y:0.4,w:8,h:0.3,fontFace:F.U,fontSize:8,bold:true,color:C.ICE,charSpacing:3});
t(s,"Engagement Tiers",{x:0.7,y:0.75,w:9,h:0.7,fontFace:F.D,fontSize:26,color:C.WHITE});
const tiers=[["Silver","Blueprint + Advisory",["Full migration blueprint","Risk register + rollback","3 advisory sessions","Go-live day support call"],"2–10 locations",C.MID,C.WHITE,C.WHITE,C.WHITE],
 ["Gold","Full-Service Migration",["Everything in Silver","Technical migration execution","140+ scenario QA","Hypercare (30 days)"],"5–20 locations",C.NAVY,C.ICE,C.WHITE,C.WHITE],
 ["Diamond","Enterprise Multi-Site",["Everything in Gold","Multi-site coordination","Dedicated migration pod","Executive status reporting"],"20+ locations",C.BLACK,C.WHITE,C.WHITE,C.WHITE]];
const tw=3.9;
tiers.forEach((tr,i)=>{
  const x=0.7+i*(tw+0.25), y=2.0;
  box(s,{x,y,w:tw,h:4.6,fill:{color:tr[4]},line:{type:"none"}});
  t(s,tr[0],{x:x+0.3,y:y+0.25,w:tw-0.6,h:0.5,fontFace:F.D,fontSize:22,color:tr[5]});
  t(s,tr[1],{x:x+0.3,y:y+0.85,w:tw-0.6,h:0.35,fontFace:F.U,fontSize:10,bold:true,color:tr[6]});
  t(s,tr[2].map(d=>({text:"–  "+d,options:{breakLine:true,color:tr[7]}})),
    {x:x+0.3,y:y+1.4,w:tw-0.6,h:2.0,fontFace:F.U,fontSize:9.5,lineSpacingMultiple:1.4});
  t(s,"Custom",{x:x+0.3,y:y+3.7,w:tw-0.6,h:0.4,fontFace:F.D,fontSize:18,color:tr[6]});
  t(s,tr[3],{x:x+0.3,y:y+4.15,w:tw-0.6,h:0.3,fontFace:F.U,fontSize:9,color:tr[7]==C.WHITE?C.WHITE:C.BLACK,transparency:28});
});
t(s,"All engagements begin with a [BLUEPRINT_FEE] Blueprint. Fee is credited in full toward Gold or Diamond.",
  {x:0.7,y:6.8,w:11,h:0.3,fontFace:F.U,fontSize:9,color:C.BLACK,transparency:40});
pageNo(s,6);

// ── 7 — CTA (split: red left / navy right) ──
s=p.addSlide();
box(s,{x:0,y:0,w:W*0.45,h:H,fill:{color:C.RED},line:{type:"none"}});
box(s,{x:W*0.45,y:0,w:W*0.55,h:H,fill:{color:C.NAVY},line:{type:"none"}});
t(s,"NEXT STEP",{x:0.7,y:0.9,w:4,h:0.3,fontFace:F.U,fontSize:8,bold:true,color:C.WHITE,charSpacing:3});
t(s,[{text:"Start with",options:{color:C.WHITE,breakLine:true}},{text:"the Blueprint.",options:{color:C.WHITE}}],
  {x:0.7,y:2.3,w:5,h:1.8,fontFace:F.D,fontSize:38,lineSpacingMultiple:1.05});
t(s,"Book a 30-minute scoping call. We'll assess your current environment and confirm whether you're a fit.",
  {x:0.72,y:4.2,w:4.6,h:1,fontFace:F.U,fontSize:11,color:C.WHITE,transparency:20,lineSpacingMultiple:1.3});
box(s,{x:0.72,y:5.4,w:3.2,h:0.55,fill:{color:C.WHITE},line:{type:"none"}});
t(s,"BOOK THE BLUEPRINT →",{x:0.72,y:5.4,w:3.2,h:0.55,fontFace:F.U,fontSize:11,bold:true,color:C.RED,align:"center"});
t(s,"info@kaizencommerce.ca  ·  kaizencommerce.ca",{x:0.72,y:6.1,w:5,h:0.3,fontFace:F.U,fontSize:9,color:C.WHITE,transparency:20});
t(s,"HOW IT WORKS",{x:W*0.45+0.6,y:0.9,w:5,h:0.3,fontFace:F.U,fontSize:8,bold:true,color:C.ICE,charSpacing:3});
[["01 — Book the Blueprint call","Fill in the 2-minute intake form. We review your situation and confirm scope."],
 ["02 — Discovery & mapping","One structured session with your ops and IT leads."],
 ["03 — Blueprint delivered","Within 7 business days: system map, risk register, rollout path."],
 ["04 — Decide your path","Keep the blueprint and execute in-house, or apply the fee toward full delivery."]].forEach((d,i)=>{
  const y=1.5+i*1.2;
  t(s,d[0],{x:W*0.45+0.6,y,w:6,h:0.35,fontFace:F.U,fontSize:11,bold:true,color:C.ICE});
  t(s,d[1],{x:W*0.45+0.6,y:y+0.4,w:6,h:0.7,fontFace:F.U,fontSize:9.5,color:C.WHITE,transparency:30,lineSpacingMultiple:1.2});
});
pageNo(s,7);

p.writeFile({fileName:"/mnt/user-data/outputs/kaizen-pitch-deck.pptx"}).then(f=>console.log("PPTX written:",f));
```

## PPTX QA Checklist

After generating, always run:

```bash
npm install -g pptxgenjs  # if not installed
node deck.js              # generate the file
python -m markitdown /mnt/user-data/outputs/deck.pptx  # text check
```

Then convert to images and inspect visually:
```bash
soffice --headless --convert-to pdf /mnt/user-data/outputs/deck.pptx
rm -f slide-*.jpg
pdftoppm -jpeg -r 150 deck.pdf slide
ls -1 "$PWD"/slide-*.jpg
```

Check for:
- Text overflow on any slide
- Card borders invisible (transparency too high)
- Eyebrow / headline overlap (y-positions too close)
- CTA pill button text contrast (must be dark text on accent fill)
- Logo readable at small size
- Orbs not covering content (verify they extend off-canvas)
- Consistent slide number in bottom-right
- Every slide title is an action title (full sentence, not topic label)
- SCR arc is readable from titles alone
- Source citations present for all external data

## Common Deck Topics (Pre-seeded)

| Deck Title | Use Case | Primary Color |
|---|---|---|
| The Migration Blueprint | Sales pitch — POS migration | Red (problem) + Navy (process) |
| The 2-Location Wall | Problem education — ops complexity | Red (problem) + Navy (solution) |
| Commerce Operations Architecture | Technical discovery | Navy dominant |
| Why AnyDB + Shopify | Solution architecture explainer | Navy + Mid Black |
| The B2B Ops Gap | B2B Shopify pitch | Red (problem) + Navy (process) |
| Blueprint First — How It Works | Process walkthrough | Navy dominant |
| The Inventory Sync Problem | Awareness / education | Red (problem) + Navy (fix) |
| KaizenCommerce Capabilities Overview | RFP response / capabilities deck | Black dominant, Navy accent |

## Deck Example — Leave-Behind (4 slides)

```
DECK: The Migration Blueprint — Leave-Behind
TYPE: Leave-Behind (4 slides)
ACCENT: Red + Navy
SCR ARC:
  S: You're running 4 locations on Lightspeed with manual inventory reconciliation.
  C: Every new location multiplies the operational chaos — oversells, blind transfers, stale data.
  R: A 14-day Blueprint diagnostic maps every gap before a single record moves.

---

SLIDE 1 — COVER (Pattern A)
Eyebrow: THE MIGRATION PROBLEM
Headline:
  Line 1 (white): Your POS works.
  Line 2 (red): Your operations don't.
  Line 3 (white): We fix the second part.
Sub-statement: Multi-location retailers lose $14K-$23K/year to operational gaps their POS can't see.

---

SLIDE 2 — THE PROBLEM (Pattern B)
Action Title: "Most multi-location retailers lose 6-12 hours per week to inventory reconciliation that a unified system eliminates"
Eyebrow: WHAT BREAKS AT SCALE
Bullets:
  - [red] Inventory drift | Each location tracks its own stock. No single truth across channels.
  - [red] Transfer chaos | Transfers logged in spreadsheets, confirmed by text, verified by memory.
  - [red] Blind replenishment | Reorder decisions made without real-time sell-through data.
Footer: KaizenCommerce analysis — based on 15+ multi-location migration assessments.

---

SLIDE 3 — THE SOLUTION (Pattern E)
Action Title: "Separating commerce from operations gives retailers one source of truth without sacrificing workflow flexibility"
Eyebrow: THE ARCHITECTURE
Left Box — SHOPIFY POS:
  -> All transactions
  -> Inventory master (single source)
  -> Customer profiles
  -> Channel sync
Right Box — ANYDB OPS:
  -> Purchase orders
  -> Receiving workflow
  -> Vendor reconciliation
  -> Custom automations
Footer: Commerce and operations in sync. Not in competition.

---

SLIDE 4 — CTA (Pattern G)
Eyebrow: KAIZEN UNIFIED COMMERCE BLUEPRINT
Headline:
  Line 1 (white): See every gap before
  Line 2 (red): a single record moves.
CTA Box:
  -> 14-day diagnostic of your inventory, POS, and operational workflows
  -> Full migration roadmap with data mapping, timeline, and risk assessment
  -> [BLUEPRINT_FEE] — credited toward your implementation

kaizencommerce.ca ->
```

---

# MODE 3: VOICE REVIEW
