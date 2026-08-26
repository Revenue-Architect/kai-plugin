# KaizenCommerce Carousel Reference

Moved verbatim from `skills/kaizen-publish.md` to keep the publish router lean without compressing or deleting any guidance.

## Existing Carousels (Reference)

### 1. The 2-Location Wall (Spreadsheet ops)
- Topic: Spreadsheets break at 2+ retail locations
- Problem: No single truth, transfer errors, stale data, inbox-based receiving
- Solution: Shopify POS + AnyDB (commerce + ops separation)
- Accent: Red + Navy

### 2. The Inventory Sync Problem
- Topic: Online inventory != shelf inventory causes oversells
- Problem: Oversell cascade, manual sync lag, blind replenishment
- Root cause: Two separate systems, not one unified source
- Solution: Unified Shopify POS — one inventory, every channel, real time
- Accent: Red + Navy

## Carousel Topic Ideas (pre-seeded)

- The POS Migration Risk (what goes wrong when you migrate wrong)
- The 5-Location Problem (ops complexity at scale)
- The B2B Trap (why B2B on Shopify requires ops architecture, not just a portal)
- The Receiving Black Hole (PO-to-shelf without a paper trail)
- The Vendor Reconciliation Problem (discrepancies, disputes, resolution workflows)
- The BOPIS Fail (click-and-collect breaking because inventory isn't unified)
- The Custom Ops Gap (what Shopify doesn't do and what fills it)
- The Blueprint Explained (what you get in 14 days)

## Carousel Example — The BOPIS Fail

```
CAROUSEL: The BOPIS Fail
ACCENT: Red + Navy
TOPIC: Click-and-collect breaks when inventory isn't unified across channels
TARGET READER: Multi-location retail ops manager or COO with 3-10 stores

---

SLIDE 1 — HOOK
Pattern: A
Eyebrow: THE BOPIS PROBLEM
Headline:
  Line 1 (white): Customer orders online.
  Line 2 (accent): Store says "we don't have it."
  Line 3 (white): You just lost both the sale and the trust.
Bold sub-statement: 73% of failed BOPIS orders trace back to one root cause.
Supporting one-liner: It's not your staff. It's your inventory architecture.

---

SLIDE 2 — FAILURE CASCADE
Pattern: B
Eyebrow: WHAT ACTUALLY HAPPENS
Headline:
  Line 1 (white): One order. Three systems.
  Line 2 (accent): Zero coordination.
Bullets:
  - [mid tick] Oversold SKU | Online showed 4 units. Shelf had 0. POS sold the last one an hour ago.
  - [mid tick] Manual cancel | Staff calls customer. Refund takes 3-5 days. Customer posts on Google.
  - [mid tick] Fulfillment scramble | Manager drives to another location. Eats the shipping margin.
  - [red tick] Lost repeat buyer | Customer switches to competitor with real-time availability.
Footer: Every failed pickup costs you more than the sale itself.

---

SLIDE 3 — THE SCALE TRAP
Pattern: F
Eyebrow: IT GETS WORSE
Headline:
  Line 1 (white): More locations.
  Line 2 (accent): More failure points.
Rows:
  - [navy bar, 20%] 1 location | Oversell rate: ~2% | Manageable
  - [navy bar, 45%] 3 locations | Oversell rate: ~8% | Weekly customer complaints
  - [alpha-red bar, 70%] 5 locations | Oversell rate: ~15% | Daily fulfillment scrambles
  - [red bar, 95%] 10 locations | Oversell rate: ~25% | Structural revenue loss
Footer: The problem doesn't grow linearly. It multiplies.

---

SLIDE 4 — ROOT CAUSE
Pattern: C
Eyebrow: ROOT CAUSE
Headline:
  Line 1 (white): Two inventory systems
  Line 2 (accent): pretending to be one.
Cards:
  - [mid cell] POS inventory | Updated at sale. Doesn't know about online orders until sync runs.
  - [mid cell] Ecommerce inventory | Shows "available" based on last batch import. Could be hours stale.
  - [navy cell] No arbitration layer | When both systems claim the same unit, the customer loses.
Footer: The gap between your POS and your website is where trust goes to die.

---

SLIDE 5 — THE SOLUTION
Pattern: E
Eyebrow: THE FIX
Headline:
  Line 1 (white): One inventory.
  Line 2 (accent): Every channel. Real time.
Left Box — SHOPIFY POS:
  --> All transactions
  --> Inventory master (single source)
  --> Real-time availability across all channels
  --> Automatic hold on BOPIS orders
Right Box — ANYDB OPS:
  --> Exception queue for stock discrepancies
  --> Receiving workflow (PO to shelf)
  --> Location transfer tracking
  --> Replenishment triggers
Footer: Commerce and operations in sync. Not in competition.

---

SLIDE 6 — BEFORE VS AFTER
Pattern: D
Eyebrow: BEFORE VS AFTER
Headline:
  Line 1 (white): Same stores.
  Line 2 (accent): Different architecture.
Rows:
  - BEFORE: Inventory syncs every 4 hours | AFTER: Real-time across all locations
  - BEFORE: BOPIS orders oversold weekly | AFTER: Automatic hold reserves stock at pickup location
  - BEFORE: Staff calls customer to cancel | AFTER: Customer gets accurate availability before ordering
  - BEFORE: Manager drives stock between stores | AFTER: Transfer workflow routes stock before it's needed
  - BEFORE: 15% oversell rate at 5 locations | AFTER: Sub-1% with unified inventory
Footer: The difference isn't effort. It's architecture.

---

SLIDE 7 — CTA
Pattern: G
Eyebrow: KAIZEN UNIFIED COMMERCE BLUEPRINT
Headline:
  Line 1 (white): Ready to make BOPIS
  Line 2 (accent): actually work?
CTA Box:
  --> 14-day diagnostic of your inventory architecture across all locations and channels
  --> Identify every sync gap, oversell risk, and fulfillment bottleneck
  --> [BLUEPRINT_FEE] — credited toward your implementation

kaizencommerce.ca -->
```

---

# MODE 2: PPTX DECK
