# Vertical Playbook — Kitchen / Home Goods Retail

Use this variant for kitchen, home goods, furniture-adjacent, and housewares retailers:
big-ticket items, special orders, supplier dropship, delivery logistics. Loads on top of the
matching scenario variant (usually pos-migration; shopify-dtc-commerce when online-led).

**Provenance:** patterns below are `[SYN]` domain knowledge; the 2026-06-11 seeding pass landed
the first `[REAL:KZ-2026]` entry (capture slots below).

## Required Context

- Special-order share of revenue (ordered-in items not stocked on the floor)
- Supplier structure: stocked vs dropship vs ordered-on-demand; lead-time ranges
- Delivery model: customer pickup / own truck / third-party white-glove
- Deposit conventions on special orders and the current tracking method
- Registry/wishlist presence; seasonal assortment swings

## Default Skill Chain

1. `skills/kaizen-qualify.md` — discovery with the angles below
2. `skills/kaizen-diagnose.md` — Blueprint; special-order workflow usually drives the AnyDB story
3. `skills/kaizen-architect.md` — special orders / supplier portal / delivery state
4. `skills/kaizen-migrate.md` — catalog breadth and option matrices are the migration load

## Vertical Pattern Library [SYN]

- **Special orders are the operating-system question:** quote → deposit → supplier PO → ETA
  management → arrival → customer notify → delivery/pickup → balance collection. Lightspeed-era
  merchants run this on paper/memory; it is the single highest-leverage workflow to systematize
  (aligns with the KaizenCommerce Special Orders v3.0 pattern — OOS special-order commitments on
  Shopify POS with an AnyDB operating layer).
- **Deposit liability discipline:** deposits on special orders are liabilities with customer
  expectations attached; ad-hoc tracking creates both accounting noise and CX failures.
- **Catalog breadth vs floor reality:** thousands of orderable SKUs, hundreds on the floor —
  "available to order" vs "in stock" distinction must survive migration and reach the online
  surface honestly.
- **Big-ticket CX asymmetry:** low transaction count, high transaction value — one botched
  special order costs a customer for life; the ops pitch is reliability, not speed.
- **Supplier lead-time truth:** ETA promises are only as good as supplier data; expectation
  management is a workflow feature (status visibility), not a forecasting feature.

## Discovery Angles

- "A customer wants the stove you don't stock — walk me through what happens, start to finish."
- "How do you track deposits taken against special orders today?"
- "When a supplier slips an ETA, who finds out, and when does the customer find out?"
- "How much of your catalog is orderable but never on the floor?"

## Data Traps

- Option matrices exceeding variant limits (finish × size × configuration on furniture)
- Special orders living as quotes/notes with no inventory representation
- Deposits recorded as completed sales (revenue recognition + liability both wrong)
- Dropship items with stock counts that mean nothing (phantom availability online)
- Delivery fees and white-glove services modeled inconsistently across surfaces

## Evidence Capture Slots (first entry seeded 2026-06-11; `proposal-safe: no`, internal only)

`[REAL:KZ-2026]` ERP-run remodeling retailer entered via small-SKU POS (2026-04-02→08,
kitchen/bath remodeling, 5 showrooms, confidence high): operations entirely in NetSuite —
NetSuite stays the source of truth; Shopify POS enters as a Phase 1 pilot for ~100 small
accessory SKUs (barcode checkout, one location first), Phase 2 customer portal + in-store
pickup. Integration leg owned by a named iPaaS partner (Versori), Kaizen sets up + verifies.
Catalog trap encountered: the ~600 SKUs targeted for "migration" existed in no catalog —
creation, not migration (full instance: finding bank, Catalog Data Debt). Win-the-room
details: buying committee = pricing quote with connector tiers → demo → department review →
owner approval.

Still pending (do not invent): special-order workflow build result · Lightspeed-parity
expectation handled · delivery/notification workflow result (deal had not reached delivery at
capture).

## Variant Depth Additions

- The special-orders pattern is productizable across this vertical — capture every engagement's
  delta from the v3.0 pattern rather than re-deriving it.
- AnyDB fit: special-order state machine, supplier ETA exceptions, delivery scheduling — yes;
  product catalog mastering — usually no (stays in Shopify unless ERP owns it).

## Anti-Selection Rules

- Fast-moving low-ticket housewares without special orders → standard retail handling.
- Pure furniture e-commerce without stores → `variants/shopify-dtc-commerce.md`.

## Known Failure Modes

- Migrating "available to order" catalog as in-stock inventory (phantom availability).
- Scoping special orders as a POS configuration instead of an operating layer.
- Ignoring variant-limit math on configurable products until import day.

## Default Evidence Gates

- No proposal-safe kitchen/home proof until slots fill; pattern language only.
- Variant-limit and option-handling claims verified via Shopify Dev MCP per protocol.

## Operating Hooks

- Memory: record special-order share, supplier model, delivery model at first discovery.
- Flywheel: capture slots at `Close Client`; deltas from the Special Orders v3.0 pattern feed
  the pattern library.

## Output Shape By Mode

- Quick Read: fit + the special-order walk-through finding.
- Client Deliverable: Blueprint §3b leads with the special-order workflow map; business impact
  framed on CX reliability and deposit discipline.
- Execution Artifact: migration runbook adds option-matrix audit and orderable-vs-stocked
  flagging to Phase 2.

## Source-Of-Truth

- Special-order state pattern: AnyDB architecture via `skills/kaizen-architect.md` ·
  Evidence: `reference/kaizen-proposal-proof-bank.md` schema · Retail ops:
  `reference/kaizen-retail-ops-patterns.md` · Pricing: `reference/kaizen-pricing.md`
