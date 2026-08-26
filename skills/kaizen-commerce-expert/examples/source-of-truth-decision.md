# Good vs Bad: Source Of Truth Decision

Use when assigning ownership across Shopify, ERP, WMS, AnyDB, or apps.

## Bad

"Shopify will be the source of truth and sync with the ERP to keep data aligned."

## Why It Fails

- "Source of truth" is too broad
- No entity-level ownership
- No direction or cadence
- No conflict rule
- Ignores ERP ownership patterns

## Good

"Source of truth should be assigned by entity, not by platform.

Products: ERP owns SKU, vendor cost, and accounting category. Shopify owns title, description,
images, collections, channel publication, and selling status.

Inventory: WMS owns warehouse on-hand. Shopify owns sellable availability for online and POS.
The connector updates Shopify every 15 minutes, and Shopify should never write inventory back
to WMS unless the connector explicitly supports adjustments.

Orders: Shopify owns order capture and payment state. ERP receives posted order and tax data for
financial reporting. Order edits, refunds, and partial fulfillment need explicit edge-case testing
before go-live."

## Why It Works

- Assigns ownership per entity and attribute
- States direction and cadence
- Preserves conflict rules
- Surfaces edge cases before implementation
