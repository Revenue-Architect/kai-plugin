# Shopify Flow and Merchant Automation

Generated Kai vendor freshness note. Use this file for navigation and recent-change awareness only.
Validate current behavior through the canonical vendor source before production guidance.

## Recent feature updates (auto-curated)

<!-- BEGIN AUTO-CURATED UPDATES -->
- [AUTO-CURATED] 2026-05-20 - [View cumulative metrics over time in Analytics](https://changelog.shopify.com/posts/view-cumulative-metrics-over-time-in-analytics)
  - Source: Shopify merchant changelog; route: Shopify Flow and Merchant Automation; categories: Analytics
  - Note: We've added cumulative metrics to Analytics so you can see how your metrics build up over time. When you turn on the Cumulative toggle in the Visualization panel (or add WITH CUMULATIVE_VALUES to your ShopifyQL query), your time-series chart shows a running total instead of individual daily values making it easy to see progress toward a goal or how a metric is trending across a period. Cumulative view works in three...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-05-14 - [Flow: Make test events for your workflows with existing shop data](https://changelog.shopify.com/posts/flow-sidekick-generates-test-cases-for-your-workflows)
  - Source: Shopify merchant changelog; route: Shopify Flow and Merchant Automation; categories: Apps
  - Note: You can now more easily test workflows with existing shop data. Suppose that a recent order was fraudulent and you've built a workflow to block the next one. You can choose that fraudulent order and see if it works. You can also add tests to make sure it doesn't block other other orders. Additionally, by clicking "Generate test events", Sidekick will analyze the workflow and find real shop data to test the logical p...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.

- [AUTO-CURATED] 2026-07-10 - [Flow: Copy and paste steps in your workflows](https://changelog.shopify.com/posts/flow-copy-and-paste-steps-in-your-workflows)
  - Source: Shopify merchant changelog; route: Shopify Flow and Merchant Automation; categories: Apps
  - Note: Building workflows often means recreating steps you've already set up somewhere else. Now you can copy an existing step and paste it, instead of rebuilding it from scratch. Select an action or condition step and use Cmd/Ctrl+C to copy it, then Cmd/Ctrl+V to paste. Flow keeps the copied step's configuration field values and, for conditions, its logic-so a pasted step arrives ready to use with only minor edits. You ca...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
<!-- END AUTO-CURATED UPDATES -->

## Canonical validation rule

- Shopify developer/API behavior: validate through Shopify Dev MCP and `shopify.dev`.
- Shopify merchant/admin behavior: validate against `help.shopify.com`, `changelog.shopify.com`, or live Admin evidence where available.
- AnyDB behavior: validate against AnyDB MCP/docs and public release notes before build-ready artifacts.

## Reviewed vendor updates

- [REVIEWED] 2026-05-19 - [Create SMS marketing automations in Shopify Messaging](https://changelog.shopify.com/posts/create-sms-marketing-automations-in-shopify-messaging)
  - Note: Shopify Messaging supports SMS automations, subject to sender registration, consent, country, and channel requirements.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.

- [REVIEWED] 2026-06-17 - [Smart delivery in Shopify Messaging](https://changelog.shopify.com/posts/smart-delivery-in-shopify-messaging)
  - Note: Smart delivery filters Shopify Messaging audiences using engagement signals and is enabled by default, with merchant controls.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.
