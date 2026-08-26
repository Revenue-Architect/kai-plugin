---
name: kaizen-build-vs-buy
description: 4-verdict decision framework for every system in a merchant's stack — NATIVE / THIRD-PARTY / CUSTOM BUILD / RETAIN & INTEGRATE. Load in kaizen-architect and kaizen-diagnose for integration mapping and future-state architecture.
---

# Build vs Buy vs Native — Decision Framework

Every system in the merchant's current stack gets one of four verdicts:

- **NATIVE** — Replace with Shopify native capability
- **THIRD-PARTY** — Replace with a best-in-class Shopify app or connector
- **CUSTOM BUILD** — Build on Shopify APIs (Functions, Extensions, Admin API, Flow)
- **RETAIN & INTEGRATE** — Keep existing system; connect via APIs/webhooks/integration layer

Apply these verdicts in `kaizen-architect` (integration mapping mode) and surface the key decisions in `kaizen-diagnose` (future-state architecture section).

---

## Kaizen AnyDB-First Commerce Override

For DTC and B2B commerce systems, evaluate AnyDB before defaulting to Shopify native, Flow, or a
standard app when the merchant needs operating control. Shopify native B2B can own companies,
company locations, catalogs, price lists, checkout, and orders. Standard apps can support narrow
jobs. AnyDB is preferred for the operating layer when the workflow needs state, approvals,
exception handling, portal intake, rep/buyer handoffs, reconciliation, or custom reporting.

Native/app-only wins only when the operator explicitly wants a lower-control path and the requirement
is simple configuration with no durable operations layer.

---

## 1. Always Shopify Native

These are Shopify's core strengths. External alternatives add cost without meaningful benefit.

| Capability | Shopify Solution | Why Always Native |
|-----------|-----------------|-------------------|
| POS transactions | Shopify POS | End-to-end Shopify ecosystem. No third-party POS. |
| Checkout | Checkout + Functions + UI Extensions | PCI Level 1, Shop Pay conversion lift, extensible via checkout targets |
| Payments processing | Shopify Payments + 100+ gateways | Eliminates transaction fee on Shopify Payments |
| CDN & infrastructure | Shopify's global CDN | 99.99% SLA (Plus), DDoS, edge caching — no merchant infra |
| Multi-currency | Markets + Shopify Payments | Auto-conversion with rounding rules per market |
| SSL & security | Auto-provisioned | PCI DSS Level 1 by default |

---

## 2. Profile-Dependent Verdicts

Source-of-truth classification (see [`kaizen-surface-complexity.md`](kaizen-surface-complexity.md)) determines these. Do not assign a verdict without knowing the merchant's profile.

| Capability | Simple Retail | Growing Multi-Location | Complex Multi-Surface |
|-----------|--------------|------------------------|----------------------|
| Product data management | NATIVE (metafields) | NATIVE or RETAIN ERP | RETAIN ERP / THIRD-PARTY PIM |
| Inventory management | NATIVE | NATIVE or RETAIN WMS/ERP | RETAIN WMS/ERP → Shopify |
| Bin/shelf-level inventory | OPERATING LAYER today; bins in Shopify feature preview since 2026-07-17 | Same, watch the preview | RETAIN WMS |
| Vendor PO lifecycle | OPERATING LAYER. Preview adds read-only PO access, not create/approve/receive | OPERATING LAYER or ERP | ERP |
| Order management | NATIVE | NATIVE + ERP sync | RETAIN OMS/ERP |
| Customer accounts | NATIVE | NATIVE + CRM enrichment | RETAIN CRM/CDP |
| B2B pricing | NATIVE (3-catalog cap, Markets-assigned) | NATIVE (Plus for unlimited catalogs + per-company assignment) | NATIVE + CUSTOM for 20% gap |
| Tax | NATIVE (Shopify Tax, US) | NATIVE or THIRD-PARTY (Avalara if global) | THIRD-PARTY (Avalara, Vertex) |
| Subscriptions | NATIVE (Subscriptions API) | NATIVE or THIRD-PARTY if complex | THIRD-PARTY (ReCharge, Bold) |

---

## 3. Always Third-Party (Best-in-Class Wins)

These have mature Shopify integrations better than building custom.

| Capability | Why Third-Party | Recommended |
|-----------|----------------|-------------|
| Email / SMS marketing | Deep native integrations; bespoke builds don't scale | Klaviyo (deepest), Attentive |
| Loyalty (standard) | Points, rewards, referrals are commoditized | Yotpo, Smile.io, LoyaltyLion |
| Reviews & UGC | Established collection + display infrastructure | Yotpo, Judge.me, Stamped |
| Returns (advanced) | Loop Returns handles complex exchange logic natively | Loop Returns, Returnly |
| Search (10K–100K SKUs) | Native search lacks advanced faceting at scale | Algolia, Klevu, Boost |
| ERP connector (established ERP) | Pre-built connectors cover 80%+ of flows | Celigo (NetSuite), Patchworks, custom |
| Fraud detection | ML models require data sets merchants can't build alone | Riskified, Signifyd |

---

## 4. Custom Build When Bespoke

When requirements are unique to this merchant and no off-the-shelf solution fits.

| Capability | Shopify APIs Used | When Custom Required |
|-----------|-------------------|---------------------|
| Complex loyalty | Checkout UI Extensions + Functions + custom app | Cross-channel redemption, custom earning rules, tiered VIP |
| Bespoke pricing logic | Shopify Functions (Product/Order Discounts) | Contract pricing, company-specific volume breaks |
| Custom B2B workflows | Draft Orders API + Company API | CPQ, multi-level approval chains, rep quoting portals |
| Real-time WMS sync | Webhooks + Inventory API | Sub-minute accuracy from external WMS |
| SSO / staff portal | Multipass (Plus) + custom app | Corporate IdP (Okta, Azure AD) for B2B buyers |
| Custom admin tools | App Bridge + Admin UI Extensions | ERP status dashboards, custom workflow UIs |
| AnyDB operational layer | AnyDB MCP + automations | Operational workflows that live outside Shopify (job tracking, client portals, staff tools) |

---

## 5. Retain & Integrate

Keep the existing system; connect it to Shopify via APIs, webhooks, or an integration layer.

Apply when:
- The system is deeply operational (ERP, WMS, HRIS) and teams are trained on it
- Switching cost exceeds integration cost
- The external system is a true source of truth (see [`kaizen-surface-complexity.md`](kaizen-surface-complexity.md))

When recommending Retain & Integrate, document:
1. Which system is retained
2. What data flows (direction, frequency, trigger)
3. What integration layer is recommended (native connector, iPaaS, custom)
4. Who owns the integration post-launch

---

## 6. Quick-Reference Lookup

| Capability | Simple Retail | Growing Multi-Location | Complex Multi-Surface |
|-----------|--------------|------------------------|----------------------|
| Accounting | THIRD-PARTY connector (QuickBooks, Xero) | RETAIN & INTEGRATE (ERP) | RETAIN & INTEGRATE |
| CRM / Email | THIRD-PARTY (Klaviyo) | THIRD-PARTY | THIRD-PARTY or RETAIN CDP |
| ERP | N/A | RETAIN & INTEGRATE | RETAIN & INTEGRATE |
| Inventory | NATIVE | NATIVE or RETAIN | RETAIN WMS/ERP |
| Loyalty | THIRD-PARTY | THIRD-PARTY or CUSTOM | CUSTOM |
| OMS | NATIVE | NATIVE + ERP sync | RETAIN OMS/ERP |
| PIM | NATIVE (metafields) | NATIVE or THIRD-PARTY | THIRD-PARTY |
| POS | NATIVE | NATIVE | NATIVE |
| Returns | NATIVE or THIRD-PARTY | THIRD-PARTY (Loop) | THIRD-PARTY |
| Search < 10K | NATIVE | NATIVE | NATIVE |
| Search 10K–100K | THIRD-PARTY | THIRD-PARTY | THIRD-PARTY |
| Subscriptions | NATIVE | NATIVE or THIRD-PARTY | THIRD-PARTY |
| Tax (US) | NATIVE | NATIVE | NATIVE or THIRD-PARTY |
| Tax (global) | N/A | THIRD-PARTY | THIRD-PARTY (Avalara) |
| WMS | N/A | NATIVE or RETAIN | RETAIN WMS |
