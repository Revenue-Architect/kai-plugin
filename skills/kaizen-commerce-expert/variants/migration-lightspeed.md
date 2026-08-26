# Migration Execution Variant — Lightspeed Source (R-Series / X-Series)

Load when the source is Lightspeed Retail. **First decision: which Lightspeed?** R-Series
(classic Retail POS) and X-Series (former Vend) are different products with different data
models and exports — confirm before anything else; "we're on Lightspeed" is not an answer.

## Entity Inventory

| Entity | R-Series | X-Series (Vend lineage) | Watch |
|---|---|---|---|
| Products + matrix | Item/Matrix export, API | Products export, API | matrix/variant attribute reconstruction differs by series `[VERIFY sample]` |
| Customers | Customer export | Customer export | store-credit balances ride on customers in X `[VERIFY]` |
| Inventory by outlet | per-shop levels | per-outlet levels | outlet→location map is a Phase-1 deliverable |
| Gift cards | gift card module export `[VERIFY access by plan]` | gift cards + store credit | X-Series store credit ≠ gift cards — two liabilities, two tie-outs |
| Sales history | sales export windows | sales ledger export | line-tax detail quality varies by config |
| Work orders / repairs | R-Series work orders module | n/a typically | not a Shopify-native concept — operating-layer decision (AnyDB), never silently dropped |
| PO/vendor data | vendors + POs | suppliers | usually rebuilt, not migrated — decide explicitly |

## Data Traps

- **Matrix reconstruction:** R-Series matrices export as parent+children with attribute columns;
  attribute order and naming must be normalized to Shopify's option model. The classic failure
  is option-value drift ("Sm"/"Small"/"S") across years of data entry — normalize in Phase 2 with
  a documented value map.
- **Two liabilities in X-Series:** gift cards AND customer store credit. Each needs its own
  financial tie-out; store credit usually lands as Shopify store credit `[VERIFY current
  mechanism]` or a documented gift-card conversion with merchant sign-off.
- **Work orders/repairs (R-Series):** active repairs at cutover are customer property with
  state. Freeze intake before cutover, carry open tickets into the new operating layer manually,
  reconcile by ticket list — never by count alone.
- **Serial numbers:** R-Series serialized inventory needs serial-level reconciliation (see
  jewelry playbook) — count parity is insufficient.
- **eCom entanglement:** Lightspeed eCom(C-Series)/X eCom may share the catalog; decide which
  copy is authoritative before export.

## Field Mapping (anchors; exact names verified per MCP protocol at build time)

| Lightspeed | Shopify | Note |
|---|---|---|
| System ID / Product ID | metafield `migration.source_id` | idempotency + audit |
| Matrix attributes 1-3 | options 1-3 | normalized value map required |
| MSRP vs Price | compare_at_price vs price | confirm merchant's semantic |
| Outlet quantity | inventory level per location | via outlet→location map |

## Validation Queries
Recipe bank R8 + R6; serialized entities reconcile serial-by-serial; X-Series adds store-credit
sum tie-out. Spot-check: matrix products specifically (the reconstruction is the risk).

## Rollback Notes
Lightspeed stays live through parallel run. Ledger from JSONL; repairs/work-orders freeze list
is also the rollback list for operational state.

## Variant Depth Additions
The series determination changes the whole Phase 1; X-Series store credit and R-Series work
orders are the two deltas that don't exist in generic runbooks — both are operating-model
decisions, surface them at Blueprint stage when possible.

## Anti-Selection Rules
Lightspeed Restaurant → not our lane. Lightspeed eCom-only (no retail POS) → use
`variants/ecommerce-to-shopify.md`.

## Known Failure Modes
Wrong-series assumptions; option-value drift imported as-is (variant explosion); store credit
discovered after customer import; open repairs orphaned at cutover.

## Default Evidence Gates
Series confirmed with a screenshot or export header before runbook drafting; both liability
tie-outs to the cent; every `[VERIFY]` resolved before execution-ready.

## Operating Hooks
Vendor freshness: export formats and store-credit mechanics drift — verify on fresh exports.
Flywheel: Lightspeed-specific findings to this variant at Close Client (most Kaizen deals are
ex-Lightspeed — this variant should fatten fastest).

## Output Shape By Mode
9-phase runbook per `skills/kaizen-migrate.md`; lane usually `api_to_api` for products/customers/
inventory with per-entity calls on liabilities; repairs → AnyDB workstream cross-reference.

## Source-Of-Truth
Lane + contract: `skills/kaizen-migrate.md` · recipes: `reference/kaizen-api-recipe-bank.md` ·
QA verdicts: `delivery-os/templates/migration-qa-evidence-pack.md` · serialized/repairs patterns:
`variants/vertical-jewelry-multilocation.md`
