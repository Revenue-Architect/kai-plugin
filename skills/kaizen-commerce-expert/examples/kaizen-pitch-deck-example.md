# KaizenCommerce Pitch Deck — Reference Example

This is the canonical KaizenCommerce sales deck for voice, structure, stat usage, and rhythm. Load
this file when generating, reviewing, or adapting a PPTX presentation or LinkedIn carousel for
KaizenCommerce.

## Canonical Visual Artifact

The visual source of truth is `../reference/kaizen-ds-v2.html`. The canonical reusable template is
`../assets/templates/kaizen-pitch-deck-template.pptx`; the adjacent
`kaizen-pitch-deck-example.pptx` is the byte-identical calibration artifact for pacing, structure,
and original brand rhythm. This markdown file is an inspection guide, not a substitute for either
artifact. When generating PPTX files, follow DS v2 first, then use the deck to preserve the
seven-slide cadence and editorial restraint.

**Do not use prior dummy decks for visual calibration.** If the `.pptx` can be inspected, inspect it
directly, then reconcile anything that differs from DS v2 back to `kaizen-ds-v2.html`.

**Format:** 7-slide LinkedIn-first pitch deck  
**Primary use:** Sales calls, partner intros, Shopify AE handoffs, cold outbound follow-ups  
**Render via:** `kaizen-publish` PPTX mode

**DS v2 deck profile:**
- Split-panel or bento editorial layouts, not a uniform card grid.
- Template-matched EB Garamond display styling for macro titles/stats; Hanken Grotesk for body, labels, small caps, and UI.
- Core DS v2 colors carry the composition. Governed grey, steel-blue, red-tint, light-panel, and reference dark-variant ramps are allowed only when matching the template/reference artifact or improving dense deck readability.
- Slide 01 is a dark hero with big serif headline, navy stat panel, and stacked stats.
- Slide 02 uses a red problem field against a light explanatory field.
- Slide 06 treats Gold as the featured Navy tier.
- No rounded cards, shadows, gradients, glows, icon clutter, or decorative geometry.

---

## Slide Structure

### Slide 01 — Hero Hook

**Eyebrow:** KaizenCommerce · Shopify POS Launch And Workflow Specialists

**Headline (3 lines):**
```
Your stores are ready.
Your workflows aren't.
Plan first. Launch with control.
```

**Pain amplifier (body):**
> Every gap your launch checklist missed shows up when stores start selling: mismatched products,
> broken workflows, gift cards that do not transfer, purchase orders that still live in email. We
> map those gaps before the rollout.

**Credibility sub-line:**
> Led by ex-Shopify retail operators who've seen it from the inside.

**Stats row (EB Garamond large numerals):**
- `200+` migrations led
- `< 1%` go-live failures
- `7 days` to blueprint

**DS v2 layout:** Full dark surface (`#0e0e0e`). Stats in EB Garamond 500. Eyebrow in Hanken
Grotesk 800 UPPERCASE. Headline in EB Garamond 500. Slide indicator `01` bottom-right.

---

### Slide 02 — Problem / Cost of Inaction

**Eyebrow:** THE COST OF A BAD MIGRATION

**Stat (full-width, centered):**
```
$30K–$80K
```
*average recovery cost per botched retail POS migration*

**Pain narrative:**
> Downtime. Manual workarounds. Angry store staff. Inventory frozen for days while you reconcile
> what the old system exported and what Shopify actually imported. Leadership asking if you can
> roll back. You can't.

**Three failure modes (pattern: bold label / description):**

| Failure Mode | Why It Happens |
|---|---|
| Data integrity | Products, variants, and inventory quantities that looked fine in staging don't survive the format conversion. Shopify and legacy POS systems don't speak the same schema. |
| Workflow gaps | Gift cards, loyalty points, B2B accounts, and staff permissions live outside the standard export. Nobody maps them until go-live — when the register throws an error. |
| Timeline compression | IT locks the cutover window. Go-live pressure forces teams to skip validation steps. Issues surface when the floor is open, not in a test environment. |

**DS v2 layout:** Stat in EB Garamond. Failure modes as bento grid cells (Mid Black `#181818`).
Red (`#a8201a`) used for the stat or a single accent mark — not for all three cells.

---

### Slide 03 — Who We Are / Differentiation

**Eyebrow:** WHO WE ARE

**Authority statement:**
> We built and managed retail operations on Shopify before we advised on them. That means we know
> where the platform bends — and where it breaks.

**Sub-statement:**
> No generalist IT consultants. No offshore dev shops. Every engagement is led by someone who
> has personally stood at a register during a go-live.

**Three differentiators (named):**

**Blueprint Diagnostic + Advisory**
> The Blueprint Diagnostic is KaizenCommerce's paid pre-implementation audit and launch plan. It
> gives capable internal teams the architecture, workflow translation, QA path, and implementation
> number before they build.

**Retail-native validation**
> Our QA checklist covers retail-specific scenarios: gift cards, loyalty, staff permissions,
> multi-location inventory, B2B pricing, reporting parity, Special Orders workflows, and store-team
> exceptions.

**Credited toward full engagement**
> The $2,000 blueprint fee applies in full to any Gold or Diamond engagement. You're not paying
> to be sold — you're paying to know what you're buying.

**DS v2 layout:** Three differentiators in bento grid (Navy `#0D1B2A` cells). Ice Blue
`#aaccdb` for eyebrow labels within Navy cells. No red on this slide — this is a trust/process slide.

---

### Slide 04 — Methodology

**Eyebrow:** Diagnose first. Launch with control. · THE KAIZENCOMMERCE METHOD

**Four-step process (numbered, sequential):**

| Step | Name | Description | Deliverables |
|---|---|---|---|
| 01 | DIAGNOSE | Structured discovery across your current POS, product catalogue, inventory, integrations, and staff workflows. | Current system audit · Data schema mapping · Integration inventory · Staff workflow review |
| 02 | ARCHITECT | We design the target-state Shopify POS configuration, launch plan, and operational workflow layer where needed. | Target-state design · Risk register · rollout plan · Go/No-go criteria |
| 03 | VALIDATE | Store-team testing against retail scenarios before broader rollout is approved. | Scenario QA · Register walkthroughs · Gift card & loyalty · Reporting parity |
| 04 | LAUNCH | Pilot launch support, phased rollout, staff training, and post-launch stabilization. | Launch oversight · Floor-hour support · Staff certification · stabilization plan |

**DS v2 layout:** Steps as bento grid row. Alternating Black `#0e0e0e` / Navy `#0D1B2A` cells.
Step numbers in EB Garamond large. Step names in Hanken Grotesk 800 UPPERCASE. Deliverables as
Hanken Grotesk 400 sub-list.

---

### Slide 05 — The Blueprint Diagnostic + Advisory Deliverable

**Eyebrow:** Paid Diagnostic And Advisory · WHAT YOU RECEIVE IN 7 BUSINESS DAYS

**Three deliverable sections:**

**System Map**
> A full technical map of your current POS environment: products, variants, inventory locations,
> integrations, and data relationships in Shopify's schema.
- Product & variant schema
- Inventory location matrix
- Integration dependencies
- Data gap analysis

**Risk Register**
> Every identified migration risk, ranked by severity, with recommended mitigation and the
> estimated effort to resolve before cutover is approved.
- Risk severity ranking
- Mitigation recommendations
- Effort estimates
- Go/No-go checklist

**Rollout Path**
> A sequenced launch plan with timing windows, staff assignments, validation checkpoints, and a
> recovery path for each phase.
- Phased cutover sequence
- Staff role assignments
- Validation checkpoints
- Tested rollback plan

**Blueprint stats (EB Garamond numerals, bottom bar):**
- `$2,000` fixed fee
- `7 days` turnaround
- Written report — PDF + working files
- Credited 100% toward Gold or Diamond

**DS v2 layout:** Three columns (bento grid). Stats bar at bottom in Black with White text.
No red except potentially on the `$2,000` stat to signal the CTA action.

---

### Slide 06 — Engagement Tiers

**Eyebrow:** Engagement Tiers · CHOOSE THE DEPTH YOUR MIGRATION REQUIRES

**Three tiers:**

| Tier | Name | Positioning | Includes | Scale |
|---|---|---|---|---|
| Silver | Blueprint + Advisory | For teams handling execution in-house who need a paid pre-implementation audit, launch plan, and technical advisor through rollout. | Full diagnostic · Risk register + launch plan · 3 advisory sessions · Go-live day support call | Custom · 2–10 locations |
| Gold | Full Implementation | End-to-end delivery. We own Shopify POS delivery, operational coverage, existing-stack integrations, and store-team testing. | Everything in Silver · Technical migration execution · workflow build where scoped · launch QA · stabilization | Custom · 5–20 locations |
| Diamond | Enterprise Multi-Site | Purpose-built for multi-banner or complex operators needing existing-stack integrations, operational workflow layer, and executive reporting. | Everything in Gold · Multi-site coordination · dedicated migration pod · executive status reporting | Custom · 20+ locations |

**Footer note:**
> All engagements begin with a $2,000 Blueprint. Fee is credited in full toward Gold or Diamond.

**DS v2 layout:** Three-column bento grid. Silver = Mid Black `#181818`. Gold = Navy `#0D1B2A`.
Diamond = Black `#0e0e0e`. Feature lists in Hanken Grotesk 400. Tier names in EB Garamond.
Scale badge at bottom of each cell.

---

### Slide 07 — CTA / Next Step

**Eyebrow:** NEXT STEP

**CTA statement:**
> Book a 30-minute scoping call. We'll assess your current environment and confirm whether you're
> a fit — no obligation.

**Primary CTA button:**
`BOOK THE BLUEPRINT →`

**Contact:**
`info@kaizencommerce.ca  ·  kaizencommerce.ca`

**Blueprint summary line:**
`$2,000 · 1-2 week turnaround · Credited toward full engagement`

**Four-step process (compact, how it works):**
1. Book the Blueprint call — Fill in the 2-minute intake form. We review your situation and confirm scope before charging anything.
2. Discovery & mapping — One structured session with your ops and IT leads. We audit your current POS, catalogue, and integration stack.
3. Blueprint delivered — Within 7 business days: system map, risk register, and phased rollout path — in writing, yours to keep.
4. Decide your path — Keep the blueprint and execute in-house, or apply the fee toward a full-service engagement. No pressure either way.

**DS v2 layout:** Full dark surface. CTA button in White `#F5F7F9` fill, Black text, Hanken
Grotesk 800 UPPERCASE, no border-radius. Red `#a8201a` used for the accent mark next to the CTA.
Process steps numbered in EB Garamond.

---

## Voice Reference (extracted from deck)

These phrases demonstrate the KaizenCommerce register. Use them as pattern examples when writing:

**Problem framing (specific, not generic):**
- "Every gap your pre-migration checklist missed shows up on go-live day"
- "Inventory frozen for days while you reconcile what the old system exported and what Shopify actually imported"
- "Leadership asking if you can roll back. You can't."

**Authority without arrogance:**
- "Led by ex-Shopify retail operators who've seen it from the inside"
- "Every engagement is led by someone who has personally stood at a register during a go-live"
- "We know where the platform bends — and where it breaks"

**Specificity over claims:**
- "140+ retail-specific scenarios" (not "comprehensive QA")
- "$30K–$80K average recovery cost per botched retail POS migration" (not "migrations can be costly")
- "7 business days" (not "fast turnaround")

**Framing that removes pressure:**
- "You're not paying to be sold — you're paying to know what you're buying"
- "Keep the blueprint and execute in-house, or apply the fee toward a full-service engagement. No pressure either way"

---

## Visual Approach — Split-Panel Layouts (slide-level summary)

Format: **13.333 × 7.5 in**. Every slide is **two full-bleed color-blocked panels** (or top band + body). Titles EB Garamond serif; eyebrows/labels/body Hanken Grotesk; flat rectangles only.

| Slide | Panel split | Eyebrow | EB Garamond | Notes |
|---|---|---|---|---|
| 01 Hero | Black (62%) + Navy (38%) | White / Ice Blue on Navy | Headline (white + red line), stat numbers | Stacked stats on Navy, no boxed stat cards |
| 02 Problem | Red (42%) + White paper (58%) | White on Red / alpha Black on light | `$30K–$80K` cost stat | Failure modes with red tick marks |
| 03 Who We Are | Navy (46%) + Black (54%) | Ice Blue on Navy / alpha White on Black | "Ex-Shopify Retail Operators." | Differentiators, Ice Blue labels only on Navy |
| 04 Method | Navy band (top) + White paper body | Ice Blue on Navy | Step numbers (navy) | Flat bento cells using Black, Mid, Navy, or rare White emphasis |
| 05 Deliverable | Black + Mid band | Alpha White | Column titles, stat-bar numbers | 3 dark columns + full-width Red stat bar |
| 06 Tiers | Navy band (top) + White paper body | Ice Blue on Navy | Tier names | Silver Mid Black / Gold Navy featured / Diamond Black |
| 07 CTA | Red (45%) + Navy (55%) | White on Red / Ice Blue on Navy | "Start with the Blueprint." | White button, black or red text; how-it-works steps |

**Palette:** DS v2 only: Black `#0e0e0e`, Mid Black `#181818`, Navy `#0D1B2A`, Red `#a8201a`, White `#F5F7F9`, Ice Blue `#aaccdb`, plus alpha black/white for muted text and hairlines.

**Never on slides:** gradients, atmospheric orbs, border-radius, single flat-color slides, Inter, IBM Plex Mono, Bebas Neue, Calibri, cyan, teal.
