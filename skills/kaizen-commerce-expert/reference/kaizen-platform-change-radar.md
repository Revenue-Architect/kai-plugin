# Kaizen Platform Change Radar

Curated Shopify platform changes that affect KaizenCommerce recommendations, scoping, or delivery.
This is a judgment layer on top of the generated feeds in `reference-content/`, which are navigation
only. Load it during scoping, Blueprint, architecture, build-vs-buy, and pre-launch QA.

**Last swept:** 2026-07-26. **Sweep window:** April 2026 to July 2026.

Confidence marks: **[CONFIRMED]** means the canonical entry or doc was read in full.
**[LISTED]** means the item appeared on a canonical changelog index with title and date, but the
entry body has not been read. Never put a `[LISTED]` item into client-facing work without opening it.

---

## 1. Already In Effect — Act Now

### Shopify Scripts are switched off [CONFIRMED]

| | |
|---|---|
| Editing/publishing ended | 2026-04-15 |
| **Execution ended** | **2026-06-30** |
| Source | `shopify.dev/changelog/shopify-scripts-will-be-deprecated-on-june-30-2026`, `changelog.shopify.com/posts/shopify-scripts-can-no-longer-be-edited-or-published` |

This deadline has passed. Any Plus merchant still relying on Scripts has broken checkout, shipping,
or payment customizations right now, not at some future date.

**Kaizen action:** add a Scripts check to every Plus merchant diagnostic. If discovery finds Scripts,
that is a live incident, not a roadmap item. Migration targets are Shopify Functions or a public app
built on Functions. The Scripts customizations report in admin accelerates the audit.

**Build-vs-buy consequence:** only **Plus** stores can install **custom** apps containing Function
APIs. Stores on any plan can install **public** App Store apps built on Functions. Below Plus, custom
checkout logic means buying an app or moving the logic out of checkout.

### Dated removal: Customer Account API checkout types, 2026-10 [LISTED]

`Customer.lastIncompleteCheckout` and the `Checkout` types are removed from the Customer Account API
in the **2026-10** version. This is the same shape of problem as Scripts, caught early enough to plan
around. Any customer-account or headless work touching abandoned-checkout recovery needs an audit
before that version lands.

**Kaizen action:** check for these fields during architecture review on customer-account and headless
engagements. Add the removal date to the risk register on any project that will still be live in
Q4 2026.

---

## 2. Feature Previews — Do Not Promise These

Preview APIs run on the unstable API version, require enabling on a development store, and are
explicitly subject to change. They belong in roadmap conversations, never in a SOW deliverable.

### Physical inventory: bins, counts, purchase orders [CONFIRMED]

| | |
|---|---|
| Announced | 2026-07-17 |
| Status | Feature preview, unstable GraphQL Admin API, dev store opt-in |
| Source | `shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps/physical-inventory-feature-preview` |

What it introduces:

- **Bins.** Named storage inside a location (shelf, rack). `binsUpsert` creates and updates them, with an optional barcode.
- **Counts.** `inventoryCountCreate` sets on-hand for an item in a bin.
- **Purchase orders.** **Read-only** through the public API: the PO, its line items, and its supplier.

The model is additive. `onHand = unbinnedQuantity + sum(bin quantities)`. Existing
`inventorySetQuantities` calls keep working and land in the unbinned quantity, and location-level
aggregates are unchanged.

**This is the most consequential item on the radar for KaizenCommerce.** Two of the stated triggers
for recommending the AnyDB operating layer are "inventory tracking needs beyond Shopify native (bin,
shelf, condition)" and "vendor PO lifecycle needs structured tracking". Shopify is building into both.

How to hold the position honestly today:

- Bin-level on-hand tracking is heading native. Stop treating "Shopify cannot do bins" as durable. It is true today on stable APIs and will not stay true.
- PO support in the preview is **read**, not lifecycle. Creating, approving, receiving against, and reconciling a PO is still not native. The AnyDB PO case stands on lifecycle and approval state, not on storage.
- Condition, serial, lot, and exception state are not in the preview at all.
- For a merchant launching in the next two quarters, scope against stable APIs and name the preview as a known direction. Do not scope a build that the preview will obsolete, and do not defer a merchant's operational need waiting for a preview to ship.

Revisit this entry when the APIs reach a stable version. The build-vs-buy tables in
`kaizen-build-vs-buy.md` and the AnyDB triggers in `kaizen-identity.md` both carry a pointer here.

### Market-driven shipping [LISTED]

Announced 2026-07-01, alongside **deprecation of merchant-owned delivery profile APIs**. A
deprecation attached to a preview is a migration signal for any merchant with custom delivery
profiles. Open the entry before scoping shipping work.

### Inventory transfers [LISTED]

Developer preview since 2025-04-08. Multi-shipment transfers, shipment tracking, receiving workflow
with accept/reject, webhooks, metafield extensibility, and bi-directional external sync. Directly
relevant to multi-location retail and called out by Shopify as aimed at POS solution providers.

---

## 3. POS Surface Changes

### POS UI extensions 2026-07: per-unit fixed-amount line item discounts [LISTED]

Announced 2026-07-08 and flagged as a **breaking change**. Any KaizenCommerce or client POS extension
doing line-item discounting needs review against the 2026-07 version before upgrading. Treat as a
compatibility gate in pre-launch QA.

### POS UI extensions 2026-07: discount allocations on bundle components [LISTED]

Announced 2026-07-15. Relevant where bundles and POS discounting meet.

### POS extensions: background extension target [LISTED]

Announced 2026-07-09. A background target opens POS automation patterns that previously needed a
foreground surface. Worth reading before scoping custom POS workflow.

---

## 4. B2B Changes

### Native B2B on Basic, Grow, and Advanced [CONFIRMED]

Announced 2026-04-02. Full treatment lives in `skills/kaizen-reference/kaizen-ref-b2b.md`, including
the plan capability matrix and the deposit and catalog-ceiling traps. Summary: B2B is no longer a
Plus conversation, but plan tier still decides architecture.

### Draft order deposit fields in Admin and Customer Account APIs [LISTED]

Announced 2026-07-01. Deposits are a Plus-only capability, so this is API surface for a gated
feature. Read before scoping any deposit workflow, and re-check whether the plan gate moved.

### B2B features in Horizon themes [LISTED]

Horizon themes carry B2B support: volume pricing tiers, quantity rules, quick order lists. Combined
with the free Trade theme on every plan, the storefront side of a B2B launch is lighter than it was.

---

## 5. DTC And Admin Changes That Reach POS

### New Collection model and APIs [LISTED]

Announced 2026-06-17. Collections underpin merchandising, catalog scoping, and B2B publications. A
model change here reaches POS, DTC, and B2B at once. Read before catalog architecture work.

### Metafield triggers and additional topics for Events [LISTED]

Announced 2026-07-21. More native trigger coverage narrows the Flow-versus-operating-layer gap.
Re-check the boundary in `kaizen-flow` before recommending a custom automation.

### Liquid templates compose with blocks and partials [LISTED]

Announced 2026-07-21. Theme architecture change. Matters for storefront scoping, not for POS.

### Bulk queries up to 4x faster [LISTED]

Announced 2026-06-17. Improves large migration extract windows. Useful input to cutover timing on
high-volume migrations.

---

## Sweep Protocol

Run this sweep monthly, and always before a Blueprint or an implementation proposal.

1. Refresh the generated index: `python3 skills/kaizen-commerce-expert/scripts/update_vendor_knowledge.py`
2. Read `reference-content/_needs-merge.md` for flagged ambiguous items.
3. Open `shopify.dev/changelog` and `changelog.shopify.com` for the period since the last sweep.
4. Promote anything that changes a Kaizen recommendation into this file with a date, a source, a confidence mark, and a "Kaizen action" line.
5. Update the sweep date at the top.

**Resolved 2026-07-26:** the `shopify.dev` developer changelog feed had stopped parsing
(`not well-formed (invalid token): line 61, column 42`). Cause was a single vertical tab (`0x0B`) in
a TOML code block. XML 1.0 forbids that character anywhere, including inside CDATA, so one bad byte
in 1.6MB made the whole document unparseable and silently cost every developer-side item for the
window. The updater now strips illegal XML characters before parsing, tracks a per-source fetch
timestamp so a failing source keeps its backlog, and exposes `--backfill` to recover a missed window.
The 23 developer entries missed during the outage were backfilled the same day, and the freshness
audit now warns when any source reports an error.

If a sweep ever finds the developer index thin again, check `_freshness-manifest.json` for a
non-empty `errors` object before assuming Shopify shipped nothing.
