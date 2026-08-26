# KaizenCommerce Blueprint Advisory — Reference Example

This is the reference structure for a KaizenCommerce Blueprint Advisory deliverable (Silver tier).
Load this file when generating, reviewing, or rendering a Blueprint Report or proposal document.
Use it to match section order, voice register, evidence requirements, and document rhythm.

## Canonical Visual Artifact

The visual source of truth is `../reference/kaizen-ds-v2.html`. The canonical reusable proposal
template is `../assets/templates/kaizen-proposal-template.pdf`; the adjacent
`kaizen-blueprint-advisory-example.pdf` is the byte-identical calibration artifact for page rhythm,
section order, and original document tone. This markdown file is an inspection guide, not a
substitute for either artifact. When rendering Blueprint Advisory or proposal-style PDFs, follow DS
v2 first, then use the PDF to preserve visual language and restraint while expanding the client
deliverable to the current 15-20 page Blueprint standard.

**Do not use earlier dummy PDFs for visual calibration.** If the `.pdf` can be inspected, inspect it
directly, then reconcile anything that differs from DS v2 back to `kaizen-ds-v2.html`.

**Tier:** Silver — Blueprint + Advisory  
**Deliverable:** PDF document, 15-20 pages minimum
**Fee:** $2,000 (credited in full toward Gold or Diamond)
**Turnaround:** 7 business days from discovery session  
**Render via:** `kaizen-render` PDF mode, cover BG `#0e0e0e`, body BG `#F5F7F9`

**DS v2 PDF visual profile:**
- Dark bookend cover and close; light interior pages.
- Editorial page rhythm with EB Garamond display/editorial copy and Hanken Grotesk functional copy.
- `SECTION 0X` eyebrows and hairline rules use alpha black/white, not fixed grey hexes or navy title bands.
- Red is reserved for document type, risk/problem/action emphasis, and contextual table headers.
- Risk severity is plain bold colored text in cells, not pills or badges.
- Core DS v2 colors carry the composition. Governed grey, steel-blue, red-tint, and light-panel ramps are allowed only when they improve dense PDF readability, print/export reliability, or reference-example fidelity.
- Panels are flat, square, and quiet: no shadows, gradients, rounded cards, decorative grids, or HUD brackets.

---

## Document Structure

### Cover Page (dark — `#0e0e0e`)

Dark front bookend. **No top bar, no gradients, no grid.** Three vertical groups (top / middle / bottom):

```
[Top]
KaizenCommerce                          ← EB Garamond serif wordmark, 30pt, #F5F7F9
MONTREAL / SHOPIFY PLUS / OPERATIONS ARCHITECTURE   ← Hanken 700, 8pt, rgba(245,247,249,0.35), UPPERCASE

[Middle]
BLUEPRINT ADVISORY                      ← red doc-type eyebrow, Hanken 700, 9pt, #a8201a, UPPERCASE
[Merchant Name] Shopify Migration Strategy   ← EB Garamond serif title, 38–40pt, #F5F7F9
Prepared for [Merchant Name] · [Month Year]  ← Hanken 11pt, rgba(245,247,249,0.35)

[Bottom]
PREPARED FOR   [Merchant]      PREPARED BY    KaizenCommerce   ← 2×2 meta grid
DATE           [Month Year]    AUTHORIZATION  SOW Version 1.0     labels Hanken 7.5pt rgba(245,247,249,0.35), values rgba(245,247,249,0.75)
Built by people who built Shopify.      ← EB Garamond italic, 12pt, rgba(245,247,249,0.35)
```

---

### Section 01 — Executive Summary

**Section header:** EB Garamond serif heading on the light page, alpha-muted `SECTION 0X · EXECUTIVE SUMMARY` eyebrow (Hanken 700, `rgba(14,14,14,0.42)`), alpha hairline beneath. No navy band.

**Framing (2–3 paragraphs, EB Garamond 400 body serif, 14–16pt):**

Open with the merchant's specific operational problem — not a generic migration description.
Name the current POS, location count, and the core gap that discovery revealed.

Example structure:
> [Merchant name] operates [N] retail locations on [current POS]. The current setup creates
> [specific problem: e.g., a weekly manual inventory reconciliation that consumes approximately
> 4 staff-hours per store, with no reliable source of truth between locations]. This blueprint
> covers the data, workflow, and integration scope required to move to Shopify POS without
> replicating the operational gaps that exist in the current system.

**Three-stat summary row (EB Garamond numerals, dark panel):**
- Locations in scope
- Data entities in migration (products / customers / gift cards)
- Identified migration risks

**Voice rules for executive summary:**
- Name the problem before naming the solution
- Use specific numbers whenever available — no "significant" or "many"
- Do not use "seamless," "robust," "best-in-class," or "leverage"
- One paragraph per idea. No multi-sentence run-ons.

---

### Section 02 — Current State Assessment

**Section header:** EB Garamond serif heading on the light page, alpha-muted `SECTION 0X · CURRENT STATE` eyebrow (Hanken 700, `rgba(14,14,14,0.42)`), alpha hairline beneath. No navy band.

**Current POS environment (table):**

| System | Entity | Status | Migration Complexity |
|---|---|---|---|
| [POS name] | Products | [count, condition] | [Low / Medium / High] |
| [POS name] | Customers | [count, condition] | [Low / Medium / High] |
| [POS name] | Gift Cards | [count, active balance] | [Low / Medium / High] |
| [Integration name] | Loyalty | [active / inactive] | [Low / Medium / High] |
| [Integration name] | Accounting | [ERP/Quickbooks/etc.] | [Low / Medium / High] |

**Integration inventory (list format):**
List every active integration, its source system, its data direction (push/pull), and whether
a Shopify-native equivalent or third-party replacement has been confirmed.

**Staff workflow review:**
Document the workflows that currently live in the POS and will need to be rebuilt or remapped
in Shopify: gift card issuance, returns, exchanges, staff permissions, end-of-day reporting,
inventory adjustments, vendor receiving.

**Data quality findings (evidence-gated):**
- Products: field coverage %, SKU uniqueness, variant structure issues
- Customers: duplicate rate, missing email %, loyalty balance discrepancies
- Gift cards: active balance total, zero-balance count, expiry distribution

---

### Section 03 — System Map

**Section header:** EB Garamond serif heading on the light page, alpha-muted `SECTION 0X · SYSTEM MAP` eyebrow (Hanken 700, `rgba(14,14,14,0.42)`), alpha hairline beneath. No navy band.

The system map is the primary technical deliverable. It shows:

1. **Current-state architecture** — all systems, data flows, integration dependencies, and staff touchpoints in the existing POS environment

2. **Target-state architecture** — the proposed Shopify POS configuration with integration replacements, AnyDB components (if applicable), and data flows post-migration

3. **Schema mapping summary** — for each entity, the source field structure and the Shopify target schema, with transformation notes

**Visual format (document):** Bento grid diagram with labeled cells per system. Current state = Mid Black `#181818` cells. Target state = Navy `#0D1B2A` cells. Integration arrows annotated.

**If AnyDB is included:** Add a third panel showing AnyDB tables, relationships, and the data flow between Shopify and AnyDB for operational workflows.

---

### Section 04 — Risk Register

**Section header:** EB Garamond serif heading on the light page, alpha-muted `SECTION 0X · RISK REGISTER` eyebrow (Hanken 700, `rgba(14,14,14,0.42)`), alpha hairline beneath. No navy band.

Render the risk register as a **red-header table** (`#a8201a` header bar, white Hanken caps). Severity / Likelihood / Impact are **plain bold text in a contextual colour inside the cell — not pills, not badges, no border, no background.**

| Identified Risk Area | Likelihood | Impact | KaizenCommerce Mitigation Control |
|---|---|---|---|
| [Specific risk — e.g., Gift card balance format mismatch on [POS] export] | Medium | High | Pre-transform balances to cents integer; validate against source total before import |
| [Risk] | Medium | High | [Mitigation] |
| [Risk] | Low–Medium | Medium | [Mitigation] |

**Severity text colours (bold Hanken, no pill):**
- High / Critical → `#a8201a` · Medium / Important → `rgba(168,32,26,0.72)` · Low / OK → `#0D1B2A`
- First column (risk area) is bold `#0e0e0e`; row separation uses alpha black hairlines or very low-alpha black fills, not fixed grey fills.

**Risk register rules:**
- Every risk is specific to this merchant — no generic risks
- Every mitigation is actionable (who does what, before which step)
- Effort estimates in hours, not "low/medium/high" buckets
- Go/No-go column: mark whether this risk must be resolved before cutover approval

---

### Section 05 — Go/No-Go Criteria

**Section header:** EB Garamond serif heading on the light page, alpha-muted `SECTION 0X · GO / NO-GO CRITERIA` eyebrow (Hanken 700, `rgba(14,14,14,0.42)`), alpha hairline beneath. No navy band.

The explicit conditions that must be met before cutover approval is granted.

**Format (checklist with evidence gate):**

```
□  Product import dry-run: zero blocking errors, SKU uniqueness confirmed
□  Customer import: duplicate email rate < 0.5%, email coverage ≥ 95%
□  Gift card balance: imported total within $0.01 of source total
□  Inventory: counts reconciled at all [N] locations
□  Integrations: [accounting system] confirmed posting test transaction
□  Hardware: all [N] registers on Shopify POS with test transaction complete
□  Staff: all floor staff completed 45-minute training session
□  Reporting: day-end report output matches legacy format
```

**Callout box (Navy left border):**
> If any CRITICAL item above is not confirmed as PASS, cutover is not approved.
> The go-live window moves. This is the guarantee.

---

### Section 06 — Rollout Path

**Section header:** EB Garamond serif heading on the light page, alpha-muted `SECTION 0X · ROLLOUT PATH` eyebrow (Hanken 700, `rgba(14,14,14,0.42)`), alpha hairline beneath. No navy band.

A sequenced cutover plan with timing windows, staff assignments, and validation checkpoints.

**Phase structure:**

**Phase 1 — Data Migration (Weeks 1–2)**
- API-first product import with dry-run validation
- Customer deduplication and import
- Gift card balance migration
- Inventory baseline load by location
- Evidence gate: dry-run pass report, reconciliation delta < 0.5%

**Phase 2 — Configuration (Week 3)**
- Shopify POS configuration: locations, staff permissions, Smart Grid
- Hardware setup and network assessment
- Integration reconnection (accounting, loyalty if applicable)
- Parallel environment active

**Phase 3 — Validation (Week 4)**
- 140+ scenario QA across all locations
- Gift card, loyalty, returns, B2B pricing validation
- Reporting parity check (day-end, inventory, sales)
- Go/No-go sign-off

**Phase 4 — Cutover (Day 0)**
- Pre-cutover: final inventory snapshot in legacy system
- Cutover window: [specific timing — e.g., Thursday close to Monday open]
- Register activation in sequence: [store order]
- KaizenCommerce on-call: floor-hour support for first 48 hours

**Phase 5 — Hypercare (30 days)**
- Daily check-ins for first 5 business days
- Weekly status for weeks 2–4
- Issue log reviewed at each checkpoint
- Retainer scope introduced at day 21

**Rollback trigger:**
> If a P0 issue (register down, inventory unreadable, gift cards not processing) is confirmed
> within the first 4 hours of cutover, rollback to legacy system is initiated. Trigger: [specific
> criteria]. Owner: [name]. Estimated rollback time: [hours].

---

### Section 07 — Recommended Scope

**Section header:** EB Garamond serif heading on the light page, alpha-muted `SECTION 0X · RECOMMENDED SCOPE` eyebrow (Hanken 700, `rgba(14,14,14,0.42)`), alpha hairline beneath. No navy band.

Based on the blueprint findings, the recommended engagement tier.

**Tier recommendation with rationale:**

```
Recommended: Gold — Full-Service Migration

Why Gold (not Silver):
- 38,000 products require API-first migration with transformation scripts
- Gift card volume ($240K active balance) requires precision validation beyond
  what an in-house team can safely execute alongside retail operations
- 4 locations require sequential cutover with floor-hour support at each

Why not Diamond:
- Single banner, single region — no multi-site coordination required
- Existing IT team capable of hardware and network configuration

Blueprint fee credit: $2,000 applied to Gold engagement
Remaining balance: [per pricing — load kaizen-pricing.md]
```

**Next step CTA (Red accent):**
> To proceed: reply with approval to move to Gold scope, or book a 30-minute scope confirmation
> call to walk through the risk register before committing.

---

### Cover Page (white documents — SOPs, Change Orders)

For white-cover document types:
- Background: `#F5F7F9`
- Top accent: 3pt solid `#a8201a`
- Title: EB Garamond 500, 36pt, `#0e0e0e`
- Subtitle: EB Garamond 400 Italic, 16pt, `rgba(14,14,14,0.55)`
- Eyebrow: Hanken Grotesk 800, 8pt, UPPERCASE, `rgba(14,14,14,0.40)`

---

## Voice Rules for Blueprint Deliverables

**Evidence-gated claims only:**
- Every risk must name the specific data source, field, or behavior that creates it
- Every mitigation must be executable by someone on the project team
- ROI / savings claims require a source calculation — never invented

**Specific over general:**
- "38,000 products across 4 locations with 3-option variant structure" not "large product catalog"
- "Gift card active balance totals $240K across 8,200 cards" not "significant gift card volume"
- "$30K–$80K average recovery cost for botched migrations" not "migrations can be costly"

**Structure the client can act on:**
- Each section ends with a clear implication: what the client must decide, confirm, or provide
- No section ends with a vague "next steps TBD"
- Go/No-go criteria are binary — pass or fail, not "generally acceptable"

**Kaizen voice register:**
- Direct. Short sentences. No filler.
- Name the problem before the solution
- Name the cost of inaction before the cost of the engagement
- Never: "seamless," "robust," "leverage," "best-in-class," "comprehensive," "cutting-edge"
