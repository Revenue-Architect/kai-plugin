# Shopify Custom Data

Generated Kai vendor freshness note. Use this file for navigation and recent-change awareness only.
Validate current behavior through the canonical vendor source before production guidance.

## Recent feature updates (auto-curated)

<!-- BEGIN AUTO-CURATED UPDATES -->
- [AUTO-CURATED] 2026-06-16 - [Metafields now require a definition to be accessed through the Customer Account API](https://shopify.dev/changelog/metafields-now-require-a-definition-to-be-accessed-through-the-customer-account-api)
  - Source: Shopify developer changelog; route: Shopify Custom Data; categories: Action Required, Platform, Update
  - Note: Starting today, metafields stored on the app resource must have a metafield definition and customer accounts permissions to be accessible through the Customer Account API. Going forward, when calling the Customer Accounts API, app metafields without a definition will no longer return a value. If your app has functionality which depends on these fields, update those metafields to use definitions with the Customer Acc...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
<!-- END AUTO-CURATED UPDATES -->

## Canonical validation rule

- Shopify developer/API behavior: validate through Shopify Dev MCP and `shopify.dev`.
- Shopify merchant/admin behavior: validate against `help.shopify.com`, `changelog.shopify.com`, or live Admin evidence where available.
- AnyDB behavior: validate against AnyDB MCP/docs and public release notes before build-ready artifacts.
