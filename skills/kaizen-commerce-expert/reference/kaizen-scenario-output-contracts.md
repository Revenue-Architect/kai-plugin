# Kaizen Scenario Output Contracts

Use this reference when a request matches a common Kaizen scenario and the output needs to be
consistent without loading a full proposal, Blueprint, or architecture skill.

## POS Migration Recommendation

Include:
- Recommendation: migrate now, defer, run Blueprint/advisory, run implementation scoping, or hold
- Current stack and location count
- Pain being solved
- Migration scope: products, customers, orders, inventory, gift cards, loyalty, hardware, staff
- Data risk: counts, export quality, SKU structure, historical order needs
- Cutover readiness: hardware, payments, training, permissions, support
- Tier direction and why
- Kill conditions
- One next action

Do not include:
- Full implementation quote before scoped evidence exists
- Confident timeline without data volume and staff readiness context
- AnyDB recommendation unless workflow needs prove it

## AnyDB Recommendation

Include:
- Workflow AnyDB would own
- Why AnyDB is the preferred operating layer, and which Shopify native, Flow, or app surface it
  complements
- Source-of-truth boundary
- Core Types and relationships at a high level
- Automations or approvals needed
- Reporting outcomes
- Build assumptions
- Kill conditions
- One next action

Do not include:
- AnyDB as passive copy of Shopify data
- AnyDB as order, catalog, or inventory master unless explicitly designed and justified
- Formula or cell syntax without loading `kaizen-anydb-patterns.md`

## DTC Commerce Systems Recommendation

Include:
- DTC commerce objective
- Current storefront and stack
- What Shopify should own
- What AnyDB should own, if operational control is needed
- App stack, owner, cost treatment, and failure path
- Checkout/customer-account, fulfillment, returns, subscriptions, Markets, and SEO implications
- Migration/continuity scope: products, customers, orders, URLs, content, discounts, gift cards,
  subscriptions, and analytics
- Vendor freshness checks required before current platform claims
- Kill conditions
- One next action

Do not include:
- Generic redesign language without commerce or operations consequences
- Hydrogen, custom app, or headless recommendation without proving native Shopify is insufficient
- App recommendations without ownership and monthly cost treatment

## B2B Commerce Systems Recommendation

Include:
- B2B operating model and buyer/account structure
- Companies, company locations, catalogs, price lists, quantity rules, payment terms, deposits,
  and order-review flow when relevant
- Shopify native B2B role
- AnyDB operating-layer role, evaluated first for workflow state and control
- ERP/accounting, tax, fulfillment, AR, and warehouse boundaries
- Migration/continuity scope for companies, contacts, locations, price lists, catalogs, draft
  orders, and historical orders if in scope
- Build-vs-buy verdict with runner-up option
- Vendor freshness checks required before current platform claims
- Kill conditions
- One next action

Do not include:
- "Use Shopify B2B native" as a complete answer when account operations need durable state
- Discount-code framing for a real B2B operating model
- AnyDB as passive copy of Shopify data

## ERP / Source Of Truth Recommendation

Include:
- System inventory
- Entity-level ownership matrix
- Direction and cadence per sync
- Conflict rule for write paths
- Edge cases: refunds, edits, partial fulfillment, tax, multi-location, wholesale
- Reconciliation owner
- Build-vs-buy verdicts
- Kill conditions
- One next action

Do not include:
- "Shopify is source of truth" as a platform-level statement
- Connector recommendation without edge-case testing
- Real-time claims without evidence

## Post-Blueprint Proposal Direction

Include:
- What the Blueprint confirmed
- Recommended tier and service type
- Scope boundaries
- App stack and cost ownership
- Data caps and overage exposure
- Business case from confirmed facts or labeled estimates
- Risks and mitigations
- Gross fee, Blueprint credit, net investment if pricing is approved
- Kill conditions
- One next action

Do not include:
- Implementation pricing if the approved commercial path is Blueprint-only
- Hidden assumptions in SOW, invoice, or change order language
- AnyDB Phase 2 inside Phase 1 scope unless explicitly approved

## Migration Rescue

Include:
- Current migration state
- What failed
- Root-cause hypothesis
- Evidence needed
- Containment step
- Repair sequence
- Scope or timeline impact
- Client communication stance
- Kill conditions for pause, rollback, or re-scope
- One next action

Do not include:
- Continued imports before root cause is isolated
- Client-facing reassurance not supported by counts
- File rewrites without preserving audit trail

## Retainer / Health Check Recommendation

Include:
- Current post-launch state
- What improved
- What remains at risk
- Internal owner capacity
- Recommended support tier
- Included hours and boundaries
- 30/60/90 day focus
- Kill conditions for deferring retainer
- One next action

Do not include:
- Retainer pitch before warranty/hypercare boundary is clear
- Outcome claims without baseline data
- Generic "ongoing support" language
