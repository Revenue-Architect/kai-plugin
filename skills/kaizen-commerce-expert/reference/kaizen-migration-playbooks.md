# Kaizen Migration Playbooks

Use this reference for migration planning, data prep, execution packages, QA, reconciliation, and
rescue work. These are pattern playbooks, not live platform documentation. Verify current Shopify,
Matrixify, AnyDB, and source-system behavior before generating version-sensitive instructions.

## Migration Principles

- API-first is the default lane for controlled, repeatable migration work.
- Matrixify is a supported lane when evidence or approved scope makes it lower risk.
- Shopify Admin CSV is for small, low-risk imports.
- Hybrid is acceptable when entities need different lanes.
- Import success is not go-live readiness.
- Every data-creating workflow needs a Created Resource Ledger and ABORT_CLEANUP path.

## Lane Decision Pattern

Use API-first when:

- source API is accessible
- idempotency keys are available
- transformation logic is complex or repeatable
- retries and dead-letter queues matter
- staged validation is required

Use Matrixify when:

- approved scope already selects Matrixify
- entity is well-supported by Matrixify columns
- team needs human-reviewable files
- source data is file-based and stable
- rollback/delete paths are understood

Use Shopify Admin CSV when:

- dataset is small
- fields are standard
- no complex retry/reconciliation path is needed

Use hybrid when:

- products/metafields need API but a narrow artifact is safer through Matrixify or CSV
- legacy exports vary by entity
- gift cards, historical orders, images, or inventory need separate treatment

## Lightspeed Pattern

Common risks:

- product and variant exports may not match Shopify's model cleanly
- inventory by location needs careful mapping
- customer history and order history may be incomplete or not worth full import
- gift card export quality must be proven before scope confidence
- staff muscle memory is a go-live risk

Evidence to request:

- products and variants export
- inventory by location export
- customers export
- gift card balances and liability report if in scope
- order history requirement and sample export
- location list and hardware plan

Judgment:

- treat location mapping and staff training as major gates
- do not quote final migration timeline from record count alone
- preserve old system availability through parallel validation

## Square Pattern

Common risks:

- item variation structure and modifiers can map poorly to Shopify variants/options
- historical orders may require a separate one-time batch plan
- customer merge rules need email/phone decisions
- cost/unit cost fields can be lost if not explicitly mapped
- gift cards, loyalty, and payments need separate scope decisions

Evidence to request:

- catalog export with variations/modifiers
- customer export
- historical transaction/order sample if in scope
- inventory export by location
- gift card and loyalty export if relevant
- cost field presence

Judgment:

- verify whether cost fields survive the chosen lane
- separate historical orders from live commerce setup
- do not let modifiers become accidental product variants without review

## WooCommerce Pattern

Common risks:

- ecommerce product data may be strong while POS workflow is absent
- attributes and variations can be inconsistent
- order history import may not support desired Shopify operational behavior
- SEO, redirects, collections, and content scope can expand quickly
- customer records may include guest checkout duplicates

Evidence to request:

- products, variations, images, and category exports
- order history scope decision
- redirects and URL structure
- customer export and guest checkout volume
- apps/plugins used for subscriptions, memberships, wholesale, or custom checkout

Judgment:

- separate ecommerce migration, POS migration, and technical SEO scope
- do not bury redirects or URL risk inside data migration
- ask whether historical order import is operationally needed or archival

## ERP-Backed Pattern

Common risks:

- ERP may own products, inventory, pricing, or financial truth
- Shopify may be commerce execution, not system-of-record
- sync direction may differ by entity
- edge cases include refunds, edits, partial fulfillment, tax, wholesale, and payouts

Evidence to request:

- entity ownership matrix
- integration map
- sync cadence and direction
- conflict resolution rules
- ERP data sample for product, inventory, customer, and order entities

Judgment:

- never make a platform-wide source-of-truth statement
- decide by entity and workflow
- require reconciliation owner and exception path

## CSV-Only Legacy Pattern

Common risks:

- exports are stale, partial, or manually edited
- data lacks stable IDs
- relationships between products, variants, customers, and orders are weak
- import files become untraceable without transformation logs

Evidence to request:

- untouched original files
- export date and owner
- field dictionary if available
- sample records across edge cases
- stable keys for each entity

Judgment:

- preserve originals
- produce transformation logs
- require sample validation before full prep
- lower confidence when stable IDs are absent

## Entity Playbooks

### Products And Variants

Watch for:

- duplicate handles
- duplicate or missing SKUs
- missing option values
- product-level data repeated on variant rows
- inconsistent price, tax, vendor, type, tags, status, and channel publishing

Evidence gates:

- source count
- output count
- unique handle count
- SKU/variant uniqueness check
- required field completeness
- POS channel publishing check

### Customers

Watch for:

- duplicate email with casing differences
- missing consent fields
- phone-only customers
- B2B or wholesale tags
- guest checkout records

Evidence gates:

- merge key decision
- duplicate count
- required field completeness
- exclusion list

### Gift Cards

Watch for:

- current balance without original issue amount
- liability mismatch
- incompatible codes
- redemption workflow uncertainty

Evidence gates:

- total liability before and after
- sample redemption path
- finance sign-off

### Inventory

Watch for:

- missing location IDs
- mismatched location names
- aggregate totals hiding per-location errors
- concurrent sales during migration

Evidence gates:

- SKU plus location reconciliation
- expected vs actual per-location counts
- parallel-run adjustment log

### Historical Orders

Watch for:

- operational need vs archival desire
- customer/order linking
- payment/refund representation
- tax and discount fidelity
- fulfillment status

Evidence gates:

- sample order mapping
- acceptance criteria for incomplete historical fields
- client sign-off on limitations

## Rescue Pattern

When migration fails:

1. Stop additional imports.
2. Preserve original files, transformed files, logs, and result exports.
3. Identify scope: entity, rows, fields, locations, systems.
4. Classify blocker vs warning.
5. Find root cause before rewriting files.
6. Build targeted fix.
7. Retest failed rows or affected entity.
8. Update Created Resource Ledger and handoff.

Do not reassure the client until counts, failure class, and remediation path are known.
