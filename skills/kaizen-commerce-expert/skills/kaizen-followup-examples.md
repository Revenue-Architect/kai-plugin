---
name: kaizen-followup-examples
description: >
  Reference examples for the kaizen-followup skill. Load this file when verifying output
  quality — every follow-up email produced by kaizen-followup should meet or exceed the
  quality bar set by these examples. Contains canonical examples for all four modes plus
  failing output patterns and a per-mode quality rating system.
metadata_version: 1
layer: supporting-reference
upstream: ["kaizen-followup"]
downstream: []
adjacent: []
canon: []
owns: ["follow-up examples and pattern demonstrations"]
does_not_own: ["live client facts or canonical policy"]
---

# KaizenCommerce — Follow-Up Examples

This file is a quality benchmark, not a template library. Do not copy these emails.
Use them to verify that your output matches the depth, specificity, and voice standard
demonstrated below.

---

## How to Use This File

When `kaizen-followup` produces an email, load this file and run the mode-specific checks:

### All Modes — Universal Checks

1. **Specificity match:** Does the output name the merchant's actual system, data model, and
   operational details the way the examples below name specific platforms, fields, and
   workflows? "Your current system" is never acceptable.

2. **Why test:** Does the output explain the reasoning behind each recommendation? "We do X"
   fails. "We do X because Y" passes.

3. **Tone calibration:** Does it read like someone who was on the call / reviewed the
   Blueprint / knows the project, or like a vendor who read a brief?

4. **Voice compliance:** No forbidden phrases, no em dash drama, no hollow opener, first line
   about the merchant.

### Mode-Specific Checks

| Mode | Additional checks |
|---|---|
| Mode 1 | Pricing present with labor/app separated? Blueprint positioned naturally? Sections match topics raised? |
| Mode 2 | Zero pricing? Every statement backed by a Blueprint finding? Proposal delivery referenced? |
| Mode 3 | Max 3 sections? No proposal recap? One proof point max? No urgency? |
| Mode 4 | Milestone dates present? Owners named? No sales language? Open items have deadlines? |

---

## Canonical Example — Mode 1: Post-Discovery

**Merchant:** Patchington
**Contact:** [NEED: contact name]
**Locations:** 8
**Current stack:** Lightspeed POS, Shopify ecommerce
**Stated goal:** Unified commerce — consolidating in-store and online onto Shopify POS
**Mode:** Post-Discovery

---

**Why this email works:**
- Opens on a fact about the merchant's situation, not a pleasantry
- Every section names Lightspeed's specific data model, not "your current system"
- The pilot section explains risk mitigation, not just validation steps
- Stocky deprecation is a one-paragraph footnote at the end — proportional to its importance
- Pricing avoids unapproved record-tier numbers and separates labor from app/tool costs with
  placeholders and a note on confirmation timing
- Closes with a low-friction CTA that offers two options without forcing a call

---

```
Subject: Patchington + Shopify POS — next steps

Hi [NEED: contact name],

Good speaking with you. Here's a breakdown of how we'd approach the migration for
Patchington across your 8 locations.

---

1. Back-Office & Data Structure

Since you're already on Shopify for ecommerce, your product catalog is partially
structured. The work here is reconciling your Lightspeed data model — departments,
categories, classes — against Shopify's product/variant/metafield architecture. These
don't map 1:1, and how we handle that early determines whether your reporting holds up
post-migration.

We'll define this together before touching any data:
- Product hierarchy and how it translates to Shopify's structure
- Store-level inventory management across all 8 locations
- Reporting continuity — what carries over, what needs to be rebuilt, and what Shopify
  handles natively
- Customer data organization and segmentation

---

2. Historical Data Migration

Not everything in Lightspeed is worth migrating — and migrating the wrong things creates
more problems than it solves. We'll audit your existing data and determine what transfers
cleanly and what should stay archived.

Typically for a retailer at your scale this includes:

Sales history — weekly, monthly, and annual totals by location
Inventory levels and product-level sales trends by store
Gross margin reporting by period and location
Customer profiles, purchase history, and store-level segmentation

Historical data migration is scoped and priced after reviewing the export. Labor and app/tool
costs should be separated:
- Migration labor: [NEED: approved migration labor price/range after export review]
- Migration tooling cost: [NEED: API tooling/app/tool cost, billed separately if required]

We'll confirm the exact scope once we've reviewed your export and know which records are
worth moving into Shopify.

---

3. Pilot Location First

Before we replicate across all 8 stores, we migrate one location first. This validates the
full configuration — catalog structure, inventory mapping, reporting accuracy, and
operational workflows — before it touches your broader network.

Once the pilot is clean, the remaining 7 locations follow the same blueprint. This is how
we avoid a bad configuration compounding across every store simultaneously.

---

4. Reporting & Multi-Location Analytics

Shopify's analytics work differently than Lightspeed's. Since you're already on Shopify
ecommerce, your team has some familiarity — but POS adds complexity, particularly around
store-level vs. company-wide reporting.

We'll walk your team through:
- How to read Shopify's analytics dashboards in a multi-location context
- Sales performance and product reporting by location
- Customer insights across your store network

If your reporting needs go beyond what Shopify handles natively — margin analysis,
cross-location sell-through, custom operational views — we can scope a BI integration as
a separate workstream.

---

5. One Thing Worth Flagging — Stocky

If any of your team is currently using Stocky for purchase orders or inventory management,
Shopify is discontinuing it this August. All functionality is moving directly into Shopify.
No action needed immediately, but worth knowing before you build any workflows around it.

---

Happy to walk through any of this on a call, or answer questions here first if that's easier.

the operator
KaizenCommerce | kaizencommerce.ca
```

---

## Canonical Example — Mode 2: Post-Blueprint

**Merchant:** Ridgeline Outfitters
**Contact:** Sarah Chen
**Locations:** 6
**Current stack:** Heartland Retail POS, Shopify ecommerce, QuickBooks Online
**Blueprint findings:** 23% of product records have no barcode, Heartland "matrix items"
don't map to Shopify variants without restructuring, QuickBooks sync will break at cutover,
seasonal staffing creates a hard deadline of September 1
**Mode:** Post-Blueprint

---

**Why this email works:**
- Opens with the most important finding, not a summary of the Blueprint process
- Each finding is framed as a decision, not a problem
- QuickBooks integration risk is named with a specific consequence and resolution path
- No pricing anywhere — defers entirely to the proposal
- Timeline section ties back to the merchant's own constraint (seasonal deadline)
- CTA gives a specific date for the proposal delivery

---

```
Subject: Ridgeline Outfitters Blueprint — findings and next steps

Hi Sarah,

The biggest thing the Blueprint surfaced is your product data structure. About 23% of your
catalog has no barcode assigned, and Heartland's matrix item format doesn't translate
directly to Shopify's variant system. Both are solvable, but how we solve them shapes the
rest of the implementation.

---

1. Data Architecture Findings

Heartland organizes products using matrix items — essentially a grid of size, color, and
style combinations. Shopify uses a different model: each combination becomes a distinct
variant under a parent product, with a maximum of 3 option axes and 100 variants per
product.

For most of your catalog this maps cleanly. The exceptions are items where Heartland allows
more than 3 dimensions or where matrix combinations exceed Shopify's variant limit. Those
items will need restructuring — either flattening dimensions or splitting into separate
products. We'll map the exact items that need this in the proposal scope.

---

2. Data Quality Assessment

The barcode gap affects roughly 340 SKUs across your 6 locations. For POS scanning to work
reliably post-migration, these either need barcodes assigned before cutover or a clear
workflow for handling unscanned items at checkout.

Your customer database is cleaner — 94% of records have a valid email address. The remaining
6% are store-only accounts with no digital contact info. We'll archive those rather than
migrate empty records.

---

3. Integration Risk Map

QuickBooks Online syncs with Heartland through a connector that will stop working the day
you cut over to Shopify POS. Shopify has native QuickBooks integration, but the field
mapping is different — specifically around tax categories, discount handling, and
multi-location inventory valuation.

We'll set up and validate the Shopify-QuickBooks connection during the pilot phase so your
accounting team isn't working with a broken sync during the busiest part of the transition.

---

4. Timeline Considerations

Your September 1 target is achievable, but it requires the proposal to be signed by mid-June
to leave enough time for pilot validation and staff training before your seasonal ramp. If
the timeline compresses, we'd prioritize the pilot and core catalog migration and phase the
historical data import to run in parallel after go-live.

---

Next Steps

I'll have the proposal ready for you by Thursday. It will scope everything above — the
catalog restructuring, barcode remediation, QuickBooks cutover, and the phased rollout
across all 6 locations — with pricing, timeline, and what we need from your team at each
stage.

If you want to walk through these findings before then, I'm available Wednesday afternoon.

the operator
KaizenCommerce | kaizencommerce.ca
```

---

## Canonical Example — Mode 3: Post-Proposal

**Merchant:** Haven Home
**Contact:** Marcus Obi
**Locations:** 4
**Current stack:** Square POS, Shopify ecommerce
**Proposal sent:** Silver tier, $7,500 implementation, 6-week timeline
**Merchant profile signals:** First major migration, price-conscious (asked about payment
terms on the call), 12,000 SKUs with seasonal rotation
**Mode:** Post-Proposal

---

**Why this email works:**
- Does not restate the proposal — adds to it
- Addresses the likely unstated concern (first migration anxiety) without being condescending
- The proof point is specific and comparable, not a generic ROI claim
- Price sensitivity is handled indirectly through value framing, not a discount offer
- Only 2 sections — confident, not defensive
- CTA is low-friction with two options

---

```
Subject: Haven Home — a few things worth noting

Hi Marcus,

Wanted to share a couple of things that are worth knowing as you review the proposal.

The pilot approach we outlined for your first location isn't just a testing phase. It's
where we validate every assumption about how your 12,000 SKUs map from Square to Shopify,
how your seasonal rotation logic translates, and whether the reporting your team relies on
survives the transition. If something doesn't hold up at one location, we adjust before it
touches the other three. The pilot runs for about 10 days, and if anything needs to change
afterward, it's a configuration adjustment on our side, not a restart.

On the timeline, a retailer with a similar catalog size — roughly 11,000 SKUs across 3
locations on Square — went from kickoff to full go-live in 5 weeks. The variable that
mattered most wasn't data volume, it was how quickly their team provided the initial export
and confirmed the product hierarchy mapping. The sooner we get your Square export, the more
buffer we build into the schedule.

Happy to jump on a 20-minute call if any of this raises questions, or reply here if that's
easier.

the operator
KaizenCommerce | kaizencommerce.ca
```

---

## Canonical Example — Mode 4: Post-Kickoff

**Merchant:** Coastal Provisions
**Contact:** Ana Reyes
**Locations:** 3
**Current stack:** Lightspeed POS (migrating to Shopify POS), Shopify ecommerce
**Tier:** Silver, $7,500
**Kickoff date:** March 10
**Key details:** Pilot location is the Wilmington flagship, Ana's ops manager (Derek Chau)
handles day-to-day data, target go-live April 14 for all 3 locations
**Mode:** Post-Kickoff

---

**Why this email works:**
- Zero sales language — purely operational
- Milestone map has specific dates and named owners
- "First Two Weeks" tells the merchant exactly what they'll experience
- Open items have deadlines and blockers are flagged explicitly
- Communication cadence is stated so the merchant knows when they'll hear from us
- CTA is simple: confirm or correct

---

```
Subject: Coastal Provisions — kickoff confirmed, here's the plan

Hi Ana,

Kickoff is done. Here's what we confirmed and what happens next.

---

Milestone Map

| Milestone | Target Date | Owner |
|---|---|---|
| Lightspeed data export delivered | March 14 | Derek (Coastal) |
| Data audit + field mapping review | March 18 | the operator (Kaizen) |
| Pilot config — Wilmington location | March 24 | the operator (Kaizen) |
| Pilot validation walkthrough | March 26 | Ana + the operator |
| Staff training — Wilmington | March 31 | the operator (Kaizen) |
| Wilmington go-live | April 2 | Joint |
| Remaining 2 locations configured | April 8 | the operator (Kaizen) |
| Full go-live — all 3 locations | April 14 | Joint |

---

Ownership

KaizenCommerce owns: data migration, Shopify POS configuration, field mapping, pilot
validation, staff training materials, go-live support for all 3 locations.

Coastal owns: Lightspeed data export (Derek, by March 14), staff availability for training
sessions (Ana, confirm by March 20), hardware confirmation for locations 2 and 3 (Ana, by
March 24).

---

First Two Weeks

Week 1 (March 10–14): We're waiting on Derek's Lightspeed export. Once it's in, we run the
data audit and flag anything that needs a decision before we start mapping. You won't hear
much from us this week unless we find something that can't wait.

Week 2 (March 17–21): Field mapping review. I'll send you a summary of how your Lightspeed
structure translates to Shopify, with any decisions that need your input called out. We'll
schedule a 30-minute call to walk through it together.

---

Open Items

1. Derek's Lightspeed export — needed by March 14. This blocks the data audit.
   If it slips past March 17, the pilot date moves accordingly.

2. Hardware for locations 2 and 3 — Ana to confirm whether existing iPads are
   compatible or whether new hardware is needed. Needed by March 24 so we can
   include any setup time in the rollout schedule.

---

Communication

Weekly check-in call every Wednesday at 10 AM ET, starting March 19. Between calls, email
is fine for anything non-urgent. If something blocks progress, I'll flag it same-day rather
than waiting for the weekly call.

---

Let me know if anything above needs correcting. Otherwise, we're underway.

the operator
KaizenCommerce | kaizencommerce.ca
```

---

## What a Failing Output Looks Like

Use this to catch outputs that don't meet the bar before they go to the merchant.

### Generic Failures (all modes)

**Too generic:**
> "We'll review your existing data structure and map it to Shopify's framework."

This could be sent to any retailer on any POS. The standard names the specific elements:
departments, categories, classes, matrix items, product/variant/metafield architecture.

**Missing the why:**
> "We recommend migrating one location first."

No reasoning. The standard explains: "This is how we avoid a bad configuration compounding
across every store simultaneously."

**Hollow opener:**
> "Thank you for taking the time to speak with us today. We really enjoyed learning about
> your business and are excited about the opportunity to work with Patchington."

Cut. The standard opens on a fact. Two sentences. Merchant-specific. No performance.

### Mode-Specific Failures

**Mode 2 — pricing leak:**
> "The catalog restructuring we identified typically runs $2,000–$3,000 in additional labor."

Pricing doesn't belong in a post-Blueprint email. That's for the proposal.

**Mode 2 — finding without Blueprint basis:**
> "We also recommend setting up a loyalty program to increase customer retention."

This wasn't a Blueprint finding. It's a sales suggestion dressed as a diagnostic result.

**Mode 3 — proposal recap:**
> "As outlined in our proposal, the Silver tier includes data migration, pilot validation,
> staff training, and full go-live support across all 4 locations."

They have the proposal. Don't restate it. Add context they don't already have.

**Mode 3 — multiple proof points:**
> "One client saw a 38% revenue lift. Another reduced inventory variance from 4.2% to 0.8%.
> A third cut reconciliation time by 80%."

One proof point is confident. Three is defensive. Pick the most relevant one.

**Mode 4 — sales language:**
> "We're thrilled to be partnering with Coastal Provisions on this exciting transformation."

The deal is closed. This is operational communication. Cut anything that reads like a pitch.

**Mode 4 — vague milestones:**
> "Phase 1 will focus on the pilot location, followed by Phase 2 for the remaining stores."

No dates, no owners, no specifics. The standard has a milestone table with target dates and
named owners for every line item.

---

## Example Quality Ratings

Use these ratings when verifying output:

| Rating | Meaning |
|---|---|
| **PASS** | Meets or exceeds the relevant mode's canonical example on all checks |
| **PASS WITH NOTES** | Passes but has one fixable issue — state it and fix before sending |
| **FAIL** | Generic, missing why, pricing error, mode bleed, or structural gap — rewrite before sending |

### Rating by Mode

When rating, compare against the canonical example for that specific mode:
- Mode 1 output → compare against Patchington example
- Mode 2 output → compare against Ridgeline Outfitters example
- Mode 3 output → compare against Haven Home example
- Mode 4 output → compare against Coastal Provisions example

Do not compare a Mode 4 output against the Mode 1 example. The tone, structure, and content
rules are different by design.
