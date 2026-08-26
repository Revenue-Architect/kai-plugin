# Vertical Playbook — Fitness Franchise

Use this variant when the merchant is a fitness/wellness franchise or multi-unit studio brand:
franchised or corporate-owned locations selling memberships/classes alongside retail (apparel,
equipment, supplements). Loads on top of the matching scenario variant (usually pos-migration or
erp-connected-retail).

**Provenance:** patterns below are `[SYN]` domain knowledge; the 2026-06-10 seeding session
landed the first `[REAL:JAZ-2026]` entries (see capture slots). Spec P2 wants the ERP
integration patterns from this vertical generalized — capture them first, generalize after.

**Seeding correction (2026-06-10):** the JAZ engagement is the franchise brand's drop-based
apparel ECOMMERCE arm (storefront migration + concurrent ERP cutover), not studio POS. Franchise
buyer dynamics and ERP integration patterns hold; member/class-pack patterns below stay `[SYN]`.

## Required Context

- Ownership model: franchisor / franchisee / corporate mix — who is the buyer and who operates
- Location count and franchise growth pipeline
- Revenue mix: memberships/classes vs retail; which system owns each today
- ERP/accounting platform (Sage Intacct, Epicor, QuickBooks) and who owns the chart of accounts
- Member data sensitivity and which system is the member source of truth

## Default Skill Chain

1. `skills/kaizen-qualify.md` — discovery with franchise-specific angles below
2. `skills/kaizen-diagnose.md` — Blueprint; §3a profile is usually Complex Multi-Surface
3. `skills/kaizen-architect.md` — source-of-truth map across POS / membership system / ERP
4. `skills/kaizen-migrate.md` + `variants/erp-connected-retail.md` when ERP is in scope

## Vertical Pattern Library [SYN]

- **Two-commerce-systems reality:** membership billing (recurring) and retail POS are different
  systems with different owners; the integration question is *which system owns the member as a
  customer record*. Forcing one platform to do both is the classic overbuild.
- **Franchise data boundary:** franchisor wants consolidated reporting; franchisees own local
  operations. Reporting rollup ≠ operational centralization — scope them separately.
- **Royalty/fee reporting:** franchise fee calculations need sales data by category by location;
  the export/reconciliation path to the ERP is usually the hidden requirement.
- **Retail is the minority revenue but the inventory complexity:** apparel size/color matrices,
  per-studio mini-assortments, frequent transfers from a central office.

## Discovery Angles (use in qualify Step 1)

- "Who owns the member record — your membership platform, your POS, or your accounting system?"
- "When a franchisee opens a new studio, what's the system setup checklist today?"
- "How does retail revenue get from the register to [ERP] for royalty calculation?"
- "Can members buy retail on their stored payment method? Should they?"

## Data Traps

- Member PII crossing systems without a defined privacy boundary (Law 25 / PIPEDA exposure)
- Gift cards sold at one franchise location, redeemed at another — liability accounting
- Class packs / punch cards living as retail SKUs (they are liabilities, not products)
- Franchisee-level tax registration differences across provinces/states

## Evidence Capture Slots (seeded 2026-06-10; all `proposal-safe: no`, internal only)

`[REAL:JAZ-2026]` ERP integration pattern — Sage Intacct (2026-05-21→06-01, confidence high):
ERP is the absolute inventory source of truth (purchasing/receiving in ERP); products originate
in Shopify and sync down; stock propagates ERP→Shopify via event webhooks through custom
middleware with a daily reconciliation script patching discrepancies. Orders flow to the ERP as
invoices only on fulfillment; all Shopify sales map to one generic ERP customer record to avoid
bloat; refunds flow for dollar reconciliation but returned items restock ONLY via the ERP. Gift
cards as non-inventory liability, sub-ledger balanced from native Shopify reporting monthly.
Fulfillment gap: native Shopify↔ShipStation can't carry ERP bin locations — a direct ERP→
ShipStation leg is required for pick locations.

`[REAL:JAZ-2026]` Kill condition observed — concurrent ERP + commerce cutover on a fixed date
(2026-05-21, confidence high): full finding lives in `reference/kaizen-blueprint-finding-bank.md`
("Concurrent ERP + Commerce Cutover Is A Compound Risk"). Franchise entitlement architecture
(tag-based B2B, native B2B rejected) lives in the proof bank `[REAL:JAZ-2026]` entry.

Still pending (do not invent): franchise reporting rollup approach — not in scope of the
advisory engagement so far.

## Variant Depth Additions

- Treat franchisor-led deals as two-stakeholder sales: the economic buyer (franchisor) and the
  daily operator (franchisee) hear different value framings — consolidated truth vs less manual work.
- AnyDB fit check: franchise onboarding checklists, transfer approvals, royalty-report exception
  handling are workflow-state candidates; membership billing is NOT — it stays in the membership
  platform.

## Anti-Selection Rules

- Single-location gym or studio without franchise structure → standard retail handling, no variant.
- Membership-platform replacement projects (Mindbody → something) without retail POS scope → not
  our lane; say so.

## Known Failure Modes

- Quoting POS migration tiers when the real complexity is the ERP/membership integration map.
- Treating the franchisor's wish list as confirmed franchisee requirements.
- Letting member-data migration into scope without a privacy boundary decision.

## Default Evidence Gates

- Proof points per proof bank schema only; this vertical has no proposal-safe entries until the
  seeding session lands them.
- ERP behavior claims verified against `reference/kaizen-erp-patterns.md` + live confirmation.

## Operating Hooks

- Memory: record ownership model and ERP platform on first contact.
- Flywheel: every fitness-franchise engagement feeds the capture slots above at `Close Client`.

## Output Shape By Mode

- Quick Read: fit assessment + the two-stakeholder framing in plain prose.
- Operator Analysis / Client Deliverable / Execution Artifact: per the routed skill, with the
  pattern library shaping §3/§6 of the Blueprint and the integration map in architect mode.

## Source-Of-Truth

- ERP patterns: `reference/kaizen-erp-patterns.md` · Pricing: `reference/kaizen-pricing.md` ·
  Evidence: `reference/kaizen-proposal-proof-bank.md` schema · Surface classification:
  `reference/kaizen-surface-complexity.md`
