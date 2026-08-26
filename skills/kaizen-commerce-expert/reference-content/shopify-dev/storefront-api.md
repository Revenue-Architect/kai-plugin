# Shopify Storefront API

Generated Kai vendor freshness note. Use this file for navigation and recent-change awareness only.
Validate current behavior through the canonical vendor source before production guidance.

## Recent feature updates (auto-curated)

<!-- BEGIN AUTO-CURATED UPDATES -->
- [AUTO-CURATED] 2026-06-24 - [Storefront MCP cart tools are being deprecated in favour of UCP Cart MCP](https://shopify.dev/changelog/storefront-mcp-cart-tools-are-being-deprecated-in-favour-of-ucp-cart-mcp)
  - Source: Shopify developer changelog; route: Shopify Storefront API; categories: Action Required, API, Deprecation Announcement
  - Note: What's changing The cart tools on the Storefront MCP server are being deprecated in favour of the UCP-conforming Cart MCP tools: get_cart and update_cart on https://{shop}.myshopify.com/api/mcp are deprecated. Cart MCP implements the UCP cart capability ( dev.ucp.shopping.cart , version 2026-04-08 ) and exposes the following tools at the https://{shop-domain}/api/ucp/mcp endpoint: create_cart : Create a new cart wit...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [Standard storefront events and actions](https://shopify.dev/changelog/standard-storefront-events-and-actions)
  - Source: Shopify developer changelog; route: Shopify Storefront API; categories: Themes, New
  - Note: Liquid storefronts now have a standard communication layer between themes and the code that runs on them. Themes emit events, while apps and agents call actions. Both work across all themes, and they ship together so you implement only once: Events are DOM events for commerce interactions: shopify:product:view , shopify:cart:lines-update , shopify:search:update , and others. Theme developers implement these in their...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-12 - [Read a cart line's `viewKey` from the `CartLine` type](https://shopify.dev/changelog/cart-line-view-key-field)
  - Source: Shopify developer changelog; route: Shopify Storefront API; categories: API, New, Storefront GraphQL API, 2026-07
  - Note: The CartLine type now exposes a viewKey field, so you can correlate a returned cart line with the viewKey you sent to cartLinesUpdate and cartLinesRemove . What's new CartLine.viewKey returns the same viewKey your Liquid storefront renders, alongside the existing UUID id . How to use Previously, identifying a line by viewKey was input-only: you could send a viewKey , but the response returned a UUID id with no viewK...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-02 - [Identify cart lines by `view_key` in `cartLinesUpdate` and `cartLinesRemove`](https://shopify.dev/changelog/cart-line-mutations-accept-view-key)
  - Source: Shopify developer changelog; route: Shopify Storefront API; categories: API, New, Storefront GraphQL API, 2026-07
  - Note: You can now identify cart lines by their view_key when calling the cartLinesUpdate and cartLinesRemove mutations, as an alternative to the cart line id . What's new cartLinesUpdate accepts a viewKey on each CartLineUpdateInput , mutually exclusive with id . cartLinesRemove accepts a viewKeys list, mutually exclusive with lineIds . How to use Provide exactly one identifier per line. Existing integrations that use id...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.

- [AUTO-CURATED] 2026-07-15 - [Storefront API `@inContext` supports `channelId`](https://shopify.dev/changelog/new-channelid-argument-for-incontext-directive-in-storefront-api-2026-10)
  - Source: Shopify developer changelog; route: Shopify Storefront API; categories: API, New, Storefront API, 2026-10
  - Note: As of Storefront API version 2026-10 , the @inContext directive accepts an optional channelId argument. Use channelId to apply a specific sales channel's context to an entire query, including channel-specific product availability and pricing. Example: query Product($handle: String!, $channelId: ID!) @inContext(channelId: $channelId) { product(handle: $handle) { id title availableForSale priceRange { minVariantPrice...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
<!-- END AUTO-CURATED UPDATES -->

## Canonical validation rule

- Shopify developer/API behavior: validate through Shopify Dev MCP and `shopify.dev`.
- Shopify merchant/admin behavior: validate against `help.shopify.com`, `changelog.shopify.com`, or live Admin evidence where available.
- AnyDB behavior: validate against AnyDB MCP/docs and public release notes before build-ready artifacts.

## Reviewed vendor updates

- [REVIEWED] 2026-06-17 - [Hydrogen developer preview](https://shopify.dev/changelog/hydrogen-developer-preview)
  - Note: Developer preview only; Hydrogen's framework-agnostic core is suitable for prototyping, not an unconditional production recommendation.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.

- [REVIEWED] 2026-06-30 - [Hydrogen now deploys to Vercel](https://shopify.dev/changelog/hydrogen-now-deploys-to-vercel)
  - Note: Hydrogen developer-preview projects can deploy to Vercel; preserve preview status and validate the current starter/runtime contract.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.

- [REVIEWED] 2026-04-22 - [Storefront Catalog MCP now implements UCP](https://shopify.dev/changelog/storefront-catalog-mcp-now-implements-ucp)
  - Note: Storefront Catalog MCP adopted UCP tool names and endpoint shapes; legacy catalog tools had a June 15, 2026 migration deadline.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.
