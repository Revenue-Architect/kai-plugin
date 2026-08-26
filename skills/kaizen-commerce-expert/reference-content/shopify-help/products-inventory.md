# Shopify Products and Inventory

Generated Kai vendor freshness note. Use this file for navigation and recent-change awareness only.
Validate current behavior through the canonical vendor source before production guidance.

## Recent feature updates (auto-curated)

<!-- BEGIN AUTO-CURATED UPDATES -->
- [AUTO-CURATED] 2026-06-30 - [Define and manage metafields on inventory transfers](https://changelog.shopify.com/posts/define-and-manage-metafields-on-inventory-transfers)
  - Source: Shopify merchant changelog; route: Shopify Products and Inventory; categories: Inventory
  - Note: Inventory transfers now support custom metafields in the Shopify admin and Admin GraphQL API. Set up transfer metafields Go to Settings > Metafields and metaobjects > Transfers to define your metafield definitions, then add and edit values from the Transfer Create and Transfer Details pages. Use cases Transfer metafields are useful when your receiving, logistics, or inventory processes rely on data that the standard...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-30 - [Use location metafields as dimensions and filters in Analytics](https://changelog.shopify.com/posts/use-location-metafields-as-dimensions-and-filters-in-analytics)
  - Source: Shopify merchant changelog; route: Shopify Products and Inventory; categories: Inventory
  - Note: If you store custom data on your locations like store tiers, internal store numbers, fulfillment capabilities, or routing zones you can now use those metafields as dimensions and filters in Analytics. How to enable it Open a location metafield definition in Settings > Metafields and metaobjects > Locations and turn on "Filter or group data in Analytics." That definition is then available as a dimension or filter acr...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-22 - [Purchase orders now create transfers to move inventory](https://changelog.shopify.com/posts/purchase-orders-now-create-transfers-to-move-inventory)
  - Source: Shopify merchant changelog; route: Shopify Products and Inventory; categories: Admin
  - Note: Purchase orders record what you ordered from a supplier and what it cost. Transfers record inventory movement. The two are now connected. When you're ready to receive a purchase order, it now creates a transfer. What this means: Receive in admin or POS - Incoming inventory can be received from either, so it can be done wherever the shipment arrives. Partial deliveries - A single transfer can have multiple shipments,...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [Visualize your data with bubble and sunburst charts in Analytics](https://changelog.shopify.com/posts/visualize-your-data-with-bubble-and-sunburst-charts-in-analytics)
  - Source: Shopify merchant changelog; route: Shopify Products and Inventory; categories: Admin
  - Note: Bubble and sunburst charts are now available in Analytics. These two new chart types give you more ways to explore your store data, whether you're comparing multiple metrics at once or breaking down totals across nested categories. The new chart types appear in the visualization picker when you create or edit a report. Bubble charts plot three metrics together so you can spot outliers, like products with high sales...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [Product listings now support a disclosures field](https://changelog.shopify.com/posts/product-listings-now-support-a-disclosures-field)
  - Source: Shopify merchant changelog; route: Shopify Products and Inventory; categories: Products
  - Note: Merchants can now add structured product disclosures directly in Shopify admin instead of storing warnings in product descriptions, theme code, or custom workarounds. Product disclosures are stored as product metafields and support built-in disclosure types for California Proposition 65 warnings and choking-hazard notices, plus custom disclosure types for other product-specific warnings or notices. On supported Onli...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-10 - [Shopify Collective is now available in Australia](https://changelog.shopify.com/posts/shopify-collective-is-now-available-in-australia)
  - Source: Shopify merchant changelog; route: Shopify Products and Inventory; categories: Collective
  - Note: Shopify Collective is now available to merchants in Australia. Australian retailers can partner with Australian suppliers to sell their products directly through their storefronts. Retailers can expand their catalog without holding inventory or upfront cost. Suppliers can reach new customers by selling through Australian retailers that match their brand. To get started, install Shopify Collective from the Shopify Ap...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-08 - [Improved catalog publishing](https://changelog.shopify.com/posts/improved-catalog-publishing)
  - Source: Shopify merchant changelog; route: Shopify Products and Inventory; categories: Admin
  - Note: You can now make edits to your catalog, then save or discard all the changes together. Configure publishing changes across multiple products in a catalog. Review changes, then save or discard them in one action. Learn more: Create and manage your catalogs
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-04 - [Scatter plots and radar charts are now in Shopify Analytics](https://changelog.shopify.com/posts/scatter-plots-and-radar-charts-are-now-in-shopify-analytics)
  - Source: Shopify merchant changelog; route: Shopify Products and Inventory; categories: Admin
  - Note: Custom reports in Shopify Analytics now support two new chart types: scatter plots and radar charts. These give you more ways to spot patterns and compare performance across your store data without exporting to a spreadsheet. Use scatter plots to see how two metrics relate. Plot revenue against units sold per product to find which products move volume but not margin. Plot session count against conversion rate per tr...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.

- [AUTO-CURATED] 2026-07-16 - [Collections now support multi-source and variants](https://changelog.shopify.com/posts/collections-now-support-multi-source-and-variants)
  - Source: Shopify merchant changelog; route: Shopify Products and Inventory; categories: Admin
  - Note: This release expands collection capabilities to help merchants run complex merchandising strategies without workarounds such as duplicate lists or third-party apps. Previously, collections were created only by automated conditions or hand-picked products. You can now build a collection from multiple sources, target specific variants, reuse other collections, and more. Highlights include: Multiple sources in one coll...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-07-15 - [Multiple product discounts on the same item](https://changelog.shopify.com/posts/multiple-product-discounts-on-the-same-item)
  - Source: Shopify merchant changelog; route: Shopify Products and Inventory; categories: Discounts
  - Note: You can now combine multiple product discounts on the same item, so overlapping promotions apply together without cart conflicts or workarounds. Previously, only one product discount could apply to an item. For example, run a sitewide 20% off the winter collection sale alongside $10 off boots from an affiliate partnership. When a customer adds winter boots to their cart, both discounts apply automatically. What you...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
<!-- END AUTO-CURATED UPDATES -->

## Canonical validation rule

- Shopify developer/API behavior: validate through Shopify Dev MCP and `shopify.dev`.
- Shopify merchant/admin behavior: validate against `help.shopify.com`, `changelog.shopify.com`, or live Admin evidence where available.
- AnyDB behavior: validate against AnyDB MCP/docs and public release notes before build-ready artifacts.
