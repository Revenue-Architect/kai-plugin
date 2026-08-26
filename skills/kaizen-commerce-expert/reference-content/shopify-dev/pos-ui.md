# Shopify POS UI

Generated Kai vendor freshness note. Use this file for navigation and recent-change awareness only.
Validate current behavior through the canonical vendor source before production guidance.

## Recent feature updates (auto-curated)

<!-- BEGIN AUTO-CURATED UPDATES -->
- [AUTO-CURATED] 2026-04-27 - [Minor rounding change for custom line item discounts in POS 11.5](https://shopify.dev/changelog/minor-rounding-change-for-custom-line-item-discounts-in-pos-115)
  - Source: Shopify developer changelog; route: Shopify POS UI; categories: API, Update, POS Extensions
  - Note: Starting with POS version 11.5, we are updating the internal calculation method for custom fixed-amount line item discounts. These discounts will now be applied on a per-unit basis rather than across the entire line. Note that this change only affects fixed-amount discounts; percentage discounts remain unchanged. If your app uses setLineItemDiscount or bulkSetLineItemDiscounts from the Cart API with a FixedAmount di...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.

- [AUTO-CURATED] 2026-07-15 - [POS UI Extensions 2026-07 adds discount allocations to bundle components](https://shopify.dev/changelog/pos-ui-extensions-2026-07-adds-discount-allocations-to-bundle-components)
  - Source: Shopify developer changelog; route: Shopify POS UI; categories: API, Update, POS Extensions, 2026-07
  - Note: Starting with POS UI Extensions API version 2026-07, product bundle components in cart line item data include discount allocation details. Apps can access component-level discount allocations from bundle components on a cart line item, for example: shopify.cartLineItem.components?.[0]?.discountAllocations The same LineItem shape is also used in Cart API cart state, so apps that read line items from shopify.cart.curr...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-07-09 - [POS Extensions now supports a background extension target](https://shopify.dev/changelog/pos-extensions-now-supports-a-background-extension-target)
  - Source: Shopify developer changelog; route: Shopify POS UI; categories: API, New, POS Extensions, 2026-07
  - Note: The pos.app.ready.data target runs for the entire POS session, letting your extension observe POS events and run background logic without rendering any UI surface. Use it for event observation, data storage, and calling non-visual background APIs. What you need to do Subscribe to Shopify POS events with shopify.addEventListener() : shopify.addEventListener('transactioncomplete', (event) => { console.log('Transaction...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-07-08 - [POS UI extensions 2026-07 uses per-unit fixed-amount line item discounts](https://shopify.dev/changelog/pos-ui-extensions-2026-07-uses-per-unit-fixed-amount-line-item-discounts)
  - Source: Shopify developer changelog; route: Shopify POS UI; categories: Action Required, API, Breaking API Change, POS Extensions, 2026-07
  - Note: Starting with POS UI extensions API version 2026-07, FixedAmount line item discounts passed to setLineItemDiscount and bulkSetLineItemDiscounts from the Cart API must represent a per-unit discount. Why it's changing In API version 2026-04 and earlier, apps could pass a total fixed discount for the entire line item, and Shopify POS automatically converted it to a per-unit value. In API version 2026-07, this conversio...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
<!-- END AUTO-CURATED UPDATES -->

## Canonical validation rule

- Shopify developer/API behavior: validate through Shopify Dev MCP and `shopify.dev`.
- Shopify merchant/admin behavior: validate against `help.shopify.com`, `changelog.shopify.com`, or live Admin evidence where available.
- AnyDB behavior: validate against AnyDB MCP/docs and public release notes before build-ready artifacts.
