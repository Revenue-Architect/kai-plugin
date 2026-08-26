# KaizenCommerce Identity, Pillars, ICP, Metrics

Reference file for the kaizen-commerce-expert skill. Loaded on demand when a task needs company background, service pillar detail, ideal client profile, or growth targets. SKILL.md keeps only the routing table and voice rules — the body of identity content lives here.

---

## Company Identity

**KaizenCommerce** — Montreal-based Shopify implementation agency. Three-partner firm. The name comes from kaizen (改善) — change for the better. Every engagement is a structured improvement, not a patch.

**Positioning Statement** (use verbatim):
> We help retailers and wholesalers run Shopify without making their operating teams the first real test. We specialize in two systems: Shopify POS for multi-location retail, and Shopify B2B for companies selling to trade accounts, dealers, and distributors. For capable internal teams, we provide a paid pre-implementation audit and launch plan. For merchants that need delivery, we handle implementation, operational coverage, existing tech stack integrations, and workflow systems around Special Orders, robust inventory management, customizable Purchase Order flows, account and approval workflows, and the exceptions store and sales teams hit daily.

**POS-only positioning statement** (use when the audience is purely retail and B2B would dilute):
> We help retailers launch Shopify POS without making store teams the first real test. For capable internal teams, we provide a paid pre-implementation audit and launch plan. For merchants that need delivery, we handle Shopify POS implementation, operational coverage, existing tech stack integrations, and workflow systems around Special Orders, robust inventory management, customizable Purchase Order flows, and store-team exceptions.

**Default two-lane positioning:**
- **Blueprint Diagnostic + Advisory:** KaizenCommerce's paid pre-implementation audit and launch
  plan for merchants with strong internal technical teams that want to self-implement but need
  launch architecture, workflow translation, QA readiness, rollout guidance, and a written
  implementation number.
- **Full implementation:** for merchants that need KaizenCommerce to own Shopify POS delivery,
  operational coverage, integrations with the merchant's existing tech stack, and workflow builds
  around store operations.

**Blueprint explanation rule:** in client-facing or partner-facing content, never assume the
audience knows what "Blueprint Diagnostic" means. Define it on first mention as
"KaizenCommerce's paid pre-implementation audit and launch plan." In short partner assets, prefer
"paid diagnostic and advisory engagement" before the branded name.

**Buyer-facing workflow language:** when an internal solution uses AnyDB, do not lead with the tool
name in sales, partner, or proposal copy. Say operational workflow layer, Special Orders workflow,
robust inventory management, customizable Purchase Order flows, store-team workflow, or existing
tech stack integrations. Treat AnyDB as technical disclosure for internal architecture or build
docs, not the headline.

**Two Specializations, One Flex Lane:** KaizenCommerce specializes in Shopify POS and Shopify B2B.
Both are operating-system problems with an operational workflow layer behind them, which is why the
same firm sells both credibly. Treat them as peers, not as a core service plus an overflow lane.

- **Shopify POS** covers multi-location retail launches and migrations. A POS engagement may include
  the merchant's DTC storefront when the deal is unified commerce: one catalog, one inventory
  position, one customer record across store and online. DTC scope inside a POS engagement is
  specialization work, not flex work.
- **Shopify B2B** covers wholesale, dealer, distributor, and trade-account commerce: companies and
  company locations, catalogs and price lists, quantity rules and volume pricing, payment terms,
  approval and ordering workflows, and the ERP/accounting boundary.

**Flexible Lane — standalone DTC.** DTC work that is not attached to a POS or B2B engagement stays
opportunistic. Accept it when it is a commerce-system problem: data, checkout, customer accounts,
fulfillment, app-stack ownership, ERP/accounting, or post-order workflow tied to a measurable
operating consequence. Do not drift into generic theme, design, or app-install work, and do not
describe standalone DTC as a specialization in sales or partner content.

### The Three Partners

| Partner | Background & Role |
|---|---|
| CTO | Ex-Shopify developer — Shopify Logistics division (pre-sale). Deep platform internals: POS architecture, API behavior, migration edge cases. The technical authority. |
| CEO | Ex-PwC digital transformation consultant. Retail and operations specialization. Leads discovery, scoping, client relationships. |
| Silent Partner | Silent operational partner — not client-facing. |

**EDGE:** The CTO worked inside Shopify Logistics before it was divested. Direct knowledge of how Shopify's infrastructure makes decisions. No other agency in Canada has this.

### What We Do NOT Do
- Single-location low-complexity merchants
- Quote implementation blind before a scoping call establishes scope, assumptions, and fit
- Minimum viable delivery — every engagement is case-study quality
- Use internal branded terms in client or partner content without defining them first

---

## Service Pillars

### Pillar 1 — Shopify POS Launch And Implementation
Advisory or full implementation for retailers moving from legacy POS (Lightspeed, Square,
Heartland, Teamwork, custom) to Shopify POS. Covers data migration, hardware readiness,
omnichannel setup, staff training, store testing, pilot launch support, phased rollout, post-launch
stabilization, and integrations with the merchant's existing tech stack.

Unified commerce scope belongs here. When a retail merchant needs the DTC storefront aligned to the
same catalog, inventory position, and customer record as the stores, that DTC work is part of the
POS engagement and is scoped and sold as such.

**Technical depth lives in:** `kaizen-migrate`, `kaizen-api-migration-exec`, `kaizen-dataprep`, `kaizen-validate`, `kaizen-reconcile`, and `kaizen-retail-expert-v2`. Read those skills for API-first migration design, Matrixify fallback format, column mappings, error triage, and reconciliation procedures.

### Pillar 2 — Shopify B2B Commerce
Advisory or full implementation for merchants selling to companies: wholesalers, dealers,
distributors, trade accounts, franchise and branch buyers, and reps ordering on behalf of accounts.
Covers the company and company-location model, catalogs and price lists, quantity rules and volume
pricing, payment terms, ordering and approval flow, the migration of companies/contacts/price lists
and historical orders, the ERP and accounting boundary, and the operational workflow layer that sits
around all of it.

Native Shopify B2B moved to Basic, Grow, and Advanced on April 2, 2026, so B2B is no longer a
Plus-only conversation and the ICP no longer carries a Plus floor. Plan tier still decides
architecture: catalog count, per-company catalog assignment, partial payments, and deposits are
plan-sensitive. Never scope a B2B engagement without confirming the merchant's plan first.

**Technical depth lives in:** `kaizen-ref-b2b`, `variants/shopify-b2b-commerce.md`,
`reference/kaizen-shopify-commerce-systems.md`, and `kaizen-architect`. Read those for the plan
capability matrix, the native-vs-workflow-layer boundary, and B2B migration entity mapping.

### Pillar 3 — Operations Architecture (AnyDB)
Custom operational workflow systems, often built on AnyDB internally. In client-facing language,
lead with the workflow: Special Orders workflow, robust inventory management, customizable Purchase
Order flows, store-team workflow, vendor PO management, multi-location inventory tracking, B2B
wholesale portals, or custom reporting.

**When to recommend AnyDB:**
- Operational data fragmented across spreadsheets, email, disconnected tools
- Inventory tracking needs beyond Shopify native (bin, shelf, condition). **Moving target:** bins and
  bin-level counts entered a Shopify feature preview on 2026-07-17. Argue this case on condition,
  serial/lot, and exception state, not on bins alone. See `reference/kaizen-platform-change-radar.md`
- Vendor PO lifecycle needs structured tracking. The same preview adds **read-only** PO access. The
  case rests on lifecycle, approval state, and receiving/reconciliation, which are not native
- B2B wholesale portal needed
- Cross-system data reconciliation consuming manual time
- Special Orders, deposits, vendor ordering, customer follow-up, or store-team exception handling
  needs a durable workflow layer

**AnyDB-first commerce rule:** Do not reject AnyDB just because Shopify native B2B, Shopify Admin,
Flow, or a standard app can perform part of the workflow. Prefer AnyDB when the merchant needs
approval state, exception queues, portals, rep/buyer handoffs, cross-system reconciliation,
custom reporting, or operational tasks that must live outside a transaction record. Use native
or app-only only when the operator explicitly wants the lower-control path and the workflow is simple
configuration with no durable operating layer.

**Technical depth lives in:** `kaizen-architect`, `kaizen-anydb-dataload`, `kaizen-anydb-audit`, and `kaizen-flow`. Read those skills for schema design, data loading procedures, build verification, and Flow vs AnyDB automation boundaries.

### Pillar 4 — AI Commerce (Future Vision)
Universal Commerce Protocol (UCP) — enabling checkout inside AI channels. **Not currently active.** Reference only as emerging capability, never as active service.

### Flexible Lane — Standalone Shopify DTC
DTC engagements with no POS or B2B component stay opportunistic. They are good fits when they are
commerce-system projects: storefront, checkout, customer account, catalog, pricing, fulfillment,
ERP/accounting, or post-order workflows tied to measurable operating consequences. DTC attached to a
retail merchant belongs in Pillar 1 as unified commerce, not here. For details, use
`reference/kaizen-shopify-commerce-systems.md`.

---

## Ideal Client Profile

### Primary ICP — Shopify POS (retail, including unified commerce)
| Attribute | Detail |
|---|---|
| Revenue | $2M–$20M top-line |
| Locations | 2–20+ retail |
| Current POS | Lightspeed, Square, Heartland, Teamwork, or custom legacy |
| Ecommerce | Already on Shopify or actively evaluating |
| Pain signal | POS and warehouse don't talk. Overselling, manual counts, spreadsheet ops |
| Decision maker | Owner or COO — not IT manager. Owner-operator fear is usually launch breakage, inventory shrink, staff readiness, or a store team losing trust in the new system |
| Budget signal | Has previously invested in technology |

### Primary ICP — Shopify B2B (wholesale, dealer, distributor, trade)
| Attribute | Detail |
|---|---|
| Revenue | $2M–$20M top-line, same band as retail. Native B2B reaching Basic/Grow/Advanced removed the Plus floor, so do not screen on plan tier |
| Buyer model | Sells to companies: trade accounts, dealers, distributors, franchisees, branches, or internal buyers. Repeat ordering, not one-off |
| Accounts | 25+ active buying accounts, or fewer accounts with account-specific pricing that someone maintains by hand |
| Current process | Spreadsheet price lists, emailed or phoned orders, rep-entered draft orders, a legacy portal, or an ERP that nobody wants to replace |
| Pain signal | Pricing maintained by hand across accounts, orders re-keyed into an ERP, approval and credit decisions living in someone's inbox, buyers who cannot self-serve |
| Plan sensitivity | Confirm the plan before scoping. Catalog count, per-company catalog assignment, partial payments, and deposits all change with tier |
| Decision maker | Owner, COO, or head of sales/wholesale. Not the ecommerce manager alone |
| Operational workflow signal | Account onboarding, approval queues, credit holds, portal state, exception handling, rep/buyer handoffs, reporting, or cross-system reconciliation |

### Flex ICP — Standalone DTC
| Attribute | Detail |
|---|---|
| Business model | DTC or Shopify-to-Shopify consolidation with no POS or B2B component |
| Platform | Shopify or actively evaluating Shopify |
| Complexity signal | Catalog/pricing, customer-account, fulfillment, subscription, ERP/accounting, or app-stack complexity |
| Fit rule | Accept when the problem is a commerce operating system problem, not cosmetic storefront work. Do not lead with it in positioning |

### Disqualification Signals
- Single location, low complexity (retail)
- Below $2M revenue
- Decision-maker not accessible
- Wants cheap/fast migration without data integrity
- DTC/B2B request is only theme polish, app installation, or basic Shopify setup with no operating complexity
- B2B: a handful of accounts on one shared price list, with no approval, terms, or reconciliation need. Native setup covers it and there is no engagement
- B2B: EDI or punchout integration is the whole ask, with no Shopify-side operating model to build
- B2B: marketplace or distributor-portal selling where the merchant does not own the buyer relationship

---

## Metrics & Targets

- **Annual Goal:** $250K ARR
- **Monthly Target:** 2 new client engagements at ~$10K blended average
- **Required qualified conversations:** 8/month; conversion health benchmarks live in `reference/kaizen-sales-os.md`
- **Retainer target:** 10 retainer clients by month 12 = $90K ARR from retainers alone

### Failure Signal Diagnostics
| Signal | Likely Problem |
|---|---|
| Activity but no qualified calls | Channel or message quality |
| Calls but low Blueprint conversion | Trust gap or weak pain quantification |
| Blueprints not converting to projects | Fit issue or pricing framing |
| Projects without retainer discussion | Revenue architecture neglect |
