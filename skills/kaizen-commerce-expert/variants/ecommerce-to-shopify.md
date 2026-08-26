# Ecommerce To Shopify Variant

Use this variant when the primary move is WooCommerce, BigCommerce, Magento, custom ecommerce,
or Shopify-to-Shopify consolidation into Shopify.

## Required Context

- Current ecommerce platform and POS relationship
- Product, customer, order, collection, page, blog, and URL counts
- SEO exposure: indexed pages, redirects, meta data, canonical structure, custom content types
- Theme and merchandising requirements
- App stack and integrations
- Whether POS, B2B, subscriptions, loyalty, gift cards, or ERP are in scope
- Whether this should become DTC Commerce, B2B Commerce, Mixed Commerce Systems, or POS-led work

## Default Skill Chain

1. `skills/kaizen-research.md` for public tech-stack and site signals
2. `reference/kaizen-shopify-commerce-systems.md` for commerce lane and AnyDB-first lens
3. `skills/kaizen-diagnose.md` for Blueprint report when strategic recommendation is needed
4. `skills/kaizen-propose.md` for scope, app stack, SEO/data continuity, and commercial terms
5. `skills/kaizen-dataprep.md` and `skills/kaizen-migrate.md` for data mapping
6. `skills/kaizen-publish.md` or storefront specialist workflow when copy or presentation is needed
7. `skills/kaizen-check.md` before client delivery

## Output Shape

- Recommendation: Shopify path and why
- Migration scope: products, customers, orders, content, redirects, gift cards, discounts
- SEO continuity plan
- App-stack recommendation with ownership and monthly cost treatment
- Operational dependency: POS, ERP, fulfillment, B2B, wholesale, or subscriptions
- AnyDB operating-layer role when workflow state, approvals, portals, exceptions, or reporting are present
- Kill conditions: SEO footprint larger than expected, custom platform data unavailable, app replacement unresolved, ERP owns catalog
- Next action

## Common Risks

- Treating ecommerce migration as only product/customer/order data
- Leaving redirects or technical SEO for after launch
- Recommending apps without ownership or monthly cost clarity
- Missing custom fields, bundles, variants, subscriptions, or B2B pricing
- Assuming Shopify should own catalog when ERP is the confirmed master

## When Not To Use

- The ask is only a storefront UX critique. Use `kaizen-frontend-audit` or `skills/kaizen-publish.md`.
- The task is POS-only with no ecommerce scope. Use `variants/pos-migration.md`.
- The user asks for actual Matrixify files. Use `skills/kaizen-matrixify-exec.md`; otherwise route generic migration packages through `skills/kaizen-api-migration-exec.md`.

## Variant Depth Additions

### Anti-Selection Rules

- Do not treat ecommerce migration as only product/customer/order movement.
- Do not scope launch without redirects, content, app stack, checkout, customer accounts, and
  analytics continuity.
- Do not let Shopify appear to own catalog if ERP is confirmed as the master.

### Known Failure Modes

- URL redirects and indexed content ignored until launch.
- Custom product fields, bundles, subscriptions, gift cards, or discounts missed.
- App replacements selected without ownership or cost clarity.
- Historical orders imported in a way that affects inventory or fulfillment incorrectly.

### Default Evidence Gates

- Source platform and entity counts.
- SEO/indexed URL exposure and redirect map.
- App stack and integration replacement map.
- Migration lane and validation plan.
- Any ERP/accounting/fulfillment ownership confirmed.

### Operating Hooks

- Vendor Freshness Auto-Gate for Shopify Admin API, checkout/accounts, Matrixify, apps, and
  platform migration behavior.
- Evidence Gate Hook for SEO, launch readiness, migration QA, and client-facing claims.
- Task / Follow-Up Hook for exports, redirect sources, app decisions, and stakeholder approvals.

### Output Shape By Mode

- Quick Read: Shopify fit, largest continuity risk, next action.
- Operator Analysis: scope, lane, app-stack decision, SEO/data risk, kill conditions.
- Client Deliverable: migration recommendation, continuity plan, assumptions, and next step.
- Execution Artifact: entity map, redirect plan, app replacement map, validation checklist.

### Source-Of-Truth And AnyDB Boundary

Shopify should own storefront, checkout, orders, customer accounts, and commerce execution. ERP,
WMS, or accounting may own catalog, inventory, pricing, fulfillment, or financial truth. AnyDB is
first considered for approvals, exception queues, content operations, reporting, and cross-system
handoffs.
