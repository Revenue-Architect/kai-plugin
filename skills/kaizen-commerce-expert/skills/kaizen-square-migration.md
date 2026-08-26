---
name: kaizen-square-migration
description: >
  KaizenCommerce Square → Shopify migration skill — the authoritative field-level reference for
  transforming Square POS product exports into API-first Shopify payloads, Matrixify-compatible
  import files when that lane is selected, or hybrid migration artifacts.
  Covers the complete transformation pipeline: variant classification, handle generation, SKU
  and barcode classification, title casing, body HTML cleaning, weight parsing, tax logic,
  metafield architecture, archived products, pipeline configuration hooks, known bugs with root
  causes and fixes, retroactive Shopify update workflows, pre-import QA checklist, and key
  lessons learned. Canonical examples drawn from the South Georgia Pecan Company (SGPC) Gift
  Shop migration (April 2026) using a specialty food retail dataset — patterns apply directly to
  any vertical: apparel, home goods, grocery, hardware, gifts, or general merchandise. Trigger
  on: "Square migration", "Square export", "Square to Shopify", "Square API migration", "Square to Matrixify",
  "transform Square CSV", "Square product import", "Square POS migration", any reference to
  a Square item library export or variation names, any Square field mapping question, any
  Matrixify import issue originating from a Square source file.
metadata_version: 1
layer: migration-execution
upstream: []
downstream: ["kaizen-dataprep", "kaizen-matrixify-exec", "kaizen-validate"]
adjacent: ["kaizen-shopify-migration"]
canon: []
owns: ["Square-specific migration transformation"]
does_not_own: ["Generic platform pricing, final QA signoff"]
---

# KaizenCommerce — Square → Shopify Migration Skill

**Pipeline position:** Plugs into the standard pipeline between **kaizen-dataprep** (audit) and
the selected execution lane. Use this skill as the Square-specific transformation reference
whenever a Square export or Square API payload is the source.

```
kaizen-dataprep (audit) → [SQUARE-MIGRATION] → kaizen-api-migration-exec or kaizen-matrixify-exec → kaizen-migrate (cutover)
```

> **Canonical source:** All examples, algorithms, and known bugs in this skill are derived from
> the SGPC (South Georgia Pecan Company) Gift Shop production migration, April 2026. SGPC is a
> specialty food retailer in the southeastern US — their Square catalog included bulk goods sold
> by weight, flavor-variant confections, and promotional clearance SKUs. The patterns generalize
> across any industry where Square is the source system. Where a retail-specific example is used,
> a generalized equivalent is noted.

<role>
You are a senior migration engineer for KaizenCommerce who has executed Square → Shopify
migrations across multiple verticals. You know Square's export quirks by heart — the Flavor
column fallback, the multi-location inventory columns, the non-barcode SKUs, the # unit
shorthand. You know the silent failure modes Square data can trigger in API payloads and
Matrixify files. You do not produce templates — you produce transformation logic precise enough
to run in production after Shopify Dev MCP validation.
</role>

<goal>
When invoked alongside a Square export, produce:
1. Correct variant classification for every product group in the source file
2. Handles, titles, option names, and values per the rules in this skill
3. SKU and barcode assignments per the classification table
4. API payload fields or Matrixify metafield column headers at the correct level
5. A pipeline configuration block (MANUAL_GROUPS, DELETE_ITEM_NAMES, KEEP_FIRST_ONLY) for
   any items requiring non-standard handling
6. A bug-aware QA pass confirming none of the known failure modes are present in the output
</goal>

---

## 1. SOURCE DATA OVERVIEW

### Square Export Columns Used

| Square Column | Description | Notes |
|---|---|---|
| `Item Name` | Product group identifier | Shared by all variants of the same product |
| `Variation Name` | Primary variant identifier | Size, type, etc.; takes priority over Flavor |
| `Flavor` | Fallback variant identifier | Only used when Variation Name is blank |
| `SKU` | May or may not be a scannable barcode | Run through `clearly_not_barcode` check |
| `GTIN` | Global Trade Item Number | Use as Variant Barcode when GTIN ≠ SKU |
| `Token` | Square's unique internal row identifier | Critical traceability canary — every row has a unique Token |
| `Archived` | Y/N flag | Separate into two pipeline outputs: active + archived |
| `Price` | Variant price | |
| `Weight (lb)` | Variant weight | Cross-check against option value string |
| `Current Quantity [Location]` | On-hand inventory by location | Column name varies by store/location name |
| `Tax - [Tax Name]` | One column per tax rule; value = 'Y' or blank | May be multiple tax columns per export |
| `Description` | Product description text | Clean before writing to Body HTML |
| `Default Vendor Name` | Supplier/vendor name | Maps to Shopify Vendor field |
| `Default Vendor Code` | Supplier item code | Store as metafield |
| `Reporting Category` | Square reporting category | Store as metafield |
| `Extracted Dimensions` | Physical dimensions | Store as metafield |

**Source data rules:**
- Square CSV exported from Square Dashboard → Items → Export Items
- Active and archived items may be in a single export (split using the `Archived` column) or separate exports
- Do NOT modify the source CSV — treat it as read-only
- Column names for inventory (`Current Quantity [Location]`) vary by store name — check the exact header in the export

---

## 2. TARGET FILE / PAYLOAD ARCHITECTURE

Default to API-first outputs unless Kai selected `matrixify_csv` or `hybrid`.

**API-first output:** normalize each Square row into a staging record with `source_row_id`,
`entity_type`, `idempotency_key`, `shopify_operation`, `payload`, `validation_status`, and
`blocker_reason`. Shopify operation names and payload shapes must be verified through Shopify Dev
MCP before production use.

**Matrixify output:** use the file architecture below only when Matrixify is the selected lane.

### 2.1 Column Structure

**Active products file — 31 columns:**
```
Handle
Title
Body HTML
Vendor
Type
Tags
Published
Published Scope
Option1 Name
Option1 Value
Option2 Name
Option2 Value
Variant SKU
Variant Barcode
Variant Price
Variant Taxable
Variant Requires Shipping
Variant Weight
Variant Weight Unit
Variant Inventory Qty
Variant Inventory Policy
Variant Inventory Tracker
Metafield: custom.square_original_item_name [single_line_text_field]
Metafield: custom.square_description_raw [multi_line_text_field]
Metafield: custom.square_vendor_code [single_line_text_field]
Metafield: custom.square_reporting_category [single_line_text_field]
Metafield: custom.square_dimensions [single_line_text_field]
Variant Metafield: custom.square_token [single_line_text_field]
Variant Metafield: custom.square_original_variation_name [single_line_text_field]
Variant Metafield: custom.square_original_sku [single_line_text_field]
Variant Metafield: custom.square_variant_description [multi_line_text_field]
```

**Archived products file — 32 columns:** Same as above, plus `Status` column inserted after `Published Scope`.

**DELETE file — 2 columns:** `Handle` + `Command` (value: `DELETE`)

### 2.2 Critical Matrixify Row Rules

These are the most common sources of silent import failures. Every row of every Square output
file must satisfy all of them.

| Rule | Column(s) | Behaviour |
|---|---|---|
| **Handle** — shared by all rows of the same product | `Handle` | All variant rows MUST share exactly the same Handle string |
| **Body HTML** — first row of Handle group ONLY | `Body HTML` | Populate on row 1; leave blank on all subsequent rows |
| **Repeat on every row** | `Title`, `Vendor`, `Tags`, `Option1 Name` | These are the opposite of Body HTML — repeat on every variant row |
| **Product-level metafields** — first row only | `Metafield: custom.*` | Only the first row's value per Handle is saved; subsequent rows silently dropped |
| **Variant-level metafields** — every row | `Variant Metafield: custom.*` | Each row saves its own value independently |
| **DELETE command** | `Command` = `DELETE` | Removes the product with that Handle from Shopify |
| **Metafield type annotation** | Column header format | Must include `[type]` in the column name |

---

## 3. COMPLETE FIELD MAPPING

| Square Column | → | Matrixify Column | Transformation |
|---|---|---|---|
| `Item Name` | → | `Handle` | Slugify (see §4) |
| `Item Name` | → | `Title` | `title_case_smart()` (see §7.1) |
| `Item Name` (raw) | → | `Metafield: custom.square_original_item_name` | Preserve original Square casing |
| `Description` | → | `Body HTML` | `clean_body_html()` — first row only (see §7.3) |
| `Description` (raw) | → | `Metafield: custom.square_description_raw` | Preserve raw text |
| `Default Vendor Name` | → | `Vendor` | Direct copy |
| `Default Vendor Code` | → | `Metafield: custom.square_vendor_code` | Product-level |
| `Reporting Category` | → | `Metafield: custom.square_reporting_category` | Product-level |
| `Extracted Dimensions` | → | `Metafield: custom.square_dimensions` | Product-level |
| `Variation Name` or `Flavor` | → | `Option1 Value` | Variation Name takes priority; fall back to Flavor |
| `Variation Name` or `Flavor` (raw) | → | `Variant Metafield: custom.square_original_variation_name` | Preserve original casing |
| `SKU` (if clean barcode) | → | `Variant SKU` + `Variant Barcode` | See §6 |
| `SKU` (if not barcode) | → | `Variant Metafield: custom.square_original_sku` | Move to metafield; leave SKU/Barcode blank |
| `GTIN` (when ≠ SKU) | → | `Variant Barcode` | Use GTIN as barcode, SKU as Variant SKU |
| `Token` | → | `Variant Metafield: custom.square_token` | Variant-level; preserve exactly |
| `Price` | → | `Variant Price` | Direct copy |
| `Weight (lb)` | → | `Variant Weight` + `Variant Weight Unit` = `lb` | Parse float; cross-check with option string (see §7.4) |
| `Current Quantity [Location]` | → | `Variant Inventory Qty` | Direct copy |
| `Tax - *` any = 'Y' | → | `Variant Taxable` = `TRUE` | FALSE if all tax columns are blank/N (see §7.5) |
| *(always)* | → | `Variant Requires Shipping` = `False` | POS-only store; evaluate per-project if omnichannel |
| *(always)* | → | `Variant Inventory Policy` = `deny` | Block oversell |
| *(always)* | → | `Variant Inventory Tracker` = `shopify` | Enable tracking |
| *(always)* | → | `Published` = `TRUE` | Active products |
| *(always)* | → | `Published Scope` | See §9 for POS-only vs. omnichannel conditional |

---

## 4. HANDLE GENERATION RULES

### Slugification Algorithm

```python
import re
import unicodedata

def slugify(text):
    text = text.lower()
    text = text.replace('&', 'and')
    text = unicodedata.normalize('NFKD', text)
    text = re.sub(r'[^\w\s-]', '', text)      # remove non-alphanumeric (keeps hyphens)
    text = re.sub(r'[\s_-]+', '-', text)       # collapse whitespace/underscores to hyphen
    text = text.strip('-')
    return text
```

### Handle Rules

- **Build handle from Item Name ONLY** — never append Variation Name, Flavor, or SKU
  - ❌ Bad: `bulk-almonds-milk-chocolate-24-16-chocolate-almonds`
  - ✅ Good: `bulk-almonds-milk-chocolate` (variants carry this through Option1 Value)
  - **Generalized example:** `mens-wool-blazer` not `mens-wool-blazer-navy-42r`
- **Active products:** `handle = slugify(Item Name)`
- **Archived products with handle conflict:** append `-arch` suffix
- **True duplicate products** (same Item Name, distinct entries): append `-2`, `-3`, etc.
- Handles must be unique across the **entire output file** — run a distinct count before delivery

---

## 5. PRODUCT GROUPING & VARIANT CLASSIFICATION

### Step 1: Group Rows by Item Name
All Square rows with the same `Item Name` belong to the same potential Shopify product.

### Step 2: Classify Each Group

| Classification | Condition | Shopify Structure | Option1 Name |
|---|---|---|---|
| `standalone` | 1 row only | Single-variant product | `Title` (default) |
| `true_duplicate` | Multiple rows, identical Variation Name AND Flavor | Separate products, handle -2/-3 suffixes | — |
| `flavor_variant` | Multiple rows, different Flavor values, Variation Name blank | One product, variants by flavor | `Flavor` |
| `bulk_size_variant` | Item Name contains a bulk-type keyword (e.g., `BULK`); Variation Name has size info | One product, variants by size | `Size` |
| `mixed_size_variant` | Variation Name or Item Name contains weight/volume size patterns (OZ/LBS/# or similar) | One product, variants by size | `Size` |
| `mixed_type_variant` | Variation Name has non-size differences (type, grade, style) | One product, variants by type | `Type` or `Variation` |

> **Adapt `bulk_size_variant` keywords to the vertical:** specialty food uses `BULK`; apparel
> might use `CASE` or `ASSORTED`; hardware might use `KIT`. Configure per project.

### ⚠️ Classification Order — Promo Keywords Check First

**Before checking size patterns, check for promotional keywords in Variation Name:**
- Default keywords: `SALE`, `CLOSE OUT`, `CLEARANCE`, `DISCOUNT`, `EVENT`
- If ANY promo keyword is present → classify as `mixed_type_variant` regardless of size patterns
- Reason: `"25# SALE"` is a sale variant, not a size variant
- **Add project-specific keywords** as needed (e.g., `SAMPLE`, `TESTER`, `DEMO` for other verticals)

```python
PROMO_KEYWORDS = {'SALE', 'CLOSE OUT', 'CLEARANCE', 'DISCOUNT', 'EVENT'}

def classify_group(group_df):
    # STEP 1: Check promo keywords FIRST
    variation_values = group_df['Variation Name'].dropna().str.upper()
    for val in variation_values:
        if any(kw in val for kw in PROMO_KEYWORDS):
            return 'mixed_type_variant'
    # STEP 2: Then check size patterns, flavor, etc.
    ...
```

### Step 3: Handle MANUAL_GROUPS Before Regular Processing

Use `MANUAL_GROUPS` when products have **different Item Names in Square** but should be **one
Shopify product**. This is common when a product was entered as separate SKUs in Square rather
than as variants.

**Canonical example (SGPC — specialty food):**
```python
# SGPC: Pecan halves were entered as two separate Square items by bag size
MANUAL_GROUPS = [
    {
        'handle': 'pecan-halves',
        'title': 'Pecan Halves',
        'option_name': 'Size',
        'items': [
            ('PECAN HALVES SMALL', '1 lb'),
            ('PECAN HALVES LARGE', '5 lbs'),
        ]
    }
]
```

**Generalized patterns by vertical:**
```python
# Apparel: colour/size matrix entered as separate Square items
MANUAL_GROUPS = [
    {
        'handle': 'canvas-tote-bag',
        'title': 'Canvas Tote Bag',
        'option_name': 'Size',
        'items': [
            ('CANVAS TOTE SMALL', 'Small'),
            ('CANVAS TOTE LARGE', 'Large'),
        ]
    }
]

# Hardware / home goods: pack sizes entered separately
MANUAL_GROUPS = [
    {
        'handle': 'wood-screws-stainless',
        'title': 'Wood Screws Stainless Steel',
        'option_name': 'Pack Size',
        'items': [
            ('WOOD SCREWS SS 50PK', '50 Pack'),
            ('WOOD SCREWS SS 100PK', '100 Pack'),
            ('WOOD SCREWS SS 500PK', '500 Pack'),
        ]
    }
]
```

**Processing order:**
1. Process `MANUAL_GROUPS` first — build rows, add Item Names to `manual_item_names` set
2. Run regular `groupby(Item Name)` loop — skip items in `manual_item_names`

---

## 6. SKU & BARCODE CLASSIFICATION

### The `clearly_not_barcode` Rule

Run every SKU through this check before assigning to Variant SKU / Barcode fields.

| Condition | Variant SKU | Variant Barcode | `square_original_sku` metafield |
|---|---|---|---|
| SKU contains **space** or **`/`** | *(blank)* | *(blank)* | Original SKU value |
| SKU is clean AND GTIN exists AND GTIN ≠ SKU | SKU | GTIN | *(blank)* |
| SKU is clean AND no GTIN | SKU | SKU | *(blank)* |
| SKU is clean AND GTIN = SKU | SKU | SKU | *(blank)* |
| No SKU at all | *(blank)* | *(blank)* | *(blank)* |

**Examples of SKUs that fail the `clearly_not_barcode` check:**
- `PECAN 1LB / BULK` — contains `/`
- `MILK CHOC ALMONDS XL` — contains spaces
- `ITEM 2024-004` — contains space (adjust pattern to your client's SKU conventions)

**Why this matters for POS:**
- At POS checkout, barcode scanners match against `Variant Barcode`
- A non-scannable value in `Variant Barcode` causes scanner lookup failures
- Duplicate barcodes across variants of the same product → Shopify cannot determine which variant to ring up
- Duplicate barcodes across different products → **flag to client; do not silently resolve**

---

## 7. TRANSFORMATION RULES BY FIELD

### 7.1 Title Casing — `title_case_smart()`

```python
MINOR_WORDS = {
    'a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor',
    'on', 'at', 'to', 'by', 'up', 'in', 'of', 'as', 'is', 'it'
}
UNIT_ABBREVS = {'lb', 'lbs', 'oz', 'kg', 'g', 'ml', 'fl'}

def title_case_smart(text):
    words = text.split()
    result = []
    for i, word in enumerate(words):
        lower = word.lower()
        if lower in UNIT_ABBREVS:
            result.append(lower)          # always lowercase — "25 lbs" not "25 Lbs"
        elif i == 0:
            result.append(word.capitalize())  # always capitalize first word
        elif lower in MINOR_WORDS:
            result.append(lower)
        else:
            result.append(word.capitalize())
    return ' '.join(result)
```

> **Adapt `UNIT_ABBREVS` by vertical:** food/grocery uses `lb`, `oz`, `ml`; fabric/textiles
> adds `yd`, `m`; lumber adds `ft`, `in`. Add project-specific units before running.

### 7.2 Pound-Sign Unit Conversion

Convert Square's pound shorthand (`#`) to spelled-out units **before** title casing.

| Input | Output | Rule |
|---|---|---|
| `1#` | `1 lb` | Value ≤ 1 → singular `lb` |
| `2#` | `2 lbs` | Value > 1 → plural `lbs` |
| `25#` | `25 lbs` | |
| `OZ` | `oz` | Uppercase unit normalization |
| `LBS` | `lbs` | |
| `LB` | `lb` | |

**⚠️ Regex pitfall — `\b` fails after `#`:**
```python
# WRONG — \b after # never matches because # is a non-word character
re.sub(r'\b(\d+)\s*#\b', ...)   # will NOT match "25#"

# CORRECT — drop trailing \b, or use lookahead
re.sub(r'\b(\d+)\s*#(?=\s|$|-|,)', ...)   # works correctly
```

> **Applies beyond food:** any vertical where Square uses `#` shorthand (e.g., wire gauge in
> electrical supply: `12#` wire) benefits from this conversion.

### 7.3 Body HTML Cleaning — `clean_body_html()`

Filter lines from the Square description before writing to Body HTML:
- **Keep** lines with ≥ 4 words
- **Keep** lines with ≥ 20 characters that contain at least one letter and one space
- **Strip** single-word lines, noise text, stray punctuation lines

```python
def clean_body_html(text):
    if not text:
        return ''
    lines = str(text).splitlines()
    cleaned = []
    for line in lines:
        line = line.strip()
        words = line.split()
        has_letter = bool(re.search(r'[a-zA-Z]', line))
        has_space = ' ' in line
        if len(words) >= 4 or (len(line) >= 20 and has_letter and has_space):
            cleaned.append(line)
    return '\n'.join(cleaned).strip()
```

### 7.4 Weight Parsing

- **Primary source:** `Weight (lb)` column → parse as float
- **Secondary:** attempt to extract weight value from Option1 Value string (e.g., `"25 lbs"` → 25.0)
- If both sources produce a value and they are within 10% of each other → use option-parsed value
- If they diverge by more than 10% → use the `Weight (lb)` column value, log the discrepancy
- `Variant Weight Unit` = `lb` always (Square exports in lbs)

> **For non-weight verticals:** if product weight is irrelevant (e.g., digital goods, services),
> leave `Variant Weight` and `Variant Weight Unit` blank — do not fill with zero.

### 7.5 Taxable Determination

Square exports one column per tax rule. A variant is taxable if **any** tax column = `'Y'`.

```python
# Adapt TAX_COLUMNS to exact column names in the client's Square export
TAX_COLUMNS = [
    'Tax - Georgia State and Local Tax (8%)',
    'Tax - Sales Tax-State (4%)',
    'Tax - Sales Tax1 (4%)'
]

def is_taxable(row):
    return any(str(row.get(col, '')).strip().upper() == 'Y' for col in TAX_COLUMNS)
```

- `Variant Taxable` = `TRUE` if ANY tax column = `Y`
- Default = `FALSE`
- **Check the export header row** to get exact column names — they vary by Square account settings

### 7.6 Traceability Metafields — Preserve Original Casing

These metafields store the **original Square values, not cleaned versions**, for audit purposes:
- `square_original_item_name` → e.g., `PECAN HALVES - BULK 25#` (not `Pecan Halves - Bulk 25 lbs`)
- `square_original_variation_name` → e.g., `SCOTCH OATMEAL COOKIES` (not `Scotch Oatmeal Cookies`)
- `square_original_sku` → original SKU before barcode classification
- `square_token` → exact Token value from Square row

---

## 8. METAFIELD ARCHITECTURE

### The Core Rule: Product-Level vs. Variant-Level

**Ask yourself for every metafield: "Is this value the same for ALL variants of the product, or unique per variant?"**

Using `Metafield:` when you need `Variant Metafield:` is the most damaging silent failure in the
pipeline. Shopify saves only ONE value per product for product-level metafields — all other rows'
values are silently dropped.

| Metafield Key | Level | Prefix | Type | Reason |
|---|---|---|---|---|
| `custom.square_original_item_name` | **Product** | `Metafield:` | `single_line_text_field` | Same Item Name across all variants |
| `custom.square_description_raw` | **Product** | `Metafield:` | `multi_line_text_field` | Product-level description |
| `custom.square_vendor_code` | **Product** | `Metafield:` | `single_line_text_field` | Same vendor code across variants |
| `custom.square_reporting_category` | **Product** | `Metafield:` | `single_line_text_field` | Category is product-level |
| `custom.square_dimensions` | **Product** | `Metafield:` | `single_line_text_field` | Same dimensions across variants |
| `custom.square_token` | **Variant** | `Variant Metafield:` | `single_line_text_field` | Every Square row has a unique Token |
| `custom.square_original_variation_name` | **Variant** | `Variant Metafield:` | `single_line_text_field` | Each variant has its own name |
| `custom.square_original_sku` | **Variant** | `Variant Metafield:` | `single_line_text_field` | SKU is per-variant |
| `custom.square_variant_description` | **Variant** | `Variant Metafield:` | `multi_line_text_field` | Variant-specific description text |

### Exact Column Header Format
Include the type annotation in brackets — Matrixify requires it:
```
Metafield: custom.square_original_item_name [single_line_text_field]
Variant Metafield: custom.square_token [single_line_text_field]
Variant Metafield: custom.square_variant_description [multi_line_text_field]
```

### Adding Project-Specific Metafields

For any additional Square fields unique to the client:
1. Decide: product-level or variant-level? (see rule above)
2. Assign to `custom.square_[field_name]` namespace to keep all Square traceability fields grouped
3. Add the column to the correct position in the output file
4. Create the Shopify metafield definition **before the first import** (see §15)

---

## 9. STATIC FIELD VALUES

### POS-Only vs. Omnichannel Conditional

**`Published Scope` depends on the store configuration:**

| Store Type | `Published Scope` | Reason |
|---|---|---|
| **POS-only** (no online storefront) | `web` | Shopify uses `web` as the internal published state for POS-only stores |
| **Omnichannel** (POS + online store) | `global` | Makes products visible in both POS and online channels |

> ⚠️ **Check the client's Shopify setup before generating files.** Using `global` on a POS-only
> store is harmless but inconsistent. Using `web` on an omnichannel store may hide products
> from the online channel.

### All Static Values for POS-Only Stores

| Column | Value | Reason |
|---|---|---|
| `Variant Requires Shipping` | `False` | No fulfilment; in-store pickup only |
| `Variant Inventory Policy` | `deny` | Block oversell at POS |
| `Variant Inventory Tracker` | `shopify` | Enable Shopify inventory tracking |
| `Published` (active) | `TRUE` | Visible and sellable in POS |
| `Published Scope` | `web` | POS-only stores (see table above) |
| `Type` | *(blank or per config)* | Optional; populate if client uses Shopify product types |
| `Tags` | *(blank or per config)* | Optional; can be derived from Reporting Category |

**If the store has an online storefront:** Change `Published Scope` to `global` and evaluate
`Variant Requires Shipping` per-product (physical goods ship; services do not).

---

## 10. ARCHIVED PRODUCTS HANDLING

Archived products require a separate pipeline output file.

### Differences from Active Products

| Setting | Active | Archived |
|---|---|---|
| `Status` column | *(absent)* | `archived` |
| `Published` | `TRUE` | `FALSE` |
| `Published Scope` | `web` (or `global`) | `web` (or `global`) |
| Handle conflict with active product | — | Append `-arch` suffix |
| File | Active Products file | Separate Archived Products file |

### Filtering
- Filter rows where Square `Archived` column = `'Y'` → archived pipeline
- Filter rows where Square `Archived` column ≠ `'Y'` (blank or `'N'`) → active pipeline
- Process each independently; they share handle-generation logic but differ in output settings

---

## 11. PIPELINE CONFIGURATION HOOKS

Add these blocks at the top of the pipeline script for project-specific overrides.
Document the reason for each entry inline.

### `MANUAL_GROUPS`
Products with different Item Names in Square that should be ONE Shopify product:
```python
MANUAL_GROUPS = [
    {
        'handle': 'product-handle',          # generated slug for the unified product
        'title': 'Product Title',            # clean display title
        'option_name': 'Size',               # or 'Flavor', 'Style', 'Pack Size', etc.
        'items': [
            ('EXACT SQUARE ITEM NAME 1', 'Option Value 1'),
            ('EXACT SQUARE ITEM NAME 2', 'Option Value 2'),
        ]
    }
]
```

### `DELETE_ITEM_NAMES`
Item Names to exclude entirely from the output:
```python
DELETE_ITEM_NAMES = {
    'ITEM NAME TO EXCLUDE',   # Reason: client discontinued before migration
}
```

### `KEEP_FIRST_ONLY`
Item Names where only the first matching row is kept (deduplication):
```python
KEEP_FIRST_ONLY = {
    'EXACT DUPLICATE ITEM NAME',   # Reason: exact duplicate entry in Square catalog
}
```

### Processing Order
1. Apply `DELETE_ITEM_NAMES` filter — exclude entirely
2. Apply `KEEP_FIRST_ONLY` filter — deduplicate
3. Process `MANUAL_GROUPS` — build cross-item products, add handles to `manual_item_names` set
4. Run regular `groupby(Item Name)` loop — skip items in `manual_item_names`

---

## 12. KNOWN BUGS & ROOT CAUSES

These bugs were identified and resolved during the SGPC production migration. They are
structural — they will appear in any Square pipeline that follows the same patterns.

---

### BUG 1 — source_row Collapse in Flavor/Variant Products ⚠️ HIGH IMPACT

**Symptom:** All variants of a multi-variant product have identical Variant SKU, Variant Barcode,
and `square_token` — all matching the LAST row's values from the Square group.

**Root cause:** The pipeline passed a cached `source_row` variable (updated in a previous loop
or set outside the inner loop) instead of the current iteration's row.

**Detection:** Check if all variants of any multi-variant product share the same `square_token`.
Since every Square row has a unique Token, identical Tokens across variants = instant indicator.

**Matrixify warning:** `"Variant SKU unusable as an index, because there are duplicates: [XXXXXXXX]"`

**Fix:**
```python
# WRONG
source_row = group_df.iloc[-1]            # last row cached outside inner loop
for _, row in group_df.iterrows():
    build_row(source_row, option_value=row['Flavor'])  # always uses last row

# CORRECT
for _, row in group_df.iterrows():
    build_row(row, option_value=row['Flavor'])         # uses current row
```

**Edge case — mixed NaN/flavor rows:**
Square sometimes has one row with NaN Flavor (standalone, no SKU) + N rows with Flavor values.
The pipeline may split these into a standalone product + a multi-variant product. After fixing
the multi-variant SKUs, check that the standalone's SKU is independently correct and is not a
cross-product barcode duplicate.

---

### BUG 2 — Missing `square_original_variation_name` for Flavor Products

**Symptom:** `square_original_variation_name` metafield is blank for all `flavor_variant`
products, even though Flavor values exist in Square.

**Root cause:** Same source_row collapse as Bug 1. The Flavor fallback code
`if not orig_var: orig_var = row.get('Flavor', '')` never fired because `row` was always
the last row (which had a Variation Name, so no fallback triggered).

**Also affects:** Single-variant products where Variation Name is blank — correct SKUs
(no collapse, only 1 row) but may still be missing the variation name metafield.

**Fix:** After fixing Bug 1, ensure the fallback explicitly checks both Variation Name and Flavor
columns and uses the raw original value (preserving original casing).

---

### BUG 3 — Metafield Level Mismatch (Product vs. Variant) ⚠️ HIGH IMPACT

**Symptom:** In Shopify Admin, multi-variant products only show metafields for the first variant.
All other variants appear to have no metafield data.

**Root cause:** Per-variant fields were imported with `Metafield:` prefix instead of
`Variant Metafield:`. Shopify stores only one value per product — only the first row's value survives.

**Silent failure:** Matrixify does NOT warn about this. Import reports OK. The data loss is
only visible by inspecting variant metafields in Shopify Admin after import.

**Recovery procedure:**
1. Shopify Admin → Settings → Custom data → Products → delete affected field definitions
   **WITH saved values** (not "Delete field only" — that leaves orphaned data)
2. Go to Settings → Custom data → Variants → create new definitions there
3. Update column headers in all import files: `Metafield:` → `Variant Metafield:`
4. Re-import

**Prevention:** Design metafield object types (product vs. variant) before the first import.
Changing this retroactively is a 3-step recovery.

---

### BUG 4 — Regex `\b` Fails After `#`

**Symptom:** Unit conversion pattern `r'\b(\d+)\s*#\b'` never matches strings like `"25#"`.

**Root cause:** `\b` is a zero-width word boundary assertion requiring one side to be `[\w]`
and the other `[^\w]`. Since `#` is `[^\w]`, `\b` after `#` requires a word character to
follow — which is often not the case at end-of-string, before a space, or before punctuation.

**Fix:**
```python
# WRONG
re.sub(r'\b(\d+)\s*#\b', replace_fn, text)

# CORRECT — drop trailing \b
re.sub(r'\b(\d+)\s*#', replace_fn, text)

# CORRECT — use positive lookahead for safety
re.sub(r'\b(\d+)\s*#(?=\s|$|-|,)', replace_fn, text)
```

---

### BUG 5 — Unit Abbreviations Capitalized in Titles

**Symptom:** Product titles show `"1 Lb"` instead of `"1 lb"`, `"25 Oz"` instead of `"25 oz"`.

**Root cause:** `title_case_smart()` didn't include unit abbreviations in its `MINOR_WORDS` set,
so they were capitalized like regular words.

**Fix:** Include `'lb', 'lbs', 'oz', 'kg', 'g', 'ml', 'fl'` in the `UNIT_ABBREVS` exception
set in `title_case_smart()`. These always render lowercase.

---

### BUG 6 — Duplicate Metafield Definition at Wrong Level

**Symptom:** Shopify shows a metafield key (e.g. `square_original_variation_name`) appearing
twice in product metafield definitions — once at product level, once at variant level — with
different record counts.

**Root cause:** When creating the new variant-level definition, the same key was accidentally
also created at the product level, creating a duplicate alongside the existing product-level def.

**Fix:** Delete BOTH instances from the product level (with saved values on both), then keep
only the single variant-level definition.

---

## 13. SQUARE CSV PATTERNS QUICK REFERENCE

| Pattern Observed | How to Handle |
|---|---|
| Flavor column present, Variation Name blank | `flavor_variant` — use Flavor as Option1 Value |
| Variation Name present (even if Flavor also present) | Use Variation Name (takes priority over Flavor) |
| Both Flavor AND Variation Name blank, multiple rows | `true_duplicate` — assign handle suffixes -2, -3 |
| SKU contains space or `/` | `clearly_not_barcode` → move to `square_original_sku` metafield; leave SKU/Barcode blank |
| GTIN ≠ SKU | Use GTIN as `Variant Barcode`; keep SKU as `Variant SKU` |
| GTIN = SKU | Use SKU for both fields |
| Variation Name contains SALE / CLOSE OUT / CLEARANCE / DISCOUNT / EVENT | `mixed_type_variant` — check promo keywords BEFORE size patterns |
| Variation Name contains OZ / LBS / # (without promo keywords) | `mixed_size_variant` or `bulk_size_variant` |
| Item Name contains `BULK` (or vertical equivalent) | `bulk_size_variant` — group by Item Name, variants by size |
| Multiple rows, identical Item Name, no Variation/Flavor difference | `true_duplicate` — separate handles with -2, -3 |
| Item Name contains `#` unit (e.g. `25#`) | Convert: `1#` → `1 lb`, `25#` → `25 lbs` |
| All variants of a product share the same Token | **source_row collapse bug** — fix pipeline before re-running |
| Same SKU/barcode on two different products | Flag to client — do not silently resolve cross-product barcode conflicts |
| NaN Flavor row mixed with Flavor rows (same Item Name) | Split into standalone (NaN) + multi-variant (Flavors); verify standalone SKU independently |

---

## 14. MATRIXIFY IMPORT WARNING REFERENCE

| Warning Message | Meaning | Action Required |
|---|---|---|
| `"Tags Command is empty — assumed as MERGE"` | No `Tags Command` column; defaulted to merge mode | None — always present, always harmless |
| `"Variant Command is empty — assumed as MERGE"` | No `Variant Command` column; defaulted to merge | None — always present, always harmless |
| `"Variants updated by SKU: N"` | N variants matched by their unique SKU ✅ | None — this is the ideal, clean state |
| `"Variants updated by Options: N"` | Matrixify couldn't match by SKU; fell back to Option values | Investigate if unexpected; harmless when some variants intentionally have no SKU |
| `"Variants updated by Barcode: N"` | Matched variants by barcode | None — acceptable fallback |
| `"Variant SKU unusable — empty values"` | Some variants have no SKU | Expected when variants intentionally have no barcode; harmless if intentional |
| `"Variant SKU unusable — duplicates: [XXXXXX]"` | Multiple variants share the same SKU value | ⚠️ **Data bug** — source_row collapse likely; fix pipeline |
| `Import Result = OK` | Row processed successfully | No action needed |
| `Import Result = Error / Failed` | Row was not imported | Investigate immediately |

### Warning Progression Across Multiple Uploads

When iteratively fixing data already live in Shopify:

| Upload Sequence | Expected Warnings | Why |
|---|---|---|
| First upload (bad SKUs from pipeline bug) | Many "by Options" + duplicate warnings | SKU data is collapsed |
| Fix file upload (correcting SKUs) | Still "by Options" + duplicate warnings | Matrixify reads current Shopify state before updating — old duplicates still there |
| Re-upload of corrected main file | "by Options" — but update goes through correctly | Matrixify updated data in previous step; warning reflects pre-update read |
| Final upload (after metafield fixes) | Majority "by SKU", zero duplicate warnings ✅ | Clean state achieved |

**Key insight:** "Variants updated by Options" on a re-upload after a fix is expected behavior,
not a sign the fix failed. Matrixify reads the Shopify state before it begins updating, so it
sees old duplicates. The actual write still succeeds.

---

## 15. SHOPIFY METAFIELD SETUP

Configure these in Shopify Admin → Settings → Custom data **before the first import**.

### Product-Level Definitions (Settings → Custom data → Products)

| Display Name | Namespace & Key | Type |
|---|---|---|
| Square Original Item Name | `custom.square_original_item_name` | Single line text |
| Square Description Raw | `custom.square_description_raw` | Multi-line text |
| Square Vendor Code | `custom.square_vendor_code` | Single line text |
| Square Reporting Category | `custom.square_reporting_category` | Single line text |
| Square Dimensions | `custom.square_dimensions` | Single line text |

### Variant-Level Definitions (Settings → Custom data → Variants)

| Display Name | Namespace & Key | Type |
|---|---|---|
| Square Token | `custom.square_token` | Single line text |
| Square Original Variation Name | `custom.square_original_variation_name` | Single line text |
| Square Original SKU | `custom.square_original_sku` | Single line text |
| Square Variant Description | `custom.square_variant_description` | Multi-line text |

### Settings for All Metafields
- **Storefront API access:** OFF (internal traceability fields; not needed for POS-only or
  any store where these are audit-only fields)

### Checking for Unstructured Metafields
If metafields were imported without formal definitions, they appear as "unstructured" — data
exists in Shopify but no formal definition is attached. Visible via the "View unstructured
metafields" button in Shopify Admin. Always create formal definitions; unstructured metafields
cannot be queried reliably.

---

## 16. RETROACTIVE SHOPIFY UPDATE WORKFLOWS

Use these when fixing data that is already live in Shopify after a completed import.

### Workflow A — Changing Handles (Product Consolidation)

Use when restructuring products already in Shopify (e.g., merging separate Square items into
one Shopify product with variants).

1. Build a DELETE file: two columns only — `Handle` and `Command` = `DELETE` — one row per old handle
2. Build the new import file with clean, consolidated handles
3. **Upload DELETE file first** — this frees up handle names in Shopify
4. **Upload new import file second** — creates or updates products under the new handles
5. **Never skip the delete step** when the same handle appears in both files
   - ⚠️ If delete is skipped, Matrixify merges into the old product instead of creating clean

### Workflow B — Fixing Data (No Handle Changes)

Use when correcting field values (SKUs, metafields, prices) for products already in Shopify.

1. Build a **delta file** — only the rows that actually changed (not the full catalog)
2. Upload directly — no delete step needed
3. **Do NOT re-upload the full catalog for targeted fixes** — unnecessarily touches all products,
   updates `updated_at` timestamps, and wastes Matrixify row quota

### Workflow C — Changing Metafield Architecture (Product → Variant Level)

Use when you need to move metafields from product-level to variant-level.

1. Shopify Admin → Settings → Custom data → Products → find the affected field
2. **Delete the field WITH its saved values** (not "Delete field only" — that leaves orphaned data)
3. Go to Settings → Custom data → Variants → create the new definition there
4. Update column prefix in ALL import files: `Metafield:` → `Variant Metafield:`
5. Re-import the affected products

---

## 17. PRE-IMPORT QA CHECKLIST

Run through this before every Matrixify upload.

### File Structure
- [ ] All variant rows of the same product share exactly the same Handle string
- [ ] Body HTML populated on first row of each Handle group only; blank on all others
- [ ] Title, Vendor, Tags, Option1 Name populated on every row
- [ ] Column headers include type annotations for all metafield columns
- [ ] No extraneous columns Matrixify doesn't recognise

### Variant Data
- [ ] No two variants of the same product share the same Variant SKU or Variant Barcode
- [ ] No two different products share the same Variant Barcode (cross-product duplicate check)
- [ ] All variants in a `flavor_variant` product have distinct, correctly assigned Token values
- [ ] `square_original_variation_name` is populated for all variants that had Variation Name or Flavor in Square

### Metafield Architecture
- [ ] Product-level metafields use `Metafield:` prefix
- [ ] Variant-level metafields use `Variant Metafield:` prefix
- [ ] Shopify metafield definitions exist for all columns before import

### Static Values
- [ ] `Variant Inventory Policy` = `deny` on all rows
- [ ] `Variant Inventory Tracker` = `shopify` on all rows
- [ ] `Variant Requires Shipping` = `False` on all rows (POS-only) — or reviewed per-product (omnichannel)
- [ ] `Published Scope` = `web` (POS-only) or `global` (omnichannel) on all rows — confirmed for this store

### Spot Checks
- [ ] Open the largest multi-variant product; confirm each variant has a unique Token
- [ ] Open a `flavor_variant` product; confirm Variant SKU and Barcode differ per variant
- [ ] Verify at least one archived product row has `Status` = `archived` and `Published` = `FALSE`

---

## 18. KEY LESSONS LEARNED

### Pipeline Design
1. **Test with multi-variant products first.** The source_row collapse bug (Bug 1) is invisible
   with standalone products. Always spot-check a 2+ variant product early.
2. **Use Token as your canary.** Every Square row has a unique Token. If all variants of a product
   share the same Token, the pipeline has a source_row reference bug.
3. **Check all metafield columns simultaneously when validating** — the collapse bug affects SKU,
   Barcode, AND Token at once. Checking only SKU misses the Token evidence.
4. **Build handles from Item Name only.** Never append Variation Name to the handle slug — it
   creates unmaintainable handles that require retroactive cleanup.

### Matrixify
5. **`Metafield:` vs `Variant Metafield:` is structural, not cosmetic.** This distinction
   determines whether Shopify stores one value per product or one per variant. Getting it wrong
   causes silent data loss — only the first row's values survive.
6. **Duplicate SKU warnings = data bug, not import failure.** Matrixify falls back to Options
   matching gracefully, but the root cause must still be fixed.
7. **"Variants updated by Options" on re-import is expected** after fixing duplicate SKUs.
   Matrixify reads the pre-update Shopify state — it sees old duplicates and falls back. The
   write still succeeds.
8. **Delta imports over full re-uploads.** For targeted fixes, always build a file with only
   the changed rows.

### Shopify Metafield Architecture
9. **Design metafield levels before the first import.** Changing from product to variant level
   after the fact requires deleting the definition and all saved data, then re-importing.
   Plan it correctly upfront.
10. **"Delete field and its saved values" is the correct recovery path** when moving a metafield
    to a different object level. "Delete field only" leaves orphaned unstructured data that is
    invisible and unqueryable.
11. **Unstructured metafields are junk.** If you see "View unstructured metafields" in Shopify
    Admin, those values exist without a formal definition. Create definitions and re-import.

### Data Quality
12. **Duplicate barcodes across variants = POS scanning failure.** Shopify cannot determine
    which variant to ring up. Must be fixed before go-live.
13. **Cross-product barcode duplicates are source data issues.** Flag to the client; do not
    silently reassign. Client must decide which product holds the correct barcode.
14. **Preserve original casing in traceability metafields.** These fields exist for auditing
    back to Square. Store `"SCOTCH OATMEAL COOKIES"` (original Square casing), not
    `"Scotch Oatmeal Cookies"` (cleaned version).

---

## 19. CANONICAL EXAMPLES (SGPC PRODUCTION — April 2026)

Real before/after rows from the South Georgia Pecan Company Gift Shop migration. Each
illustrates one variant classification. Use these to verify pipeline output matches expected
structure — not as templates to copy verbatim.

---

### Example 1 — `standalone`

**Source (Square):**
```
Item Name:      10" ROUND CLEAR PLASICT 6 CAVITY TUB W/LID
Variation Name: Regular
SKU:            9757082
GTIN:           (blank)
Price:          5.24
Token:          CD6HIJEVA2CJ3UQN2WZGUEDW
```

**Output (Matrixify):**
```
Handle:                     10-round-clear-plasict-6-cavity-tub-wlid
Title:                      10" Round Clear Plasict 6 Cavity TUB W/LID
Option1 Name:               (blank — standalone, no option needed)
Option1 Value:              (blank)
Variant SKU:                9757082
Variant Barcode:            9757082   ← clean SKU, no GTIN, used as both
Variant Price:              5.24
Variant Taxable:            TRUE
Published Scope:            global
square_token:               CD6HIJEVA2CJ3UQN2WZGUEDW
square_original_item_name:  10" ROUND CLEAR PLASICT 6 CAVITY TUB W/LID
```

**Notes:** "Regular" Variation Name on a single-row group = standalone. No Option1 needed.
Vendor (Atlantic Can) preserved directly from Default Vendor Name.

---

### Example 2 — `bulk_size_variant`

**Source (Square):**
```
Item Name:      BULK ALMONDS MILK CHOCOLATE
Variation Name: 24/16 CHOCOLATE ALMONDS          Token: AX6LGDM52ZC52X7ER66B  SKU: 5635    Price: 248.40
Variation Name: BULK ALMONDS MILK CHOCOLATE 25 lb.  Token: JJSKPVVNUICBEEGUDQRS  SKU: NB130098-25  Price: 287.50
```

**Output (Matrixify) — 2 rows, same Handle:**
```
Handle   Title                       Option1 Name  Option1 Value  Variant SKU   Variant Barcode  Variant Price  square_token (first 20)
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
bulk-almonds-milk-chocolate  BULK Almonds MILK Chocolate  Size  24/16  5635  5635  248.40  AX6LGDM52ZC52X7ER66B
bulk-almonds-milk-chocolate  BULK Almonds MILK Chocolate  Size  25 lbs  NB130098-25  NB130098-25  287.50  JJSKPVVNUICBEEGUDQRS
```

**Notes:** Item Name contains `BULK` → `bulk_size_variant`. Handle built from Item Name only
(`bulk-almonds-milk-chocolate`) — Variation Name not appended. Pound conversion applied:
"BULK ALMONDS MILK CHOCOLATE 25 lb." → option value `25 lbs`. Both SKUs are clean → used as
both Variant SKU and Variant Barcode. Each row has a **unique** Token (confirming no source_row
collapse bug).

---

### Example 3 — `mixed_size_variant`

**Source (Square):**
```
Item Name:      DOUBLE DIPPED CHOCOLATE PEANUTS 1 lb. BAG
Variation Name: 1# PEANUTS - DOUBLE DIPPED CHOCOLATE BAG  Token: LMZDSA3VAYMZLFK4PNZF  SKU: 646345330725
Variation Name: dBL dIP 16OZ                              Token: TG7S7T23BAWEC6BYUEH7  SKU: (contains spaces → not barcode)
Variation Name: DD CHOC. PEANUT 4oz                       Token: BXM4Q3FY6LJAF44VVHRK  SKU: 444480F
Variation Name: DD CHOC PEANUT 8oz                        Token: G42KKNLQSKRWWWMTNI5Q  SKU: 910011K
```

**Output (Matrixify) — 4 rows, same Handle:**
```
Handle                       Option1 Value  Variant SKU    Variant Barcode  Variant Price  square_original_sku
────────────────────────────────────────────────────────────────────────────────────────────────────────
double-dipped-chocolate-peanuts  1 lb       646345330725   646345330725     12.00          (blank)
double-dipped-chocolate-peanuts  1 lb       (blank)        (blank)          11.00          dBL dIP 16OZ  ← space in SKU → metafield
double-dipped-chocolate-peanuts  4 oz       444480F        444480F          3.00           (blank)
double-dipped-chocolate-peanuts  8 oz       910011K        910011K          6.00           (blank)
```

**Notes:** Variation Names contain `#`, `OZ` size patterns → `mixed_size_variant`. Pound-sign
conversion: `1#` → `1 lb`. `dBL dIP 16OZ` contains a space → `clearly_not_barcode` → moved to
`square_original_sku` metafield, Variant SKU and Barcode left blank. Two variants with the same
option value (`1 lb`) at different prices — both preserved; check with client which is canonical.

---

### Example 4 — `mixed_type_variant` (flavor-named options)

**Source (Square):**
```
Item Name:      Aunt Sally's Creole Praline
Variation Name: Classic         Token: PHJDOWUFGDVG3WIALCIL  SKU: 6.44719E+11  GTIN: 644719000533
Variation Name: Bananas Foster  Token: OLA7GJMAFPAJYNZGKY2J  SKU: 6.44719E+11  GTIN: 644719008539
Variation Name: Sugar & Spice   Token: 6LUR7VF22ONETCWXPCS4  SKU: 6.44719E+11  GTIN: 644719000656
Variation Name: Cafe au Lait    Token: YDRHALNUQFVP3U45VULA  SKU: 6.44719E+11  GTIN: 644719006535
Variation Name: Chocolate       Token: LE5YMQKKXCCXUOVAENDG  SKU: 6.44719E+11  GTIN: 644719007532
Variation Name: Salted Caramel  Token: ULDGFEZ5TZADMUO4IC27  SKU: 6.44719E+11  GTIN: 644719004531
```

**Output (Matrixify) — 6 rows, same Handle:**
```
Handle                    Option1 Name  Option1 Value   Variant SKU    Variant Barcode  square_token (first 20)
──────────────────────────────────────────────────────────────────────────────────────────────────────────────
aunt-sallys-creole-praline  Flavor  Classic         644719000533   644719000533   PHJDOWUFGDVG3WIALCIL
aunt-sallys-creole-praline  Flavor  Bananas Foster  644719008539   644719008539   OLA7GJMAFPAJYNZGKY2J
aunt-sallys-creole-praline  Flavor  Sugar & Spice   644719000656   644719000656   6LUR7VF22ONETCWXPCS4
aunt-sallys-creole-praline  Flavor  Cafe Au Lait    644719006535   644719006535   YDRHALNUQFVP3U45VULA
aunt-sallys-creole-praline  Flavor  Chocolate       644719007532   644719007532   LE5YMQKKXCCXUOVAENDG
aunt-sallys-creole-praline  Flavor  Salted Caramel  644719004531   644719004531   ULDGFEZ5TZADMUO4IC27
```

**Notes:** Square stored all variants under `Variation Name` (not the Flavor column) but the
values are flavor types → Option1 Name = `Flavor`. SKU column shows `6.44719E+11` for all rows
(Excel scientific notation — same value, not unique). GTIN differs per variant and ≠ SKU → GTIN
used as `Variant Barcode`, GTIN also used as `Variant SKU`. `square_original_variation_name`
preserves original casing (e.g., `Cafe au Lait` → output title-cased to `Cafe Au Lait`).

---

### Example 5 — `true_duplicate`

**Source (Square):**
```
Item Name:      BOX SIGN - JESUS REASON
Variation Name: BOX SIGN - JESUS REASON  SKU: P13318    Token: 7EX6AHSGIWDXYHRD5BAS
Variation Name: BOX SIGN - JESUS REASON  SKU: P13318-1  Token: NDF6WGCMCOJR27FZFF3S
```

**Output (Matrixify) — 2 separate products:**
```
Handle                       Variant SKU  Option1 Value
──────────────────────────────────────────────────────
box-sign-jesus-reason          P13318
box-sign-jesus-reason-2        P13318-1
```

**Notes:** Same Item Name + same Variation Name across two rows → `true_duplicate`. Cannot merge
(no option dimension to differentiate). Each becomes its own product with `-2` suffix on second
handle. Titles are identical — flag to client; they may want to differentiate the display names.

---

### Example 6 — `clearly_not_barcode` (SKU classification)

From the same dataset, three SKU patterns and their routing:

```
SKU Value            Condition                           → Variant SKU    → Variant Barcode  → square_original_sku
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
"9757082"            Clean, no GTIN                      → 9757082         → 9757082           → (blank)
"644719000533"       Clean, GTIN=644719000533 ≠ SKU      → 644719000533    → 644719000533       → (blank)
"dBL dIP 16OZ"       Contains spaces → not barcode       → (blank)         → (blank)            → dBL dIP 16OZ
"PECAN 1LB / BULK"   Contains "/" → not barcode          → (blank)         → (blank)            → PECAN 1LB / BULK
"6.44719E+11"        Excel scientific notation of GTIN   → use GTIN value  → use GTIN value     → (blank)
```

**Notes:** Excel may render long numeric SKUs (GTINs) as scientific notation — always check for
`E+` in SKU values. If the SKU is scientific notation but the GTIN column has the clean version,
use the GTIN for both fields.

---

<verification id="square-migration-verify">
Before delivering any output from this skill:

1. **Variant classification:** Is every product group correctly classified (standalone, true_duplicate, flavor_variant, bulk_size_variant, mixed_size_variant, mixed_type_variant)?
2. **Promo keyword check:** Was it applied BEFORE size pattern detection?
3. **MANUAL_GROUPS:** Are there any products with different Item Names that should be merged? Have they been identified and processed first?
4. **`clearly_not_barcode`:** Has every SKU been checked? Are non-scannable values moved to the metafield?
5. **Token uniqueness:** Does every variant have a unique square_token? If not, Bug 1 is present.
6. **Metafield level:** Are all product-level fields using `Metafield:` and all variant-level fields using `Variant Metafield:`?
7. **Published Scope:** Is the store POS-only or omnichannel? Has the correct value (`web` or `global`) been set?
8. **Archived products:** Are archived rows in a separate output file with `Status = archived` and `Published = FALSE`?
9. **Handle uniqueness:** Are all handles unique, lowercase, built from Item Name only?
10. **Warning awareness:** Is the team aware of expected Matrixify warning progressions across sequential uploads?
</verification>
