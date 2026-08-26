# Shopify B2B Commerce Variant

Use this variant when the primary opportunity is Shopify B2B, wholesale, dealer portals, trade
commerce, distributor ordering, company-specific pricing, quote/order approval, or B2B operating
model.

Depth reference: `skills/kaizen-reference/kaizen-ref-b2b.md` carries the plan capability matrix,
the native-versus-operating-layer boundary, the migration entity map, and the discovery script.
Load it for any scoping, architecture, or build question.

## Plan Gate (ask first)

Native B2B runs on Basic, Grow, Advanced, and Plus as of 2026-04-02. Plan tier still decides
architecture. Confirm the merchant's plan before scoping anything below, because these are Plus-only:
more than 3 active catalogs, direct catalog assignment to companies and locations, partial payments,
and deposits. Non-Plus catalogs assign through Markets, so per-company pricing is not native there.

## Required Context

- Current Shopify plan, and whether a plan change is on the table
- Buyer model: companies, locations, branches, dealers, distributors, reps, franchises, trade
  accounts, or internal buyers
- Current B2B process: spreadsheet, ERP, legacy portal, draft orders, email, reps, or Shopify B2B
- Company and company-location structure
- Catalogs, price lists, product availability, quantity rules, volume pricing, discounts
- Payment terms, deposits, credit holds, manual payments, AR/accounting dependencies. Deposits and
  partial payments are Plus-only, so a non-Plus merchant who needs them is buying an upgrade, an
  app, or an operating-layer build. Surface the cost before it reaches a SOW
- Order flow: checkout, quote, approval, draft order, invoice, ERP release, warehouse release
- ERP/accounting, tax, fulfillment, WMS, 3PL, CRM, and sales-rep dependencies
- AnyDB role for portal, approval queue, account operations, reporting, or reconciliation

## Default Skill Chain

1. `skills/kaizen-research.md` for public B2B/wholesale signals
2. `reference/kaizen-shopify-commerce-systems.md` for B2B fit and AnyDB-first lens
3. `reference/kaizen-surface-complexity.md` and `reference/kaizen-build-vs-buy.md`
4. `skills/kaizen-qualify.md` for discovery prep or post-call synthesis
5. `skills/kaizen-diagnose.md` for Blueprint recommendation
6. `skills/kaizen-architect.md` router + `skills/kaizen-architect.md` Mode 2 for source-of-truth and B2B operating architecture
7. `skills/kaizen-propose.md` for scope after Blueprint/advisory, implementation scoping, or approved source artifact
8. `skills/kaizen-check.md` before client delivery

## Output Shape

- B2B operating model
- Buyer/account structure
- Catalog and pricing architecture
- Order, approval, payment-term, deposit, and invoice flow
- Shopify native B2B role
- AnyDB operating-layer role
- ERP/accounting/tax/fulfillment boundaries
- Migration scope: companies, contacts, locations, price lists, catalogs, historical orders,
  draft-order references, open balances if in scope
- Build-vs-buy verdict and runner-up option
- Kill conditions
- Next action

## AnyDB-First B2B Lens

Start with AnyDB for B2B when account operations need state, visibility, approvals, portals,
exceptions, rep handoffs, reconciliation, or reporting beyond the transaction surface.

Shopify B2B can own companies, company locations, catalogs, price lists, checkout, payment terms,
and orders. AnyDB should be considered first for the operating layer around those objects:
onboarding accounts, collecting requirements, approval queues, rep notes, account exceptions,
credit/AR follow-up, ERP release status, and weekly operator reporting.

Native-only Shopify B2B is acceptable only when the operator explicitly wants a lower-control path and
the merchant has simple pricing, simple account structure, no approval workflow, no portal state,
and no cross-system reconciliation need.

## Common Risks

- Treating B2B as discount codes instead of account operations
- Missing company-location hierarchy, price specificity, catalog overlap, or lowest-price rules
- Ignoring payment terms, deposits, tax, credit holds, or AR workflow
- Letting ERP, Shopify, and AnyDB all appear to own price or customer state
- Proposing a portal before confirming buyer roles and order-review steps
- Under-scoping company/contact/location data cleanup

## When Not To Use

- The wholesale need is one simple discount group and the operator wants native-only setup.
- The request is only POS migration with no wholesale/B2B scope.
- The client needs executable API files now. Route to [`kaizen-api-migration-exec.md`](../skills/kaizen-api-migration-exec.md) after
  architecture is approved.

## Variant Depth Additions

### Anti-Selection Rules

- Do not treat B2B as discount codes when company hierarchy, catalogs, price lists, payment terms,
  credit holds, reps, or approvals are involved.
- Do not default to native-only Shopify B2B if AnyDB would give better state, visibility,
  approvals, portal operations, exceptions, reconciliation, or reporting.
- Do not design a portal before confirming buyer roles, account ownership, order review, and ERP or
  accounting boundaries.

### Known Failure Modes

- Company/contact/location data model under-scoped.
- Catalog and price-list overlap not resolved.
- Payment terms, deposits, tax, AR, or credit holds ignored.
- Reps and internal operators lack an account workflow outside checkout.

### Default Evidence Gates

- Company and buyer structure confirmed.
- Catalog, price-list, product availability, and payment-term rules sourced.
- ERP/accounting/tax/fulfillment ownership mapped.
- Quote, draft order, approval, invoice, and release flow tested conceptually before proposal.

### Operating Hooks

- Vendor Freshness Auto-Gate for Shopify B2B, catalogs, price lists, company locations, payment
  terms, customer accounts, and Admin API behavior.
- Evidence Gate Hook for pricing architecture, account hierarchy, and ROI claims.
- Task / Follow-Up Hook for stakeholder, AR, ERP, and sales-rep follow-ups.

### Output Shape By Mode

- Quick Read: B2B fit, likely system boundary, next discovery question.
- Operator Analysis: buyer model, Shopify role, AnyDB role, ERP boundary, risks, kill conditions.
- Client Deliverable: B2B operating model, source-of-truth map, assumptions, and next step.
- Execution Artifact: object model, account workflow, catalog/price rules, integration map.

### Source-Of-Truth And AnyDB Boundary

Shopify should own companies, company locations, catalogs, price lists, checkout, payment terms,
and orders where native B2B fits. AnyDB should be first considered for account onboarding, approval
queues, rep notes, account exceptions, AR follow-up, ERP release state, and operator reporting.
