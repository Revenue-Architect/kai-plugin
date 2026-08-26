---
name: kaizen-erp-patterns
description: ERP integration patterns, data flows, source-of-truth mapping, and vendor-specific notes. Load when ERP integration is confirmed in scope — typically Gold and Diamond tiers and any merchant with an accounting system beyond QuickBooks.
---

# ERP Integration Patterns

ERP integration is the highest-effort, highest-risk element of most Kaizen Gold/Diamond engagements. Do not underestimate it. If an ERP is confirmed in scope, it belongs on the critical path, alongside the API-first migration lane decision and before any fallback CSV or Matrixify work is treated as sufficient.

**Effort allocation rule:** ERP integration typically consumes 30–40% of total integration effort. Budget this honestly in proposals.

---

## 1. Source-of-Truth Matrix

Establish this for every ERP engagement before architecture work begins. Fill it in per merchant.

| Data Domain | Typical Source of Truth | Direction | Shopify API | Sync Frequency |
|-------------|------------------------|-----------|-------------|----------------|
| Products / Catalog | ERP or PIM | ERP/PIM → Shopify | `products`, Bulk Operations | Scheduled (15–60 min) or on-change |
| Inventory | ERP or WMS | ERP/WMS → Shopify | `inventory_levels` per location | Near-real-time (webhook + polling fallback) |
| Orders | Shopify | Shopify → ERP | `orders` via webhook `orders/create`, `orders/paid` | Real-time webhook |
| Customers | Shared | Bidirectional | `customers`, Customer Account API | Real-time + nightly reconciliation |
| Pricing | ERP | ERP → Shopify | `variants` (price, compare_at), Catalogs API (B2B) | Scheduled (hourly or on price-change event) |
| Fulfillment / Shipping | ERP or WMS | ERP/WMS → Shopify | Fulfillment Orders API | Real-time on shipment event |
| Returns | Shared | Bidirectional | `returns`, `refunds` | Real-time |
| Financial reconciliation | Shopify → ERP (payouts) | One-way | Payouts API, Transactions API | Daily or per-payout |

---

## 2. ERP Integration Patterns by Vendor

### QuickBooks Online (QBO) — Most Common for Silver/Gold Clients

- **Integration approach:** Native Shopify-QBO connector apps (QuickBooks Connector by OneSaas, A2X, Bench Accounting's export)
- **Primary data flow:** Orders → QBO as Sales Receipts or Invoices; payouts reconciled; products/inventory optionally synced
- **Connector apps:** QuickBooks Connector (official), A2X (Shopify Payments payout reconciliation), Bold Commerce QBO
- **Common gotcha:** QBO connector apps do NOT work with QuickBooks Desktop. If merchant has QB Desktop, either migrate them to QBO first or build custom middleware. Flag in discovery.
- **Common gotcha:** QBO has entity limits on the free tier — confirm merchant's QBO plan before integration design
- **Common gotcha:** Sales tax mapping between Shopify Tax and QBO tax codes requires careful configuration; validate with the merchant's accountant
- **Effort:** Low — connector apps handle most flows; custom work rarely needed

### QuickBooks Desktop (QB Desktop / QB Enterprise)

- **Integration approach:** Custom middleware required; QB Desktop does not have a cloud API
- **Options:**
  1. Migrate merchant to QBO (recommend if feasible — much simpler integration path)
  2. QODBC driver (read-only; limited for bidirectional flows)
  3. QuickBooks SDK (IIF imports, Web Connector) — fragile, maintenance-heavy
  4. Third-party middleware that supports Desktop (e.g., Connex by Sync with Connex)
- **Effort:** High — flag as custom integration scope if Desktop cannot be migrated to QBO

### NetSuite — Most Common for Diamond / Complex Gold Clients

- **Primary connector:** Celigo (most mature Shopify-NetSuite integration)
- **Alternative connectors:** Patchworks, custom middleware
- **Celigo specifics:**
  - Pre-built flows for orders, customers, items, inventory, fulfillment
  - SuiteApp installed in NetSuite side — uses RESTlets and Saved Searches
  - Supports multi-subsidiary mapping to Shopify Markets
  - **Common gotcha:** NetSuite Saved Search row limit defaults to 1,000 — configure pagination in Celigo flows or data misses silently
  - **Common gotcha:** NetSuite sandbox refresh wipes integration credentials — plan re-auth in staging environment
  - **Common gotcha:** NetSuite custom records often need SuiteScript + Celigo custom steps — not covered by out-of-box flows
- **Standard entities:** Sales Orders, Item Fulfillments, Customer Deposits, Cash Sales, Inventory Items
- **Effort:** Medium — Celigo covers 80%; custom SuiteScript for the remaining 20%

### SAP Business One (SAP B1) — Mid-Market ERP

- **Integration approach:** Service Layer (REST API) — modern and well-documented. DI API (legacy SDK) — avoid if possible.
- **Primary connectors:** Custom middleware; limited pre-built ecosystem for Shopify-SAP B1 specifically
- **Connector tools:** Celigo has partial SAP B1 support; Patchworks covers B1 for some flows; custom is often required
- **Standard entities:** Business Partners (customers/vendors), Items (products), Sales Orders, Inventory (Item Warehouses), A/R Invoices
- **Common gotcha:** SAP B1 uses UDF (User-Defined Fields) for custom attributes — map to Shopify metafields; confirm field types
- **Common gotcha:** SAP B1 has per-company database model — ensure integration credentials connect to the correct company database
- **Effort:** Medium–High — custom middleware likely; Service Layer API is clean but connector ecosystem is thinner than NetSuite

### Microsoft Dynamics 365 Business Central (BC) — Mid-Market ERP

- **Integration approach:** Dataverse Web API (OData v4) — REST-based, well-documented
- **Primary connectors:** Celigo (D365 + Shopify), Microsoft's own Shopify Connector in Business Central
- **Microsoft's native connector:** Business Central includes a native Shopify Connector (shipping with BC 2022 Wave 2+) — if merchant is on current BC version, this is the fastest path
- **Standard entities:** Sales Orders, Customers, Items, Item Ledger Entries (inventory), Shipped Sales Shipments
- **Common gotcha:** D365 Finance & Operations (enterprise) vs Business Central (SMB) — completely different APIs and complexity levels. Confirm which version.
- **Common gotcha:** Business Events (async triggers in D365) behave differently from webhooks — design for eventual consistency
- **Effort:** Medium — Microsoft's native connector covers core flows; custom work for edge cases

### SAP S/4HANA — Enterprise (Rare for Kaizen, Present for Diamond)

- **Integration approach:** OData APIs (recommended for new integrations), IDoc-based (legacy async), BAPI/RFC (synchronous)
- **Primary connectors:** MuleSoft, Boomi, custom middleware
- **Effort:** High — requires SAP specialist alongside Kaizen; budget SAP basis team involvement
- **Common gotcha:** SAP transport system (DEV → QA → PROD) means integration changes move slowly — align timelines
- **Common gotcha:** SAP defaults to ISO-8859-1 encoding; ensure UTF-8 conversion in all data pipelines
- **When to flag:** If merchant is on SAP S/4HANA, this is a Diamond engagement minimum. Do not attempt without a designated SAP integration resource.

### Sage (50 / 100 / 200 / X3)

- **Integration approach:**
  - Sage 50 / Sage 100: Limited or no cloud API — custom middleware via ODBC/SDK or SFTP file exchange
  - Sage 200: REST API available; connector apps emerging
  - Sage X3: Web Services API (SOAP) or newer REST gateway
- **Connector apps:** Limited native ecosystem. Third-party middleware (Patchworks, custom) typically required.
- **Common gotcha:** Sage 50 / 100 are on-premise — requires VPN or agent-based integration approach. Not compatible with most cloud iPaaS directly.
- **Effort:** Medium–High depending on version; flag custom scope if Sage 50/100 with no upgrade path

---

## 3. Standard Data Flows

### Product / Catalog Sync (ERP/PIM → Shopify)
- **Trigger:** Scheduled batch or event-driven from source
- **Shopify API:** Admin API `POST /products`, Bulk Operations for large catalogs (>1K SKUs)
- **Idempotency:** Use external ERP ID stored in metafield (`custom.erp_id`) to match existing products; update if found, create if not
- **Common gotcha:** Shopify 100-variant limit per product — if ERP has products with more, requires modeling workaround (split products or combined options)

### Inventory Sync (ERP/WMS → Shopify)
- **Trigger:** Webhook from ERP/WMS on stock change, or scheduled poll (every 5–15 min)
- **Shopify API:** `inventory_levels/set` (absolute value — preferred) or `inventory_levels/adjust` (delta)
- **Always use `set` (absolute), not `adjust` (delta)** — prevents cumulative drift if a sync message is missed
- **Multi-location:** Map ERP warehouse IDs to Shopify Location IDs. Document this mapping explicitly.
- **Common gotcha:** Shopify inventory is per-variant per-location — source system must provide this granularity

### Order Sync (Shopify → ERP)
- **Trigger:** Webhook `orders/create` or `orders/paid` (confirm with ERP what triggers the transaction)
- **Idempotency:** Use Shopify order ID or order number as external reference in ERP; check for duplicates before create
- **Common gotcha:** `orders/edited` webhook fires separately when a Shopify order is modified post-creation — ERP must handle order updates, not just order creates

### Customer Sync (Bidirectional)
- **Trigger:** `customers/create` and `customers/update` webhooks (Shopify → ERP); ERP event or schedule (ERP → Shopify)
- **Conflict resolution strategy required:** Either last-write-wins (timestamp-based) or field-level ownership (ERP owns billing, Shopify owns marketing preferences)
- **Canonical identifier:** Establish one canonical merge key early — email is default; some merchants use an external CRM ID stored in metafield

### Fulfillment / Tracking (ERP/WMS → Shopify)
- **Trigger:** ERP/WMS shipment confirmation event
- **Shopify API:** Fulfillment Orders API (`POST /fulfillment_orders/{id}/fulfillments`)
- **Common gotcha:** Partial fulfillments require fulfilling specific line items — not just the whole order

### Financial Reconciliation (Shopify → ERP)
- **Trigger:** Scheduled (daily or per Shopify Payments payout)
- **Shopify API:** Payouts API, Transactions API, `orders` (financial_status)
- **Key concern:** Shopify Payments payouts aggregate multiple orders into one payout — ERP needs line-level detail for proper reconciliation. A2X handles this specific problem well.

---

## 4. The "Last 10%" Problem

These edge cases consume disproportionate ERP integration effort — often 30–50% of total integration time. Scope them explicitly; never assume they're covered by standard connector flows.

1. **Order edits after submission** — Shopify `orders/edited` arrives separately; ERP must process amendments to already-created orders
2. **Partial fulfillments across locations** — Single Shopify order fulfilled from multiple POS locations or warehouses
3. **Complex return/exchange workflows** — Return item A, exchange for B, partial refund, restock to different location
4. **Gift cards crossing system boundaries** — Gift card purchased in Shopify, redeemed at POS, balanced tracked in ERP
5. **Tax recalculation on modified orders** — Shopify recalculates tax on order edits; ERP must receive updated tax lines
6. **Discount allocation across systems** — Shopify's discount distribution model may not match how ERP expects to receive discount data

---

## 5. ERP Integration Scope Protection Language

Use this in proposals and change orders when ERP is in scope:

> "ERP integration covers the standard data flows outlined in the architecture spec (orders, inventory, customers, fulfillment). Edge cases including order edits, partial multi-location fulfillments, and complex return/exchange flows are scoped as time-and-materials additions. Kaizen will flag each edge case when encountered and produce a change order estimate before proceeding."

This prevents ERP integration from becoming an open-ended scope item.
