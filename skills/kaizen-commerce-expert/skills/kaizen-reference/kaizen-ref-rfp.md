---
name: kaizen-ref-rfp
description: "Deep retail reference for rfp questions routed by Kai."
metadata_version: 1
layer: retail-reference
upstream: ["kaizen-retail-expert-v2"]
downstream: []
adjacent: []
canon: []
owns: ["rfp domain reference"]
does_not_own: ["final implementation recommendation without routed skill context"]
---

### 3J. Common RFP Answers

---

#### Common RFP/RFI Answers

##### Q: Describe your POS capabilities for in-store selling.

Shopify POS is a cloud-based, mobile point-of-sale system that unifies in-store and online selling on a single platform. Key capabilities:
- Hardware flexibility: Runs on iPad, Android tablets, iPhone (Tap to Pay), and POS Go
- Payment processing: tap (NFC), chip (EMV), swipe, cash, gift cards, custom payment methods, split payments
- Smart grid: Customizable home screen with quick-access tiles
- Staff management: Unlimited PINs, role-based permissions (POS Pro), per-staff attribution
- Customer profiles: Unified across online and in-store
- Omnichannel: BOPIS, ship-from-store, local delivery, endless aisle (POS Pro)
- Offline capability: Cash sales during network interruptions; catalog cached locally
- Extensibility: POS UI Extensions API for custom functionality

Plan tiers: POS Lite (free) provides core selling. POS Pro ($89/month per location) adds advanced inventory, staff management, omnichannel, exchanges, detailed reporting.

##### Q: Does the POS support offline transactions?

Supported (with limitations). Cash transactions work during network interruptions using locally cached product catalog and customer data. Card-present transactions require network connectivity for authorization (industry standard). When connectivity returns, all cached data and queued transactions synchronize automatically. For environments with unreliable connectivity, we recommend Shopify's POS Go device which supports WiFi connectivity, or establishing dedicated network infrastructure.

##### Q: How does the POS handle returns and exchanges?

Returns available on all POS plans: look up original orders, select items, process refunds to original payment, store credit, or cash. Exchanges (POS Pro): swap items in single transaction, calculate price differences. Cross-channel returns supported (buy online, return in store). Restocking options: restock returned items or mark as damaged (not restocked).

##### Q: Describe the POS hardware requirements.

iPad (7th gen+), iPad Air (3rd gen+), iPad mini (5th gen+), iPad Pro (all). Android tablets with Android 10+. iPhone (XS+, iOS 16.4+) for Tap to Pay. POS Go (all-in-one handheld). Peripherals: thermal receipt printers, barcode scanners, cash drawers, label printers, retail stands. Card readers: Shopify Tap & Chip Reader (Bluetooth, NFC + EMV + swipe). Requires Shopify Payments.

##### Q: How does the platform manage inventory across multiple locations?

Supported (OOTB). Unlimited locations (warehouses, stores, pop-ups, fulfillment centers, 3PLs). Real-time synchronization across all sales channels. Variant-level tracking per location. Five inventory states (available, committed, incoming, reserved, unavailable). Full GraphQL API, webhooks, and reporting (ABC analysis, adjustment history, turnover metrics).

##### Q: Does the platform support inventory transfers between locations?

Supported (OOTB with POS Pro). Create transfers, lifecycle tracking (Pending, In Transit, Received), partial receiving, full audit trail, GraphQL API support (`inventoryTransferCreate` mutation), POS receiving and sending.

##### Q: How does inventory integrate with third-party systems?

GraphQL Admin API (`inventoryAdjustQuantities` for incremental, `inventorySetQuantities` for absolute sync), webhooks for real-time events, middleware partners (Celigo, MuleSoft, Pipe17), 500+ inventory apps, Fulfillment Services API for 3PLs. Supports Shopify-as-master, external-as-master, and bidirectional sync with optimistic concurrency controls.

##### Q: What inventory features are NOT natively supported?

Batch/lot tracking with expiry, serialized inventory, demand forecasting, complex UoM, warehouse task management, consignment, advanced routing optimization. All addressable through app ecosystem and API. Recommended partners: Katana (manufacturing/batch), SKULabs (serialized), Inventory Planner (forecasting), ShipHero (WMS).

##### Q: Does the platform support BOPIS?

Supported (OOTB with POS Pro). Customer selects "Pick up" at online checkout, system verifies inventory, store staff receive notification, pick items (with barcode verification), mark as ready, customer collects. Configurable pickup instructions per location, estimated ready times, and automated customer communications.

##### Q: Does the platform support Ship from Store?

Supported (OOTB with POS Pro). Order routing selects optimal fulfillment location based on inventory availability, customer proximity, and merchant rules. Store staff pick, pack, and ship from their location. Tracking updated automatically.

##### Q: How does the platform handle multi-location fulfillment and order routing?

Supported (OOTB). Shopify creates fulfillment orders automatically -- one fulfillment order per inventory location when an order is placed. Automatic routing based on inventory availability, proximity, and merchant rules. Support for merchant-managed and fulfillment-service locations. Split shipment support when items are at different locations. Full API support for custom fulfillment workflows (`fulfillmentOrderSubmitFulfillmentRequest`, `fulfillmentCreateV2`).

##### Q: What payment methods are supported?

Card (Visa, MC, AMEX, Discover via tap/chip/swipe), Apple Pay, Google Pay, cash (with full tracking), gift cards (physical/digital, unified balance), custom payment methods, split payments, manual card entry, Tap to Pay on iPhone/Android.

##### Q: Can the POS process split/partial payments?

Supported (OOTB). Shopify POS supports split payments across multiple payment methods in a single transaction. For example, a customer can pay $50 with a gift card and the remaining balance with a credit card. Any combination of supported payment methods can be used. If a split payment is cancelled mid-transaction, previously processed payments are automatically reverted.

##### Q: How does the POS handle staff management?

Unlimited staff PINs, role-based permissions (POS Pro, 24+ granular permissions), sales attribution, cash management per shift, device security (auto-lock, remote lock, remote sign-out), full audit trail, daily summaries (POS Pro).

##### Q: What security measures protect POS transactions?

PCI DSS Level 1 compliant, end-to-end encryption, tokenization (no card data stored on device), PIN-based staff access, remote management, audit logging, automatic updates, cloud-based (minimal local storage). SOC 1 Type 2, SOC 2 Type 2, SOC 3 certifications.

##### Q: What retail-specific reporting is available?

**POS Pro reports:** Daily sales summaries (emailed to managers), sales by staff member, sales by location, sales by product/variant, cash tracking reports (expected vs actual), discount usage reports, return rate analysis, inventory reports (levels, adjustments, transfers), customer acquisition (new vs returning).

**Platform-wide analytics:** ShopifyQL Notebooks for custom retail queries, Shopify Analytics dashboards, ABC inventory analysis, product performance across channels, customer lifetime value analysis.

**Third-party analytics:** Polar Analytics (retail analytics), RetailNext (foot traffic integration), Lifetimely (customer LTV).

##### Q: How does the POS scale for enterprise?

Shopify Plus: dedicated support, custom SLAs, 20 free POS Pro locations (all free with Shopify Payments). Supports hundreds of locations. Device fleet management (OTA updates, remote lock). Checkout infrastructure handles 40,000+ checkouts/minute per store. 99.99% uptime SLA. SOC 1/2/3 + PCI DSS Level 1. Security patches deployed within hours; no-downtime upgrades.

**Performance Benchmarks:**

| Metric | Benchmark |
|--------|-----------|
| Single item sale (excluding card processing) | Under 20 seconds |
| Peak in-store throughput | 50+ orders/hour per location |
| Platform checkout capacity | 40,000+ checkouts/minute per store |
| New associate training time | 15-30 minutes for basics |
| Security patch deployment | Within hours; rolling deployment where supported |
| Backend user location limit | 250 location accesses per user (hard limit) |

**POS Pro Pricing:** [INTERNAL-ONLY]

| Plan | POS Pro Included |
|------|-----------------|
| Basic / Shopify / Advanced | $89/month per location (30-day or yearly billing) |
| Retail plan | 1 free POS Pro location |
| Plus | 20 free POS Pro locations |
| Plus + Shopify Payments | ALL locations free |
| Plus billing | 30-day intervals only (no yearly option) |

---
