# Shopify Admin API

Generated Kai vendor freshness note. Use this file for navigation and recent-change awareness only.
Validate current behavior through the canonical vendor source before production guidance.

## Recent feature updates (auto-curated)

<!-- BEGIN AUTO-CURATED UPDATES -->
- [AUTO-CURATED] 2026-07-03 - [OrderDisplayFulfillmentStatus now returns FULFILLMENT_NOT_REQUIRED for orders with no items to fulfill](https://shopify.dev/changelog/orderdisplayfulfillmentstatus-now-returns-fulfillmentnotrequired)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, Update, Admin GraphQL API, 2026-10
  - Note: As of API version 2026-10, the OrderDisplayFulfillmentStatus enum can return a new value: FULFILLMENT_NOT_REQUIRED . It is returned for orders that are not fulfilled but have no items remaining to fulfill - for example, an order that was fully cancelled or fully refunded before any items were fulfilled. Previously, these orders returned UNFULFILLED . This is a backward-compatible, additive change: integrations that...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-07-01 - [Draft order deposit fields are now available in the GraphQL Admin API and Customer Account API](https://shopify.dev/changelog/draft-order-deposit-fields-now-available-in-the-admin-and-customer-account-graphql-apis)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, New, Admin GraphQL API, Customer Accounts, 2026-07
  - Note: As of the 2026-07 API version, draft order deposit fields are available in the GraphQL Admin API and Customer Account API. Apps can now set a deposit when creating or updating a draft order with DraftOrderInput.deposit in the GraphQL Admin API. This supports draft order flows where part of the payment is due at checkout and the remaining balance is due later, such as due-on-fulfillment payment terms. The Customer Ac...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-07-01 - [Deprecation of cumulative marketing engagements](https://shopify.dev/changelog/deprecation-of-cumulative-marketing-engagements)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: Action Required, API, Deprecation Announcement, Admin GraphQL API, 2026-07
  - Note: The isCumulative argument to the marketingEngagementCreate mutation is being deprecated, defaulting to false . Please update your integration to send non-cumulative engagements, as needed. Existing activities that have been sending cumulative metrics can migrate to non-cumulative at any time.
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-07-01 - [New `lineItem` field on the `GiftCard` object](https://shopify.dev/changelog/new-lineitem-field-on-the-giftcard-graphql-object)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, New, Admin GraphQL API, 2026-07
  - Note: The GraphQL Admin API's GiftCard object now includes a lineItem field, representing the LineItem from the order that initiated the gift card's creation. The field returns null for gift cards that were issued manually instead of through an order.
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-07-01 - [`BusinessEntity` now exposes `legalEntityId` in the GraphQL Admin API](https://shopify.dev/changelog/businessentity-now-exposes-legalentityid-in-the-admin-api)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, New, Admin GraphQL API, 2026-07
  - Note: As of API version 2026-07 , the BusinessEntity type in the GraphQL Admin API includes a new legalEntityId field. This field returns the stable Central Legal Entity ID from Shopify's Organizations Platform, giving Partners a consistent identifier for the same legal entity across multiple shops, markets, and sales channels. What's new The BusinessEntity type now includes: legalEntityId ( BigInt , nullable): The stable...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-07-01 - [Market-driven shipping Admin API](https://shopify.dev/changelog/market-driven-delivery-profiles-admin-api)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, New, Admin GraphQL API, 2026-07
  - Note: Starting in API version 2026-07, the GraphQL Admin API supports market-driven shipping configuration. You can now configure shipping directly on a market, which helps apps support different shipping strategies for different markets without creating a separate shipping profile resource. What changed The Market object now includes a delivery field for market delivery settings. Use Market.delivery.shipping to read the...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-30 - [Configure order attribution for sales channel apps](https://shopify.dev/changelog/order-attribution-definitions-are-available-in-order-channel-filters)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, New, Admin Extensions, Admin GraphQL API, Storefront GraphQL API, 2026-07
  - Note: Starting in API version 2026-07 , sales channel apps can use order attribution definitions to identify the source that created an order. Order attribution definitions are useful when your sales channel app needs attribution that is more specific than the app or channel itself. For example, you can attribute orders to a marketplace, region, account, or surface. Apps that only need default app or channel attribution d...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-27 - [Payment mandates now expose an id field](https://shopify.dev/changelog/payment-mandates-id-field)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, New, Admin GraphQL API, 2026-07
  - Note: In API version 2026-07 and later, the PaymentMandateResource object includes a new id field. PaymentMandateResource is returned by the mandates connection on CustomerPaymentMethod . Its id is the same as the corresponding CustomerPaymentMethod.id , which lets you determine which payment method to use for a given mandate scope (for example, the SUBSCRIPTIONS scope) when a single payment instrument is associated with...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-26 - [Carrier services will no longer be automatically added to the default shipping profile](https://shopify.dev/changelog/carrier-services-will-no-longer-be-automatically-added-to-the-default-shipping-profile)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, Breaking API Change, Admin GraphQL API, Admin REST API, 2026-10
  - Note: Starting with GraphQL Admin API version 2026-10, creating a carrier service no longer automatically adds it to the shop's General shipping profile. This breaking change affects carrier services created using: GraphQL Admin API: carrierServiceCreate REST Admin API: POST /admin/api/{version}/carrier_services.json Previously, active API carrier services created through these APIs were automatically added to eligible sh...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-23 - [`DraftOrderDiscountNotAppliedWarning.priceRule` removed in GraphQL Admin API 2026-10](https://shopify.dev/changelog/remove-pricerule-from-draft-order-discount-warning)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: Action Required, API, Breaking API Change, Admin GraphQL API, 2026-10
  - Note: Starting with GraphQL Admin API version 2026-10 , the deprecated priceRule field on the DraftOrderDiscountNotAppliedWarning object is removed. This is a breaking change for apps that query priceRule on DraftOrderDiscountNotAppliedWarning , which is returned in draft order discount warnings from mutations such as draftOrderCalculate , draftOrderCreate , and draftOrderUpdate . If your app selects priceRule in these re...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-19 - [Removal of ITEM_NOT_STOCKED_AT_LOCATION error](https://shopify.dev/changelog/removal-of-itemnotstockedatlocation-error)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: Action Required, API, Breaking API Change, Admin GraphQL API, 2026-10
  - Note: The ITEM_NOT_STOCKED_AT_LOCATION error will be removed from InventoryAdjustQuantities , InventoryMoveQuantities , InventorySetOnHandQuantities , and InventorySetQuantitiesUserErrorCode as of API version 2026-10. Following the changes described here , inventory quantities can now be adjusted at any location. As a result, the condition that previously triggered ITEM_NOT_STOCKED_AT_LOCATION can no longer occur, and thi...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [New purchaseType and recurringCycleLimit fields in the discounts API for discount UI extensions](https://shopify.dev/changelog/new-purchasetype-and-recurringcyclelimit-fields-available-in-the-discount-ui-extension-api)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, New, Admin Extensions, 2026-04
  - Note: You can now configure purchaseType and recurringCycleLimit for app discounts directly from discount UI extensions using the discounts plugin. Previously, these fields were only accessible through the GraphQL Admin API. App developers building discount UI extensions had no way to let merchants control whether a discount applies to one-time purchases, subscriptions, or both, or how many subscription billing cycles a d...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [Admin GraphQL API now supports app-owned delivery profiles that cover all shippable items](https://shopify.dev/changelog/admin-graphql-api-now-supports-app-owned-delivery-profiles-that-cover-all-shippable-items)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, Update, Admin GraphQL API, 2026-07
  - Note: As of GraphQL Admin API version 2026-07, app-owned shipping delivery profiles support a new boolean coversAllItems field. Use coversAllItems on app-owned shipping delivery profiles to indicate that a profile applies to every shippable product variant in the store, without explicitly assigning each product or variant to that profile. The field is available on the DeliveryProfile type: query { deliveryProfiles(first:...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [Define and set metafields on inventory transfers in the GraphQL Admin API](https://shopify.dev/changelog/define-and-set-metafields-on-inventory-transfers-in-the-admin-graphql-api)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, New, Admin GraphQL API, 2026-07
  - Note: As of GraphQL Admin API version 2026-07 , you can define metafields for inventory transfers and set metafields directly when creating or editing transfers. Use MetafieldOwnerType.TRANSFER with metafield definition mutations to create transfer-specific metafield definitions. You can also pass metafields in the metafields input on the following mutations: inventoryTransferCreate inventoryTransferCreateAsReadyToShip in...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [Create channel markets with the GraphQL Admin API](https://shopify.dev/changelog/create-channel-markets-with-the-graphql-admin-api)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, New, Admin GraphQL API, 2026-07
  - Note: Starting in API version 2026-07 , the GraphQL Admin API supports channel markets. Apps can now create and update Markets that apply to one or more sales channels, then use existing catalog and market APIs to manage channel-specific product availability, pricing, and currency. This is an additive change. Existing apps don't need to make updates unless they create, query, or make assumptions about Markets or market ca...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [WhatsApp marketing consent now available in the Admin API and Customer Account API](https://shopify.dev/changelog/whatsapp-marketing-consent-now-available)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: Action Required, API, New, Admin GraphQL API, Customer Account API, Webhook, 2026-07
  - Note: WhatsApp marketing consent can now be managed through both the Customer Account and Admin APIs. Use the customerWhatsAppMarketingConsentUpdate mutation to update a customer's WhatsApp marketing consent status for their default phone number. You can read the current WhatsApp marketing consent value from the CustomerPhoneNumber object via the whatsAppMarketingConsent field. For more details on managing WhatsApp market...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [Bulk queries now execute up to 4X faster](https://shopify.dev/changelog/bulk-queries-now-execute-faster)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, Update, Admin GraphQL API
  - Note: Exporting large datasets from Shopify is now up to 4X faster, thanks to optimizations to bulk queries . Bulk operations are the most efficient way to import and export data from Shopify stores. Compared to synchronous use of the Admin API, you can build functionality faster with bulk operations, process large datasets in less time, and spend less on infrastructure. Other recent improvements to bulk operations includ...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [Buy Shipping Labels with the GraphQL Admin API](https://shopify.dev/changelog/label-purchase-mutation)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, New, Admin GraphQL API, 2026-07
  - Note: New shippingLabelPurchase mutation in the GraphQL Admin API The GraphQL Admin API now includes the shippingLabelPurchase mutation, which lets apps purchase Shopify Shipping labels for eligible fulfillment orders. Apps can provide the fulfillment order, shipping date and time, package details, total weight, customer notification preference, and optional preferred carrier/service selection. If a preferred rate isn't p...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-17 - [New Collection model and APIs now available](https://shopify.dev/changelog/new-collection-model-and-apis-now-available)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: Action Required, API, New, Admin GraphQL API, Functions, 2026-07
  - Note: The 2026-07 release replaces a collection's single ruleSet with a multi-source model in the GraphQL Admin API. Each collection now has one or more CollectionSource objects that define typed inclusion and exclusion conditions, plus manual selections. Shopify Functions also gain variant-level collection membership fields on the ProductVariant type. In API version 2026-07 and later, collections that use the new sources...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-16 - [New appSubscriptionCancel mutation in the Partner API](https://shopify.dev/changelog/new-appsubscriptioncancel-mutation-in-the-partner-api)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, New, 2026-07
  - Note: Starting with API version 2026-07, Partner API clients can use the new appSubscriptionCancel mutation to cancel app subscriptions for public apps they own. The mutation supports: Immediate cancellation Deferred cancellation at the end of the current billing cycle Requesting prorated credits, when applicable Optionally skipping the final usage charge for usage-billed subscriptions This mutation is available to Partne...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-11 - [Streamlined Metaobject API](https://shopify.dev/changelog/streamlined-metaobject-api)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, New, Admin GraphQL API, 2026-07
  - Note: It's now easier to work with metaobjects. With the new values property , you can fetch all fields of a metaobject in a single call without handling deserialization in your app. The API returns a JSON-compatible object that's ready to use directly. You can also use values when creating or updating metaobjects . Provide a JSON-style object that matches your metaobject's field keys, and the API handles serialization fo...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-05 - [`GiftCardCashOutTransaction` is now resolvable from `GiftCardTransaction`](https://shopify.dev/changelog/giftcardcashouttransaction-now-resolvable-from-giftcardtransaction)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, New, Admin GraphQL API, 2026-07
  - Note: Starting with GraphQL Admin API version 2026-07, the [ GiftCardCashOutTransaction ]( https://shopify.dev/docs/api/admin-graphql/2026-07/objects/GiftCardCashOutTransaction type is introduced as a new variant of the GiftCardTransaction interface. This type specifically represents transactions where a gift card balance is paid out through a point of sale (POS) system. In previous API versions, such as 2026-04 and earli...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-05 - [Local currency support gift cards now available in the GraphQL Admin API](https://shopify.dev/changelog/gift-card-local-currency-support)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, Update, Admin GraphQL API, 2026-07
  - Note: Starting in API version 2026-07 , the GraphQL Admin API supports local currency gift cards. You can create gift card products that are issued in a specific currency, and control whether buyers can redeem those gift cards across currencies. If your app creates gift cards directly, migrate from the deprecated initialValue field to initialAmount . What changed Use the new giftCardProductSet mutation to create and updat...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-06-05 - [Inventory transfer webhooks include origin and destination location IDs, and mutation documentation clarified](https://shopify.dev/changelog/inventory-transfer-webhooks-include-origin-and-destination-location-ids-and-mutation-documentation-clarified)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, Update, Admin GraphQL API, 2026-07
  - Note: Inventory transfer webhooks: new origin and destination fields Payloads for the following webhook topics now include the source and destination location of the transfer as Location Global IDs: inventory_transfers/add_items inventory_transfers/update_item_quantities inventory_transfers/remove_items inventory_transfers/ready_to_ship inventory_transfers/cancel inventory_transfers/complete Each payload now includes: ori...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-05-27 - [Build App Home as a UI extension](https://shopify.dev/changelog/build-app-home-as-a-ui-extension)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, New, Admin Extensions, 2026-07
  - Note: You can now create your app's landing page in App Home as a Preact-based admin UI extension using the new admin.app.home.render target. This means your App Home UI extensions are bundled with your other admin UI extensions, eliminating the need for a separate web server to render your app's primary workspace. Use this extension type when you want: A persistent, full-page app workspace that's integrated into your ext...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-05-21 - [Shopify CLI 4.0: SemVer, auto-updates, removing deprecated flags and commands](https://shopify.dev/changelog/shopify-cli-40-semver-auto-updates-removing-deprecated-flags-and-commands)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: Tools, Update
  - Note: The release of Shopify CLI 4.0 today brings clarity to CLI versioning, the introduction of automatic updates, and the announced removal of the deprecated --force flag from shopify app deploy . Semantic Versioning Shopify CLI is now following semantic versioning practices. Releases with new features will be minor versions, and bug fixes will be patch versions. When required, major version releases will be used to com...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-05-20 - [Expiring offline access tokens required for all public apps as of January 1, 2027](https://shopify.dev/changelog/expiring-offline-access-tokens-required-for-all-public-apps-as-of-january-1-2027)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: Action Required, API, Breaking API Change, Admin GraphQL API, Admin REST API
  - Note: We're changing how public apps handle offline access tokens to enhance merchant data protection. Starting January 1, 2027, all public apps must use expiring offline access tokens when calling the Admin API. After that date, public apps still using non-expiring tokens will receive authentication errors. This extends the April 1, 2026 change , which applied only to newly created public apps, to all public apps, includ...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-05-20 - [Removing deprecated PRIVATE and PUBLIC_READ enums on metaobject definitions](https://shopify.dev/changelog/removing-deprecated-private-and-publicread-enums-on-metaobject-definitions)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, Deprecation Announcement, Admin GraphQL API, 2026-10
  - Note: We are updating the MetaobjectAdminAccess enum by deprecating the PRIVATE and PUBLIC_READ values. These values are now obsolete and are never returned by the API. This change removes ambiguity, as the deprecated access values do not accurately reflect the intended access behaviors. There are no required changes, but updating your code will help maintain clarity and prevent potential access issues.
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-05-15 - [New `checkoutToken` field added to the `Order` object](https://shopify.dev/changelog/new-checkouttoken-field-added-to-the-order-object)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, New, Admin GraphQL API, 2026-07
  - Note: The checkoutToken field is now available on the GraphQL Admin API's Order object. This field returns the token associated with the checkout that was used to create the order, matching the existing checkout_token field in the REST Admin API.
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.

- [AUTO-CURATED] 2026-07-24 - [Invalid metafield queries now return errors in the GraphQL Admin API](https://shopify.dev/changelog/invalid-metafield-queries-now-return-errors-in-the-graphql-admin-api)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: Action Required, API, Breaking API Change, Admin GraphQL API, Metafields and metaobjects, 2026-10
  - Note: Starting in API version 2026-10, the GraphQL Admin API returns an error when a query filters by a metafield that isn't set up for filtering, instead of silently returning incorrect results. This is a breaking change. It affects apps that filter resources by metafield on version 2026-10 or later, and you'll need to update affected queries before you upgrade. What changed In API version 2026-10 and later, the GraphQL...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-07-16 - [Card deposit endpoint now requires mTLS certificate](https://shopify.dev/changelog/card-deposit-endpoint-now-requires-mtls-certificate)
  - Source: Shopify developer changelog; route: Shopify Admin API; categories: API, Update
  - Note: Shopify's card-deposit endpoint now requires a Shopify-issued mTLS client certificate. Apps that store cardholder data with the customerPaymentMethodCreditCardCreate and customerPaymentMethodCreditCardUpdate GraphQL Admin API mutations must first deposit that data at Shopify's /sessions card-deposit endpoint to receive a session identifier. That deposit call must present a Shopify-issued certificate by October 15, 2...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
<!-- END AUTO-CURATED UPDATES -->

## Canonical validation rule

- Shopify developer/API behavior: validate through Shopify Dev MCP and `shopify.dev`.
- Shopify merchant/admin behavior: validate against `help.shopify.com`, `changelog.shopify.com`, or live Admin evidence where available.
- AnyDB behavior: validate against AnyDB MCP/docs and public release notes before build-ready artifacts.

## Reviewed vendor updates

- [REVIEWED] 2026-04-29 - [Analytics metric targets now available in the GraphQL Admin API](https://shopify.dev/changelog/analytics-metric-targets-now-available-in-the-graphql-admin-api)
  - Note: Shipped GraphQL operations for reading, creating, updating, and deleting Analytics metric targets; validate the target API version before implementation.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.

- [REVIEWED] 2026-05-08 - [More admin intents now support Settings](https://shopify.dev/changelog/more-admin-intents-now-support-settings)
  - Note: Seven additional Settings intents can open contextual admin settings; validate supported intents against current docs.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.

- [REVIEWED] 2026-05-19 - [Next Generation Events now available in developer preview](https://shopify.dev/changelog/next-generation-events-now-available-in-developer-preview)
  - Note: Developer preview only; field-level filtering and custom webhook payloads require preview-specific validation.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.

- [REVIEWED] 2026-05-18 - [Shipping line field now available on FulfillmentOrderLineItem](https://shopify.dev/changelog/shipping-line-field-now-available-on-fulfillmentorderlineitem)
  - Note: Available in Admin API 2026-07; use the shippingLine field only after version-specific schema validation.
  - Freshness rule: preserve stated preview, rollout, plan, country, and API-version caveats.
