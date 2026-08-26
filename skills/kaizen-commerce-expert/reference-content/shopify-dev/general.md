# General

Reviewed vendor freshness notes. Validate the canonical source live before production guidance.

## Reviewed vendor updates

- [REVIEWED] 2026-05-06 - [App deployment in CI/CD is now available for all apps](https://shopify.dev/changelog/app-deployment-in-cicd-is-now-available-for-all-apps)
  - Note: Shipped app-scoped automation tokens for CI/CD deployment; confirm current Shopify CLI requirements before configuring pipelines.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.

- [REVIEWED] 2026-06-02 - [App quality checks now managed in Partner Dashboard](https://shopify.dev/changelog/app-quality-checks-now-managed-in-partner-dashboard)
  - Note: App quality checks and reviewer communication are now managed in Partner Dashboard under app distribution.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.

- [REVIEWED] 2026-04-15 - [Automatic CSS subsetting for `{% stylesheet %}` tags](https://shopify.dev/changelog/automatic-css-subsetting-for-stylesheet-tags)
  - Note: Shipped automatic CSS subsetting for stylesheet tags; themes should keep component styles colocated and test cross-section dependencies.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.

- [REVIEWED] 2026-06-17 - [Color palettes in Themes](https://shopify.dev/changelog/color-palettes)
  - Note: Themes can define a global color-palette setting; validate current theme schema syntax before implementation.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.

- [REVIEWED] 2026-05-28 - [Customize /llms.txt, /llms-full.txt and /agents.md](https://shopify.dev/changelog/customize-llmstxt-llms-fulltxt-and-agentsmd)
  - Note: Stores can customize machine-readable agents and LLM text endpoints through corresponding Liquid templates; validate theme behavior live.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.

- [REVIEWED] 2026-05-11 - [Shopify App Pricing: charge for usage, recurring subscriptions, or both](https://shopify.dev/changelog/shopify-app-pricing-charge-for-usage-recurring-subscriptions-or-both)
  - Note: Shopify App Pricing replaces Managed Pricing terminology and supports recurring, usage-based, or combined models in Partner Dashboard.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.

- [REVIEWED] 2026-06-17 - [New App Store requirements for Sidekick app extensions](https://shopify.dev/changelog/sidekick-app-extensions-app-store-requirements)
  - Note: App Store requirements now constrain Sidekick extensions to core app functionality and prohibit promotional or cross-sell behavior.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.

- [REVIEWED] 2026-06-17 - [Sidekick app extensions available today](https://shopify.dev/changelog/sidekick-app-extensions-available-today)
  - Note: Sidekick App Data and App Actions extensions are available; validate eligibility, scopes, and App Store requirements before use.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.

- [REVIEWED] 2026-04-23 - [Update to app uninstall reasons](https://shopify.dev/changelog/update-to-app-uninstall-reasons)
  - Note: Merchants must select a standardized uninstall reason; treat the resulting analytics as directional rather than perfect causal data.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.
