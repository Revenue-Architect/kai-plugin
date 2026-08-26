---
name: kaizen-ref-features
description: "Deep retail reference for features questions routed by Kai."
metadata_version: 1
layer: retail-reference
upstream: ["kaizen-retail-expert-v2"]
downstream: []
adjacent: []
canon: []
owns: ["features domain reference"]
does_not_own: ["final implementation recommendation without routed skill context"]
---

### 3I. Recent Features 2025-2026

---

#### Recent POS & Retail Features

##### Quick Counts (POS Extension) -- Shipped 2025

Native POS extension that lets store staff verify and correct inventory levels directly from POS using barcode scanning. Replaces Stocky stock takes.

**Capabilities:** Barcode scanning (top-right scanner button), search by name (paginated in batches of 50), enter actual count per variant with discrepancy view, bulk submission, remove items from count mid-session, supports ~1,000 items per session (optimized local storage), tablet-optimized button layout. Renamed from "Cycle Count" to "Stock Count" / "Quick Count" for merchant clarity.

**Limitations:**
- No blind counts (staff sees expected quantity)
- No scheduled/managed count plans from admin
- No manager approval workflow for large variances
- No multi-user concurrent counting with merged results
- No zone/bin-level counting
- No discrete count event audit trail (adjustments go into general history)
- No recount/verification flow for high-variance items
- `inventorySetQuantities` mutation is all-or-nothing -- if one item has a stale quantity (sold during count), entire submission fails

**Pre-Sales Positioning:**
> "Shopify POS now includes native Quick Counts -- staff scan items, enter actual quantities, and the system highlights discrepancies and submits adjustments directly. For basic cycle counting at retail locations, this eliminates the need for separate tools. For enterprise-grade counting with blind counts, scheduled rotations, and multi-user sessions, third-party apps like Stocktake Online or SKULabs provide that layer."

##### Liquid Receipt Customization -- Shipped 2025

Full Liquid template editor for all receipt types (sales, gift, return, exchange). POS Pro required. Customization includes store logo, custom header/footer, QR codes, 1D barcodes, custom properties, VAT compliance (France, Spain).

**Settings architecture:** [INTERNAL-ONLY]
- Global settings stored in `physical_receipt_global_settings` table (logo_id)
- Local (per-location) settings in `physical_receipt_local_settings` table
- Accessed via GraphQL

##### Cash Management Enhancements -- Shipped March 2026

Register-based cash sessions (tied to specific registers, not just locations), native cash tracking, reason-coded adjustments, custom workflow automation. Fixed: cash tracking on saved carts now updates based on device that completed checkout.

##### POS Pick & Pack for BOPIS -- Shipped March 2026

Barcode scanning for pick and pack on in-store pickup orders. Staff scan items to verify picks before marking as ready.

##### Smart Grid Improvements -- 2025-2026

Discount code tiles (staff select admin-created codes instead of typing), Smart Grid v2 editor, tiles for products, collections, discounts, apps, custom actions.

##### Gift Card Cashout -- Shipped March 2026

POS can cash out gift cards under $15 where permitted by law (parts of US and Canada). Automatic compliance with state/provincial gift card cashout regulations.

##### POS v11 Checkout Redesign -- Shipped Feb-March 2026 [INTERNAL-ONLY]

Major UX overhaul: Cart visible throughout checkout, side panel modifiers, multi-line-item editing, improved customer search, faster payment selection, inline number pads, multi-select in cart for bulk edits.

**iOS v11.0:**
- Cart remains visible throughout checkout (no context loss)
- Cart modifiers open in side panel (not full screen) for faster edits
- Line item actions in a tray with multi-line-item editing (bulk edits)
- Simplified "More Actions" menu (order-level tasks only)
- Improved customer search with inline form for faster profile creation

**Android v11.0:**
- Multi-select in cart for bulk edits
- Key actions open in left panel workspace
- Smarter add-customer flow with autofill

v11.1: Search highlights exact matches, View Customer Details permission, Italy fiscal updates (Epson RT II: gift card payments as multi-use vouchers).
v11.2: Keyboard shortcuts, barcode scanning BOPIS, register-based cash sessions, discount UX improvements, gift card cashout, France/Spain VAT receipt compliance.

##### Outgoing Transfers from POS -- Shipped Feb 2026

Store staff can now pick, pack, and send inventory to other locations directly from POS. Previously could only receive. Found under Orders section in POS (incoming transfers remain under Products). POS now supports full transfer lifecycle: create, ship, receive.

##### Per-Device Offline Controls -- Shipped Feb 2026

Merchants can enable/disable offline selling on individual devices independently (previously global setting). Use case: enable offline on POS Go (mobile/pop-up) but disable on fixed registers with reliable WiFi.

##### Inventory States Visible in POS -- 2025-2026

POS now displays Committed and Incoming inventory states in addition to Available. Staff can see what's actually sellable vs committed to pending orders.

##### POS Hub Hardware -- Shipped 2026

USB hub connecting multiple wired peripherals. Eliminates Bluetooth disconnection issues.

##### Buy X Get Y Discount Codes at POS -- 2025-2026

"Buy X Get Y" discount codes now supported at POS. Configurable for specific products, collections, or customer segments. Options to set maximum uses per order and total usage limits.

##### Remote Login via QR Code -- Shipped 2026 [INTERNAL-ONLY]

- Admin staff can authorize POS login remotely by scanning a QR code or entering an 8-digit code
- More secure than sharing admin credentials
- Only admin-level staff can provide remote authorization

##### Regional Receipt Compliance -- March 2026

France and Spain: Printed receipts now include line-item VAT and VAT summary by default. Automatic compliance.

##### Italy Fiscal Reporting (Epson RT II) -- Shipped 2026

- Gift card payments reported as multi-use vouchers (not subtotal adjustments)
- Return/exchange items applied to new purchase reported as store credit
- Specific to Italy with Epson RT II fiscal printers

##### POS Core Exchange Primitives Migration -- In Progress [INTERNAL-ONLY]

POS is migrating to use core Shopify exchange primitives (same engine as online), enabling consistent exchange behavior across channels.

**Impact:**
- Unified exchange logic between POS and online
- Enables Liquid receipt customization for exchanges
- Better data consistency for reporting

##### Inventory Management Migration (Post-Stocky)

Stocky is being sunset. Key features migrating to core Shopify: Quick Counts (shipped), purchase orders (in progress), stock transfers (already native), inventory adjustments (already native). Supplier management TBD (third-party recommended). Demand forecasting not expected in core (use Inventory Planner, Flieber).

##### What to Watch (Roadmap Signals) [INTERNAL-ONLY]

These are areas with active development signals -- do NOT promise to merchants:
- Enhanced POS fulfillment workflows (pick & pack improvements)
- Expanded Quick Count capabilities
- Further receipt customization
- Cash management automation
- POS UI Extensions expanding to new targets
- Polaris web components migration for POS extensions (2025-10+)
- Inventory groups (logical groupings beyond physical locations)
- Named quantities system replacing legacy inventory adjustments

Always check Vault (`vault-mcp`) for latest project status before discussing roadmap.

---

