# Shopify Markets and localization

Generated Kai vendor freshness note. Use this file for navigation and recent-change awareness only.
Validate current behavior through the canonical vendor source before production guidance.

## Recent feature updates (auto-curated)

<!-- BEGIN AUTO-CURATED UPDATES -->
- [AUTO-CURATED] 2026-06-26 - [Shopify now supports 3 EU import customs duty collection](https://changelog.shopify.com/posts/new-3-eu-import-customs-duty-arrives-july-1)
  - Source: Shopify merchant changelog; route: Shopify Markets and localization; categories: Markets
  - Note: Shopify Managed Markets and Shopify's import tax and duty calculation now support the EU's flat 3 customs duty per tariff line on qualifying orders up to 150 shipped into the EU from outside the EU, effective July 1, 2026. If you use either product, Shopify handles this fee for you automatically. No settings changes required. What's now supported In Shopify Managed Markets: The 3 fee is calculated, displayed, and co...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-24 - [Custom draft order line item discounts now use presentment currency](https://changelog.shopify.com/posts/improvement-to-draft-order-custom-discount-currency)
  - Source: Shopify merchant changelog; route: Shopify Markets and localization; categories: Admin
  - Note: Custom discounts added to draft order line items now use the draft order's presentment currency instead of the shop currency. This makes discount amounts easier to understand in draft order flows where the customer is checking out in a different currency than the shop's default currency. Learn more about custom discounts for draft orders in the Help Center .
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-23 - [B2B discounts are now enabled by default for new B2B stores and eligible existing stores](https://changelog.shopify.com/posts/b2b-discounts-are-now-available-by-default-on-new-stores)
  - Source: Shopify merchant changelog; route: Shopify Markets and localization; categories: Discounts
  - Note: Previously, stores had to contact Shopify Support to activate discounts for B2B. Now, discounts for B2B are activated automatically, so you can create automatic discounts and discount codes for your B2B customers right away. What's changing New stores using B2B : Discounts for B2B are activated by default. No setup step is required. Existing B2B stores without active or scheduled discounts : Discounts for B2B are be...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-18 - [Self-serve returns now support cancellations](https://changelog.shopify.com/posts/self-serve-returns-now-support-cancellations)
  - Source: Shopify merchant changelog; route: Shopify Markets and localization; categories: Customer-account
  - Note: Buyers can now request order cancellations through self-serve, in addition to requesting returns. You can set cancellation rules alongside your return rules. Both return and cancellation rules are configurable per market. A default policy applies storewide, with the option to add market-specific rules that override it for individual markets. This enables merchants selling in the EU to offer a withdrawal policy-from...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [Set channel-specific prices, availability and currency with Markets](https://changelog.shopify.com/posts/set-channel-specific-prices-availability-and-currency-with-markets)
  - Source: Shopify merchant changelog; route: Shopify Markets and localization; categories: Admin
  - Note: Channels are now available as a market type in Shopify Markets. This enables merchants to create a market for one or more sales channels and, optionally, region(s), assign a catalog, and customize pricing, product availability, and currency while keeping each channel's own publishing controls in place. Channel Markets are now available to all merchants using Markets. Learn more about using Markets with sales channel...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [Understand your Markets setup at a glance with the redesigned graph](https://changelog.shopify.com/posts/understand-your-markets-setup-at-a-glance-with-the-redesigned-graph)
  - Source: Shopify merchant changelog; route: Shopify Markets and localization; categories: Admin
  - Note: The Markets graph now makes your configuration easy to understand at a glance. No more clicking into individual market pages to simply verify the number of products or mentally tracing what settings each sub-market inherits from its parent. Redesigned graph - A clearer visual map with product images on nodes, number of products and discounts for each node. Aggregated panel for all markets - See what settings are car...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.

- [AUTO-CURATED] 2026-07-16 - [Shopify Managed Markets now supports EU buyer cancellation and return requests](https://changelog.shopify.com/posts/shopify-managed-markets-now-supports-eu-buyer-cancellation-and-return-requests)
  - Source: Shopify merchant changelog; route: Shopify Markets and localization; categories: Markets
  - Note: Shopify Managed Markets now supports buyer cancellation and return requests for applicable EU orders to comply with newly established Right of Withdrawal requirements for online stores. For merchants using Managed Markets to sell into EU countries, Shopify has added a managed 14-day cancellation and return rule for covered EU-bound orders. What's supported: * Applicable EU Managed Markets orders now include a 14-day...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-07-10 - [Drive international conversion with automated duties-inclusive pricing from Shopify Managed Markets](https://changelog.shopify.com/posts/drive-international-conversion-with-automated-duties-inclusive-pricing-from-shopify-managed-markets)
  - Source: Shopify merchant changelog; route: Shopify Markets and localization; categories: Markets
  - Note: Shopify Managed Markets merchants can now use a managed pricing strategy across supported international markets. Pricing will account for cross-border costs like guaranteed duties and import taxes, transaction fees, and currency conversion in product prices, so international buyers can see stable, transparent pricing throughout their journey with no surprise fees at checkout or delivery. When managed pricing is acti...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-07-10 - [Turn automatic hreflang tags on or off from your admin settings](https://changelog.shopify.com/posts/turn-automatic-hreflang-tags-on-or-off-from-your-admin-settings)
  - Source: Shopify merchant changelog; route: Shopify Markets and localization; categories: Admin
  - Note: Hreflang tags tell search engines which language or region version of a page to serve to which visitors. Shopify generates them automatically from your Markets language and domain settings. The automatic hreflang tag setting is on by default, but you can turn it off if you prefer to manage hreflang tags yourself and want to avoid duplicate tags. To turn it off, go in your Shopify admin to Online Store > Preferences...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
<!-- END AUTO-CURATED UPDATES -->

## Canonical validation rule

- Shopify developer/API behavior: validate through Shopify Dev MCP and `shopify.dev`.
- Shopify merchant/admin behavior: validate against `help.shopify.com`, `changelog.shopify.com`, or live Admin evidence where available.
- AnyDB behavior: validate against AnyDB MCP/docs and public release notes before build-ready artifacts.

## Reviewed vendor updates

- [REVIEWED] 2026-05-07 - [Assign discounts to specific markets](https://changelog.shopify.com/posts/assign-discounts-to-specific-markets)
  - Note: Available to merchants on Basic and above using the new Markets experience; preserve market and customer-eligibility interaction caveats.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.
