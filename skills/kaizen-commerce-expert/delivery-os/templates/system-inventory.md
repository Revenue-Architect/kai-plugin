# Template — Current System Inventory

Completed by the CTO during the Blueprint or Shopify Referral intake. Captures the full current-state stack so the Engagement Baseline, migration lane, entity scope, and integration architecture rest on observed facts, not assumptions. Carries forward into Pack 2 (Migration) as the basis for the entity map.

**Legend:** `[CONFIRMED]` observed / vendor-confirmed · `[ASSUMPTION]` inferred · `[OPEN]` unverified

---

## 1. Point of sale

| Field | Value | Status |
|-------|-------|--------|
| POS system + version | | |
| Contract end / lock-in | | |
| Custom modifications / scripts | | |
| Export capability (API / CSV / DB) | | |
| Known data quality issues | | |
| Gift card / store credit system | | |

---

## 2. Ecommerce

| Field | Value | Status |
|-------|-------|--------|
| Platform (Shopify? plan level) | | |
| Theme + customizations | | |
| Existing store to migrate into, or build new? | | |
| Sales channels published | | |
| Apps installed (and data dependencies) | | |

---

## 3. Catalog data profile

| Entity | Count | Key quality (clean / dirty / dupes) | Status |
|--------|-------|--------------------------------------|--------|
| Products | | | |
| Variants | | | |
| Collections | | | |
| Customers | | | |
| Orders (history depth) | | | |
| Inventory records (by location) | | | |
| Metafields / metaobjects in use | | | |
| Discounts / promotions | | | |

---

## 4. Back-office / operational systems

| System | Purpose | Integration method today | Data owner |
|--------|---------|--------------------------|------------|
| ERP / accounting | | | |
| WMS / 3PL | | | |
| Reporting / BI | | | |
| Spreadsheets / manual tools | | | |

---

## 5. Integrations & data freshness

For each integration, name the source of truth and apply the kaizen-brain freshness defaults.

| Integration | A ↔ B | Direction | Update type (event / scheduled / reconcile) | Source of truth | Status |
|-------------|-------|-----------|---------------------------------------------|-----------------|--------|
| | | | | | |

Source-of-truth heuristics: origin of the business event → system used for reconciliation → cleanest keys → system finance trusts → declare split ownership explicitly if no single source is stable.

---

## 6. Hardware & payments

| Location | Terminals | Readers | Receipt printers | Processor | Region availability OK? |
|----------|-----------|---------|------------------|-----------|--------------------------|
| | | | | | |

---

## 7. Migration lane signals

Capture the signals; the lane decision itself lives in Pack 2's decision tree.

- API access available on source system? (clean export via API?)
- Volume per entity (drives batch vs event handling):
- Edge cases present (gift cards, B2B accounts, bundles, multi-currency):
- Anything that requires **current Shopify documentation verification** before committing: **[FLAG]**

**Indicative lane:** API-first (default) / Matrixify (fallback) / Admin CSV (fallback) — _reasoning:_

---

## 8. Risk inputs feeding the Engagement Baseline register

| Observed condition | Likelihood (1–3) | Impact (1–3) | Score | Severity |
|--------------------|------------------|--------------|-------|----------|
| | | | | |

---

*KaizenCommerce | kaizencommerce.ca | Internal — Confidential*
