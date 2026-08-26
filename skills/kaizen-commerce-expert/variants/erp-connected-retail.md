# ERP Connected Retail Variant

Use this variant when ERP, accounting, WMS, 3PL, or another operational system may own products,
inventory, pricing, orders, customers, or financial state.

## Required Context

- Systems in scope and their current roles
- ERP or accounting platform, if known
- Entity ownership today: product, inventory, pricing, customer, order, payment, fulfillment
- Desired Shopify role after migration
- Integration method: connector, iPaaS, custom API, manual export, or unknown
- Refresh expectations and reconciliation requirements
- Edge cases: returns, order edits, partial fulfillment, multi-location inventory, wholesale, tax

## Default Skill Chain

1. `reference/kaizen-surface-complexity.md`
2. `reference/kaizen-build-vs-buy.md`
3. `reference/kaizen-erp-patterns.md`
4. `reference/kaizen-risk-matrix.md`
5. `skills/kaizen-architect.md` router + `skills/kaizen-architect.md` Mode 2
6. `skills/kaizen-check.md` Decision Review before final recommendation

## Output Shape

- System inventory
- Source-of-truth matrix
- Entity flow map with direction and cadence
- Build-vs-buy verdict per system
- Shopify ownership boundary
- AnyDB role, if any
- Reconciliation and failure ownership
- Last 10 percent edge cases
- Kill conditions and open questions

## Common Risks

- Letting Shopify appear to own data ERP must own
- Recommending a connector before confirming edge cases
- Ignoring financial state, refunds, partial fulfillments, or order edits
- Treating scheduled sync as real-time sync
- Assigning two systems the same write path without a conflict rule

## When Not To Use

- No external operational system is involved and Shopify can own the workflow.
- The user only needs a plain-language app comparison. Use `skills/kaizen-retail-expert-v2.md`.
- The user asks for executable API work. Route to the relevant execution skill or bounded implementation workflow.

## Variant Depth Additions

### Anti-Selection Rules

- Do not recommend a connector before confirming the last 10 percent edge cases.
- Do not assign two systems the same write path without a conflict and recovery rule.
- Do not let Shopify own financial, inventory, pricing, or fulfillment truth if ERP is confirmed
  as master.

### Known Failure Modes

- Returns, refunds, partial fulfillment, order edits, or tax flows ignored.
- Scheduled sync described as real-time behavior.
- Manual exports accepted without owner, cadence, and reconciliation.
- Connector limitations discovered after scope is sold.

### Default Evidence Gates

- Source-of-truth matrix by entity.
- Data direction, cadence, owner, and fallback by integration.
- Last 10 percent edge-case review.
- Reconciliation owner and exception path.

### Operating Hooks

- Vendor Freshness Auto-Gate for Shopify API, connector, ERP, WMS, and AnyDB sync behavior.
- Evidence Gate Hook for source-of-truth and integration recommendations.
- Task / Follow-Up Hook for ERP/accounting owner decisions and connector evidence.

### Output Shape By Mode

- Quick Read: likely system boundary, biggest unresolved edge case, next question.
- Operator Analysis: entity ownership, flow, connector verdict, risks, kill conditions.
- Client Deliverable: system map, ownership boundaries, assumptions, and next step.
- Execution Artifact: integration matrix, flow spec, error handling, reconciliation plan.

### Source-Of-Truth And AnyDB Boundary

ERP/accounting/WMS systems may own catalog, inventory, pricing, fulfillment, or financial state.
Shopify owns commerce execution where appropriate. AnyDB owns coordination, exception workflows,
approval state, and operator reporting when neither Shopify nor ERP should become the work queue.
