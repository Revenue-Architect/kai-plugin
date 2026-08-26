---
name: kaizen-ref-pos
description: "Deep retail reference for pos questions routed by Kai."
metadata_version: 1
layer: retail-reference
upstream: ["kaizen-retail-expert-v2"]
downstream: []
adjacent: []
canon: []
owns: ["pos domain reference"]
does_not_own: ["final implementation recommendation without routed skill context"]
---

# Shopify POS Reference Pack — POS, Hardware, Checkout, Payments, Staff, Extensions

### 3A. POS & In-Store Commerce

---

#### POS UI Extension Targets & APIs

##### Extension Targets

**Home Screen:**

| Target | Renders | Description |
|--------|---------|-------------|
| `pos.home.tile.render` | Home screen tile (smart grid) | Small tile on POS home; entry point for extensions |
| `pos.home.modal.render` | Full-screen modal | Complex workflows launched from home tile |

**Product Details:**

| Target | Renders | Description |
|--------|---------|-------------|
| `pos.product-details.block.render` | Block on product detail page | Display metafields, loyalty info, custom product data |
| `pos.product-details.action.render` | Action button on product page | Product-level operations (print label, adjust inventory) |

**Cart & Checkout:**

| Target | Renders | Description |
|--------|---------|-------------|
| `pos.checkout.block.render` | Block on checkout screen | Custom checkout fields, order notes, loyalty redemption |
| `pos.purchase.post.action.render` | After purchase completes | Post-purchase surveys, loyalty enrollment, custom receipts |

**Inventory (Newer):**

| Target | Renders | Description |
|--------|---------|-------------|
| `pos.inventory.block.render` | Inventory management screens | Custom inventory workflows, stock counts |

**Customer:**

| Target | Renders | Description |
|--------|---------|-------------|
| `pos.customer-details.block.render` | Customer detail page | Custom CRM data, purchase history, notes |
| `pos.customer-details.action.render` | Action on customer page | Customer-level operations |

**Cart Line Item Management:**

| Target | Renders | Description |
|--------|---------|-------------|
| `pos.cart.line-item.action.render` | Cart > Manage Line Item screen | Action extensions on individual line items in cart (NEW 2026) |

**Order:**

| Target | Renders | Description |
|--------|---------|-------------|
| `pos.order-details.block.render` | Order detail page | Custom order info, fulfillment status |
| `pos.order-details.action.render` | Action on order page | Order-level operations |

##### Available APIs by Target

**Standard APIs (Available to ALL targets):**
```typescript
// Navigation
api.navigation.navigate(screen); // Navigate between screens
api.navigation.goBack();         // Return to previous screen

// Toast notifications
api.toast.show("Message");       // Show brief notification

// Session
api.session.currentSession;      // Current staff session info
api.session.shop;                // Shop details

// Locale
api.locale.current;              // Current locale string
```

**Cart API (checkout/purchase targets):**
```typescript
// Read cart state
api.cart.subscribable;           // Subscribe to cart changes
api.cart.lineItems;              // Current line items
api.cart.subtotal;               // Cart subtotal
api.cart.taxTotal;               // Tax total
api.cart.grandTotal;             // Grand total

// Modify cart
api.cart.addLineItem(variantId, quantity);
api.cart.removeLineItem(lineItemId);
api.cart.setLineItemQuantity(lineItemId, quantity);
api.cart.setLineItemDiscount(lineItemId, discount);
api.cart.addCustomSale(title, price, quantity, taxable);
api.cart.setCustomer(customerId);
api.cart.removeCustomer();
api.cart.addProperties(properties);
api.cart.setLineItemProperties(lineItemId, properties);
api.cart.clearCart();
```

**Scanner API:**
```typescript
api.scanner.subscribable;        // Subscribe to scan events
api.scanner.scanBarcode();       // Trigger barcode scan
// Returns: { data: string, type: 'ean13' | 'code128' | ... }
```

**Product API (product-details targets):**
```typescript
api.product.id;                  // Current product GID
api.product.title;               // Product title
api.product.variants;            // Array of variants
api.product.images;              // Product images
```

**Customer API (customer-details targets):**
```typescript
api.customer.id;                 // Customer GID
api.customer.email;
api.customer.firstName;
api.customer.lastName;
```

**Order API (order-details targets):**
```typescript
api.order.id;                    // Order GID
api.order.name;                  // Order number
api.order.lineItems;
```

##### Direct API Access

Available from 2025-10+ API versions. Extensions can query the Admin GraphQL API directly.

**Setup:**
1. Set `api_version` in extension TOML to `2025-10` or later
2. Ensure app has required access scopes (e.g., `read_products`, `read_customers`)
3. App must be installed on the POS shop

**Usage:**
```typescript
import React, { useState } from 'react';
import {
  reactExtension,
  useApi,
  Button,
  Text,
  Stack,
} from '@shopify/ui-extensions-react/point-of-sale';

const Modal = () => {
  const api = useApi<'pos.home.modal.render'>();
  const [products, setProducts] = useState([]);

  const fetchProducts = async () => {
    const response = await fetch('shopify:admin/api/graphql.json', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        query: `{
          products(first: 10) {
            edges {
              node { id title }
            }
          }
        }`
      }),
    });
    const { data } = await response.json();
    setProducts(data.products.edges.map(e => e.node));
  };

  return (
    <Stack>
      <Button title="Load Products" onPress={fetchProducts} />
      {products.map(p => (
        <Text key={p.id}>{p.title}</Text>
      ))}
    </Stack>
  );
};

export default reactExtension('pos.home.modal.render', () => <Modal />);
```

**Fetching Metafields:**
```typescript
const fetchMetafields = async () => {
  const productId = api.product.id;
  const result = await fetch('shopify:admin/api/graphql.json', {
    method: 'POST',
    body: JSON.stringify({
      query: `
        query GetProductMetafield($productId: ID!) {
          product(id: $productId) {
            metafield(namespace: "custom", key: "loyalty_points") {
              value
              type
            }
          }
        }
      `,
      variables: { productId: `gid://shopify/Product/${productId}` }
    }),
  });
  return result.json();
};
```

##### UI Components

**POS-Specific Components (Touch-Optimized):**
```typescript
import {
  // Layout
  Screen, ScrollView, Stack, POSBlock, POSBlockRow,
  // Content
  Text, Image, Icon, Badge, Banner, Divider,
  // Interactive
  Button, TextField, NumberField, SearchBar, Selectable,
  Stepper, Toggle, RadioButtonList, SegmentedControl,
  // Navigation
  Navigator,
  // Data Display
  List, ListRow, SectionHeader, Tile,
  // Feedback
  Dialog, Sheet,
} from '@shopify/ui-extensions-react/point-of-sale';
```

**Multi-Screen Workflow:**
```typescript
const Extension = () => {
  return (
    <Navigator>
      <Screen name="home" title="My Extension">
        <Button title="Next" onPress={() => api.navigation.navigate('details')} />
      </Screen>
      <Screen name="details" title="Details">
        <Button title="Back" onPress={() => api.navigation.goBack()} />
      </Screen>
    </Navigator>
  );
};
```

**POSBlock Pattern (for block targets):**
```typescript
const ProductBlock = () => {
  const api = useApi<'pos.product-details.block.render'>();
  return (
    <POSBlock>
      <POSBlockRow
        leftSide={{ label: 'Loyalty Points', badge: { text: '500', variant: 'highlight' } }}
        rightSide={{ showChevron: true }}
        onPress={() => { /* navigate to detail */ }}
      />
    </POSBlock>
  );
};
```

##### Extension TOML Configuration

```toml
# shopify.extension.toml
api_version = "2025-10"

[[extensions]]
type = "pos_ui_extension"
name = "My POS Extension"
handle = "my-pos-extension"

  [[extensions.targeting]]
  target = "pos.home.tile.render"
  module = "./src/Tile.tsx"

  [[extensions.targeting]]
  target = "pos.home.modal.render"
  module = "./src/Modal.tsx"

[extensions.capabilities]
api_access = true  # Required for Direct API access
```

##### Development Workflow

**Local Development:**
```bash
shopify app dev                    # Start dev server
# POS app connects to dev server automatically when on same network
# Extension appears in POS with "Developer" badge
```

**Deployment:**
```bash
shopify app deploy                 # Deploy to Shopify Partners
# Then install app on shop via Partners dashboard
# Extension appears in POS after app installation
```

**Testing:**
- Use Shopify POS app on physical device (iOS/Android)
- Create a development store for testing
- Enable test mode for payments

##### Performance Best Practices

1. Lazy load data -- don't fetch everything on mount; use progressive loading
2. Cache API responses -- use local state to avoid redundant fetches
3. Minimize re-renders -- use `useMemo`, `useCallback` appropriately
4. Keep bundle small -- POS extensions should be lightweight
5. Handle offline gracefully -- show cached data when network unavailable
6. Touch targets -- minimum 44x44pt for all interactive elements
7. Loading states -- always show loading indicators; retail staff need feedback

##### Auth & Session

- `authApi` in the sandbox automatically attaches session tokens to requests going to registered `appUrl`
- Session tokens are short-lived; the sandbox handles refresh
- PCATs (Primary Client Access Tokens): 90-day session (14 days for SAML)
- POS mobile uses Identity SDK (NOT web-based Unified Sessions)

##### API Versioning

- POS extensions use calendar versioning (e.g., `2025-10`)
- Stable releases happen 4x per year
- Use release candidate versions (e.g., `2025-10-rc-1`) for pre-release features
- `unstable` is no longer supported -- use latest RC instead
- Breaking changes follow standard Shopify API versioning policy

---

#### Hardware & Payments

##### Hardware Lineup

**Card Readers:**

| Device | Connection | Accepts | Key Features |
|--------|-----------|---------|--------------|
| Shopify Tap & Chip Reader | Bluetooth | Tap (NFC), Chip (EMV), Swipe | Wireless, portable, pairs with iOS/Android |
| Shopify Chip & Swipe Reader | Audio jack / Lightning | Chip (EMV), Swipe | Budget option, no NFC |
| Chipper 2X BT | Bluetooth | Tap, Chip, Swipe | Legacy Stripe-based reader |

**Tap to Pay (No Hardware):**

| Platform | Requirements |
|----------|-------------|
| Tap to Pay on iPhone | iPhone XS or later, iOS 16.4+, Shopify Payments enabled |
| Tap to Pay on Android | NFC-enabled Android device, Android 9+, Shopify Payments enabled |

Tap to Pay turns the merchant's phone into a contactless payment terminal with no additional hardware.

**POS Terminal Hardware:**

| Device | Description | Key Specs |
|--------|-------------|-----------|
| POS Go | All-in-one handheld POS device | 5.5" display, built-in card reader (tap/chip/swipe), barcode scanner, Wi-Fi, battery-powered |
| POS Terminal | Countertop terminal | Touchscreen, integrated payment, receipt printer port |
| iPad Setup | iPad + card reader + optional accessories | Most flexible; use any supported iPad |

**Accessories:**

| Accessory | Purpose |
|-----------|---------|
| Receipt Printer | Bluetooth or USB thermal receipt printer |
| Barcode Scanner | Bluetooth barcode scanner for product lookup |
| Cash Drawer | Connects to receipt printer; auto-opens on cash sale |
| Label Printer | Print product labels with barcodes |
| Retail Stand | iPad mount for countertop use |
| Dock (POS Go) | Charging dock for POS Go device |

##### POS Hub

A USB hub that connects multiple wired peripherals to POS, eliminating Bluetooth disconnections with stable wired connections.

**Supported Peripherals via Hub:**

| Category | Models |
|----------|--------|
| Card Readers | Tap & Chip Reader, WisePad 3, Chipper 2X BT |
| Barcode Scanners | HP Engage 2D G2, Zebra DS2278 (wireless), Zebra DS2208 (USB), HID-mode scanners |
| Receipt Printers | Star mC-Print3, Epson TM-m30II, Epson TM-m30III, Star TSP143IVUE, Star TSP143IVUEWB, Star TSP143IIIU |
| Cash Drawers | mPOP, Star SMD2 |
| Keyboards | Any USB keyboard |

Hub notes:
- Does NOT work with the POS Tablet Stand (use one or the other)
- Has a Sleep Mode that affects connected peripherals
- Card reader auto-switches between USB (via Hub) and Bluetooth. USB takes priority when plugged in
- Eliminates the #1 hardware complaint: Bluetooth disconnections

##### Customer View (Customer-Facing Display)

Shopify's recommended Customer View app runs on a second screen.

**Supported Hardware:**
- POS Terminal built-in secondary display
- Third-party Android device as second screen

**What Customer View Displays:**
- Idle/welcome screen with store branding
- Live cart with discounts (updates in real-time as staff builds cart)
- Tip selection (if tipping enabled)
- Payment processing status
- Receipt options (customer selects: email, SMS, print, gift receipt)

**Setup:** Both devices must be on same WiFi network. Pair via QR code scan or auto-connect.

##### Specific Hardware Models

**Barcode Scanners:**

| Model | Connection | Notes |
|-------|-----------|-------|
| Socket Mobile | Bluetooth | Wireless, portable |
| Zebra DS2208 | USB (via Hub or Stand) | Wired, reliable |
| Zebra DS2278 | Wireless | Wireless with charging cradle |
| HP Engage 2D G2 | USB (via Hub) | Commercial grade |
| HID-mode scanners | USB | Emulates keyboard input; enable HID mode in POS Settings |

HID mode: When enabled, scanning on home screen automatically adds matching product to cart. Supports 1D and 2D barcodes.

**Receipt Printers:**

| Model | Connection |
|-------|-----------|
| Star mC-Print3 | USB (via Hub), Bluetooth |
| Epson TM-m30II | USB (via Hub), Bluetooth |
| Epson TM-m30III | USB (via Hub), Bluetooth |
| Star TSP143IVUE | USB (via Hub) |
| Star TSP143IVUEWB | USB (via Hub), WiFi, Bluetooth |
| Star TSP143IIIU | USB (via Hub) |

##### Regional Hardware Availability

**CRITICAL: Hardware availability varies significantly by country. Always verify before recommending.**

- US, Canada, UK, Ireland, Australia: Full hardware lineup
- EU markets: Most hardware available; some readers region-specific
- POS Go: Limited markets. Verify at shopify.com/hardware before recommending
- Tap to Pay on iPhone: Expanding; check country-specific availability
- Tap to Pay on Android: Now available in Canada (shipped Feb 2026) + expanding

Verification: Official hardware store at `hardware.shopify.com` or `shopify.com/pos/hardware`. Help docs at `help.shopify.com/en/manual/sell-in-person/hardware`.

##### Payment Processing

**Shopify Payments (Required for Shopify Hardware):**
- Shopify Payments must be enabled to use Shopify card readers and Tap to Pay
- Processing rates vary by plan (Basic: 2.7%, Shopify: 2.5%, Advanced: 2.4%, Plus: custom)
- In-person rates are lower than online rates on all plans
- Supported: Visa, Mastercard, AMEX, Discover, Apple Pay, Google Pay

**Payment Methods Supported at POS:**

| Method | POS Lite | POS Pro | Notes |
|--------|----------|---------|-------|
| Card (tap/chip/swipe) | Yes | Yes | Via Shopify card reader or Tap to Pay |
| Cash | Yes | Yes | With cash tracking |
| Gift cards | Yes | Yes | Physical and digital |
| Custom payment | Yes | Yes | Mark as paid (loyalty, store credit, etc.) |
| Split payment | Yes | Yes | Multiple methods on one transaction |
| Manual card entry | Yes | Yes | Key in card number manually |

**Split Payments:**
- Combine any payment methods in a single transaction
- Example: $50 on gift card + remainder on credit card
- Payment reversion supported if merchant cancels mid-checkout

**Custom Payment Methods:**

Created via `retailPaymentProviderCreate` GraphQL mutation:
- Stored with `custom=true` flag
- UI shows "Mark as paid" option
- Use cases: loyalty points, store credit, corporate accounts, third-party payment apps

**Payment Processors:** [INTERNAL-ONLY]

| Processor | Handles |
|-----------|---------|
| `CashPaymentProcessor` | Cash transactions |
| `CardReaderPaymentProcessor` | Physical card reader payments |
| `ManualCreditCardPaymentProcessor` | Keyed-in card numbers |
| `CustomPaymentProcessor` | Custom/third-party payment methods |
| `GiftCardPaymentProcessor` | Gift card redemption |
| `SessionTokenPaymentProcessor` | Tokenized stored payments |
| `LocalPaymentMethodPaymentProcessor` | Region-specific methods (Maestro, etc.) |

##### Recommended Hardware Setups by Business Type

**Boutique / Small Retail (1-2 locations):**
- iPad + Shopify Tap & Chip Reader + Receipt Printer
- Or: Tap to Pay on iPhone (zero hardware cost)
- Plan: POS Lite (free) or POS Pro ($89/mo)

**Multi-Location Retail (3-10 locations):**
- iPad + Card Reader + Receipt Printer + Cash Drawer per location
- POS Go for mobile associates / pop-ups
- Barcode scanners if high-volume
- Plan: POS Pro ($89/mo per location)

**High-Volume Retail (10+ locations):**
- POS Terminal or iPad setup per register
- POS Go for floor associates
- Full accessory suite (receipt, barcode, cash drawer, label printer)
- Device management for fleet control
- Plan: Shopify Plus + POS Pro (negotiated pricing)

**Pop-Up / Events:**
- POS Go (all-in-one, battery-powered) OR
- iPhone + Tap to Pay (zero hardware)
- Plan: POS Lite (free)

**Restaurant / Food Service:**
- Shopify POS is NOT optimized for restaurant use
- No kitchen display system, table management, or tip pooling
- Recommend: Square for Restaurants, Toast, or Clover for food service

##### Offline Mode Architecture [INTERNAL-ONLY]

**What Works Offline:**
- Cash sales -- process cash transactions without connectivity
- Cart building -- browse products, build cart from cached catalog
- Customer lookup -- from local cache (may be stale)

**What Requires Connectivity:**
- New card authorizations -- cannot authorize new credit card charges offline
- Real-time inventory checks -- uses cached data; may allow overselling
- Gift card validation -- requires server verification
- Discount code validation -- server-side validation needed
- Customer creation -- queued until online
- Tax calculation -- uses cached tax rates

**Technical Architecture:** [INTERNAL-ONLY]
- **Local SQLite** -- Persistent cache with 5-minute staleness policy
- **Apollo Client** -- In-memory GraphQL cache
- **Sync on reconnect** -- Pending mutations processed with version tokens
- **Conflict resolution** -- Latest server state fetched + delta applied

##### Device Management [INTERNAL-ONLY]

**Fleet Management Features:**
- **OTA updates** -- Push updates to POS devices remotely
- **Remote lock** -- Lock a device remotely (security)
- **Remote sign-out** -- Force sign-out staff sessions
- **Geo-fencing** -- Restrict device operation to specific locations
- **WiFi provisioning** -- Configure WiFi settings remotely
- **Device inventory** -- View all registered devices, battery levels, firmware versions

**POS Go Specific:** [INTERNAL-ONLY]
- **Default DDG** (Device Deployment Group) -- Production update channel
- **Staging DDG** -- Development devices with test payment keys
- **DMSDK** (Device Management SDK) -- Stripe-managed access to device settings
- **Available settings**: Network, Bluetooth, display mode, screen lock, brightness, accessibility

**Device Types in System:** [INTERNAL-ONLY]

| Device Type | Connection | Notes |
|------------|------------|-------|
| POS Tablet (Whistler) | WiFi | iPad or Android tablet |
| Receipt Printer | Bluetooth/USB | Supports parent-child hierarchy |
| Barcode Scanner | Bluetooth | Multiple vendors supported |
| Card Reader | Bluetooth/USB | Shopify branded or compatible |
| Label Printer | Bluetooth/USB | Retail label printing |
| POS Go | WiFi/Cellular | All-in-one device |

---

#### Checkout Architecture

##### Three-Layer Architecture
```
+--------------------------------------------------+
|  DraftCheckout (Mutable)                         |
|  - Add/remove line items                         |
|  - Apply discounts, customer, notes              |
|  - Tax calculation                               |
|  - Can be edited at any time                     |
+--------------------------------------------------+
|  Checkout (Immutable after creation)             |
|  - Created when payment begins                   |
|  - Tracks all payments (success + attempts)      |
|  - Amounts locked                                |
|  - Only payment info can change                  |
+--------------------------------------------------+
|  Order (Final)                                   |
|  - Created after successful payment              |
|  - Triggers fulfillment workflow                 |
|  - Inventory committed                           |
|  - Customer notified                             |
+--------------------------------------------------+
```

##### Standard Sale Flow
1. Build Cart: Staff adds items via barcode scan, product search, or smart grid
2. Set Customer (optional): Attach customer profile for loyalty, tax exemptions
3. Apply Discounts (optional): Line item or order-level discounts
4. Start Checkout: DraftCheckout syncs with server, Checkout created
5. Select Payment: Cash, card, gift card, custom, or split
6. Process Payment: Payment processor handles authorization
7. Complete: Order created, receipt generated, inventory committed

##### Payment Flows

**Single Payment:**
```
Cart -> Checkout -> Payment -> Order
```

**Split Payment Flow:**
```
Cart -> Checkout -> Payment 1 (partial) -> Payment 2 (remainder) -> Order
```

Split payment supports combining ANY payment methods: gift card + credit card, cash + credit card, store credit + cash + credit card, any combination.

**Split Payment Error Handling:**
- If merchant cancels mid-split: first payment is reverted
- TotalPriceUpdated error: If checkout total changes between payments, flow aborts and restarts
- All partial payments tracked on the Checkout object

##### Checkout SDK Architecture [INTERNAL-ONLY]

**SDK Flow Classes:**

| Class | Lifecycle | Responsibility |
|-------|-----------|---------------|
| `DraftCheckoutFlow` | Cart building | Manage mutable cart, sync with server, trigger checkout |
| `CheckoutFlow` | Payment phase | Process payments against immutable checkout |
| `CheckoutPaymentFlow` | Payment completion | Finalize individual payment transactions |
| `OrderPaymentFlow` | Order payments | Handle post-order payments (e.g., additional charges) |
| `CardPresentRefundFlow` | Refunds | Process card-present refunds back to original card |
| `CheckoutRestorationFlow` | Recovery | Restore interrupted checkout from persisted state |

**DraftCheckoutFlow API:** [INTERNAL-ONLY]
```typescript
// Key methods
draftCheckout.sync();                          // Sync cart with server
draftCheckout.addCheckoutUpdateCallback(cb);   // Subscribe to changes
draftCheckout.startCheckoutFlow();             // Transition to Checkout

// Internal: mini state machine manages transitions
// Final sync performed before payment begins
```

**Payment Processing Sequence:** [INTERNAL-ONLY]
```
1. Create Checkout (from DraftCheckout)
2. Update Checkout (apply any last-minute changes)
3. Post Payment (submit payment to processor)
4. Poll Until Complete (check payment status)
5. Complete Checkout (finalize -> create Order)
```

##### Payment Method Details

**Card-Present Payments:**
```
Staff selects "Card" -> POS connects to card reader -> Customer taps/inserts/swipes
-> Reader sends encrypted data to Shopify Payments -> Authorization -> Capture -> Receipt
```

Supported interactions: Contactless (NFC) for Apple Pay, Google Pay, contactless cards. Chip (EMV) for insert card. Swipe (magnetic stripe) as fallback.

**Cash Payments:**
```
Staff selects "Cash" -> Enters amount tendered -> POS calculates change
-> Cash drawer opens (if connected) -> Transaction complete
```

Cash tracking features: Starting cash float per shift, cash in/out tracking, end-of-day reconciliation, expected vs actual cash count.

**Gift Card Payments:**
- Physical and digital gift cards supported
- Partial redemption supported (remaining balance stays on card)
- Gift cards work across online + POS (unified balance)

**Custom Payment Methods:**
```
Staff selects custom method -> POS shows "Mark as paid" -> Staff confirms
-> Transaction recorded with custom payment type
```

Setup via GraphQL:
```graphql
mutation {
  retailPaymentProviderCreate(input: {
    name: "Loyalty Points"
    custom: true
  }) {
    retailPaymentProvider { id name }
    userErrors { field message }
  }
}
```

Use cases: Loyalty points redemption, corporate purchase orders, store credit / trade-in value, third-party financing (Afterpay, Klarna in-store), employee discount programs.

##### Refunds & Returns at POS

**Card-Present Refund:**
- Requires same card reader
- Processing time: instant authorization, 5-10 business days for funds

**Refund to store credit:**
- Issues gift card automatically
- Immediate availability
- Works across POS + online

**Exchange Flow (POS Pro):**
```
Look up order -> Select return items -> Scan new items -> Calculate difference
-> Process payment/refund for difference -> Both transactions linked
```

##### Tax Calculation

**How POS Calculates Tax:**
1. Location-based: Tax rates based on store location (origin-based states)
2. Destination-based: Tax based on customer's address (if available)
3. Tax overrides: Merchant can configure tax exemptions per product/collection
4. Customer tax exemptions: B2B customers can be marked tax-exempt
5. Shopify Tax: Automated tax calculation with jurisdiction detection

**Tax in Offline Mode:** Uses cached tax rates from last successful sync.

##### Tipping at POS

Tips only work with credit card payments via supported card readers (Tap & Chip reader, Chip & Swipe reader, WisePad 3 reader, POS Go built-in reader). Cash tips are NOT processed through POS.

**Tip Configuration:**
- Up to 3 preset tip percentages (e.g., 15%, 18%, 20%)
- Custom tip option: Customer can enter any amount
- Smart minimums: For transactions below a threshold, replace percentages with fixed dollar amounts

**Tip Limits by Currency:**

| Currency | Tip Cap |
|----------|---------|
| USD / CAD | $10 max for totals up to $500; above $500 max is 2x checkout total |
| All other currencies | 2x the checkout total |
| Split payments | Always 2x the checkout total regardless of currency |

**Tip Reporting:**
- Tips appear in **Analytics > Reports > Finances > Tips report**
- Total tips also shown in Finances report overview
- **Tip-only refunds**: Can refund a tip without refunding the entire order

##### Custom Sales

Staff can create a custom sale (line item with custom title, price, and quantity) for items not in the product catalog. Custom sales are taxable (follows location tax settings by default; can be toggled), appear in order history, do NOT affect inventory, and can be combined with regular products.

##### Saved Carts

| Feature | Saved Cart | Draft Order |
|---------|-----------|-------------|
| Where created | POS only | POS or Admin |
| Persistence | Device-level | Server-level (visible in Admin) |
| Customer assignment | Optional | Optional |
| Inventory reservation | No | Yes (reserves inventory) |
| Invoiceable | No | Yes (can send invoice) |
| Editable in Admin | No | Yes |
| Payment link | No | Yes |

##### Cash Rounding

Cash rounding automatically rounds cash transaction totals to the nearest denomination where small coins have been eliminated (e.g., penny rounding in Canada, Australia, New Zealand). Only applies to cash payments (card payments are exact). Rounding follows local country rules.

##### Discount Handling at POS

**Discount Types:**

| Type | Application | Notes |
|------|------------|-------|
| Order discount | Entire order | Percentage or fixed amount |
| Product discount | Line item | Per-product pricing adjustment |
| Shipping discount | Shipping cost | Applicable to ship-to-customer orders |
| Discount codes | Order level | Customer provides code; staff enters or uses Smart Grid tile |
| Automatic discounts | Applied automatically | Requires POS Pro; can target specific customers/segments |
| Staff/manual discounts | Configurable | Role-based permissions control who can discount |

**Automatic Discounts + POS Pro:**
- Automatic discounts are only available at POS Pro locations
- Discounts set for specific customers or segments apply at POS Pro by default
- Discount codes created in admin work at both POS Lite and POS Pro

**Discount Functions Compatibility:**
- Third-party discount apps built with Shopify Discount Functions work at POS
- Same discounts applied online can be used at POS if built with Functions API
- Discount apps can be added to the Smart Grid via POS editor in admin

**Discount Stacking Rules:**
- Automatic + manual: Automatic discounts CAN combine with manually applied discounts (depending on merchant settings)
- Multiple automatic discounts: Only ONE automatic discount applies per order (highest value wins unless configured otherwise)
- Discount codes: Only ONE discount code per order (Shopify limitation, applies online and POS)
- Code + automatic: A discount code CAN combine with an active automatic discount
- Line item + order: A line-item discount and an order-level discount CAN stack
- Maximum discount limits: Configurable per discount (e.g., cap percentage discount at $50)
- Staff permission: Role-based control over who can apply manual discounts; separate permission for discount amount vs percentage
- Discount code tiles: Smart Grid tiles can reference admin-created discount codes for one-tap application (no manual entry)

**Store Credit at POS:**
- Gift cards as store credit: Issue a gift card for return value
- Gift card balance: Unified across POS and online
- Partial redemption supported
- Store credit apps: Rise.ai, Govalo for more advanced store credit (credit accounts, expiry, branded cards)
- Refund to store credit: Staff selects "Refund to gift card" during return -- creates new gift card with refund amount
- Corporate gift cards / bulk: Available via admin; not natively bulk-issuable from POS

##### Tax Handling at POS

| Method | When Used |
|--------|----------|
| Origin-based | Tax based on store/POS location (default for in-person sales in origin-based states) |
| Destination-based | Tax based on customer shipping address (for ship-to-customer orders from POS) |
| Manual tax rates | Merchant-configured rates per location |
| Shopify Tax | Automated tax calculation with jurisdiction detection (US-focused) |
| Third-party tax engines | Avalara, TaxJar via app integration |

Tax nuances for POS:
- In-store sales: Typically origin-based
- Ship-to-customer from POS: Destination-based
- Tax-exempt customers: Can mark customers as tax-exempt in profile; auto-applies at POS
- Product tax overrides: Certain products (food, clothing in some states) may have different rates; configurable per product
- Compound tax: Some jurisdictions (Canada, GST+PST) require compound tax calculation; Shopify handles this natively
- VAT-inclusive pricing: Supported for markets where prices include tax (EU, UK, AU)
- VAT on receipts: France and Spain auto-include line-item VAT and VAT summary on printed receipts
- Offline tax: Uses cached tax rates; may be slightly stale

##### Shopify Markets + POS Interaction

- POS locations are tied to a specific market based on their physical address
- Pricing, tax rules, and currency follow the market configuration
- Multi-currency at POS is NOT natively supported. POS transacts in the shop's currency for that location
- For merchants in multiple countries: each country needs its own Markets configuration; POS locations inherit that market's settings
- Price lists (Plus): Can create location-specific pricing via price lists tied to markets

##### Label Printing

- Basic product label printing via connected label printer
- Barcode generation for products (SKU/barcode printed on labels)
- Label Printing Apps (Recommended): Retail Barcode Labels (custom templates, bulk printing), Dymo/Brother integration

##### Localization & Multi-Language

- Receipt language follows the POS location's language setting
- Limitation: Only ONE language per location for printed receipts. No per-transaction toggle
- Workaround for bilingual: Use custom Liquid templates for email receipts (can include both languages)
- RTL languages: Limited support; verify for specific language before committing
- POS app interface language follows the device language setting
- Product names/descriptions display as entered in admin (no auto-translation)

##### POS + Online Checkout Differences

| Feature | Online Checkout | POS Checkout |
|---------|----------------|-------------|
| Cart building | Customer self-serve | Staff-assisted |
| Payment collection | Online gateway | Card reader / cash / Tap to Pay |
| Tax calculation | Destination-based | Origin or destination-based |
| Discount codes | Customer enters | Staff enters or scans |
| Checkout extensibility | Full (Checkout UI Extensions) | Limited (POS UI Extensions) |
| Scripts/Functions | Supported | Limited support |
| Customer accounts | Full account flow | PIN-based staff, customer lookup |
| Abandoned checkout recovery | Yes | No (cart cleared on close) |
| Offline capability | No | Limited (cash sales) |
| Multi-currency | Yes (Markets) | No (location currency only) |
| Store credit | Gift card redemption | Gift card redemption |
| Discount stacking | 1 code + 1 automatic | 1 code + 1 automatic + manual |
| Receipt customization | Email only | Printed (Liquid) + email + SMS |

---

#### Retail Operations

##### Omnichannel Fulfillment

**BOPIS (Buy Online, Pick Up In Store) -- POS Pro required:**

How it works:
1. Customer selects "Pick up" at online checkout
2. Order routed to selected store location
3. Staff receives notification in POS, picks items, marks as ready
4. Customer arrives, staff fulfills pickup, marks as complete

Pre-sales positioning: "BOPIS drives foot traffic to stores. Industry data shows 30-50% of BOPIS customers make additional in-store purchases. Shopify's unified inventory ensures real-time stock visibility so customers only see pickup options where inventory exists."

**Ship from Store -- POS Pro required:**

Order routing logic: Inventory availability at each location, customer proximity (minimize shipping time/cost), minimize split shipments, priority rules configurable by merchant.

Pre-sales positioning: "Ship-from-store turns every retail location into a mini fulfillment center. This reduces shipping costs, speeds up delivery, and moves inventory that might otherwise sit unsold in-store."

**Ship and Carry Out (Mixed Fulfillment):** A single order can contain items the customer takes home now AND items that ship later, combined into one transaction.

**Local Delivery -- POS Pro required:** Merchant defines delivery zones by postal code or radius. Customers see local delivery option at checkout. Staff manages delivery queue.

**Endless Aisle:** Staff can sell products not physically in-store by creating orders for items at other locations or warehouse. Uses draft orders or "ship to customer" flow.

##### Exchanges & Returns

**Exchanges (POS Pro Only):**
- Even exchange (same price item)
- Exchange with price difference (customer pays or gets refund)
- Original payment method refund + new charge
- Inventory restocked at return location

**Returns (POS Lite and POS Pro):**

| Type | Description |
|------|-------------|
| Full refund | Refund entire order |
| Partial refund | Refund specific items |
| Store credit | Issue gift card for return amount |
| Exchange | Swap for different item (POS Pro) |
| No restock | Refund without adding back to inventory (damaged goods) |

**Verified vs Unverified Returns:**
- Verified return: Staff looks up original order; return is linked to that order
- Unverified return: Staff processes return without linking to an original order

Return rules: Merchants can configure return policies (return window, restocking fees, final-sale items) that POS enforces.

##### Staff Management

**POS Lite:** Unlimited staff PINs, basic role distinction (admin vs staff), clock in/out tracking.

**POS Pro:** Granular role-based permissions, custom roles with specific capabilities, per-staff sales reporting.

**Staff Permissions (POS Pro) -- Complete List:**

| Permission | API Field | Controls |
|-----------|-----------|----------|
| Apply custom discounts | `is_apply_custom_discounts_allowed` | Manual percentage/fixed discounts |
| Apply discount codes | `is_apply_discount_codes_allowed` | Enter/scan discount codes |
| Access apps | `is_apps_allowed` | Use installed apps from POS |
| Cash tracking | `is_cash_tracking_allowed` | Cash management features |
| Customer tab | `is_customers_tab_allowed` | Access customer list |
| View customer details | `is_view_customer_details_allowed` | See customer info (NEW v11.1) |
| Edit taxes in cart | `is_edit_taxes_in_cart_allowed` | Modify tax on cart items |
| Customize Smart Grid | `is_home_grid_customization_allowed` | Edit home screen layout |
| Location settings | `is_location_settings_allowed` | Modify location config |
| Log out | `is_log_out_allowed` | Sign out of POS |
| Manager approval | `is_manager_approval_allowed` | Approve restricted actions |
| Start/close cash sessions | `is_manually_start_close_payment_tracking_sessions_allowed` | Register cash sessions |
| Open cash drawer | `is_open_cash_drawer_allowed` | Open drawer without sale |
| View other location orders | `is_orders_at_other_locations_allowed` | Cross-location order view |
| Payment settings | `is_payment_settings_allowed` | Modify payment config |
| Cash session history | `is_payments_cash_session_history_allowed` | View past cash sessions |
| Manage POS roles | `is_pos_roles_allowed` | Create/edit staff roles |
| Customize receipts | `is_receipt_customization_allowed` | Edit receipt templates |
| Process refunds/exchanges | `is_refund_and_exchange_orders_allowed` | Handle returns |
| Register shift settings | `is_register_shift_settings_allowed` | Configure shifts |
| View retail reports | `is_retail_reports_allowed` | Access analytics |
| Sales attribution | `is_sale_attributions_for_orders_allowed` | Attribute sales to staff |
| Ship cart to customer | `is_ship_cart_to_customers_allowed` | Ship orders from POS |

**Manager Approval (POS Pro):** Certain staff actions can require a manager's PIN before completing. Configurable per-role: either disallow entirely or allow with manager override. Use cases: price overrides, large discounts, returns over a threshold, tax edits. Shows informational banner at start of workflow, warning banner before final step.

**Cash Management:**
- Cash tracking: Track cash in drawer throughout shift
- Cash float: Set starting cash amount per shift
- Cash in/out: Record non-sale cash movements (petty cash, tips, etc.)
- End-of-day reconciliation: Compare expected vs actual cash
- Daily sale summaries: Emailed to manager (POS Pro)

##### Clienteling

**Customer Profiles at POS:**
- View customer purchase history during sale
- See total lifetime spend, notes, tags
- Online + in-store order history (unified)
- Custom metafields: Store custom data (birthdays, loyalty status, preferences)
- Tax exemption status: Mark customers as tax-exempt; auto-applied at checkout
- Marketing consent: Capture email/SMS opt-in at point of sale
- Required data capture (POS Pro): Set customer fields as recommended or required during checkout
- Customer segmentation: Use collected data for targeted campaigns (e.g., promote in-store events to nearby customers)

**Clienteling Capabilities:**

| Capability | Native | App Required |
|-----------|--------|-------------|
| Customer lookup | Yes | No |
| Purchase history | Yes | No |
| Customer notes | Yes | No |
| Customer tags | Yes | No |
| Email/SMS from POS | No | Yes (Klaviyo, Endear) |
| Appointment booking | No | Yes |
| Style/preference profiles | No | Yes (Endear, Clientbook) |
| Commission tracking | No | Yes |
| Outreach automation | No | Yes (Klaviyo, Endear) |

**Clienteling Apps:**
- Endear: Full clienteling CRM for retail (popular for fashion/luxury)
- Clientbook: Luxury retail clienteling
- Klaviyo: Email/SMS with POS purchase triggers
- Marsello: Loyalty + clienteling combined

##### Loyalty Programs

**Native Capabilities:** Gift cards (physical and digital), customer accounts, Shopify Flow automations.

**Loyalty Apps (POS-Compatible):**

| App | Key Feature | POS Integration |
|-----|------------|-----------------|
| Smile.io | Points, VIP tiers, referrals | Full POS integration |
| Yotpo Loyalty | Points, rewards, VIP | POS compatible |
| Marsello | Loyalty + marketing | Deep POS integration |
| LoyaltyLion | Points, tiers, rewards | POS compatible |
| Rise.ai | Gift cards + store credit | POS integration |

##### Inventory Operations (Retail-Specific)

**Stock Counts / Cycle Counts:**

POS Pro includes: Stock adjustments from POS app, barcode scanning, adjustment reasons, per-location counts.

For full inventory counting: Quick Counts (native POS extension) with scan, count, submit, discrepancy view. Third-party apps (Stocktake Online, Veeqo, SKULabs) for advanced features like blind counts, scheduled counts, multi-user.

**Purchase Orders:** Being migrated into core Shopify admin. Current/emerging: Create POs to suppliers, track incoming inventory, receive stock against POs, supplier management. Gaps: No vendor portals, limited demand forecasting, no auto-reorder triggers.

**Inventory Transfers (POS Pro):** Transfer stock between locations. Track status (pending, in transit, received). Partial receiving supported. Full audit trail.

**ABC Inventory Analysis:** Available in Shopify admin reporting. A items: Top 80% of revenue (typically 20% of products). B items: Next 15%. C items: Bottom 5%.

##### Omnichannel Architecture Patterns

**Pattern 1: Unified Commerce (Most Common)**
```
                 +---------------+
                 |   Shopify     |
                 |   (Single     |
                 |   Instance)   |
                 +-------+-------+
            +------------+------------+
            v            v            v
      +-----------+ +-----------+ +-----------+
      | Online    | | POS       | | POS       |
      | Store     | | Store 1   | | Store 2   |
      +-----------+ +-----------+ +-----------+

Shared: Inventory, Customers, Products, Orders, Gift Cards
```

**Pattern 2: Hub & Spoke (Multi-Location)**
```
                    +---------------+
                    |   Shopify     |
                    +-------+-------+
                            |
              +-------------+-------------+
              v             v             v
        +-----------+ +-----------+ +-----------+
        | Warehouse | | Store 1   | | Store 2   |
        | (Hub)     | | (Spoke)   | | (Spoke)   |
        +-----------+ +-----------+ +-----------+
              |             ^             ^
              +-- Transfers -+------------+

Warehouse fulfills online + replenishes stores via transfers
```

**Pattern 3: ERP-Integrated**
```
  +-----------+         +---------------+
  |  ERP      |<------->|   Shopify     |
  | (Master)  | Sync    |               |
  +-----------+         +-------+-------+
       |                 +------+------+
       |                 v      v      v
       |            Online  POS 1  POS 2
       |
       +--> WMS/3PL (fulfillment)

ERP is inventory master; Shopify syncs via API/middleware
```

##### Receipt Customization

**Liquid Receipt Templates (POS Pro):** Full Liquid template editor for sales receipts, gift receipts, return receipts, and exchange receipts.

**Receipt Options:** Printed (thermal), email receipt, SMS receipt, no receipt.

**Customization Elements:** Store logo and branding, custom header and footer text, QR codes (loyalty programs, surveys, order lookup), 1D barcodes, custom order/line item properties, return policy text, regional tax compliance (VAT line items auto-enabled in France/Spain).

**Receipt Settings by Plan:** [INTERNAL-ONLY]

| Plan | Available Customizations |
|------|------------------------|
| POS Lite (new) | Header and footer only |
| POS Lite (legacy) | Header, footer, and a few more options |
| POS Pro (no Liquid) | Header, footer, custom QR code, 1D barcode |
| POS Pro (Liquid enabled) | Full Liquid template editing; printing options in app |

##### Smart Grid

The customizable home screen of the POS app. Tiles for quick access to products, collections, discounts, and app actions.

| Feature | POS Lite | POS Pro |
|---------|----------|---------|
| Default tiles | Yes | Yes |
| Custom product tiles | Limited | Yes |
| Collection tiles | Limited | Yes |
| Discount code tiles | Limited | Yes (select admin-created codes, no typing) |
| App extension tiles | Limited | Yes |
| Custom layouts per location | No | Yes |
| Multiple grid pages | No | Yes |

##### Cash Management (Enhanced 2026)

Register-based sessions: Cash tracking tied to specific registers (not just locations). Each register has its own cash session and drawer count.

Cash Tracking Workflow:
1. Opening: Set cash float per register
2. During shift: System tracks expected cash from sales
3. Cash in/out: Record non-sale movements with reason codes (petty cash, tips, float adjustment, bank deposit, etc.)
4. Closing: Compare expected vs actual cash count per register
5. Reporting: Full audit trail with reason codes

Reason-Coded Adjustments:
- Every cash in/out requires a reason code
- Custom reason codes available
- Automated workflow support for recurring cash management tasks

##### Gift Cards at POS

- Sell physical and digital gift cards
- Redeem gift cards as payment (full or partial)
- Check gift card balance
- Issue gift card as store credit for returns
- Gift card balance unified across online + POS
- Gift card cashout (shipped 2026): Cash out cards under $15 where required by law

##### Daily Retail Operations Checklist

**Store Opening:**
1. Open POS app -> Sign in with staff PIN
2. Set cash float per register (register-based sessions)
3. Review pending orders (BOPIS pickups, transfers to receive)
4. Check low stock alerts
5. Review daily schedule/appointments (if using clienteling app)

**During Day:**
- Process sales (card, cash, gift card, split payment)
- Handle returns/exchanges
- Fulfill BOPIS orders (with barcode-verified pick & pack)
- Receive inventory transfers
- Run Quick Counts for cycle counting
- Manage walk-in customers (add to profiles, notes)

**Store Closing:**
- Run end-of-day report
- Reconcile cash drawer per register (reason-coded adjustments for discrepancies)
- Review daily sales summary
- Process any pending returns
- Lock POS device (remote lock available for fleet management)

##### Reporting (POS Pro)

| Report | What It Shows |
|--------|--------------|
| Daily sales summary | Total sales, transactions, average order value |
| Sales by staff | Per-associate performance |
| Sales by location | Compare store performance |
| Sales by product | Best/worst sellers |
| Inventory reports | Stock levels, adjustments, transfers |
| Cash tracking | Cash in/out, discrepancies |
| Discount usage | Which discounts used, by whom |
| Return rate | Return volume and reasons |

Analytics Integration: ShopifyQL Notebooks (custom queries), Shopify Analytics (built-in dashboards), third-party (Polar Analytics, Lifetimely, RetailNext for foot traffic).

---

