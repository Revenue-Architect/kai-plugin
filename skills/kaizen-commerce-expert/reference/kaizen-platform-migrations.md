---
name: kaizen-platform-migrations
description: Platform-specific migration patterns and data model notes for every source platform Kaizen encounters. Load when the legacy platform is identified and before running kaizen-dataprep or kaizen-migrate.
---

# Platform-Specific Migration Reference

Quick-load this file when the source platform is confirmed. Each section covers data model notes,
known export quirks, field mapping guidance, migration lane implications, and timeline add-ons.

KaizenCommerce is API-first by default. Use these platform notes to decide whether the lane should
remain `api_to_api`, switch to `matrixify_csv`, use `shopify_admin_csv`, or become `hybrid`.
Matrixify references in this file are fallback or entity-specific options, not the default lane.

For Square specifically, read [`kaizen-square-migration.md`](../skills/kaizen-square-migration.md) — it is the most complete platform skill and serves as the pattern all other sections follow.

---

## Lightspeed R-Series (Retail)

### Export Path
- Product export: Admin → Products → Export (CSV). Exports Item name, SKU, UPC, Price, Category, Supplier, Description, custom fields per item.
- Customer export: Admin → Customers → Export.
- Inventory: Per-location inventory export from Reporting or directly from product export.
- Sales history: Reporting module → Export (limited format).

### Data Model Notes

| Lightspeed Concept | Shopify Target | Notes |
|-------------------|---------------|-------|
| Item (parent) | Product | Handle derived from Item name |
| Item Variation | Variant | Options from variation attributes |
| Custom Field | Metafield | Map to appropriate namespace.key type |
| Category | Collection (automated rule) | Recreate as automated collection rule on tag |
| Supplier | Vendor | Direct map |
| UPC / EAN | Variant Barcode | Use as Barcode field; SKU stays as SKU |
| Price Tier (price books) | B2B Price List (any paid plan) or Shopify discount | Price tiers → B2B Price Lists if wholesale; not natively migrated for retail. More than 3 active catalogs needs Plus |

### Known Export Quirks
- Images are not in the CSV — require separate manual download or API pull.
- Lightspeed custom fields export with column names unique to the merchant's config — map manually.
- Archived/discontinued items are included in export; flag with `status = draft` or exclude.
- Inventory export includes all locations; separate into per-location files before import.

### Migration Mapping Path
- Default: API-first transformation into Shopify Admin API payloads, with Shopify Dev MCP used to
  verify current target operations before production use.
- Matrixify fallback:
- Products: `Handle` from Item name (slugify), `Title`, `Variant SKU`, `Variant Barcode`, `Variant Price`, `Vendor`, `Tags` from Category
- Customers: `Email`, `First Name`, `Last Name`, `Phone`, `Tags`, optional loyalty metafields
- Inventory: Per-location inventory adjustment post-product import

### Timeline Add-on: +0–1 weeks (clean export format, minor transformation complexity)

---

## Lightspeed X-Series (formerly Vend)

### Export Path
- Products: Admin → Products → Export. Column structure differs from R-Series.
- Customers: Admin → Customers → Export.
- Inventory: Separate inventory count export per location.

### Data Model Notes
Lightspeed X has a cleaner export than R-Series. Product handles, variants, and pricing are more
directly migration-compatible, whether the selected lane is API-first or Matrixify.

| X-Series Concept | Shopify Target | Notes |
|-----------------|---------------|-------|
| Product Name | Title / Handle | |
| Variant Name | Option values | |
| Tags | Tags | Direct map |
| Price | Variant Price | |
| Supply Price | Variant Cost | Map to Cost per item |
| Loyalty points | Metafield or loyalty app migration | No native Shopify equivalent; use third-party loyalty app |

### Timeline Add-on: +0 weeks (one of the cleaner legacy exports)

---

## Heartland Retail (Retail Management Hero / RMH)

### Export Path
- Products: CSV export from Item Manager. Columns include Item Code (SKU), Description, Category, UPC, Price, Cost, Vendor.
- Customers: Customer list export.
- Inventory: Per-location inventory report.

### Data Model Notes

| Heartland Concept | Shopify Target | Notes |
|-----------------|---------------|-------|
| Item Code | Variant SKU | |
| Description | Title | Handle derived from Description |
| Matrix Item (parent) | Product | Matrix items have sub-items (variants) |
| Sub-item | Variant | Matrix attribute values → option values |
| Category | Collection tag rule | |
| Vendor | Vendor | |
| UPC | Variant Barcode | |

### Known Export Quirks
- Matrix items export as separate rows with parent/sub-item relationship indicated by a flag column — requires grouping logic to reconstruct product/variant hierarchy.
- Images not in export.
- Custom fields vary by configuration.

### Timeline Add-on: +1 week (matrix item grouping logic)

---

## Clover POS

### Export Path
- Products: Clover Dashboard → Items → Export (CSV). Columns: Name, Price, SKU, Category, Enabled.
- Customers: Dashboard → Customers → Export.
- Orders/History: Dashboard → Reporting. Limited export options.
- Inventory: Items export includes current stock (single-location).

### Data Model Notes

| Clover Concept | Shopify Target | Notes |
|---------------|---------------|-------|
| Item | Product (or Variant if modifier-based) | Clover modifiers ≠ Shopify variants — requires classification |
| Modifier Group | Product options | Complex modifier groups may need manual restructuring |
| Category | Collection | |
| SKU | Variant SKU | |
| Label / Tag | Product tag | |

### Known Export Quirks
- Clover modifiers are more like options than variants — evaluate whether to model as Shopify variants or Shopify Functions-based customizations.
- Multi-location Clover requires per-device/per-location exports — time-consuming.
- Sales history export is limited; historical order import via Matrixify typically not practical.

### Timeline Add-on: +1–2 weeks (modifier classification + multi-location reconciliation)

---

## Revel Systems (iPad POS)

### Export Path
- Products: Back Office → Products → Export. Columns include Product Name, SKU, Price, Cost, Barcode, Category.
- Customers: Back Office → Customers → Export.
- Inventory: Per-location inventory export from reporting.

### Data Model Notes

| Revel Concept | Shopify Target | Notes |
|--------------|---------------|-------|
| Product | Product | |
| Modifier | Variant option or custom app | Same challenge as Clover — modifiers ≠ variants |
| Composite Product | Bundle | Shopify Bundles app or custom |
| Category | Collection | |
| Barcode | Variant Barcode | |
| Customer Display Name | Title | |

### Known Export Quirks
- Revel is common in restaurant/QSR — many merchants have menu items, not retail products. Validate catalog before assuming standard product migration.
- Composite products (combos, bundles) have no direct Shopify equivalent; model as bundle app or metafield relationships.
- Loyalty data is usually in a separate Revel Loyalty module — confirm scope.

### Timeline Add-on: +1–2 weeks (modifier classification; menu-vs-retail catalog validation)

---

## Teamwork Commerce

### Export Path
- Teamwork exports via Reporting module or direct database access for enterprise clients.
- Products: Style/SKU hierarchy export. Style = parent product, SKU = variant.
- Customers: Customer profile export.
- Inventory: Per-location inventory export.

### Data Model Notes

| Teamwork Concept | Shopify Target | Notes |
|-----------------|---------------|-------|
| Style | Product | Handle from Style name |
| SKU (child of Style) | Variant | Each SKU row becomes a variant row |
| Attribute (Color, Size, etc.) | Product Option | Up to 3 options natively |
| Department / Class / Vendor | Vendor, tags, collections | |
| UPC | Variant Barcode | |
| Cost | Variant Cost | |

### Known Export Quirks
- Teamwork is common in mid-market apparel and footwear — expect 3-option variant structures (Color / Size / Width).
- Merchants using Teamwork often have NetSuite or D365 — flag ERP integration in scope (see [`kaizen-erp-patterns.md`](kaizen-erp-patterns.md)).
- Teamwork uses an internal Style Number as product identifier — confirm whether to use as SKU or metafield.

### Timeline Add-on: +0–1 weeks (clean hierarchy, standard apparel structure)

---

## BigCommerce

### Data Model Notes

| BigCommerce Concept | Shopify Target | Notes |
|-------------------|---------------|-------|
| Product (simple) | Product with no variants | Direct map |
| Product (configurable with options) | Product + Variants | BC options → Shopify variant dimensions (max 3) |
| Product Modifiers | Custom via Functions or metafields | Not in standard export — requires BC API extraction |
| Category Tree | Collections (flat, rule-based) | Requires merchandising redesign |
| Customer Groups | Customer tags, B2B Price Lists | Group-based pricing → B2B Price Lists or Functions |
| Brand | Vendor | Direct map |
| Custom Fields | Metafields (typed) | Significant upgrade — plan mapping |

### Export / Migration Path
1. BC V3 API extraction where available → API-first Shopify payloads
2. BC CSV export for simple products and customers → Admin CSV or Matrixify fallback when lower-risk
3. BC V3 API extraction for modifiers and complex products → custom transformation → API-first payloads
4. Customer group pricing → B2B Price Lists or Shopify discount logic

### Known Export Quirks
- **Modifiers are not in standard CSV export** — must use BC API. This is the most common BigCommerce migration surprise.
- Category → Collection redesign is always a discovery conversation with the merchandising team.

### Timeline Add-on: +0–2 weeks (add 2 if heavy use of product modifiers)

---

## WooCommerce (WordPress)

### Export Path
- Products: WooCommerce → Products → Export (CSV). Columns include Name, SKU, Type, Price, Categories, Attributes, Images (URLs).
- Customers: WooCommerce → Customers → Export or WordPress Users export.
- Orders: WooCommerce → Orders → Export.

### Data Model Notes

| WooCommerce Concept | Shopify Target | Notes |
|--------------------|---------------|-------|
| Simple Product | Product (single variant) | |
| Variable Product | Product + Variants | Attribute sets → Option dimensions |
| Product Category | Collection | |
| Product Tag | Product tag | |
| SKU | Variant SKU | |
| External Product | N/A — remove or redirect | |
| Grouped Product | Metafield relationships or bundle app | |
| Customer (WordPress user) | Customer | Email is the merge key; passwords do not migrate |

### Known Export Quirks
- WooCommerce exports image URLs (not files) — images must be re-imported from those URLs or downloaded manually.
- Variable product attributes export as a single pipe-delimited string — requires parsing into separate option columns.
- Password hashes (wp-hashed) are incompatible with Shopify — must force password reset.
- Customer accounts in WooCommerce are WordPress Users — export via WP All Export or WooCommerce customer export; not the standard WP user export.

### Timeline Add-on: +1–2 weeks (image handling, attribute parsing)

---

## Shopify → Shopify (Store Consolidation or Replatform)

### When This Occurs
- Merchant acquired another brand; merging two Shopify stores
- Migrating from a Shopify Starter / Basic store to a new Plus store
- Moving from a partner-managed store to a merchant-owned store
- Regional stores being consolidated into a single Markets-based store

### Export Path
- Products: Shopify Admin export or Admin API pull. API-first for large stores or custom data.
- Customers: Shopify Admin export or Admin API pull. API-first when dedupe/retry reporting matters.
- Orders: Shopify Admin export, Admin API pull, or Matrixify historical orders when that lane is selected.
- Inventory: Export per location; adjust import targets per location on destination store.

### Data Model Notes

| Source Shopify Concept | Target Shopify | Notes |
|----------------------|---------------|-------|
| Product (all fields) | Product | Near-direct; check metafield definitions match on destination |
| Metafields | Metafields | Metafield definitions must exist on destination before import |
| Customers | Customers | Email is merge key; loyalty metafields need destination definitions |
| Historical orders | Historical orders | API-first or Matrixify lane; verify current contract before committing |
| Collections (manual) | Manual collections | Re-add membership after product import |
| Collections (automated) | Automated collections | Recreate rules — do not need product membership import |

### Known Quirks
- Product IDs change on destination store — any external system referencing Shopify product IDs must be updated.
- Metafield definitions must be created on destination store before metafield data is imported.
- Apps installed on source store must be reinstalled on destination — their data (loyalty points, reviews, subscriptions) may need separate migration.
- Gift card codes and balances must reconcile; verify current API/tooling lane before committing.

### Timeline Add-on: +0 weeks (source data is already Shopify-structured; fastest migration type)
