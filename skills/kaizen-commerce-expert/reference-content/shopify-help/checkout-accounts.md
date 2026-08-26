# Shopify Checkout and Customer Accounts

Generated Kai vendor freshness note. Use this file for navigation and recent-change awareness only.
Validate current behavior through the canonical vendor source before production guidance.

## Recent feature updates (auto-curated)

<!-- BEGIN AUTO-CURATED UPDATES -->
- [AUTO-CURATED] 2026-06-17 - [Customer accounts get a design uplift](https://changelog.shopify.com/posts/customer-accounts-get-a-design-uplift)
  - Source: Shopify merchant changelog; route: Shopify Checkout and Customer Accounts; categories: Customer-account
  - Note: Customer account pages get a design uplift that makes it easier for your customers to navigate their account, track orders, and take actions. The refreshed pages now use a streamlined single-column layout, feature more intuitive and accessible navigation, and include mobile-first optimizations. What's new for your buyer experience Account menus with up to 4 navigation links are now displayed inline on mobile , at th...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-11 - [Unlink a customer from your custom identity provider](https://changelog.shopify.com/posts/unlink-a-customer-from-your-custom-identity-provider)
  - Source: Shopify merchant changelog; route: Shopify Checkout and Customer Accounts; categories: Customer-account
  - Note: If your store uses a connected OpenID Connect (OIDC) identity provider for customer accounts (such as Okta, Auth0, Microsoft Entra ID), you can now unlink a customer from your identity provider directly in the Shopify admin. When a customer's account is linked to the wrong subject in your identity provider, the customer might see the following error when they try to sign in: "The sign-in method you used doesn't matc...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-05 - [Schedule, publish, and A/B test new themes and checkout and customer account configurations](https://changelog.shopify.com/posts/schedule-publish-and-a-b-test-new-themes-and-checkout-and-customer-account-configurations)
  - Source: Shopify merchant changelog; route: Shopify Checkout and Customer Accounts; categories: Admin
  - Note: Rollouts now supports scheduling, gradually publishing and A/B testing your themes and checkout and customer accounts configurations. You can now: 1. Schedule an entire new checkout or theme to go live at a specific date and time. For example, switch from Dawn to Horizon on a specific date. 2. Temporarily swap to a different theme or checkout setup. For example, activating a BFCM theme for one week with automatic re...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
<!-- END AUTO-CURATED UPDATES -->

## Canonical validation rule

- Shopify developer/API behavior: validate through Shopify Dev MCP and `shopify.dev`.
- Shopify merchant/admin behavior: validate against `help.shopify.com`, `changelog.shopify.com`, or live Admin evidence where available.
- AnyDB behavior: validate against AnyDB MCP/docs and public release notes before build-ready artifacts.

## Reviewed vendor updates

- [REVIEWED] 2026-05-20 - [A refreshed sign-in page for customer accounts, now customizable in the editor](https://changelog.shopify.com/posts/draft-a-refreshed-sign-in-page-for-customer-accounts-now-customizable-in-the-editor)
  - Note: The refreshed customizable sign-in layout applies to new customer accounts; legacy-account merchants must confirm migration readiness.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.
