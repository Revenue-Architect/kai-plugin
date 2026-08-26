# Kai Pricing Usage Standard

Use this reference when maintaining pricing language, proposal economics, invoice math, retainer
economics, or audits that detect pricing drift.

## Source Of Truth

`reference/kaizen-pricing.md` is the canonical pricing source. Load it for:

- proposals
- SOWs
- invoices
- change orders
- engagement P&L
- tier recommendations with dollar values
- Blueprint credit math
- overage language
- retainer pricing

## Allowed Literal Pricing

Literal pricing may appear outside `kaizen-pricing.md` only when it serves one of these purposes:

- a worked example or example deliverable
- a finance, proposal, invoice, or QA check that verifies pricing math
- an explicit placeholder format such as `[NEED: approved price]`
- a sales guardrail that says not to pitch implementation pricing before discovery
- a pipeline target or retainer goal documented as a business target

## Symbolic Pricing Tokens

Outside `reference/kaizen-pricing.md`, prefer these stable tokens instead of repeating dollar
figures:

| Token | Meaning |
|---|---|
| `[BLUEPRINT_FEE]` | Current Blueprint fee from `reference/kaizen-pricing.md` |
| `[SILVER_POS_PRICE]` | Current Silver POS price from `reference/kaizen-pricing.md` |
| `[GOLD_POS_PRICE]` | Current Gold POS price from `reference/kaizen-pricing.md` |
| `[DIAMOND_POS_PRICE]` | Current Diamond POS price from `reference/kaizen-pricing.md` |
| `[ANYDB_STANDARD_BUILD_PRICE]` | Current AnyDB Standard Build price from `reference/kaizen-pricing.md` |
| `[ANYDB_ADVANCED_BUILD_PRICE]` | Current AnyDB Advanced Build price from `reference/kaizen-pricing.md` |
| `[RETAINER_MRR_TARGET]` | Current retainer MRR target from the business plan |

## Drift Risk

Hardcoded tier values in normal instructions create drift. When adding new guidance:

- prefer "load `reference/kaizen-pricing.md`" over repeating dollar tables
- use tier names without dollar values when the dollar value is not needed
- use `[NEED: approved price]` when the current conversation has not approved pricing
- keep Blueprint credit math explicit when a commercial artifact requires it

## Client-Facing Rule

Never invent implementation pricing, payment terms, warranty terms, legal terms, or ROI. If the
approved commercial input is missing, ask for it or mark it as needed.

## Audit Interpretation

The pricing drift audit is advisory in this phase. A warning means "review this literal price for
drift risk," not "delete it immediately." Do not remove pricing text without confirming whether it
is an example, a math gate, or a deliberately embedded commercial guardrail.
