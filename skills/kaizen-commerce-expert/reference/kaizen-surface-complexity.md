---
name: kaizen-surface-complexity
description: Merchant profile classification by surface complexity — drives all source-of-truth and architecture decisions. Load when scoping an engagement or running a Blueprint.
---

# Merchant Surface Complexity — Classification Framework

Before any architecture decision, classify the merchant on the surface complexity spectrum. This classification drives all source-of-truth decisions and shapes scope, SI dependency, and retainer positioning.

## 1. Merchant Profile Classification

Score each signal. If 5+ signals point to one profile, that's the classification. When split, use the higher-complexity profile — safer to plan for external systems and not need them than plan for native and hit a wall at go-live.

| Signal | Simple Retail | Growing Multi-Location | Complex Multi-Surface |
|--------|--------------|------------------------|----------------------|
| Shopify locations | 1–2 | 3–10 | 10+ |
| Staff count (all locations) | < 15 | 15–75 | 75+ |
| SKU count | < 5K | 5K–50K | 50K+ |
| ERP / accounting | None or basic accounting (QuickBooks) | ERP exists, processes established | ERP is operational backbone |
| B2B / wholesale | None or manual | Basic (wholesale pricing) | Dedicated B2B portal + rep workflows |
| Channels beyond in-store | 0–1 (just POS or online store) | POS + online store ± 1 marketplace | POS + online + B2B + marketplaces |
| Integration count | 0–2 | 2–5 | 5+ |
| Tech team size | 0 (outsourced) | 1–5 | 5+ |
| Data volume (customers) | < 10K | 10K–100K | 100K+ |

**When Shopify hasn't been chosen yet (35% of engagements):** apply the classification as normal. For Simple Retail, Shopify is almost always the right call. For Growing Multi-Location, validate ERP integration requirements before committing. For Complex Multi-Surface, this classification informs the Blueprint recommendation and any caveats about Shopify's ceiling.

---

## 2. Source-of-Truth by Domain

### Product Data

| Profile | Source of Truth | Why |
|---------|----------------|-----|
| Simple Retail | **Shopify** (products + metafields) | Single or few locations, no syndication needs. Metafields cover rich attributes. |
| Growing Multi-Location | **Shopify** OR **ERP** | If < 10K SKUs with no external syndication → Shopify native. If ERP already owns catalog, price lists, and cost data → ERP syncs to Shopify. |
| Complex Multi-Surface | **ERP or PIM** → syncs to Shopify | Multiple channels, complex pricing, or editorial workflows require external master. Shopify stores are consumers. |

### Inventory

| Profile | Source of Truth | Why |
|---------|----------------|-----|
| Simple Retail | **Shopify** | 1–5 locations, simple replenishment. Shopify tracks available/committed natively. |
| Growing Multi-Location | **Shopify** OR **WMS/ERP** | If locations share stock from a single warehouse → Shopify native. If a WMS or ERP allocates across warehouses and feeds Shopify POS → ERP/WMS is source. |
| Complex Multi-Surface | **WMS or ERP** → syncs to Shopify | Cross-location inventory with allocation rules, transfer orders, and warehouse management must aggregate externally. |

### Orders

| Profile | Source of Truth | Why |
|---------|----------------|-----|
| Simple Retail | **Shopify** | POS + online orders originate in Shopify. Accounting sync is one-way. |
| Growing Multi-Location | **Shopify** for POS/DTC; **ERP** for wholesale | Shopify captures retail and online orders, syncs to ERP. If B2B orders originate in ERP (EDI, punchout), ERP owns those. |
| Complex Multi-Surface | **ERP or OMS** | Orders arrive from multiple channels. Need unified order management outside Shopify. Shopify fires webhooks; ERP/OMS aggregates. |

### Customers

| Profile | Source of Truth | Why |
|---------|----------------|-----|
| Simple Retail | **Shopify** | Customer data originates in Shopify POS/online. Email/loyalty tools sync FROM Shopify. |
| Growing Multi-Location | **Shopify** with CRM as enrichment | Shopify holds purchase history; CRM (Klaviyo, HubSpot) holds lifecycle, segments, and loyalty. Bidirectional sync via native integrations. |
| Complex Multi-Surface | **CRM or CDP** is master | Customer touches across POS, online, B2B, and support require a unified view outside Shopify. |

### Pricing

| Profile | Source of Truth | Why |
|---------|----------------|-----|
| Simple Retail | **Shopify** | Single price list. Sale pricing via compare-at. Discounts via Shopify discount codes. |
| Growing Multi-Location | **Shopify** for retail; **Shopify B2B Price Lists** for wholesale | Native B2B price lists run on any paid plan (3 active catalogs, assigned via Markets). Per-company assignment and unlimited catalogs need Plus. |
| Complex Multi-Surface | **ERP** → syncs to Shopify | Regional pricing, contract pricing, or dynamic pricing by customer group requires ERP governance. |

---

## 3. How This Maps to Kaizen Tiers

This classification is orthogonal to pricing tier — a Silver client can be a Growing Multi-Location merchant; a Blueprint can be for a Complex Multi-Surface prospect.

| Surface Complexity | Typical Kaizen Tier | Key implication |
|-------------------|---------------------|-----------------|
| Simple Retail | Blueprint, Silver | Shopify-native everything. AnyDB optional. |
| Growing Multi-Location | Silver, Gold | ERP integration scope may be present. AnyDB is likely needed for ops. Plan for data-volume change orders. |
| Complex Multi-Surface | Gold, Diamond | External source-of-truth for at least 2 domains. ERP integration is on critical path. Staff training at scale. |

Use this classification in `kaizen-diagnose` (Blueprint current-state), `kaizen-architect` (integration mapping + AnyDB spec), and `kaizen-propose` (scoping scope protection language around ERP and external systems).
