# Template — Migration Entity & Field Map

Two zoom levels of the same artifact: the **entity map** (one row per in-scope entity) and the **field map** (one sheet per entity). Built by the CTO from the Pack 1 [system-inventory](system-inventory.md), governed by [Pack 2 — API-First Migration](../02-api-first-migration-package.md) §3–4. The lane may differ per entity; **API-first is the default** and every fallback needs a documented reason and CTO sign-off.

> Do not assume migratability or platform behavior for gift cards, store credit, metaobjects, or POS permissions, and never guess a Shopify target field name. Tag uncertainty `[FLAG: verify current Shopify docs before client commitment]`.

**Client:** ______  **Baseline date:** ______  **Data cap:** ______  **CTO sign-off:** ______

---

## Part A — Entity map (one row per entity)

| Entity | Source location | Shopify target | Lane (API / Matrixify / CSV) | Lane reason | Volume | Key / match field | Load-order dep | Flags |
|--------|-----------------|----------------|------------------------------|-------------|--------|-------------------|----------------|-------|
| Products | | | API (default) | | | | — | |
| Variants | | | API (default) | | | | after products | |
| Collections | | | API (default) | | | | after products | |
| Customers | | | API (default) | | | | — | |
| Orders | | | API (default) | | | | after customers | |
| Inventory | | | API (default) | | | | after variants + locations | |
| Locations | | | API (default) | | | | first | |
| Metafields | | | API (default) | | | | after parent record | `[FLAG: verify current Shopify docs before client commitment]` if behavior uncertain |
| Metaobjects | | | API (default) | | | | after dependencies | `[FLAG: verify current Shopify docs before client commitment]` |
| Gift cards / store credit | | | TBD | | | | — | `[FLAG: verify current Shopify docs before client commitment]` |
| Discounts / promotions | | | TBD | | | | — | if applicable |
| Staff / POS permissions | | | TBD | | | | — | `[FLAG: verify current Shopify docs before client commitment]` |

**Lane decision rule:** default API-first → choose Matrixify only with a clean structured bulk export and good entity support → choose Admin CSV only for small/simple entities or no-API one-time loads. Record the reason in the Lane reason column. Final lane is CTO/partner sign-off (see Pack 2 §1).

---

## Part B — Field map (copy one block per entity)

**Entity:** ______  **Lane:** API / Matrixify / Admin CSV  **Match / idempotency key:** ______

| Source field | Shopify target field | Transform (format/units/encoding) | Default if empty | Validation rule | Flag |
|--------------|----------------------|-----------------------------------|------------------|-----------------|------|
| | | | | | |
| | | | | | |

**Idempotency:** the match key above ensures a partial re-run updates rather than duplicates. Define it before any load. Never silently drop a field.

**Open decisions (fields with no clean target):**

| Field | Issue | Proposed handling | Owner | Status |
|-------|-------|-------------------|-------|--------|
| | | | | |

*KaizenCommerce | kaizencommerce.ca | Internal — Confidential*
