# Good vs Bad: AnyDB Architecture Recommendation

Use when deciding whether AnyDB belongs in scope.

## Bad

"AnyDB should be used as the operational database for all inventory, orders, and reporting so
the merchant has one centralized source of truth for the business."

## Why It Fails

- Makes AnyDB the master system without proving ownership
- Treats "centralized" as automatically better
- Risks duplicating Shopify or ERP
- Does not name the workflow AnyDB actually owns

## Good

"AnyDB should not own products, inventory, or orders. Shopify should remain the system of record
for commerce-facing product data, inventory availability, and order state.

AnyDB has a clear role if purchasing and vendor follow-up are in scope: it should own the purchase
order workflow, approval state, supplier communication log, receiving exceptions, and reorder
review queue. Shopify provides product and inventory context into that workflow, but AnyDB owns
the operational process around decisions Shopify does not model cleanly."

## Why It Works

- Protects Shopify as the commerce source of truth
- Gives AnyDB a specific job
- Names objects and workflows
- Avoids an unnecessary second operational master
