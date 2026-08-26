---
name: kaizen-ref-b2b
description: "Deep retail reference for b2b questions routed by Kai."
metadata_version: 1
layer: retail-reference
upstream: ["kaizen-retail-expert-v2"]
downstream: []
adjacent: []
canon: []
owns: ["b2b domain reference"]
does_not_own: ["final implementation recommendation without routed skill context"]
---

# Shopify B2B Reference Pack — Plans, Companies, Catalogs, Terms, Ordering, Workflow Layer

Peer of `kaizen-ref-pos.md`. Load this for any Shopify B2B qualification, architecture, scoping,
migration, or build question.

**Freshness status:** plan capability facts below were validated live on 2026-07-26 against
`changelog.shopify.com` and `shopify.com/news`. Plan availability is the single most
rollout-sensitive area in this pack. Re-verify before any client-facing commitment older than
14 days. See `reference/kaizen-vendor-freshness-protocol.md`.

---

### 4A. Plan Capability Matrix

#### The April 2026 Change

Native Shopify B2B moved off Plus-exclusivity on **April 2, 2026**. Basic, Grow, and Advanced
merchants can sell wholesale using native B2B in the admin at no additional cost.

Canonical sources checked:

- `https://changelog.shopify.com/posts/key-b2b-features-now-available-on-non-plus-plans`
- `https://www.shopify.com/news/b2b-for-all`

This is the fact that changed KaizenCommerce's B2B ICP. The old assumption (B2B means Plus, so B2B
means enterprise budget) is dead. A $3M wholesaler on Advanced is now a real B2B engagement.

#### What Every Paid Plan Gets

Source: `https://help.shopify.com/en/manual/b2b/getting-started/plan-features` (checked 2026-07-26).

| Capability | Notes |
|---|---|
| Companies and company locations | Full hierarchy |
| Location-level permissions | Per-location ordering rights |
| Quantity rules and price breaks | Minimum, maximum, increment, volume tiers |
| Net payment terms | See the template list in 4B |
| Payment reminders | Native dunning on terms |
| ACH | US only |
| Vaulted credit cards | Stored card on the company location |
| Draft orders and PO numbers | Rep-entered ordering, buyer PO reference |
| Easy reorders | Buyer-side repeat ordering |
| Sales staff permissions | Rep access scoping |
| Trade theme | Free, B2B-purpose-built. Available on every plan |
| Quick order list | Bulk SKU entry |
| Shopify Flow automations | B2B triggers carry no separate plan gate |

#### What Stays Plus-Only

| Capability | Why it matters to scoping |
|---|---|
| Unlimited B2B market catalogs | Non-Plus caps at 3 active catalogs across all B2B markets. More than 3 genuine pricing tiers hits a wall |
| Direct company catalog assignment | This is customer-level pricing. Non-Plus assigns catalogs **via Markets**, so true per-company pricing is not native below Plus |
| **Deposit requirements** (companies and draft orders) | Deposit-taking is Plus-only |
| Partial payments | Split or instalment collection on a B2B order |
| Payment requests per fulfillment | Bill as you ship |
| Contextual checkout via Shopify Markets | |
| Contextual storefront customization | |

#### The Advanced Line

Contextual checkout and storefront require **Advanced or Plus**. Basic and Grow do not get them. A
Basic or Grow merchant who wants a buyer-contextualized storefront experience is looking at an
Advanced upgrade before any custom work is scoped.

#### The Two Scoping Traps

**Trap 1 — deposits.** KaizenCommerce's own B2B scope language has historically listed deposits as
standard B2B scope. On non-Plus that is not a native capability. If a merchant on Basic/Grow/Advanced
needs deposits, the options are a Plus upgrade, an app, or a workflow-layer build. Name the
constraint and the cost before it lands in a SOW.

**Trap 2 — the 3-catalog ceiling and Markets assignment.** Non-Plus catalogs attach through Markets,
not directly to a company or location. A merchant who says "every dealer has their own pricing" is
describing per-company assignment, which is Plus. Below Plus you get at most 3 pricing contexts
natively, and everything past that needs the operating layer or an upgrade.

Both traps are plan-sensitive, so both are hard-gate items under the freshness protocol. Confirm the
merchant's actual plan in discovery. Never scope B2B from the logo on the invoice.

#### Catalog Architecture Under The Cap

Company locations support multiple catalog assignments, which enables a pricing-only plus
publication-only split instead of one full catalog per combination:

- pricing-only catalogs, one per price list
- publication-only catalogs, one per product assortment
- assign several to the same company location

A Plus merchant with 50 pricing tiers and 10 assortments builds 60 catalogs, not 500. Resolution
rules: when multiple pricing catalogs apply the buyer receives the **lowest** price, and a product
must be published in at least one applicable publication to be visible.

On non-Plus, the 3-catalog cap applies to this same pool, so the split pattern buys much less. Plan
the assortment/pricing model around the cap before promising tiered pricing.

---

### 4B. Prerequisites And Hard Limits

| Constraint | Detail |
|---|---|
| Customer accounts | B2B works **only** with new customer accounts. A merchant on legacy customer accounts must migrate auth/login first. This is a real work item, not a checkbox |
| Purchase options | B2B does **not** support subscriptions, pre-orders, or try-before-you-buy |
| Automatic payment capture | **Not supported on B2B checkouts.** Merchants capture manually when the fulfillment event occurs. D2C checkouts do support automatic capture. This shapes the AR workflow and is a frequent surprise |
| Payment customization functions | Setting payment terms dynamically through the Payment Customization API requires Plus. Merchant-configured terms on B2B orders do not |
| Custom Function apps | Only Plus stores can install **custom** apps containing Shopify Function APIs. Any plan can install **public** App Store apps built on Functions. This decides build-vs-buy for checkout logic below Plus |
| Merchant review requirement | Can be applied only to B2B checkouts. Not to orders, draft-order invoice checkouts, or draft-order calculation flows in admin |
| API access for app builds | Admin API B2B resources are reachable only from dev stores, Shopify Plus Partner orgs, and Shopify affiliates. Plus Partners need a sandbox organization |
| Deprecated field | `PriceList.contextRule` is deprecated from API version 2023-04. Build on catalogs |

#### Payment Terms Templates

Confirmed via the `paymentTermsTemplates` Admin GraphQL query (2026-07-26). `PaymentTermsType`
values are `NET`, `FIXED`, `FULFILLMENT`, `RECEIPT`, `UNKNOWN`.

| Template | Type | Due |
|---|---|---|
| Due on receipt | RECEIPT | On receipt |
| Due on fulfillment | FULFILLMENT | On fulfillment |
| Net 7 / 15 / 30 / 45 / 60 / 90 | NET | 7, 15, 30, 45, 60, or 90 days after issue |
| Fixed | FIXED | A specified date |

#### Buyer Experience Configuration

`CompanyLocation.BuyerExperienceConfiguration` is where checkout behavior settles: payment terms and
whether orders require merchant review. Company location, not company, is the configuration unit.
Model the merchant's branches correctly in discovery or the whole checkout behavior lands wrong.

The customer-accounts prerequisite is the most commonly missed item in B2B scoping. A merchant with
a heavily customized legacy account experience is buying an account migration alongside the B2B
build, and that belongs in the estimate.

---

### 4C. Data Model

| Object | Role |
|---|---|
| Company | The buying organization. Top of the hierarchy |
| Company location | Where pricing, catalogs, payment terms, and tax settle. The real unit of configuration |
| Company contact | A customer record attached to a company, with ordering permissions |
| Catalog | Binds a price list and/or publication to a context (company location on Plus, market otherwise) |
| Price list | Prices or percentage adjustments applied in an eligible context |
| Publication | The product set visible in that context |
| Quantity rules | Minimum, maximum, and increment per variant in context |
| Quantity price breaks | Volume tiers within a price list |

Company location is where most merchant confusion lives. A dealer with three branches that order
separately, hold separate terms, and ship separately is three company locations, not three
companies. Get this right in discovery because it drives catalog count, which drives plan fit.

---

### 4D. Ordering And Approval Flows

| Flow | How it works | When to recommend |
|---|---|---|
| Self-serve B2B checkout | Buyer logs in, sees contextualized catalog and pricing, checks out against terms | The target state for most engagements. Highest operational leverage |
| Draft order, merchant-created | Merchant or rep builds the order, buyer reviews/approves and pays | Rep-led accounts, negotiated orders, complex configurations |
| Quote-to-order | Quote is drafted, negotiated, converted | Needed when price is negotiated per order rather than per account |
| Approval workflow | Buyer-side approval before an order is placed | Larger trade accounts with internal purchasing controls |

Shopify's native lifecycle covers company creation, contact login, draft-order review, and checkout.
Buyer-side multi-step approval chains, credit-hold logic, and exception queues are not native
behavior. That gap is the workflow layer, addressed below.

---

### 4E. Native Versus Operating Layer

This is the KaizenCommerce judgment call and the reason the firm sells B2B rather than configuring
it. Apply `reference/kaizen-build-vs-buy.md` and the AnyDB-first rule in `kaizen-identity.md`.

**Stay native when:**

- pricing tiers fit inside the plan's catalog budget
- terms are standard net terms with no credit decisioning
- ordering is self-serve or simple rep-entered draft orders
- no buyer-side approval chain
- the ERP is the system of record and a straightforward sync covers it

**Build the operating layer when:**

- per-account pricing exceeds the catalog ceiling on the merchant's plan
- approval state must persist and be queryable (who approved, when, against which limit)
- credit holds, over-limit exceptions, or collections state drive whether an order releases
- reps and buyers hand work back and forth and someone must see the queue
- deposits or partial payments are required below Plus
- reconciliation runs across Shopify, ERP, and accounting and today lives in a spreadsheet
- the merchant needs reporting Shopify does not produce and the ERP will not expose

The rule from identity holds: do not reject the operating layer merely because native B2B, Flow, or
an app performs part of the workflow. Prefer it when the merchant needs durable approval state,
exception queues, portals, rep/buyer handoffs, cross-system reconciliation, or operational tasks
that cannot live on a transaction record.

State the boundary explicitly in every B2B architecture output: what Shopify owns, what the
operating layer owns, what the ERP owns, and where each record is authored.

---

### 4F. ERP, Accounting, And Tax Boundary

Most B2B merchants have an ERP or accounting system that predates Shopify and will outlive the
engagement. Decide and document these before build:

| Entity | Common system of truth | Watch for |
|---|---|---|
| Product and price master | ERP, sometimes Shopify | Two-way price sync is a frequent failure point. Prefer one authoring direction |
| Inventory | ERP or WMS | B2B and DTC drawing on one pool needs an allocation rule |
| Company/customer master | ERP or CRM | Shopify companies must map to ERP account codes |
| Orders | Shopify authors, ERP consumes | Define the release trigger and the failure path |
| Invoices and AR | ERP/accounting | Terms in Shopify must not silently disagree with AR |
| Tax and exemption certificates | Tax engine or ERP | Resale/exemption handling is jurisdictional. Treat as `[VERIFY]` per merchant |

Tax exemption for resale is the item most likely to be assumed and least likely to be simple.
Confirm how certificates are captured, stored, validated, and expired before scoping it.

---

### 4G. Migration Entity Map

Scope B2B migrations against this list. Anything not named here is out of scope until it is.

| Entity | Notes |
|---|---|
| Companies | Names, external IDs, ERP account codes |
| Company locations | Addresses, terms, tax settings, shipping defaults |
| Company contacts | Requires the new-customer-accounts path |
| Catalogs and publications | Assortment per context |
| Price lists | Fixed prices and percentage adjustments |
| Quantity rules and price breaks | Per variant, per context |
| Payment terms assignments | Per company location |
| Historical orders | Decide reference-only versus full import early. Drives effort more than any other line |
| Open orders and backorders | Cutover-sensitive. Needs a freeze plan |
| Open AR and balances | Usually stays in the ERP. Confirm, never assume |
| Draft orders and quotes in flight | Often forgotten and always noticed at go-live |

---

### 4H. Discovery Questions

Ask these before any B2B recommendation. They map to the decisions above.

1. What plan are you on today, and is a plan change on the table?
2. How many buying accounts, and how many ship-to locations across them?
3. How is pricing set: shared tiers, per-account, or negotiated per order? How many distinct tiers?
4. Who places orders today: buyers themselves, your reps, or both?
5. What has to happen between a buyer submitting and the order being fulfilled? Any approval or credit check?
6. Do you take deposits or partial payment on any orders?
7. What are your payment terms, and who decides when an account goes on hold?
8. What is your ERP or accounting system, and what does it own today?
9. Are you on new or legacy customer accounts?
10. What do you re-key by hand right now, and how many hours does it cost?

Question 1 gates the architecture. Question 6 detects the deposit trap. Question 9 detects the
customer-accounts migration. Question 10 produces the number the proposal is built on.

---

### 4I. Kill Conditions

Walk away or downscope when:

- a handful of accounts share one price list with no terms, approval, or reconciliation need
- EDI or punchout is the entire ask with no Shopify-side operating model
- the merchant does not own the buyer relationship (marketplace or distributor-portal selling)
- the merchant wants per-company pricing at scale, refuses Plus, and refuses an operating layer
- the ERP owner is not in the room and will not be

---

### 4J. Verification Log

All items opened on 2026-07-26 were settled the same day against canonical sources. Nothing in this
pack is currently `[VERIFY]`.

| Question | Verdict | Source |
|---|---|---|
| Exact net-terms options | Confirmed: receipt, fulfillment, Net 7/15/30/45/60/90, fixed | `paymentTermsTemplates` Admin GraphQL query |
| Trade theme availability and gating | Free, on every plan | `help.shopify.com/en/manual/b2b/getting-started/plan-features` |
| Flow B2B automation gating | No separate gate. Listed as available on all plans | Same |
| Non-US payment coverage | ACH is US-only. Vaulted cards on all plans. No broader non-US method set claimed | Same, plus the April changelog |

Re-verify this pack's plan matrix before any client-facing commitment more than 14 days after the
date stamped at the top. Plan tiers are the most rollout-sensitive surface Kai touches.
