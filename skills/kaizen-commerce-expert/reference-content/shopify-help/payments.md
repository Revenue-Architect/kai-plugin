# Shopify Payments

Generated Kai vendor freshness note. Use this file for navigation and recent-change awareness only.
Validate current behavior through the canonical vendor source before production guidance.

## Recent feature updates (auto-curated)

<!-- BEGIN AUTO-CURATED UPDATES -->
- [AUTO-CURATED] 2026-07-01 - [Brazil CNPJ validation now supports alphanumeric identifiers](https://changelog.shopify.com/posts/brazil-cnpj-validation-now-supports-alphanumeric-identifiers)
  - Source: Shopify merchant changelog; route: Shopify Payments; categories: Checkout
  - Note: We've updated Brazil CNPJ validation to support Receita Federal's new alphanumeric CNPJ format. New CNPJs can include letters or numbers in the first 12 positions while keeping numeric check digits in the final two positions. Existing numeric CNPJs continue to validate as before. For example, Shopify can now validate alphanumeric CNPJs such as 12.ABC.345/01DE-35 . Partners or apps that validate CNPJ values should ma...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-22 - [Checkout email field: new saved indicator and tooltip](https://changelog.shopify.com/posts/checkout-email-field-new-saved-indicator-and-tooltip)
  - Source: Shopify merchant changelog; route: Shopify Payments; categories: Admin
  - Note: We've added a new saved indicator to the email field at checkout. When a buyer enters their email, a tooltip now shows a short note explaining how it's used; for order confirmation and cart reminders, along with a brief saved label once entered. This gives buyers clearer visual feedback that their information was saved and its intended use, helping build confidence and trust.
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [Updated disclosure for subscription purchases on Checkout](https://changelog.shopify.com/posts/updated-disclosure-for-subscription-purchases-on-checkout)
  - Source: Shopify merchant changelog; route: Shopify Payments; categories: Admin
  - Note: As checkout evolves over time, we refine defaults to keep your buyer experience clear and consistent. This update refines the disclosure so your buyers see up-to-date information about subscriptions at checkout. As part of this change, we will begin using the following new translation keys for this disclosure: * Purchase options subscription agreement label * Purchase options subscription consent text * Purchase opt...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [Flow: Automatic charging for vaulted payment methods](https://changelog.shopify.com/posts/flow-automatic-charging-for-vaulted-payment-methods)
  - Source: Shopify merchant changelog; route: Shopify Payments; categories: B2b
  - Note: The Charge vaulted payment for B2B order action charges a customer's vaulted credit card or debits a vaulted bank account for an order with payment terms when payment is due. Learn more about the Charge vaulted payment for B2B order Flow action in the Shopify Help Center .
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [Checkout Blocks: Prevent non-compliant shipping addresses at checkout](https://changelog.shopify.com/posts/checkout-blocks-block-non-compliant-shipping-addresses-at-checkout)
  - Source: Shopify merchant changelog; route: Shopify Payments; categories: Apps
  - Note: Address format validation in Checkout Blocks is now available to all merchants. Use the new checkout rule to block noncompliant shipping addresses. This can be found by going to Settings  Checkout  Checkout rules  Address format validation in the Shopify admin. Rules are enforced consistently in checkouts across online and agentic experiences. Buyers see an inline error and can't complete checkout until the address...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [Ship and pickup in one order available for Plus and Enterprise plans](https://changelog.shopify.com/posts/ship-and-pickup-in-one-order)
  - Source: Shopify merchant changelog; route: Shopify Payments; categories: Checkout
  - Note: Merchants on Plus and Enterprise plans can now offer customers the flexibility to select shipping and store pickup for different items within a single checkout. Previously, customers had to create separate orders for each delivery method. Customers can see all available delivery options for each item based on the shop's configured locations, inventory, and delivery methods. Customers can choose to ship or pick up al...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [Reduced bot noise in abandoned checkouts](https://changelog.shopify.com/posts/reduced-bot-noise-in-abandoned-checkouts)
  - Source: Shopify merchant changelog; route: Shopify Payments; categories: Admin
  - Note: When bots test your checkout with stolen card numbers and don't complete payment, Shopify no longer creates an abandoned checkout for that session. Previously, these bot attempts filled your recovery list with sessions that were never real customers. Now your abandoned checkout list stays focused on buyers who are worth following up with. Learn more about recovering abandoned checkouts .
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-13 - [Expanded multi-currency payout support in US, HK and SG](https://changelog.shopify.com/posts/expanded-multi-currency-payout-support-in-us-hk-and-sg)
  - Source: Shopify merchant changelog; route: Shopify Payments; categories: Payments
  - Note: We've expanded Multi-Currency Payouts for eligible Shopify Payments merchants. For the first time, merchants in the United States can receive payouts in multiple currencies, with support for CAD, EUR, AUD and GBP. We've also added more supported payout currencies in Singapore and Hong Kong: Singapore merchants can now receive payouts in EUR, GBP, and JPY, and Hong Kong merchants can now receive payouts in EUR, GBP,...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-05-30 - [Local payment methods are now available in more countries](https://changelog.shopify.com/posts/more-local-payment-methods-are-now-available-in-additional-countries)
  - Source: Shopify merchant changelog; route: Shopify Payments; categories: Payments
  - Note: Offering buyers a familiar, local way to pay can reduce friction and improve conversion at checkout. We've expanded the local payment methods available through Shopify Payments to more countries across Europe and beyond. Depending on where your business is located, you can now offer: MobilePay Austria, Belgium, Bulgaria, Croatia, Cyprus, Czechia, Estonia, Finland, Greece, Hungary, Ireland, Italy, Latvia, Liechtenste...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-05-23 - [Clearer payout balance and reserve information in Shopify Payments](https://changelog.shopify.com/posts/clearer-payout-balance-and-reserve-information-in-shopify-payments)
  - Source: Shopify merchant changelog; route: Shopify Payments; categories: Payments
  - Note: We've updated the Shopify Payments Payouts page to make payout information easier to understand. The amount previously labeled To be paid is now labeled Payout balance , matching the language used across Finance. We've also added help text that explains how payout balance is calculated: payments minus refunds, disputes, and fees. If funds are held in reserve on your account, the Payouts page continues to show the re...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-05-15 - [Sell from multiple legal entities in the same country using Shopify Payments](https://changelog.shopify.com/posts/sell-from-multiple-legal-entities-in-the-same-country-using-shopify-payments)
  - Source: Shopify merchant changelog; route: Shopify Payments; categories: Admin
  - Note: Merchants with more complex business structures can now sell from multiple legal entities in the same country using Shopify Payments. Previously, merchants often needed separate stores or expansion store workarounds when different parts of their business operated under different legal entities in the same country. Now, eligible merchants can configure multiple Shopify Payments accounts within a single store using Ma...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.

- [AUTO-CURATED] 2026-07-24 - [New app-added annotations on your analytics charts](https://changelog.shopify.com/posts/new-app-added-annotations-on-your-analytics-charts)
  - Source: Shopify merchant changelog; route: Shopify Payments; categories: Analytics
  - Note: Apps can now add business context directly to your analytics charts with annotations . Annotations mark important events on a specific date or date range, such as a product launch, collection launch, marketing campaign, discount, checkout offer, supplier change, landing page launch, payment method change, popup store, market launch, program change, or business milestone. When an app adds an annotation, we will displ...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
<!-- END AUTO-CURATED UPDATES -->

## Canonical validation rule

- Shopify developer/API behavior: validate through Shopify Dev MCP and `shopify.dev`.
- Shopify merchant/admin behavior: validate against `help.shopify.com`, `changelog.shopify.com`, or live Admin evidence where available.
- AnyDB behavior: validate against AnyDB MCP/docs and public release notes before build-ready artifacts.

## Reviewed vendor updates

- [REVIEWED] 2026-05-12 - [All Shopify Payments payment methods now available in Shop Pay checkout.](https://changelog.shopify.com/posts/more-shopify-payments-methods-available-in-shop-pay-checkout)
  - Note: Shop Pay supports additional Shopify Payments local and regional methods; availability still depends on market, currency, and payment-method eligibility.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.
