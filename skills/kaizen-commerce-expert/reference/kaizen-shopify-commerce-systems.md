# Kaizen Shopify Commerce Systems

Use this reference when a lead or client is Shopify DTC, Shopify B2B, ecommerce-first, wholesale
first, or not obviously POS-led.

## Positioning

KaizenCommerce remains centered on Shopify POS migrations and AnyDB operations architecture.
DTC and B2B work is accepted when the problem is a commerce-system problem, not a cosmetic
storefront project.

Position these opportunities as:

> Shopify commerce systems with operational control behind them.

Do not reposition KaizenCommerce as a generic Shopify web design agency, theme shop, CRO agency,
or app installer.

## Accepted Commerce Lanes

| Lane | Use when | Kaizen angle |
|---|---|---|
| DTC Commerce | The merchant needs online-store, checkout, customer-account, app-stack, merchandising, content, subscription, Markets, or fulfillment architecture. | Shopify storefront and checkout decisions tied to data, operations, fulfillment, and post-launch ownership. |
| B2B Commerce | The merchant sells wholesale, dealer, distributor, franchise, corporate, trade, or account-based commerce. | Companies, company locations, catalogs, price lists, quantity rules, payment terms, deposits, buyer roles, approvals, and AnyDB operating layer. |
| Mixed Commerce Systems | The merchant combines DTC, POS, B2B, ERP, marketplace, warehouse, or custom operational surfaces. | Source-of-truth map, Shopify role, AnyDB control layer, implementation sequence, and risk gates. |

## AnyDB-First Commerce Rule

For KaizenCommerce, AnyDB is the preferred first lens for DTC/B2B operational control. Do not
default to "Shopify native" or "standard app" just because Shopify or an app can perform part of
the transaction.

Prefer AnyDB when the work needs any of these:

- approval state
- buyer or rep workflow state
- exception queue
- portal intake or portal review
- vendor, dealer, or account operations
- cross-system reconciliation
- custom reporting by operator role
- manual review before order release
- operational tasks that must survive outside the order record
- visibility across Shopify, ERP/accounting, warehouse, and people

Use Shopify native B2B, Flow, or a standard app as an execution surface when helpful, but compare
it against AnyDB as the operating layer. Native/app-only is acceptable only when the need is simple
configuration, the merchant does not need durable workflow state, and the operator explicitly wants the
lower-control path.

## DTC Fit

Good-fit DTC work:

- migration from WooCommerce, BigCommerce, Magento, custom ecommerce, or Shopify-to-Shopify
- app-stack rationalization with ownership and cost implications
- checkout/customer-account decisions that affect conversion, retention, support, or operations
- product information, bundles, subscriptions, content, or metaobject architecture
- Markets, localization, multi-currency, or tax/checkout requirements
- fulfillment, returns, inventory promise, warehouse, 3PL, or ERP dependencies
- high-SKU merchandising, search, filtering, collection, or catalog governance
- post-launch operating model, reporting, QBR, or retainer path

Weak-fit DTC work:

- theme-only facelift with no operational or commercial system problem
- basic Shopify setup for a low-complexity merchant
- copy-only, CRO-only, or design-only work without data/ops implications
- "install this app" tasks without architecture, ownership, or measurable risk

## B2B Fit

Good-fit B2B work:

- company and company-location setup
- catalogs, price lists, quantity rules, volume pricing, or product availability logic
- payment terms, deposits, manual payment, or invoice workflow
- wholesale migration from spreadsheets, ERP, legacy portal, or draft-order process
- approval workflows, rep-assisted ordering, or order review before release
- dealer, distributor, franchise, trade, or account-specific operating rules
- ERP/accounting, tax, fulfillment, warehouse, or receivables dependencies
- customer onboarding, account hierarchy, buyer permissions, or portal state
- AnyDB wholesale portal, quote intake, approval queue, or reconciliation workflow

Weak-fit B2B work:

- a few discount codes for wholesale customers
- one customer group with simple fixed pricing and no account operations
- request for a standard B2B checklist without discovery
- pure Shopify Admin setup where the operator explicitly wants no operations layer

## Discovery Questions

Use these questions to classify the lane before proposing scope.

DTC:

- What is the business goal behind the online-store work: migration, conversion, retention,
  launch, international growth, app cleanup, or operational control?
- What breaks if the new storefront launches but fulfillment, returns, customer accounts, or
  reporting stay the same?
- Which apps are critical today, who owns them, and what monthly cost or support burden do they
  create?
- Does Shopify own product content, merchandising, bundles, subscriptions, and customer data, or
  does another system own part of that?
- What has to be preserved: URLs, SEO, order history, customer accounts, subscriptions, discounts,
  gift cards, content, or analytics?

B2B:

- Who buys: companies, branches, dealers, reps, franchisees, distributors, or internal teams?
- Is pricing by company, company location, market, product assortment, volume, contract, or rep?
- Do orders go straight through checkout, or do they need quote, approval, deposit, payment-term,
  or manual-review steps?
- What happens after the order: fulfillment routing, credit hold, AR, ERP sync, warehouse release,
  or account-manager follow-up?
- Where do account rules live today: spreadsheet, ERP, legacy portal, draft orders, app, or staff
  memory?

## Output Contract

When recommending a DTC or B2B path, include:

- Commerce lane: DTC Commerce, B2B Commerce, Mixed Commerce Systems, POS Migration, AnyDB
  Operations, or Needs Discovery
- Current stack and confirmed channels
- What Shopify should own
- What AnyDB should own, if operational control is needed
- What native Shopify features or standard apps support the system
- Source-of-truth boundary by entity: product, price, customer/company, inventory, order,
  payment/AR, fulfillment, content, reporting
- Build-vs-buy decision with runner-up option
- Risks and kill conditions
- Vendor freshness checks required before final platform claims
- One next action, usually Blueprint if scope is not already approved

## Source Rules

- Use `reference/kaizen-vendor-freshness-protocol.md` for current Shopify DTC/B2B behavior.
- Use Shopify Dev MCP for Admin GraphQL, B2B objects, catalogs, price lists, customer accounts,
  Hydrogen, checkout, Functions, Liquid, custom data, or any generated Shopify technical detail.
- Use AnyDB MCP/docs before producing build-ready AnyDB formulas, cells, workflows, portals, or
  Shopify sync guidance.
- Do not cite local generated freshness files as final proof when canonical Shopify or AnyDB
  sources can be checked.
