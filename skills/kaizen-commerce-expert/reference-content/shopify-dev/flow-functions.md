# Shopify Flow and Functions

Generated Kai vendor freshness note. Use this file for navigation and recent-change awareness only.
Validate current behavior through the canonical vendor source before production guidance.

## Recent feature updates (auto-curated)

<!-- BEGIN AUTO-CURATED UPDATES -->
- [AUTO-CURATED] 2026-07-03 - [[DRAFT] Markets APIs now support MarketRegionSubdivision](https://shopify.dev/changelog/markets-apis-now-support-marketregionsubdivision)
  - Source: Shopify developer changelog; route: Shopify Flow and Functions; categories: API, Update
  - Note: Sub-region Markets are available in the Admin GraphQL API 2026-07 release candidate Apps using Admin GraphQL 2026-07 can encounter Markets configured with country-subdivision regions, such as states and provinces as merchants upgrade to market-driven shipping. Use MarketRegionSubdivision as the stable country-subdivision region type, and read sub-region membership through market.conditions.regionsCondition.regions ....
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-07-01 - [Shop Minis May June 2026 update](https://shopify.dev/changelog/shop-minis-may-june-2026-update)
  - Source: Shopify developer changelog; route: Shopify Flow and Functions; categories: API, New, Shop Minis
  - Note: New Features Product variant intents The React SDK added typed product variant intent hooks for selecting variants, adding variants to cart, and sending buyers to express checkout: useSelectVariant wraps select:shopify/ProductVariant . useAddToCart wraps add_to_cart:shopify/ProductVariant . useBuyNow wraps buy_now:shopify/ProductVariant . These hooks can open the native Shop variant selector sheet over the Mini WebV...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-07-01 - [Discount application information now available for draft orders on the Customer Account API](https://shopify.dev/changelog/discount-application-information-now-available-for-draft-orders-on-the-customer-account-api)
  - Source: Shopify developer changelog; route: Shopify Flow and Functions; categories: API, New, Customer Account API, 2026-07
  - Note: As of GraphQL Customer Account API version 2026-07, draft orders now expose discount applications. You can use the new discountApplications field on DraftOrder to query discounts applied to a draft order, and the new discountAllocations field on DraftOrderLineItem to query how discounts are allocated across line items. For example: query DraftOrderDiscounts($id: ID!) { draftOrder(id: $id) { discountApplications(firs...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-07-01 - [Merchant-owned delivery profile APIs are deprecated for market-driven shipping](https://shopify.dev/changelog/merchant-owned-delivery-profile-apis-are-deprecated-for-market-driven-shipping)
  - Source: Shopify developer changelog; route: Shopify Flow and Functions; categories: Action Required, API, Deprecation Announcement, Admin GraphQL API, 2026-07
  - Note: What's changing We're moving merchant-owned shipping configuration from legacy delivery profiles to Markets as part of market-driven shipping, a new model where shipping is configured per Market. When a shop uses market-driven shipping, the legacy delivery profile fields and mutations in the Admin GraphQL API no longer represent the shop's live merchant-owned shipping configuration. Reads may return a stale snapshot...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [Apps can now open Shopify's file picker with the Intents API](https://shopify.dev/changelog/intents-api-file-picker)
  - Source: Shopify developer changelog; route: Shopify Flow and Functions; categories: Tools, New, Admin Extensions, App Bridge
  - Note: Apps can now open Shopify's native file picker with the Intents API. This lets your app prompt merchants to choose files from their Shopify file library without building a custom picker or sending them through a separate flow. With a single API call, your app can open the file picker, optionally filter by media type, enable multiple selection, and preselect files. When the merchant finishes selecting files, your app...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [Purchase-type filtering now enforced for app discounts](https://shopify.dev/changelog/purchase-type-filtering-now-enforced-for-app-discounts)
  - Source: Shopify developer changelog; route: Shopify Flow and Functions; categories: API, New, Admin GraphQL API
  - Note: The appliesOnSubscription and appliesOnOneTimePurchase fields on app discounts are now enforced at checkout. Previously, these fields existed on DiscountCodeAppInput and DiscountAutomaticAppInput but had no effect. All app discounts applied to every line item regardless of purchase type. What changed If an app discount is configured with appliesOnSubscription: false , it will only apply to one-time purchase line ite...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [Monitor admin web vitals in the Dev Dashboard](https://shopify.dev/changelog/monitor-admin-web-vitals-in-the-dev-dashboard)
  - Source: Shopify developer changelog; route: Shopify Flow and Functions; categories: Tools, Update
  - Note: Your app's admin performance data is now available in the Dev Dashboard, alongside your existing monitoring tools. This change eliminates the need to switch between Partner Dashboard tabs to check web vitals. What's changed The admin performance dashboards have moved from the Partner Dashboard to the Dev Dashboard. You can now access daily and 28-day P75 rollups for three Core Web Vitals: LCP (Largest Contentful Pai...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-13 - [Shop User Metafields in Shopify Functions](https://shopify.dev/changelog/shop-user-metafields-in-shopify-functions)
  - Source: Shopify developer changelog; route: Shopify Flow and Functions; categories: API, New, Functions, 2026-07
  - Note: Shop User is Shopify's cross-merchant buyer identity. Partners who use metafields on Shop Users can now read those metafields during checkout using Shopify Functions. To learn more, see the Shop User metafields guide in the Shopify developer documentation: https://shopify.dev/docs/api/shop/guides/use-cases/metafields
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-05-20 - [Shop Minis March April 2026 update](https://shopify.dev/changelog/shop-minis-march-april-2026-update)
  - Source: Shopify developer changelog; route: Shopify Flow and Functions; categories: API, Update, Shop Minis
  - Note: New Features Optional Consent Users can now reject scopes and continue using your Mini. Consent is no longer all-or-nothing - if a user declines a scope, your Mini should gracefully degrade rather than block the experience. If your Mini hard-fails when a scope is rejected, please update it using the new hooks below. useCheckScopesConsent Hook Check at runtime which scopes a user has granted. Use this to conditionall...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.

- [AUTO-CURATED] 2026-07-07 - [Shopify Flow: Changes to Action extensions result in fewer breaking changes](https://shopify.dev/changelog/shopify-flow-changes-to-action-extensions-result-in-fewer-breaking-changes)
  - Source: Shopify developer changelog; route: Shopify Flow and Functions; categories: Tools, Update, 2026-07
  - Note: Your server-side code now has more control over how breaking changes to an action's configuration fields are handled. Instead of failing validation when there's a field mismatch, workflows that use older versions of an action will continue to execute, and Shopify will still send the request to the configured endpoint URL. Your server can then decide how to handle schema differences: for example, it can set default v...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-07-07 - [Shopify Flow: Action runtime URLs now update automatically](https://shopify.dev/changelog/shopify-flow-action-runtime-urls-now-update-automatically)
  - Source: Shopify developer changelog; route: Shopify Flow and Functions; categories: Tools, Update, 2026-07
  - Note: Shopify Flow now resolves an action's runtime_url on every execution. When the runtime_url is changed and the app is redeployed, the new URL is automatically used by existing workflows the next time they run. Merchants no longer need to edit or re-save their workflows to use the updated URL. During local development, when you use shopify app dev , the runtime_url is also updated automatically in any development shop...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-07-02 - [Deprecating the useBuyerJourneyIntercept API on checkout UI extensions](https://shopify.dev/changelog/deprecating-the-usebuyerjourneyintercept-api-on-checkout-ui-extensions)
  - Source: Shopify developer changelog; route: Shopify Flow and Functions; categories: Action Required, Polaris, Deprecation announcement, 2026-07
  - Note: Starting in version 2026-07 , the useBuyerJourneyIntercept hook on checkout UI extensions, and the block_progress capability it depends on, are deprecated. Existing extensions will continue to work on current and prior API versions, but this API will be removed in a future version , so you should plan to migrate. The following are deprecated: useBuyerJourneyIntercept (Preact hook) in checkout UI extensions The block...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
<!-- END AUTO-CURATED UPDATES -->

## Canonical validation rule

- Shopify developer/API behavior: validate through Shopify Dev MCP and `shopify.dev`.
- Shopify merchant/admin behavior: validate against `help.shopify.com`, `changelog.shopify.com`, or live Admin evidence where available.
- AnyDB behavior: validate against AnyDB MCP/docs and public release notes before build-ready artifacts.

## Reviewed vendor updates

- [REVIEWED] 2026-06-18 - [Flow action extensions now support relative paths for endpoint URLs](https://shopify.dev/changelog/flow-action-extensions-now-support-relative-paths-for-endpoint-urls)
  - Note: Relative endpoint paths are supported for Flow action extensions and resolve differently in development versus production.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.
