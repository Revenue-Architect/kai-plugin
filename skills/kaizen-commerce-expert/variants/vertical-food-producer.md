# Vertical Playbook — Food Producer / Specialty Food Retail

Use this variant for food producers and specialty food retailers selling across surfaces:
own retail/farm store, wholesale to grocers/restaurants, farmers' markets, and online. Loads on
top of the matching scenario variant (pos-migration, shopify-b2b-commerce, or both).

**Provenance:** patterns below are `[SYN]` domain knowledge; the 2026-06-10 seeding session
landed the first `[REAL:SGP-2026]` entry (capture slots below).

## Required Context

- Surface mix: retail store(s) / wholesale accounts / markets / DTC online — and revenue split
- Lot/batch tracking and expiry-date requirements (compliance level: MAPAQ / CFIA / FDA)
- Catchweight or unit-of-measure complexity (sold by weight vs each vs case)
- Wholesale price-list structure (by account, volume, contract) and MOQ rules
- Production system, if any, and where recipes/yields live

## Default Skill Chain

1. `skills/kaizen-qualify.md` — discovery with the angles below
2. `skills/kaizen-diagnose.md` — Blueprint; profile usually Complex Multi-Surface even at small size
3. `variants/shopify-b2b-commerce.md` when wholesale is in scope
4. `skills/kaizen-architect.md` — AnyDB for lot tracking, wholesale approvals, standing orders

## Vertical Pattern Library [SYN]

- **Small revenue, high surface complexity:** a food producer can be Complex Multi-Surface
  at modest scale — three channels with different prices, units, and tax treatment for the
  same physical product. Surface count, not revenue, drives the architecture.
- **Lot/expiry is a compliance requirement, not a feature preference:** recall capability
  ("which accounts received lot X") is the question that exposes whether current systems are
  adequate. Native POS rarely owns this; it's an operating-layer pattern.
- **Unit-of-measure transforms:** produced in batches, sold by weight at retail, by case
  wholesale, by each online — the SKU model must encode the transforms or inventory is fiction.
- **Standing orders / route delivery:** weekly repeating wholesale orders with delivery-day
  logistics; workflow state (AnyDB candidate), not a cart feature.
- **Seasonality and perishability:** stockout cost is wasted production, not just lost sales —
  forecasting conversations land differently here.

## Discovery Angles

- "If you had to recall a batch tomorrow, how would you know who received it?"
- "Same cheese: how is it priced at the counter, by the case, and online? Who maintains those?"
- "How do your standing wholesale orders get placed — phone, text, email, habit?"
- "What gets thrown out, and what would knowing demand earlier be worth?"

## Data Traps

- Catchweight items migrated as fixed-price units (price-per-kg lost)
- Lot/expiry data living in labels/spreadsheets with no system record
- Wholesale terms (net-30, deposits on kegs/totes) entangled with retail tax settings
- Market/event sales recorded outside any system (cash float reconciliation gap)
- Mixed GST/QST treatment across prepared vs unprepared food categories

## Evidence Capture Slots (first entry seeded 2026-06-10; `proposal-safe: no`, internal only)

`[REAL:SGP-2026]` Repeat-order / card-on-file requirement surfaced mid-delivery (2026-05-28,
food producer Square→Shopify migration, confidence high for the requirement / resolution TBD):
merchant asked where customer credit cards can be stored on file for subsequent orders — repeat
purchasing is core to the vertical, and discovery never asked. Pattern: ALWAYS probe
repeat/standing-order workflows in food-producer discovery; the answer drives a payment-vaulting
vs draft-order vs subscriptions architecture decision that is expensive to bolt on later.

Still pending (do not invent): multi-surface pricing/source-of-truth decision · lot-tracking /
recall-readiness build · standing-order workflow RESULT (the requirement above is captured; the
shipped resolution is not yet observed).

## Variant Depth Additions

- B2B + DTC + POS co-existing is the normal case here — lead architecture with the Mixed
  Commerce baseline question (two-plus active surfaces with cross-surface dependency).
- AnyDB-first lens applies strongly: lot genealogy, wholesale account approvals, standing-order
  exceptions are workflow state Shopify shouldn't fake.

## Anti-Selection Rules

- Restaurant/food-service operations (table service, KDS) → not our lane; refer.
- Single-surface farm stand without wholesale/online ambitions → standard retail, no variant.

## Known Failure Modes

- Quoting POS tiers when the actual project is a B2B portal + operating layer.
- Modeling catchweight as variants instead of solving unit-of-measure properly.
- Treating compliance lot-tracking as a nice-to-have because the merchant downplays it.

## Default Evidence Gates

- No proposal-safe food-producer proof exists yet; pattern language only until slots fill.
- Tax treatment claims (GST/QST on food categories) verified, never recalled from memory.

## Operating Hooks

- Memory: record surface mix, compliance regime, and UoM complexity at first discovery.
- Flywheel: capture slots at `Close Client`.

## Output Shape By Mode

- Quick Read: surface-complexity verdict + the recall-readiness question.
- Client Deliverable: Blueprint §3a classifies Complex Multi-Surface with the three-price
  exhibit; §6 separates commerce surfaces from the operating layer.
- Execution Artifact: migration runbook adds UoM transform mapping and lot-field decisions to
  Phase 2.

## Source-Of-Truth

- B2B patterns: `variants/shopify-b2b-commerce.md` · Surface classification:
  `reference/kaizen-surface-complexity.md` · Evidence: `reference/kaizen-proposal-proof-bank.md`
  schema · Pricing: `reference/kaizen-pricing.md`
