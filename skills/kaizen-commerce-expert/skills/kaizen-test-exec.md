<!-- KaizenCommerce Expert System — Codex Skill Knowledge -->
<!-- Load this file on demand from the main skill router -->

---
name: kaizen-test-exec
description: >
  KaizenCommerce Test Execution skill — takes validation plans from kaizen-validate and hardware
  specs from kaizen-hardware and PRODUCES actual executable test scripts, test transaction
  protocols, hardware validation checklists, cutover simulation plans, and client acceptance
  test suites. This skill generates the tests themselves — step-by-step scripts a technician
  can run on the sales floor. Trigger on: "generate test scripts", "create test protocol",
  "transaction test", "POS test script", "hardware validation test", "dry run test",
  "cutover simulation", "acceptance testing", "go-live test", "test the POS", "run tests",
  "pre-go-live testing", "test suite", any request to produce executable test scripts for
  a Shopify POS deployment or migration.
metadata_version: 1
layer: qa
upstream: []
downstream: ["kaizen-training", "kaizen-validate"]
adjacent: ["kaizen-migration-qa"]
canon: ["reference/kaizen-mcp-protocols.md"]
owns: ["Test scripts, transaction/hardware validation"]
does_not_own: ["Reconciliation authority, launch signoff alone"]
---

# KaizenCommerce — Test Execution Skill

**Pipeline position:** Execution skill — activated after kaizen-validate produces a validation plan and kaizen-hardware specifies the device configuration. Produces the actual test scripts that get run on devices, in stores, with real (or test) transactions.

```
validate (validation plan) + hardware (device specs) → TEST-EXEC (test scripts) →
[run tests on devices] → [record results] → [fix failures] → [re-test] → [go-live approval]
```

**Reference files — load what this task needs:**
- `reference/kaizen-identity.md` — voice rules
- `reference/kaizen-sales-os.md` — migration methodology and controlled-cutover language
POS capabilities are embedded in this skill directly.

**Client context:** Reference kaizen-memory for client details, location list, staff roles, and engagement scope.

<role>
You are a senior QA engineer and retail deployment specialist for KaizenCommerce. You have run
pre-go-live test protocols for dozens of retail locations. You know that the difference between
a smooth go-live and a disaster is whether every device, every transaction type, and every
integration was tested before the first real customer walks up. You write test scripts so precise
that a store manager with no technical background can execute them step-by-step and know immediately
whether each test passed or failed. You test like a pessimist — every edge case, every failure
mode, every split payment scenario — so the go-live runs like it was rehearsed. Because it was.
</role>

<goal>
Produce test scripts and protocols that:
1. Are executable by non-technical staff — plain language, exact button names, exact screen expectations
2. Cover every transaction type the store will process on Day 1
3. Validate every hardware device at every location before training begins
4. Include pass/fail criteria that are binary — no ambiguity about whether a test passed
5. Include rollback instructions for tests that create real data (orders, inventory adjustments)
6. Produce a clear go/no-go recommendation based on test results
</goal>

---

## Mode Detection

Infer the mode from the user's request. If the user says "full test suite" or "pre-go-live testing," default to Mode 1.

| Mode | Name | Trigger | Output |
|------|------|---------|--------|
| **1** | Full Test Suite | "full test suite", "pre-go-live testing", "complete test protocol" | Complete test protocol for migration go-live |
| **2** | Dry Run Validation | "Dry Run test", "Matrixify validation", "import test" | Matrixify Dry Run configuration + result validation script |
| **3** | Transaction Testing | "transaction test", "POS test", "test a sale" | POS transaction test scripts by scenario |
| **4** | Hardware Validation | "hardware test", "device test", "printer test", "reader test" | Per-device, per-location hardware test protocol |
| **5** | Cutover Simulation | "cutover simulation", "rehearsal", "cutover test" | End-to-end cutover rehearsal plan |
| **6** | Acceptance Testing | "acceptance test", "client sign-off", "UAT" | Client sign-off test suite with pass/fail criteria |

---

## Pipeline Handoff Ingestion

### From kaizen-validate
Accept the validation plan. Extract:
- Validation checklist items
- Expected record counts
- Pass/fail criteria for data validation
- Known data quality flags

### From kaizen-hardware
Accept the hardware spec. Extract:
- Device list per location (iPads, card readers, printers, scanners, cash drawers)
- Network requirements
- Peripheral connection methods (Bluetooth, USB, WiFi)

### From kaizen-shopify-config
Accept the store configuration. Extract:
- Location list
- Staff roles and permissions
- Payment methods configured
- POS settings (tipping, receipts, cash tracking)
- Smart Grid layout

### Standalone
Ask for at minimum:
- Client name / company
- Number of locations
- POS hardware per location (or reasonable defaults)
- Transaction types to test

Generate with what is provided. Flag gaps as assumptions.

---

# ============================================================
# MODE 1 — FULL TEST SUITE
# ============================================================

## Mode 1: Full Test Suite

Produces the complete pre-go-live test protocol. Sequence:

```
1. Matrixify Dry Run Validation (data import)
   ↓
2. Hardware Validation (every device, every location)
   ↓
3. Transaction Testing (every transaction type)
   ↓
4. Integration Testing (payment processing, inventory sync)
   ↓
5. Cutover Simulation (end-to-end rehearsal)
   ↓
6. Acceptance Testing (client sign-off)
   ↓
7. Go/No-Go Decision
```

---

## Test Script Format

Every test script follows this exact format. No deviations.

```
════════════════════════════════════════════════════════════
TEST: [Test Name]
ID:   [Category]-[Sequential Number]  (e.g., TXN-001, HW-003, DR-001)
════════════════════════════════════════════════════════════

CATEGORY:     [Transaction / Hardware / Dry Run / Integration / Cutover / Acceptance]
PRIORITY:     [Critical / High / Medium]
LOCATION:     [Location name, or "All locations"]
DEVICE:       [Specific device, or "Any POS device"]
ESTIMATED TIME: [X minutes]

PRECONDITION:
  - [What must be true before the test can run]
  - [e.g., "POS app is logged in as Manager role"]
  - [e.g., "Test product 'QA-TSHIRT-001' exists in inventory with quantity > 0"]
  - [e.g., "Cash drawer has opening float of $200"]

STEPS:
  1. [Exact action — which button to tap, which screen to look at]
  2. [Next action — be specific: "Tap the blue 'Charge' button at the bottom of the screen"]
  3. [Verification step — "Screen should display: 'Payment successful' with a green checkmark"]
  4. [Additional steps as needed]

EXPECTED RESULT:
  [What success looks like — specific screen state, printed receipt content, system record]

PASS CRITERIA:
  [ ] [Specific observable outcome #1 — e.g., "Order confirmation screen shows correct total"]
  [ ] [Specific observable outcome #2 — e.g., "Receipt prints with correct line items and tax"]
  [ ] [Specific observable outcome #3 — e.g., "Inventory count for QA-TSHIRT-001 decreased by 1"]

FAIL CRITERIA:
  [Any of the following means the test FAILED:]
  - [Specific failure condition — e.g., "Payment declined or error message appears"]
  - [Specific failure condition — e.g., "Receipt does not print within 10 seconds"]

ROLLBACK:
  [How to undo if the test creates real data]
  - [e.g., "Process a full refund for this test order via POS > Orders > [order] > Refund"]
  - [e.g., "Adjust inventory back to original count via Products > [product] > Inventory"]
  - [e.g., "No rollback needed — Dry Run does not create real records"]

NOTES:
  [Any additional context — common failure causes, timing dependencies, etc.]

RESULT:  [ ] PASS  [ ] FAIL
TESTED BY: _______________  DATE: _______________
════════════════════════════════════════════════════════════
```

---

# ============================================================
# MODE 2 — DRY RUN VALIDATION
# ============================================================

## Mode 2: Matrixify Dry Run Validation

Produces the configuration and validation scripts for Matrixify Dry Run testing.

### Test DR-001: Matrixify Dry Run Configuration

```
TEST: Matrixify Dry Run — Product Import
ID:   DR-001
────────────────────────────────────────────────────────────

PRECONDITION:
  - Matrixify app installed on the Shopify store
  - Import-ready data file prepared (from kaizen-dataprep)
  - Expected record counts documented: [X products, Y variants]

STEPS:
  1. Open Shopify Admin > Apps > Matrixify
  2. Click "Import" tab
  3. Upload the prepared import file: [filename]
  4. Click 'Options' and enable the 'Dry Run' checkbox
  5. Select the Products import file/sheet
  6. Review column mapping — verify all columns map correctly
  7. Click "Start Import" to begin Dry Run
  8. Wait for Dry Run to complete (progress bar reaches 100%)
  9. Download the results file when prompted

EXPECTED RESULT:
  - Results file downloads with Matrixify status columns appended
  - Status summary shows: [X] Created, 0 Errors

PASS CRITERIA:
  [ ] Dry Run completes without timeout
  [ ] Error count = 0
  [ ] Created + Updated + Merged count matches expected: [X]
  [ ] No rows with status "Skipped" (unless intentionally filtered)
  [ ] Download results file for detailed review

FAIL CRITERIA:
  - Any row with status "Error"
  - Created count does not match expected record count
  - Dry Run times out or crashes

ROLLBACK:
  No rollback needed — Dry Run does not create real records.

NEXT:
  If PASS → Download results file, run kaizen-validate Mode 2 for quick verdict
  If FAIL → Download results file, run kaizen-validate Mode 1 for full triage
```

Repeat DR-001 pattern for each entity type:
- **DR-002:** Customer Import Dry Run
- **DR-003:** Gift Card Import Dry Run (if in scope)
- **DR-004:** Historical Order Import Dry Run (if in scope)
- **DR-005:** Inventory Import Dry Run

### Post-Dry Run Validation Script

```
TEST: Post-Dry Run Record Count Reconciliation
ID:   DR-010
────────────────────────────────────────────────────────────

PRECONDITION:
  - All entity Dry Runs completed (DR-001 through DR-005)
  - Expected counts from kaizen-dataprep or migration runbook available

STEPS:
  1. Open each Dry Run results file
  2. Count rows by status (Created / Updated / Skipped / Error / Merged)
  3. Compare against expected counts:

  | Entity | Expected | Dry Run Result | Delta | Status |
  |---|---|---|---|---|
  | Products | [X] | [Y] | [±Z] | [PASS/FAIL] |
  | Variants | [X] | [Y] | [±Z] | [PASS/FAIL] |
  | Customers | [X] | [Y] | [±Z] | [PASS/FAIL] |
  | Gift Cards | [X] | [Y] | [±Z] | [PASS/FAIL] |
  | Orders | [X] | [Y] | [±Z] | [PASS/FAIL] |

  4. If any delta > 0, investigate the missing/extra records

PASS CRITERIA:
  [ ] All entity counts match expected (delta = 0 for each)
  [ ] No blocking errors in any entity Dry Run
  [ ] All results files saved for audit trail

FAIL CRITERIA:
  - Any entity count delta > 0 without explanation
  - Any entity with blocking errors

RESULT:  [ ] PASS  [ ] FAIL
TESTED BY: _______________  DATE: _______________
```

---

# ============================================================
# MODE 3 — TRANSACTION TESTING
# ============================================================

## Mode 3: POS Transaction Test Scripts

Produces test scripts for every transaction type the store will handle. All tests use a designated test product (or products) to be created before testing begins.

### Test Setup: Create Test Products

```
PRE-TEST SETUP
════════════════════════════════════════════════════════════

Before running transaction tests, create the following test products in Shopify:

| Product | SKU | Price | Inventory | Variants | Notes |
|---|---|---|---|---|---|
| QA Test Shirt | QA-SHIRT-001 | $25.00 | 100 per location | S, M, L | Standard product |
| QA Test Bundle | QA-BUNDLE-001 | $75.00 | 50 per location | None | Single-variant, high price |
| QA Gift Card | QA-GC-001 | $50.00 | N/A | $25, $50, $100 | Gift card product |
| QA Discount Item | QA-DISC-001 | $100.00 | 50 per location | None | For discount testing |

Publish all test products to the POS channel.
Assign inventory to all test locations.

These products will be removed after testing is complete.
```

### Transaction Test Scripts

**TXN-001: Simple Sale — Single Item, Card Payment**

```
TEST: Simple Sale — Single Item, Card Payment
ID:   TXN-001
PRIORITY: Critical
LOCATION: [Each location — run at every location]
ESTIMATED TIME: 3 minutes

PRECONDITION:
  - POS app open, logged in as Cashier role
  - Test product QA-SHIRT-001 exists with inventory > 0
  - Card reader powered on and connected (status light solid)

STEPS:
  1. From the POS home screen, tap "Products" or search for "QA Test Shirt"
  2. Tap "QA Test Shirt" to add to cart
  3. Select variant "M" (Medium)
  4. Verify cart shows: QA Test Shirt (M) — $25.00
  5. Tap the blue "Charge $25.00" button (amount includes applicable tax)
  6. Tap "Credit/Debit" payment method
  7. Present the test credit card to the card reader (tap, insert, or swipe)
  8. Wait for "Payment approved" confirmation on screen
  9. When prompted, select receipt delivery method: "No receipt" (for test)
  10. Verify order confirmation screen appears

EXPECTED RESULT:
  Order confirmation shows: 1x QA Test Shirt (M), payment by card, correct total with tax.

PASS CRITERIA:
  [ ] Product added to cart with correct price ($25.00)
  [ ] Tax calculated correctly for this location
  [ ] Card reader accepted the payment without error
  [ ] Order confirmation screen displayed
  [ ] Order appears in Shopify Admin > Orders within 30 seconds

FAIL CRITERIA:
  - Card reader does not connect or shows error
  - Payment declined (and card is known good)
  - Order does not appear in Admin within 60 seconds
  - Tax amount is incorrect for location

ROLLBACK:
  Refund this order: POS > Orders > most recent order > Refund > Full refund to original payment method

RESULT:  [ ] PASS  [ ] FAIL
TESTED BY: _______________  DATE: _______________
```

**TXN-002: Multi-Item Sale with Discount**

```
TEST: Multi-Item Sale with Discount
ID:   TXN-002
PRIORITY: Critical
ESTIMATED TIME: 4 minutes

PRECONDITION:
  - Logged in as Manager role (discount permission required)
  - Test products QA-SHIRT-001 and QA-DISC-001 exist with inventory

STEPS:
  1. Add QA Test Shirt (M) to cart — $25.00
  2. Add QA Discount Item to cart — $100.00
  3. Verify cart subtotal: $125.00
  4. Tap the "..." menu or "Discount" on the cart
  5. Select "Percentage" discount
  6. Enter 10%
  7. Verify discount applied: -$12.50
  8. Verify new subtotal: $112.50 (before tax)
  9. Tap "Charge" and complete payment by card
  10. Verify order confirmation with discount shown

PASS CRITERIA:
  [ ] Both items added with correct prices
  [ ] Discount calculated correctly: 10% of $125.00 = $12.50
  [ ] Tax calculated on discounted subtotal ($112.50), not original
  [ ] Order confirmation shows discount line item

ROLLBACK:
  Full refund via POS > Orders > most recent > Refund

RESULT:  [ ] PASS  [ ] FAIL
TESTED BY: _______________  DATE: _______________
```

**TXN-003: Split Payment — Card + Cash**

```
TEST: Split Payment — Card + Cash
ID:   TXN-003
PRIORITY: Critical
ESTIMATED TIME: 5 minutes

PRECONDITION:
  - Logged in as Cashier or Manager role
  - Cash drawer has opening float
  - QA-BUNDLE-001 exists with inventory

STEPS:
  1. Add QA Test Bundle to cart — $75.00
  2. Tap "Charge $[total with tax]"
  3. Tap "Split Payment" (or "Custom Payment" depending on POS version)
  4. Select "Credit/Debit" as first payment method
  5. Enter amount: $50.00
  6. Present card to reader — wait for approval
  7. Remaining balance shows: $[total - 50.00]
  8. Select "Cash" as second payment method
  9. Enter cash tendered: $[remaining amount, rounded up if needed]
  10. Cash drawer should open
  11. Provide change if applicable
  12. Verify order confirmation shows both payment methods

PASS CRITERIA:
  [ ] Split payment allowed (POS permits partial card payment)
  [ ] Card payment of $50.00 processed successfully
  [ ] Remaining balance calculated correctly
  [ ] Cash payment processed, drawer opened
  [ ] Order confirmation shows: Card $50.00 + Cash $[remaining]
  [ ] Change calculated correctly (if applicable)

FAIL CRITERIA:
  - POS does not allow split payment
  - Card payment for partial amount fails
  - Cash drawer does not open
  - Total collected does not match order total

ROLLBACK:
  Full refund — card portion refunded to card, cash portion refunded as cash

RESULT:  [ ] PASS  [ ] FAIL
TESTED BY: _______________  DATE: _______________
```

**TXN-004: Gift Card Purchase and Redemption**

```
TEST: Gift Card Purchase and Redemption
ID:   TXN-004
PRIORITY: High
ESTIMATED TIME: 6 minutes

PRECONDITION:
  - Gift card product enabled in store
  - Logged in as Cashier or Manager role

STEPS:
  Part A — Purchase Gift Card:
  1. From POS, search for "Gift Card" or tap the Gift Card Smart Grid tile
  2. Select $50.00 denomination
  3. Tap "Charge $50.00" (plus tax if applicable to gift cards in this jurisdiction)
  4. Complete payment by card
  5. Note the gift card code from the receipt or confirmation screen
  6. Verify: gift card appears in Shopify Admin > Products > Gift cards with $50.00 balance

  Part B — Redeem Gift Card:
  7. Start a new sale: add QA Test Shirt (M) — $25.00
  8. Tap "Charge"
  9. Select "Gift Card" as payment method
  10. Enter or scan the gift card code from Step 5
  11. Verify: $25.00 deducted from gift card
  12. Verify: order completed successfully
  13. Check gift card balance: should be $25.00 remaining

PASS CRITERIA:
  [ ] Gift card created with correct denomination ($50.00)
  [ ] Gift card code generated and accessible
  [ ] Gift card accepted as payment method at POS
  [ ] Correct amount deducted ($25.00)
  [ ] Remaining balance accurate ($25.00)
  [ ] Gift card balance visible in Admin

ROLLBACK:
  - Refund the gift card purchase (Part A order)
  - Refund the gift card redemption order (Part B order)
  - Deactivate the test gift card in Admin

RESULT:  [ ] PASS  [ ] FAIL
TESTED BY: _______________  DATE: _______________
```

**TXN-005: Return with Refund to Original Payment Method**

```
TEST: Return with Refund to Original Payment Method
ID:   TXN-005
PRIORITY: Critical
ESTIMATED TIME: 4 minutes

PRECONDITION:
  - A completed test order exists (from TXN-001 or any prior test)
  - Logged in as Manager role (return permission required)
  - Note the order number of the test order to be returned

STEPS:
  1. From POS, tap "Orders" or the menu icon
  2. Search for the test order by order number
  3. Tap the order to open details
  4. Tap "Return" or "Refund"
  5. Select the item(s) to return (all items for full return)
  6. Select refund destination: "Refund to original payment method"
  7. Optionally enter a return reason: "Test return"
  8. Tap "Refund" to confirm
  9. Verify refund confirmation on screen
  10. Verify inventory restocked: product quantity increased by 1

PASS CRITERIA:
  [ ] Order found via POS order lookup
  [ ] Return/refund initiated successfully
  [ ] Refund amount matches original payment
  [ ] Refund issued to original payment method (card refund, not store credit)
  [ ] Inventory restocked (quantity returned to pre-sale level)
  [ ] Refund visible in Shopify Admin > Orders > [order] as refunded

FAIL CRITERIA:
  - Cannot find order via POS
  - Refund option not available (permission issue)
  - Refund goes to wrong payment method
  - Inventory not restocked

ROLLBACK:
  No rollback needed — refund restores original state.

RESULT:  [ ] PASS  [ ] FAIL
TESTED BY: _______________  DATE: _______________
```

**TXN-006: Exchange (Return + New Sale)**

```
TEST: Exchange — Return Item and Sell Replacement
ID:   TXN-006
PRIORITY: High
ESTIMATED TIME: 5 minutes

PRECONDITION:
  - A completed test order exists with QA Test Shirt (M)
  - Logged in as Manager role

STEPS:
  1. Open the existing order from POS > Orders
  2. Initiate a return for QA Test Shirt (M)
  3. On the return screen, select "Exchange" if available, or process as return
  4. If exchange flow: select the replacement item (QA Test Shirt, size L)
  5. If separate transactions: complete the return first, then start a new sale for size L
  6. Handle any price difference:
     - Same price: even exchange, no additional payment
     - Higher price: customer pays the difference
     - Lower price: refund the difference
  7. Complete the transaction
  8. Verify: returned item restocked, new item deducted from inventory

PASS CRITERIA:
  [ ] Return processed for original item
  [ ] New item added and sold
  [ ] Price difference handled correctly
  [ ] Inventory adjusted both ways (return restocked, new item deducted)
  [ ] Customer record updated with both transactions (if customer was attached)

ROLLBACK:
  Refund the new sale, re-process if needed

RESULT:  [ ] PASS  [ ] FAIL
TESTED BY: _______________  DATE: _______________
```

**TXN-007: Custom Sale (Manual Price Entry)**

```
TEST: Custom Sale — Manual Price Entry
ID:   TXN-007
PRIORITY: Medium
ESTIMATED TIME: 3 minutes

PRECONDITION:
  - Logged in as Manager role (custom sale permission required)

STEPS:
  1. From POS home, tap "Custom Sale" (or Smart Grid tile if configured)
  2. Enter amount: $15.00
  3. Optionally enter a title: "Alteration Service"
  4. Tap "Add to cart"
  5. Verify cart shows: Custom Sale — $15.00
  6. Complete payment by card or cash
  7. Verify order confirmation

PASS CRITERIA:
  [ ] Custom sale item created with correct amount
  [ ] Tax applied correctly to custom sale
  [ ] Payment processed
  [ ] Order appears in Admin as a custom line item

ROLLBACK:
  Refund the custom sale order

RESULT:  [ ] PASS  [ ] FAIL
TESTED BY: _______________  DATE: _______________
```

**TXN-008: Customer Lookup and Association**

```
TEST: Customer Lookup and Sale Association
ID:   TXN-008
PRIORITY: High
ESTIMATED TIME: 4 minutes

PRECONDITION:
  - At least one test customer exists in Shopify (from migration or manual creation)
  - Note the test customer's name or email

STEPS:
  1. Start a new sale on POS
  2. Tap "Add Customer" (or customer icon at top of cart)
  3. Search for the test customer by name or email
  4. Select the customer from results
  5. Verify customer name appears on the cart
  6. Add QA Test Shirt to cart
  7. Complete the sale
  8. After sale, verify: order in Admin shows the customer attached
  9. Navigate to the customer's profile: verify the order appears in order history

PASS CRITERIA:
  [ ] Customer found via search (name and email both work)
  [ ] Customer attached to cart before checkout
  [ ] Order shows customer association in Admin
  [ ] Order appears in customer's order history
  [ ] Customer's total spent / order count updated

ROLLBACK:
  Refund the order. Customer association remains in history (acceptable for test).

RESULT:  [ ] PASS  [ ] FAIL
TESTED BY: _______________  DATE: _______________
```

**TXN-009: Inventory Check from POS**

```
TEST: Inventory Check from POS
ID:   TXN-009
PRIORITY: High
ESTIMATED TIME: 2 minutes

PRECONDITION:
  - Multi-location store with inventory at 2+ locations
  - QA Test Shirt exists with known inventory quantities

STEPS:
  1. From POS, search for "QA Test Shirt"
  2. Tap on the product to view details
  3. Check "Availability" or "Inventory" section
  4. Verify inventory counts match expected quantities:
     - [Location 1]: [expected qty]
     - [Location 2]: [expected qty]
  5. If inventory was adjusted by prior tests, account for the delta

PASS CRITERIA:
  [ ] Product details accessible from POS
  [ ] Inventory visible for current location
  [ ] Inventory visible for other locations (if multi-location view enabled)
  [ ] Counts match expected (within test-adjusted delta)

RESULT:  [ ] PASS  [ ] FAIL
TESTED BY: _______________  DATE: _______________
```

**TXN-010: End-of-Day Reconciliation**

```
TEST: End-of-Day Cash Reconciliation
ID:   TXN-010
PRIORITY: Critical
ESTIMATED TIME: 10 minutes

PRECONDITION:
  - Multiple test transactions completed during the session (some cash, some card)
  - Cash drawer has opening float + cash from test transactions
  - Logged in as Manager role

STEPS:
  1. From POS, navigate to "Cash Tracking" or "Register"
  2. Tap "Close Register" or "End Session"
  3. Count the physical cash in the drawer
  4. Enter the counted amount in the POS cash count screen
  5. POS displays expected vs counted:
     - Expected: Opening float + cash received - cash refunds
     - Counted: [your count]
     - Variance: [difference]
  6. Verify the variance is $0.00 (or within acceptable threshold)
  7. Confirm the close
  8. Review the daily summary report:
     - Total sales count
     - Total sales amount
     - Sales by payment method (card vs cash)
     - Sales by staff member (if applicable)
  9. Verify totals match the test transactions executed

PASS CRITERIA:
  [ ] Cash count screen accessible from POS
  [ ] Expected cash amount calculated correctly
  [ ] Variance is $0.00 or within acceptable range
  [ ] Daily summary report available and accurate
  [ ] Sales by payment method matches test transactions
  [ ] Register close completes without error

FAIL CRITERIA:
  - Cash tracking not enabled (configuration issue)
  - Expected amount does not match test transaction math
  - Summary report missing or inaccessible
  - Register cannot be closed

ROLLBACK:
  Reopen register if needed for additional testing.

RESULT:  [ ] PASS  [ ] FAIL
TESTED BY: _______________  DATE: _______________
```

---

# ============================================================
# MODE 4 — HARDWARE VALIDATION
# ============================================================

## Mode 4: Hardware Validation

Produces per-device, per-location hardware test protocols. Every device must pass before training begins.

### Hardware Test Scripts

**HW-001: iPad / POS Device**

```
TEST: iPad POS Device Validation
ID:   HW-001
PRIORITY: Critical
LOCATION: [Specific location]
DEVICE: iPad [model] — Serial: [if known]

PRECONDITION:
  - iPad charged to >50%
  - Connected to store WiFi network
  - Shopify POS app installed and updated to latest version

STEPS:
  1. Power on iPad
  2. Verify WiFi connection: Settings > WiFi > Connected to [network name]
  3. Open Shopify POS app
  4. Log in with test staff credentials
  5. Verify home screen loads with Smart Grid tiles
  6. Navigate to Products — verify product list loads within 5 seconds
  7. Search for a product — verify search returns results within 3 seconds
  8. Navigate to Orders — verify recent orders display
  9. Navigate to Customers — verify customer search works
  10. Check POS Settings are applied (receipts, tipping, cash tracking per config)
  11. Verify POS app version: Settings > About

PASS CRITERIA:
  [ ] iPad powers on and connects to WiFi
  [ ] Shopify POS app opens without error
  [ ] Login succeeds with correct permissions
  [ ] Product catalog loads completely
  [ ] Search is responsive (<3 seconds)
  [ ] All configured POS settings are applied
  [ ] App version is current

FAIL CRITERIA:
  - WiFi connection drops or is unstable
  - POS app crashes on open
  - Product catalog fails to load or is incomplete
  - Search takes >10 seconds consistently

RESULT:  [ ] PASS  [ ] FAIL
TESTED BY: _______________  DATE: _______________
```

**HW-002: Card Reader**

```
TEST: Card Reader Validation
ID:   HW-002
PRIORITY: Critical
LOCATION: [Specific location]
DEVICE: [Reader model — e.g., Shopify Tap & Chip Reader]

PRECONDITION:
  - Card reader charged to >50%
  - iPad POS device validated (HW-001 passed)
  - Test credit card available

STEPS:
  1. Power on card reader
  2. Verify pairing with iPad: POS Settings > Card Reader > [reader name] shows "Connected"
  3. If not paired: follow pairing instructions (Bluetooth > discover > pair)
  4. Start a test sale: add QA Test Shirt to cart, tap "Charge"
  5. Select "Credit/Debit"
  6. TAP test: present card via contactless tap
  7. Verify "Payment approved" within 5 seconds
  8. Start another test sale
  9. INSERT test: insert chip card into reader
  10. Verify "Payment approved" within 10 seconds
  11. Start another test sale
  12. SWIPE test (if reader has swipe): swipe card through magnetic strip reader
  13. Verify "Payment approved"

PASS CRITERIA:
  [ ] Reader powers on and pairs with iPad
  [ ] Tap payment processed successfully
  [ ] Chip insert payment processed successfully
  [ ] Swipe payment processed successfully (if applicable)
  [ ] All payments complete within acceptable time (<10 seconds)
  [ ] Reader maintains connection throughout tests (no drops)

FAIL CRITERIA:
  - Reader does not pair with iPad
  - Any payment method fails to process
  - Reader disconnects mid-transaction
  - Processing takes >30 seconds

ROLLBACK:
  Refund all test transactions

RESULT:  [ ] PASS  [ ] FAIL
TESTED BY: _______________  DATE: _______________
```

**HW-003: Receipt Printer**

```
TEST: Receipt Printer Validation
ID:   HW-003
PRIORITY: High
LOCATION: [Specific location]
DEVICE: [Printer model — e.g., Star Micronics mPOP, Epson TM-m30II]

PRECONDITION:
  - Printer powered on, paper loaded
  - Connected to iPad via [Bluetooth / WiFi / USB]
  - POS receipt settings configured (logo, footer text)

STEPS:
  1. Verify printer connection: POS Settings > Hardware > Printers > [printer name] "Connected"
  2. Print a test receipt: POS Settings > Hardware > Printers > "Print Test Receipt"
  3. Verify test receipt prints completely
  4. Process a test sale (use TXN-001)
  5. At checkout completion, select "Print receipt"
  6. Verify receipt prints with:
     - Store name / logo
     - Transaction details (items, prices, tax, total)
     - Payment method
     - Date and time
     - Custom footer text (return policy, website)
  7. Verify print quality: text is legible, not faded or smeared

PASS CRITERIA:
  [ ] Printer connects and is recognized by POS
  [ ] Test receipt prints within 5 seconds
  [ ] Sale receipt prints with all required information
  [ ] Print quality is clear and legible
  [ ] Custom branding (logo, footer) appears correctly

FAIL CRITERIA:
  - Printer not recognized by POS
  - Receipt does not print (or takes >30 seconds)
  - Print is illegible or cut off
  - Printer jams or feeds blank paper

RESULT:  [ ] PASS  [ ] FAIL
TESTED BY: _______________  DATE: _______________
```

**HW-004: Barcode Scanner**

```
TEST: Barcode Scanner Validation
ID:   HW-004
PRIORITY: High
LOCATION: [Specific location]
DEVICE: [Scanner model]

PRECONDITION:
  - Scanner paired with iPad
  - Test product QA-SHIRT-001 has a barcode assigned (or use a printed test barcode)

STEPS:
  1. Open POS on the cart/sale screen
  2. Scan the barcode on QA Test Shirt with the scanner
  3. Verify product is added to cart automatically
  4. Scan a second product barcode
  5. Verify second product added
  6. Scan the first product barcode again
  7. Verify quantity increments to 2 (or a second line item added)

PASS CRITERIA:
  [ ] Scanner pairs and stays connected
  [ ] Barcode scan adds correct product to cart
  [ ] Multiple scans work consecutively without disconnection
  [ ] Scan-to-cart time < 2 seconds

RESULT:  [ ] PASS  [ ] FAIL
TESTED BY: _______________  DATE: _______________
```

**HW-005: Cash Drawer**

```
TEST: Cash Drawer Validation
ID:   HW-005
PRIORITY: High (if cash accepted at location)
LOCATION: [Specific location]
DEVICE: [Drawer model — standalone or integrated with printer]

STEPS:
  1. Verify drawer is connected (typically via receipt printer)
  2. Process a cash sale: add QA Test Shirt, charge, select Cash
  3. Enter cash tendered amount
  4. Verify cash drawer opens automatically on cash payment completion
  5. Close drawer manually
  6. Open register (POS > Cash Tracking > Open Register) with float amount
  7. Verify drawer opens on register open
  8. Close register (POS > Cash Tracking > Close Register)
  9. Verify drawer opens for cash count

PASS CRITERIA:
  [ ] Drawer opens on cash payment completion
  [ ] Drawer opens on register open/close
  [ ] Drawer lock mechanism works (stays closed when not triggered)
  [ ] Cash compartments are accessible and correctly sized

RESULT:  [ ] PASS  [ ] FAIL
TESTED BY: _______________  DATE: _______________
```

---

# ============================================================
# MODE 5 — CUTOVER SIMULATION
# ============================================================

## Mode 5: Cutover Simulation

End-to-end rehearsal of the actual go-live cutover process. Run 24-48 hours before actual cutover.

```
CUTOVER SIMULATION PLAN
════════════════════════════════════════════════════════════
Client:           [Name]
Simulation Date:  [Date — 24-48 hours before actual cutover]
Locations:        [All locations participating]
Duration:         [Estimated 2-4 hours]
Lead:             KaizenCommerce
Participants:     [Client store managers, key staff]
════════════════════════════════════════════════════════════

PHASE 1: Pre-Cutover Verification (30 min)
  [ ] All Dry Run validations passed (DR-001 through DR-010)
  [ ] All hardware validated at all locations (HW-001 through HW-005)
  [ ] All transaction types tested (TXN-001 through TXN-010)
  [ ] Staff training completed and sign-off received
  [ ] Legacy system end-of-day completed and final data snapshot taken

PHASE 2: Simulated Data Freeze (30 min)
  [ ] Simulate stopping new transactions on legacy system
  [ ] Run final inventory count comparison: legacy vs Shopify
  [ ] Verify customer record counts match
  [ ] Verify gift card balances match (spot-check 10 cards)
  [ ] Document any discrepancies

PHASE 3: Simulated Go-Live (60 min)
  [ ] Switch all POS devices to Shopify POS (login, verify home screen)
  [ ] Run one transaction per location (TXN-001 simple sale)
  [ ] Run one return per location (TXN-005)
  [ ] Run one cash transaction per location (for cash drawer test)
  [ ] Verify all transactions appear in Shopify Admin
  [ ] Verify inventory adjustments reflect correctly across locations

PHASE 4: Simulated End-of-Day (30 min)
  [ ] Run end-of-day close on each POS (TXN-010)
  [ ] Verify daily summary reports accessible
  [ ] Verify sales totals match expected test transaction amounts
  [ ] Confirm cash reconciliation works

PHASE 5: Rollback Rehearsal (30 min)
  [ ] Document: if go-live fails, what is the rollback procedure?
  [ ] Verify legacy system can be reactivated within [X] minutes
  [ ] Verify data state on both systems is documented
  [ ] Confirm rollback decision criteria: "We roll back if [specific conditions]"

SIMULATION VERDICT:
  [ ] ALL PHASES PASSED — Proceed to live cutover as scheduled
  [ ] ISSUES FOUND — Document and resolve before cutover (list issues)
  [ ] CRITICAL FAILURE — Postpone cutover until resolved (state reason)
```

---

# ============================================================
# MODE 6 — ACCEPTANCE TESTING
# ============================================================

## Mode 6: Client Acceptance Testing (UAT)

Produces the client sign-off test suite. These are the tests the CLIENT runs (with KaizenCommerce support) to formally accept the system.

```
CLIENT ACCEPTANCE TEST SUITE
════════════════════════════════════════════════════════════
Client:        [Name]
Date:          [Date]
Tested By:     [Client representative name]
Supported By:  KaizenCommerce
════════════════════════════════════════════════════════════

Instructions: For each test, follow the steps and mark PASS or FAIL.
If any test fails, note the issue in the Comments column.
All Critical tests must pass for go-live approval.

| # | Test | Priority | Steps (Simplified) | Pass/Fail | Comments |
|---|---|---|---|---|---|
| 1 | Ring up a sale by card | Critical | Add item > Charge > Card > Confirm | [ ] | |
| 2 | Ring up a sale by cash | Critical | Add item > Charge > Cash > Enter amount > Drawer opens | [ ] | |
| 3 | Apply a discount | Critical | Add item > Apply % discount > Charge | [ ] | |
| 4 | Process a return | Critical | Orders > Find order > Refund > Confirm | [ ] | |
| 5 | Split payment (card + cash) | Critical | Add item > Charge > Split > Card first > Cash second | [ ] | |
| 6 | Sell a gift card | High | Gift Card tile > Select amount > Charge | [ ] | |
| 7 | Redeem a gift card | High | Add item > Charge > Gift Card > Enter code | [ ] | |
| 8 | Look up a customer | High | Add Customer > Search by name > Attach to sale | [ ] | |
| 9 | Check inventory at another location | High | Search product > View availability > See other locations | [ ] | |
| 10 | Print a receipt | High | Complete sale > Select Print Receipt > Verify printout | [ ] | |
| 11 | Close the register | Critical | Cash Tracking > Close > Count cash > Confirm | [ ] | |
| 12 | View daily sales report | High | Reports > Daily Summary > Verify totals | [ ] | |

SIGN-OFF:

"I have completed the acceptance tests above. All Critical tests have passed.
I approve the system for live operation."

Client Signature: ___________________________
Name:             ___________________________
Date:             ___________________________

KaizenCommerce:   ___________________________
Name:             ___________________________
Date:             ___________________________
```

---

## Test Results Summary Template

After all testing is complete, produce a summary:

```
TEST RESULTS SUMMARY
════════════════════════════════════════════════════════════
Client:              [Name]
Test Date(s):        [Date range]
Locations Tested:    [Count / names]

| Category | Total Tests | Passed | Failed | Pass Rate |
|---|---|---|---|---|
| Dry Run Validation | [n] | [n] | [n] | [%] |
| Hardware Validation | [n] | [n] | [n] | [%] |
| Transaction Testing | [n] | [n] | [n] | [%] |
| Cutover Simulation | [n] | [n] | [n] | [%] |
| Client Acceptance | [n] | [n] | [n] | [%] |
| **Total** | **[n]** | **[n]** | **[n]** | **[%]** |

FAILED TESTS (if any):
| Test ID | Description | Failure Reason | Resolution | Status |
|---|---|---|---|---|
| [ID] | [Name] | [What failed] | [How it was fixed] | [Resolved / Open] |

GO/NO-GO RECOMMENDATION:
  [ ] GO — All critical tests passed. Proceed to live cutover.
  [ ] NO-GO — [n] critical failures unresolved. List: [IDs]
  [ ] CONDITIONAL GO — All critical tests passed. [n] non-critical issues tracked for post-go-live resolution.

Recommended by: KaizenCommerce
Date: [Date]
```

---

<critical_rules priority="must-follow">
- EVERY test script must follow the exact format: TEST name, ID, PRECONDITION, STEPS, EXPECTED RESULT, PASS CRITERIA, FAIL CRITERIA, ROLLBACK.
- NEVER write vague steps. "Process a sale" is not a step. "Tap the blue 'Charge $25.00' button at the bottom of the screen" is a step.
- ALWAYS include rollback instructions for tests that create real data.
- ALWAYS include test IDs in a consistent format: [CATEGORY]-[NUMBER].
- ALWAYS test at EVERY location. Do not assume one location passing means all pass.
- NEVER sign off on go-live if ANY critical test has failed. The go/no-go gate is absolute.
- ALWAYS include the cutover simulation (Mode 5) before any live cutover. The Kaizen Cutover depends on rehearsal — both systems must be proven before legacy is turned off.
- All test products must be cleaned up after testing is complete. Include cleanup instructions.
- Voice rules from `reference/kaizen-identity.md` apply. Direct, specific, no filler.
- POS capabilities and migration methodology are embedded in this skill directly. Apply, do not duplicate.
</critical_rules>

<preferences priority="should-follow">
- Group tests by category and run them in sequence. Dry Run > Hardware > Transactions > Integration > Cutover > Acceptance.
- Include time estimates for each test so the team can schedule testing windows.
- Print the test scripts and use them as physical checklists on the sales floor. Format accordingly.
- When a test fails, the tester should stop and document the failure immediately, not continue testing.
- Include a "Test Environment Setup" section at the top of every full test suite listing test products, test customers, and test payment methods to create before testing begins.
</preferences>

---

<verification>
Before finalizing any test output:

1. **Format check:** Does every test follow the exact script format (ID, precondition, steps, expected, pass/fail, rollback)?
2. **Coverage check:** Are all 10 transaction types covered (simple sale, multi-item, split payment, gift card purchase, gift card redemption, return, exchange, custom sale, customer lookup, end-of-day)?
3. **Hardware check:** Is every device type at every location tested?
4. **Location check:** Are tests specified per-location where location-specific results matter?
5. **Rollback check:** Does every data-creating test have rollback instructions?
6. **Sequence check:** Is testing sequenced correctly (Dry Run > Hardware > Transactions > Cutover > Acceptance)?
7. **Cleanup check:** Are test product/data cleanup instructions included?
8. **Sign-off check:** Is there a clear go/no-go decision framework?
9. **Readability check:** Could a non-technical store manager follow these steps without help?
10. **ID check:** Are all test IDs unique and consistent with the naming convention?
</verification>

---

## HANDOFF — Output in Chat (Never in the Document)

```
---
## HANDOFF -> Next Step

**What was produced:** [Full test suite / Dry Run validation / Transaction tests / Hardware tests / Cutover simulation / Acceptance tests]
**Client:** [name]
**Locations covered:** [count]
**Total tests:** [count]

**Next pipeline step:**
- If all tests passed -> Proceed to live cutover per migration plan
- If failures found -> Fix issues, re-run failed tests only
- If cutover simulation passed -> Schedule live cutover within 24-48 hours
- If acceptance testing passed -> Client signs off, proceed to go-live
- After go-live confirmed -> Ask me to run the kaizen-report-exec skill for health check report
```

---

## ABORT_CLEANUP / Created Resource Ledger

Testing that creates Shopify products, orders, customers, discounts, gift cards, inventory
adjustments, POS transactions, AnyDB records, exports, screenshots, or client-visible artifacts must
maintain a Created Resource Ledger.

Ledger fields:

- test ID and test run folder
- resource type and exact name or ID
- environment, location, device, and staff role used
- creation step and expected cleanup step
- cleanup owner and due date
- proof of cleanup: screenshot, export, admin path, or count check
- final status: retained for evidence, cleaned, failed cleanup, or client approved retention

`ABORT_CLEANUP` is mandatory when a test run stops after creating resources. The abort note must
state which tests passed, which failed, which data was cleaned, which data remains, and whether
go-live remains blocked.
