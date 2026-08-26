# Shopify DTC Commerce Variant

Use this variant when the primary opportunity is Shopify DTC, ecommerce-first, online-store
migration, storefront architecture, checkout/customer-account architecture, app-stack cleanup, or
post-launch DTC operating model.

Do not use this variant for cosmetic theme-only work unless the request also affects data,
conversion-critical commerce flows, fulfillment, retention, reporting, or operating ownership.

## Required Context

- Current ecommerce platform and Shopify status
- Current POS relationship, if any
- Product, customer, order, content, URL, subscription, discount, and gift-card scope
- SEO exposure and redirect risk
- Checkout, customer account, Markets, subscription, fulfillment, return, and app-stack needs
- ERP/accounting, WMS, 3PL, marketing, loyalty, review, and analytics dependencies
- Whether AnyDB should own any post-order, content, reporting, exception, or approval workflow

## Default Skill Chain

1. `skills/kaizen-research.md` for public stack and channel signals
2. `reference/kaizen-shopify-commerce-systems.md` for DTC fit and AnyDB-first lens
3. `skills/kaizen-qualify.md` for discovery prep or post-call synthesis
4. `skills/kaizen-diagnose.md` for Blueprint when strategic recommendation is needed
5. `skills/kaizen-propose.md` for commercial scope after Blueprint/advisory, implementation scoping, or approved source artifact
6. `skills/kaizen-architect.md` router + `skills/kaizen-architect.md` Mode 2 when source-of-truth or app-stack architecture matters
7. `skills/kaizen-check.md` before client delivery

## Output Shape

- DTC commerce objective
- Current storefront and stack
- What Shopify should own
- What AnyDB should own, if any
- App-stack recommendation with owner and cost treatment
- Migration or continuity scope: products, customers, orders, URLs, content, subscriptions,
  discounts, gift cards, analytics
- Checkout/customer-account and post-order implications
- SEO and launch-risk plan
- Kill conditions
- Next action

## AnyDB-First DTC Lens

Start with AnyDB when the DTC project exposes a workflow that needs operator state outside the
storefront: return review, subscription exception queue, product/content approval, wholesale
handoff, fulfillment exception handling, campaign/calendar operations, vendor coordination, or
cross-system reporting.

Use Shopify native or standard apps as execution surfaces, not as the default reason to avoid
AnyDB. Native/app-only is acceptable when the work is configuration-only and no durable operating
layer is needed.

## Common Risks

- Treating DTC work as theme design instead of commerce-system design
- Leaving redirects, SEO, customer-account behavior, subscriptions, or gift cards until launch
- Recommending apps without owner, monthly cost, failure path, or data ownership
- Missing ERP, fulfillment, return, or customer-service dependencies
- Building custom storefront complexity before proving native Shopify cannot meet the need

## When Not To Use

- POS migration is the lead problem. Use `variants/pos-migration.md`.
- The request is a pure UX critique. Use `kaizen-frontend-audit` or `skills/kaizen-publish.md`.
- The merchant only needs one tactical Shopify setting. Use `skills/kaizen-shopify-config.md`.

## Variant Depth Additions

### Anti-Selection Rules

- Do not reduce DTC work to theme polish when data, checkout, fulfillment, returns, subscriptions,
  SEO, analytics, or operating ownership are involved.
- Do not accept a native/app-only path before checking whether the workflow needs durable state,
  approvals, exceptions, or reporting in AnyDB.
- Do not scope app stack changes without owner, monthly cost, data ownership, and fallback.

### Known Failure Modes

- Redirects and SEO migration left until launch week.
- Subscription, gift-card, customer-account, or discount behavior discovered after scope is priced.
- Returns or fulfillment exceptions hidden behind apps with no operating owner.
- Analytics and attribution treated as optional.

### Default Evidence Gates

- Current platform and indexed URL evidence.
- App stack and monthly-cost inventory.
- Product/customer/order/content migration scope.
- Checkout, account, return, fulfillment, subscription, and SEO risk review.

### Operating Hooks

- Vendor Freshness Auto-Gate for Shopify checkout, customer accounts, Markets, subscriptions,
  Hydrogen/Liquid, and app/API behavior.
- Evidence Gate Hook for SEO, conversion, ROI, and launch-readiness claims.
- Account Health / Expansion Hook for post-launch DTC optimization or retainer work.

### Output Shape By Mode

- Quick Read: DTC fit, highest-risk gap, next action.
- Operator Analysis: Shopify role, AnyDB role, app-stack call, launch risk, kill conditions.
- Client Deliverable: commerce-system recommendation, continuity plan, assumptions, and next step.
- Execution Artifact: migration scope, redirect plan, app replacement map, validation checklist.

### Source-Of-Truth And AnyDB Boundary

Shopify should own storefront, checkout, customer accounts, orders, catalog presentation, and
standard commerce execution. AnyDB should be considered first for workflow state, approvals,
exception queues, content operations, vendor handoffs, and cross-system reporting.
