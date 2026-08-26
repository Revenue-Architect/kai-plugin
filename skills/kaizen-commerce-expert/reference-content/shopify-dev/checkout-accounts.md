# Shopify Checkout and Customer Accounts

Generated Kai vendor freshness note. Use this file for navigation and recent-change awareness only.
Validate current behavior through the canonical vendor source before production guidance.

## Recent feature updates (auto-curated)

<!-- BEGIN AUTO-CURATED UPDATES -->
- [AUTO-CURATED] 2026-07-01 - [`discountedUnitPrice` on `DraftOrderLineItem` Customer Account API deprecation](https://shopify.dev/changelog/discountedunitprice-on-draftorderlineitem-customer-account-api-deprecation)
  - Source: Shopify developer changelog; route: Shopify Checkout and Customer Accounts; categories: API, Deprecation Announcement, Customer Account API, 2026-07
  - Note: The discountedUnitPrice field on the DraftOrderLineItem object in the Customer Account API is now deprecated. Use approximateDiscountedUnitPrice instead. This new field calculates the discounted total divided by the quantity, resulting in an approximate per-unit price reduction. Update your queries to use approximateDiscountedUnitPrice .
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [Built for Shopify requirements for Returns and exchanges apps and Subscription apps (effective December 1, 2026)](https://shopify.dev/changelog/built-for-shopify-requirements-for-returns-and-exchanges-and-subscription-apps)
  - Source: Shopify developer changelog; route: Shopify Checkout and Customer Accounts; categories: Action Required, Built for Shopify, Update
  - Note: Effective December 1, 2026 , Returns and exchanges apps and Subscription apps that provide buyer-facing self-service experiences must authenticate customers using the Customer Account API. Apps that don't meet this requirement by the deadline are at risk of losing Built for Shopify status . What's changing Returns and exchanges and Subscription apps with buyer-facing self-service experiences must use the Customer Ac...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-11 - [Shopify AI Toolkit for upgrading extensions to Polaris web components](https://shopify.dev/changelog/shopify-ai-toolkit-for-upgrading-extensions-to-polaris-web-components)
  - Source: Shopify developer changelog; route: Shopify Checkout and Customer Accounts; categories: Action Required, Tools, Update
  - Note: The Shopify AI Toolkit now supports upgrading checkout and customer account UI extensions to new API versions, including the migration to Polaris web components. Use the AI Toolkit with your preferred AI coding agent to skip repetitive manual work and speed up the heavy lifting. Your agent will leverage the Shopify AI Toolkit, paired with our enhanced developer documentation, to go through the required migration ste...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-08 - [Headless checkout SSO is now documented with sso=silent](https://shopify.dev/changelog/headless-checkout-sso-is-now-documented-with-ssosilent)
  - Source: Shopify developer changelog; route: Shopify Checkout and Customer Accounts; categories: API, New, Customer Account API, Hydrogen, Storefront GraphQL API
  - Note: We've updated our headless checkout authentication docs to refer to the silent single sign-on query parameter as sso=silent instead of logged_in=true . This is a terminology and documentation update only. Existing checkout URLs that use logged_in=true will continue to work. Going forward, Shopify docs and examples will use sso=silent when describing the silent SSO flow from a headless storefront to checkout. Learn m...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.

- [AUTO-CURATED] 2026-07-06 - [Customer Account API Customer.lastIncompleteCheckout and Checkout types removed in 2026-10](https://shopify.dev/changelog/customer-account-api-last-incomplete-checkout-and-checkout-types-removed)
  - Source: Shopify developer changelog; route: Shopify Checkout and Customer Accounts; categories: Action Required, API, Breaking API Change, Customer Account API, 2026-10
  - Note: As of Customer Account API version 2026-10, the deprecated Customer.lastIncompleteCheckout field is removed. This also removes the now-unreachable Customer Account API Checkout type subtree, including: Checkout Checkout.appliedGiftCards AppliedGiftCard AvailableShippingRates CheckoutLineItem CheckoutLineItemConnection CheckoutLineItemEdge ShippingRate The Customer.lastIncompleteCheckout field was previously deprecat...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-05-13 - [Checkout And Accounts Configuration API for unified branding across checkout, customer accounts, and sign-in](https://shopify.dev/changelog/checkout-and-accounts-configuration-api-for-unified-branding-across-checkout-customer-accounts-and-sign-in)
  - Source: Shopify developer changelog; route: Shopify Checkout and Customer Accounts; categories: API, New, Admin GraphQL API, 2026-04
  - Note: As of API version 2026-04, the new Checkout And Accounts Configuration API is now available to unlock consistent branding customizations across checkout, customer accounts, and sign-in surfaces. This API is exclusively available to Shopify Plus merchants. This new API replaces the Checkout Profile API and Checkout Branding API (both are now deprecated). All capabilities to customize settings and branding for checkou...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
<!-- END AUTO-CURATED UPDATES -->

## Canonical validation rule

- Shopify developer/API behavior: validate through Shopify Dev MCP and `shopify.dev`.
- Shopify merchant/admin behavior: validate against `help.shopify.com`, `changelog.shopify.com`, or live Admin evidence where available.
- AnyDB behavior: validate against AnyDB MCP/docs and public release notes before build-ready artifacts.

## Reviewed vendor updates

- [REVIEWED] 2026-05-20 - [Feature preview: Customer account improvements](https://shopify.dev/changelog/feature-preview-customer-account-improvements)
  - Note: Feature preview only; test existing customer-account extensions against the refreshed layout before any rollout recommendation.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.

- [REVIEWED] 2026-07-01 - [Market-driven shipping now available in feature preview](https://shopify.dev/changelog/market-driven-shipping-now-available-in-feature-preview)
  - Note: Feature preview with staged rollout; audit assumptions around delivery profiles and Markets before migration or app changes.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.

- [REVIEWED] 2026-04-23 - [Ship and pickup in one order now available in feature preview](https://shopify.dev/changelog/ship-and-pickup-in-one-order-feature-preview)
  - Note: Plus and Enterprise feature preview; apps must test multiple delivery groups and mixed shipping/pickup fulfillment assumptions.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.
