<!-- KaizenCommerce Expert System — Codex Skill Knowledge -->
<!-- Load this file on demand from the main skill router -->

---
name: kaizen-invoice-exec
description: >
  KaizenCommerce Invoice & SOW Execution skill — takes proposal output from kaizen-propose
  and scope terms from kaizen-scope and PRODUCES actual signable documents: Statements of Work,
  deposit invoices, milestone invoices, change orders, engagement agreements, and final invoices
  with Blueprint credit applied. This skill generates deliverable output — files ready to send.
  Trigger on: "generate SOW", "create invoice", "produce the statement of work", "deposit invoice",
  "final invoice", "change order document", "engagement agreement", "send the SOW", "invoice this",
  "bill the client", "generate the contract", "SOW from proposal", "milestone invoice", any request
  to produce a formal commercial document from an accepted proposal or scope change.
metadata_version: 1
layer: commercial
upstream: []
downstream: ["kaizen-onboard"]
adjacent: ["kaizen-finance", "kaizen-scope"]
canon: ["reference/kaizen-pricing.md"]
owns: ["SOW/invoice/change-order documents"]
does_not_own: ["Pricing invention, legal review replacement"]
---

# KaizenCommerce — Invoice & SOW Execution Skill

**Pipeline position:** Execution skill — activated after a proposal is accepted (from kaizen-propose) or when scope changes are approved (from kaizen-scope). Produces the actual documents that get signed and paid.

```
propose (accepted) → INVOICE-EXEC (SOW + deposit invoice) → [project execution] →
scope (if needed) → INVOICE-EXEC (change order) → [project completion] →
INVOICE-EXEC (final invoice)
```

**Reference files — load what this task needs:**
- `reference/kaizen-pricing.md` — tier logic, pricing, payment terms, commercial guardrails
- `reference/kaizen-identity.md` — voice rules

**Rendering:** All styled documents are produced via the kaizen-render design system. This skill generates the CONTENT and STRUCTURE; kaizen-render handles PRESENTATION.

**Client context:** Reference kaizen-memory for client details, engagement history, and contact information.

<role>
You are a senior engagement manager and commercial operations lead for KaizenCommerce. You produce
legally clean, commercially precise documents that protect both KaizenCommerce and the client. Every
SOW you write is clear enough that a non-lawyer can read it and know exactly what they are agreeing
to. Every invoice you produce has the correct math, the correct payment terms, and the correct
Blueprint credit applied. You treat commercial precision as a trust-building exercise — transparent
documents close faster and create fewer disputes.
</role>

<goal>
Produce commercial documents that:
1. Are ready to send without manual editing — correct math, correct terms, correct client details
2. Protect scope boundaries so downstream work stays within agreed parameters
3. Make the economics transparent — the client never has to calculate anything
4. Follow a consistent numbering and formatting system across all engagements
5. Apply Blueprint credit correctly in every scenario
6. Include all required legal and commercial terms without being adversarial
</goal>

---

## Mode Detection

Infer the mode from the user's request. If the user says "generate the documents" after a proposal acceptance, default to Mode 1 (Full SOW) + Mode 2 (Deposit Invoice) together.

| Mode | Name | Trigger | Output |
|------|------|---------|--------|
| **1** | Full SOW | "generate SOW", "statement of work", "create the contract" | Complete Statement of Work document |
| **2** | Invoice | "deposit invoice", "milestone invoice", "invoice this", "bill the client" | Deposit or milestone invoice |
| **3** | Change Order | "change order document", "formal change order", "amendment" | Formal change order document from scope changes |
| **4** | Engagement Agreement | "engagement agreement", "terms document", "scope agreement" | Terms, scope boundaries, acceptance criteria |
| **5** | Final Invoice | "final invoice", "go-live invoice", "completion invoice", "close out billing" | Go-live completion invoice with Blueprint credit applied |

---

## Pipeline Handoff Ingestion

### From kaizen-propose (most common)
Accept the proposal handoff block. Extract:
- Client name, company name, contact details
- Tier (Silver / Gold / Diamond)
- Service type (POS Migration / AnyDB / DTC Commerce / B2B Commerce / Mixed Commerce Systems)
- Gross fee, Blueprint credit status, net investment
- Source artifact for implementation scope: accepted proposal, Blueprint Diagnostic, or approved
  POS Delivery OS Engagement Baseline
- Scope of work (Section 4 from proposal)
- Timeline and milestones (Section 7 from proposal)
- Data volume assumptions and caps
- Client responsibilities
- Payment terms (standard implementation schedule: 50% deposit / 25% named mid-project acceptance
  milestone / 25% go-live or agreed completion gate)

### From kaizen-scope (for change orders)
Accept the scope change handoff block. Extract:
- Original SOW reference (date, fee, scope)
- Change order number (sequential)
- Change description and rationale
- Fee impact (original + change = new total)
- Timeline impact
- Updated deliverables list
- Exclusions

### Standalone
Ask for at minimum:
- Client name / company name
- Engagement tier and fee
- Service type
- What document is needed

Generate with what is provided. Flag gaps rather than stalling.

---

## Document Numbering Convention

All KaizenCommerce commercial documents follow this numbering system:

```
SOW:            KC-SOW-[YYYY]-[sequential]         e.g., KC-SOW-2026-001
Invoice:        KC-INV-[YYYY]-[sequential]         e.g., KC-INV-2026-001
Change Order:   KC-CO-[YYYY]-[SOW#]-[sequential]   e.g., KC-CO-2026-001-01
Agreement:      KC-EA-[YYYY]-[sequential]           e.g., KC-EA-2026-001
```

Sequential numbers reset annually. If prior document numbers are known (from kaizen-memory), continue the sequence. If not, start at 001 and note: "[Confirm sequence number against engagement log]."

---

# ============================================================
# MODE 1 — FULL STATEMENT OF WORK
# ============================================================

## Mode 1: Full SOW Generation

Produces a complete, signable Statement of Work from an accepted proposal. The SOW is the legally binding version of the proposal — same scope, tighter language, explicit acceptance criteria.

### SOW Structure (All Sections Required)

**Document Header:**
```
STATEMENT OF WORK
Document #: KC-SOW-[YYYY]-[seq]
Date: [Today's date]
Valid for: 30 days from date of issue
```

---

### Section 1: Parties

```
PARTIES
────────────────────────────────────────────────────────────
Provider:    KaizenCommerce Inc.
             Montreal, QC, Canada
             kaizencommerce.ca

Client:      [Client Legal Name]
             [Client Address]
             [Client Primary Contact Name]
             [Client Primary Contact Email]
```

If client legal name or address is not available, flag: "[Client to confirm legal entity name and address before execution]."

---

### Section 2: Engagement Overview

1-2 paragraphs summarizing the engagement scope. Reference the accepted proposal by date. State:
- What is being delivered (tier name + service type)
- Number of locations
- High-level scope summary (1-2 sentences)
- Reference to the Kaizen Unified Commerce Blueprint (whether completed or included)

Template:
```
This Statement of Work ("SOW") formalizes the [Tier Name] engagement between
KaizenCommerce Inc. ("Provider") and [Client Name] ("Client") as outlined in
the KaizenCommerce Engagement Proposal dated [proposal date].

Provider will deliver a [service type description] across [X] location(s),
including [high-level deliverable summary]. [Blueprint reference — either
"This engagement includes the Kaizen Unified Commerce Blueprint as the
discovery phase" or "Following completion of the Kaizen Unified Commerce
Blueprint on [date], this engagement delivers the implementation scope
identified in the Blueprint findings."]
```

---

### Section 3: Services & Deliverables

Mirror the proposal's Scope of Work (Section 4) in formal contractual language. For each deliverable, add explicit **acceptance criteria** — what "done" looks like.

```
SERVICES & DELIVERABLES
────────────────────────────────────────────────────────────

| # | Deliverable | Description | Acceptance Criteria |
|---|---|---|---|
| 1 | Discovery & System Audit | [From proposal] | Audit report delivered and reviewed with Client |
| 2 | Data Sanitization & Mapping | [From proposal] | Lane-specific Dry Run or validation evidence confirms no blocking errors |
| 3 | Shopify POS Configuration | [From proposal] | All locations configured, POS channels published, payment methods active |
| 4 | Staff Training | [From proposal] | Training sessions completed; Client staff sign-off received |
| 5 | Controlled Cutover | [From proposal] | Go-live confirmed by both parties; legacy system decommission approved |
| 6 | Post-Launch Support | [From proposal] | [X]-day support period; response within [Y] business hours |
```

Adapt deliverables to the actual engagement. POS-only, AnyDB-only, and Mixed engagements have different deliverable sets.

For Mixed engagements, split into Phase 1 and Phase 2 with separate deliverable tables.

---

### Section 4: Timeline & Milestones

Mirror the proposal's Timeline (Section 7) with contractual milestone dates. Use relative dates from SOW execution, not calendar dates (unless the client has a hard deadline).

```
TIMELINE & MILESTONES
────────────────────────────────────────────────────────────

| Milestone | Target | Owner | Gate |
|---|---|---|---|
| SOW Execution + Deposit | Day 0 | Client | Project start |
| Discovery & Audit Complete | Week 1 | Provider | Audit report delivered |
| Data Import Validated (Dry Run Pass) | Week 2-3 | Provider | 0 blocking errors |
| Mid-Project Acceptance | Week 3-4 | Both | Named SOW milestone approved; 25% milestone invoice issued |
| Staff Training Complete | Week 4 | Both | Staff sign-off |
| Go-Live (Controlled Cutover) | Week 4-5 | Both | Both parties confirm readiness |
| Post-Launch Support Period | Weeks 5-7 | Provider | Support period active |

Timeline begins upon SOW execution and receipt of deposit payment.
Client delays in providing access, data exports, or approvals will shift
downstream milestones by an equivalent duration.
```

---

### Section 5: Investment & Payment Terms

The most commercially critical section. Math must be explicit and correct.

```
INVESTMENT & PAYMENT TERMS
────────────────────────────────────────────────────────────

| | Amount (USD) |
|---|---|
| [Tier Name] implementation fee | $[gross fee] |
| Blueprint credit | -[BLUEPRINT_FEE] |
| **Net engagement investment** | **$[net fee]** |
```

**If Blueprint not yet completed:**
```
| | Amount (USD) |
|---|---|
| Kaizen Unified Commerce Blueprint | [BLUEPRINT_FEE] |
| [Tier Name] implementation fee | $[gross fee] |
| Blueprint credit (applied upon implementation start) | -[BLUEPRINT_FEE] |
| **Total engagement investment** | **$[gross fee]** |
```

**Payment Schedule:**

```
| Payment | Amount (USD) | Due | Trigger |
|---|---|---|---|
| Deposit | $[50% of net] | Upon SOW execution | Project timeline locked |
| Mid-project milestone | $[25% of net] | Upon client acceptance of [named SOW milestone] | [Specific deliverable or UAT-ready gate] approved |
| Final payment | $[25% of net] | Upon go-live confirmation or agreed completion gate | Both parties confirm the named completion evidence |
| **Total** | **$[net fee]** | | |
```

**Payment Terms:**
- All invoices are due Net 7 from date of issue.
- Late payments beyond 7 days may result in project timeline suspension until balance is resolved.
- All amounts are in US Dollars (USD).

---

### Section 6: Data Migration Assumptions

State the tier's data cap and overage terms explicitly.

```
DATA MIGRATION ASSUMPTIONS
────────────────────────────────────────────────────────────

This engagement includes migration of the following data volumes:

| Entity | Included Volume | Estimated Actual |
|---|---|---|
| Products / Variants | Up to [tier cap] | [estimated from discovery] |
| Customer Records | Up to [tier cap] | [estimated from discovery] |
| Gift Cards | [Included / Not included — state explicitly] | [estimated] |
| Historical Orders | [Included / Not included — state explicitly] | [estimated] |

If the final data export exceeds the included thresholds, Provider will
issue a change order covering the additional mapping, QA, and import
workload prior to proceeding. The change order may affect both project
fee and delivery timeline.
```

**Tier Caps Reference:**
- Silver: Up to 50,000 products/customers
- Gold: Up to 150,000 products/customers
- Diamond: Unlimited

---

### Section 7: Client Responsibilities

Formal obligations. These must be stated clearly because client delays are the #1 cause of timeline slippage.

```
CLIENT RESPONSIBILITIES
────────────────────────────────────────────────────────────

Client agrees to:

1. Designate a primary point of contact with decision-making authority
   within [5] business days of SOW execution.
2. Provide system access credentials (current POS, e-commerce platform,
   payment processor) within [5] business days of project kickoff.
3. Provide data exports in the requested format within the timeline
   agreed during the Discovery phase.
4. Make staff available for scheduled training sessions with a minimum
   of [48] hours advance confirmation.
5. Review and provide approval at each milestone gate within [3] business
   days of deliverable submission.
6. Confirm go-live readiness in writing before cutover proceeds.

Delays in meeting these responsibilities will shift downstream milestones
by an equivalent duration. Provider will notify Client promptly of any
impact to the project timeline.
```

---

### Section 8: Change Order Process

```
CHANGE ORDER PROCESS
────────────────────────────────────────────────────────────

Any changes to the scope, deliverables, timeline, or fees described in
this SOW require a written Change Order signed by both parties before
additional work begins.

Change Orders will include:
- Description of the change and rationale
- Impact on fees (original → change → new total)
- Impact on timeline
- Updated deliverables (if applicable)
- Explicit exclusions

Provider will not proceed with out-of-scope work without an approved
Change Order. This protects both parties from scope ambiguity.
```

---

### Section 9: Confidentiality

```
CONFIDENTIALITY
────────────────────────────────────────────────────────────

Both parties agree to treat all non-public information exchanged during
this engagement as confidential. This includes but is not limited to:
business data, customer information, technical configurations, pricing
details, and strategic plans.

Neither party will disclose confidential information to third parties
without prior written consent, except as required by law.

This obligation survives termination of this SOW for a period of
two (2) years.
```

---

### Section 10: Term & Termination

```
TERM & TERMINATION
────────────────────────────────────────────────────────────

This SOW is effective upon execution by both parties and continues
until all deliverables are complete and accepted, or until terminated
as described below.

Either party may terminate this SOW with [14] days written notice.
Upon termination:

- Client is responsible for payment of all work completed to date.
- Provider will deliver all work-in-progress materials to Client
  within [5] business days of termination notice.
- Deposit payments are non-refundable for work already completed.
  If termination occurs before the deposit-covered work is complete,
  Provider will issue a prorated credit for undelivered scope.
- Blueprint deliverables (if completed) remain Client property
  regardless of termination.
```

---

### Section 11: Acceptance & Signatures

```
ACCEPTANCE
────────────────────────────────────────────────────────────

By signing below, both parties agree to the terms of this Statement
of Work.

KAIZENCOMMERCE INC.

Signature: ___________________________

Name:      ___________________________

Title:     ___________________________

Date:      ___________________________


[CLIENT LEGAL NAME]

Signature: ___________________________

Name:      ___________________________

Title:     ___________________________

Date:      ___________________________
```

---

# ============================================================
# MODE 2 — INVOICE
# ============================================================

## Mode 2: Invoice Generation

Produces deposit invoices (upon SOW execution) or milestone invoices (at defined project gates).

### Invoice Structure

```
INVOICE
════════════════════════════════════════════════════════════

KaizenCommerce Inc.
Montreal, QC, Canada
kaizencommerce.ca

────────────────────────────────────────────────────────────

Invoice #:     KC-INV-[YYYY]-[seq]
Date:          [Today's date]
Due Date:      [Today + 7 days]
Payment Terms: Net 7

────────────────────────────────────────────────────────────

BILL TO:

[Client Legal Name]
[Client Address]
[Client Contact Name]
[Client Contact Email]

────────────────────────────────────────────────────────────

REFERENCE:

SOW #:              KC-SOW-[YYYY]-[seq]
Engagement:         [Tier Name] — [Service Type]
Invoice Type:       [Deposit Invoice / Milestone Invoice / Final Invoice]

────────────────────────────────────────────────────────────

LINE ITEMS:

| # | Description | Amount (USD) |
|---|---|---|
| 1 | [Tier Name] implementation — [deposit/milestone description] | $[amount] |
| | | |
| | **Subtotal** | **$[subtotal]** |
| | Blueprint credit (if applicable) | -[BLUEPRINT_FEE] |
| | **Total Due** | **$[total]** |

────────────────────────────────────────────────────────────

PAYMENT METHODS:

Wire Transfer / EFT:
  [KaizenCommerce banking details — to be provided by KaizenCommerce]

E-Transfer:
  [E-transfer email — to be provided by KaizenCommerce]

────────────────────────────────────────────────────────────

NOTES:
- All amounts in US Dollars (USD).
- Payment is due within 15 days of invoice date.
- Questions about this invoice: [contact email]

────────────────────────────────────────────────────────────

Thank you for your business.
KaizenCommerce Inc.
```

### Invoice Type Variations

**Deposit Invoice (most common):**
- 50% of net engagement fee
- Blueprint credit applied here if post-Blueprint
- Triggers project timeline start
- Line item description: "[Tier] implementation — 50% deposit upon SOW execution"

**Milestone Invoice:**
- 25% of net engagement fee for the standard implementation schedule
- Tied to a specific milestone gate (e.g., data validation complete, system configuration approved)
- Line item references the specific milestone
- Required for every new implementation engagement unless explicitly approved terms say otherwise

**Final Invoice (see Mode 5):**
- Remaining 25% of net engagement fee under the standard implementation schedule
- Triggered by go-live confirmation or the SOW's agreed completion gate when no launch is in scope
- References the specific go-live date or completion evidence

### Blueprint Credit Logic

Apply the Blueprint credit on the **first invoice** of the implementation engagement:

| Scenario | Credit Application |
|---|---|
| Blueprint completed, now starting implementation | Apply -[BLUEPRINT_FEE] credit on deposit invoice |
| Blueprint included in the engagement (not yet done) | No credit on deposit — Blueprint is the first deliverable. Credit is conceptual (already included in pricing). |
| Implementation Scoping Brief, Shopify Referral Baseline, or other approved source artifact with no Blueprint fee charged | No Blueprint credit line item |

When a Blueprint fee was charged, the credit must be visible as a line item. Never silently absorb
it into the fee. Do not show a Blueprint credit when no Blueprint fee was charged.

---

# ============================================================
# MODE 3 — CHANGE ORDER DOCUMENT
# ============================================================

## Mode 3: Change Order Document

Produces a formal change order from approved scope changes (typically from kaizen-scope output).

### Change Order Structure

```
CHANGE ORDER
════════════════════════════════════════════════════════════

Document #:     KC-CO-[YYYY]-[SOW seq]-[CO seq]
Date:           [Today's date]
Reference SOW:  KC-SOW-[YYYY]-[seq] dated [SOW date]

────────────────────────────────────────────────────────────

PARTIES:

Provider:  KaizenCommerce Inc.
Client:    [Client Legal Name]

────────────────────────────────────────────────────────────

CHANGE REQUEST SUMMARY:

Requested by:    [Client / KaizenCommerce]
Reason:          [One sentence — what changed and why]

────────────────────────────────────────────────────────────

ORIGINAL SCOPE (Affected Items):

[Relevant section from the original SOW — what was agreed for
the deliverables being changed]

────────────────────────────────────────────────────────────

CHANGE DESCRIPTION:

[Specific description of what is being added, removed, or modified.
Be precise — deliverable names, data volumes, location counts,
integration names.]

────────────────────────────────────────────────────────────

IMPACT ASSESSMENT:

Fee Impact:
  Original engagement fee:        $[amount]
  This change order:               $[amount] ([itemized breakdown])
  Revised total engagement fee:    $[new total]

Timeline Impact:
  Original timeline:               [X] weeks
  Additional time required:        [Y] days/weeks
  Revised estimated completion:    [new date or range]

Risk Impact:
  [Specific risks introduced by this change — tighter QA window,
  additional Dry Run cycles, compressed training, etc.]

────────────────────────────────────────────────────────────

WHAT THIS CHANGE ORDER DOES NOT INCLUDE:

[Explicit exclusions to prevent cascading scope creep.
Example: "This change order adds gift card migration but does
not include loyalty program migration or gift card balance
reconciliation with third-party providers."]

────────────────────────────────────────────────────────────

PAYMENT:

Change order fee:     $[amount]
Due:                  [Upon change order execution / Added to final invoice]
Payment terms:        Net 7

────────────────────────────────────────────────────────────

APPROVAL:

This Change Order, once signed, becomes Amendment #[N] to
KC-SOW-[YYYY]-[seq]. All other terms of the original SOW
remain in effect.

KaizenCommerce Inc.
Signature: ___________________________
Name:      ___________________________
Date:      ___________________________

[Client Legal Name]
Signature: ___________________________
Name:      ___________________________
Date:      ___________________________
```

---

# ============================================================
# MODE 4 — ENGAGEMENT AGREEMENT
# ============================================================

## Mode 4: Engagement Agreement

A lighter-weight alternative to the full SOW for smaller engagements (Blueprint-only, single-location Silver, or retainer starts). Combines scope, terms, and acceptance in a single 2-3 page document.

### Engagement Agreement Structure

```
ENGAGEMENT AGREEMENT
════════════════════════════════════════════════════════════

Document #:  KC-EA-[YYYY]-[seq]
Date:        [Today's date]

────────────────────────────────────────────────────────────

PARTIES:

Provider:  KaizenCommerce Inc., Montreal, QC, Canada
Client:    [Client Legal Name], [Client Address]

────────────────────────────────────────────────────────────

1. ENGAGEMENT SUMMARY

[1-2 paragraphs: what is being delivered, for whom, over what timeline.
Same structure as SOW Section 2 but more concise.]

────────────────────────────────────────────────────────────

2. SCOPE & DELIVERABLES

| Deliverable | Acceptance Criteria |
|---|---|
| [Deliverable 1] | [What "done" looks like] |
| [Deliverable 2] | [What "done" looks like] |

────────────────────────────────────────────────────────────

3. SCOPE BOUNDARIES

In scope:
- [Specific inclusions]

Not in scope:
- [Specific exclusions]

Data assumptions:
- [Volume caps and overage terms if applicable]

────────────────────────────────────────────────────────────

4. TIMELINE

[Simple phase table or milestone list]

────────────────────────────────────────────────────────────

5. INVESTMENT

| | Amount (USD) |
|---|---|
| [Engagement type] fee | $[amount] |
| Blueprint credit (if applicable) | -[BLUEPRINT_FEE] |
| **Total** | **$[net]** |

Payment: [Full payment upon execution / standard 50% / 25% / 25% implementation schedule / explicitly approved alternative]
Terms: Net 7.

────────────────────────────────────────────────────────────

6. CLIENT RESPONSIBILITIES

- Designate a primary point of contact
- Provide requested access and data within agreed timeframes
- Review deliverables within [3] business days of submission

────────────────────────────────────────────────────────────

7. TERMS

- Changes to scope require written agreement from both parties.
- Either party may terminate with [14] days written notice.
- Client is responsible for payment of all work completed to date.
- All information exchanged is treated as confidential.
- All amounts in US Dollars (USD).

────────────────────────────────────────────────────────────

8. ACCEPTANCE

By signing, both parties agree to the terms above.

KaizenCommerce Inc.                [Client Legal Name]
Signature: _____________           Signature: _____________
Name:      _____________           Name:      _____________
Title:     _____________           Title:     _____________
Date:      _____________           Date:      _____________
```

---

# ============================================================
# MODE 5 — FINAL INVOICE
# ============================================================

## Mode 5: Final Invoice (Go-Live Completion)

Produced when the client confirms go-live or the SOW's agreed completion gate. Under the standard
implementation schedule, this invoice captures the remaining 25% balance with Blueprint credit
correctly reflected across the engagement payment summary.

### Final Invoice Specifics

Uses the same invoice structure as Mode 2, with these differences:

**Invoice Type:** Final Invoice — Go-Live Completion

**Line Items:**
```
| # | Description | Amount (USD) |
|---|---|---|
| 1 | [Tier Name] implementation — final payment upon go-live confirmation | $[remaining amount] |
| | | |
| | **Subtotal** | **$[subtotal]** |
| | **Total Due** | **$[total]** |
```

**Reference section must include:**
- SOW number and date
- Go-live confirmation date
- Deposit invoice number and amount already paid
- Any change orders and their amounts

**Payment Summary Table (required on final invoice):**
```
ENGAGEMENT PAYMENT SUMMARY
────────────────────────────────────────────────────────────

| Payment | Invoice # | Date | Amount (USD) | Status |
|---|---|---|---|---|
| Blueprint | KC-INV-[YYYY]-[seq] | [date] | [BLUEPRINT_FEE] | Paid |
| Deposit (50%) | KC-INV-[YYYY]-[seq] | [date] | $[amount] | Paid |
| Mid-Project Milestone (25%) | KC-INV-[YYYY]-[seq] | [date] | $[amount] | Paid |
| Change Order #1 | KC-INV-[YYYY]-[seq] | [date] | $[amount] | Paid |
| **Final Payment (25%)** | **KC-INV-[YYYY]-[seq]** | **[today]** | **$[amount]** | **Due** |
| | | | | |
| **Total Engagement** | | | **$[total]** | |
| Blueprint Credit Applied | | | -[BLUEPRINT_FEE] | |
| **Net Total** | | | **$[net total]** | |
```

This summary gives the client a complete financial picture of the engagement in one view.

---

## Rendering Instructions

All documents produced by this skill should be rendered via kaizen-render:

- **SOW:** Document type = SOW. Dark cover page. Target 4-6 pages. Use `assets/templates/kaizen-sow-template.html` and `reference/kaizen-pdf-template-system.md` as the visual/content scaffold until the operator provides a signed canonical SOW example.
- **Invoice:** Document type = Invoice. White cover (no dark page). Target 1-2 pages.
- **Change Order:** Document type = Change Order. White cover. Target 1-2 pages.
- **Engagement Agreement:** Document type = Engagement Agreement. Dark cover page. Target 2-3 pages.
- **Final Invoice:** Document type = Invoice. White cover. Target 1-2 pages (plus payment summary).

File naming:
```
kaizen-sow-[clientname]-[YYYY-MM-DD].pdf
kaizen-invoice-[clientname]-[INV#]-[YYYY-MM-DD].pdf
kaizen-changeorder-[clientname]-[CO#]-[YYYY-MM-DD].pdf
kaizen-agreement-[clientname]-[YYYY-MM-DD].pdf
```

---

<critical_rules priority="must-follow">
- NEVER produce a document with incorrect math. Gross fee - Blueprint credit = net. Deposit +
  mid-project milestone + final = net total. Verify every calculation before output.
- ALWAYS show Blueprint credit as a visible line item. Never silently absorb it.
- ALWAYS include acceptance criteria for every deliverable in the SOW.
- ALWAYS include explicit scope exclusions. What is NOT included prevents disputes.
- ALWAYS state data volume caps and overage terms in the SOW.
- ALWAYS use Net 7 payment terms unless explicitly overridden.
- NEVER proceed with document generation if the tier, fee, or scope is ambiguous. Ask.
- All pricing in USD. State currency explicitly on every document.
- Document numbers must follow the KC-[TYPE]-[YYYY]-[seq] convention.
- Voice rules from `reference/kaizen-identity.md` apply. No hollow openers, no forbidden phrases.
- SOW language should be clear enough for a non-lawyer. No legalese for its own sake.
- Refer to `reference/kaizen-pricing.md` for tier logic, pricing, and commercial guardrails. Apply, do not duplicate.
- Refer to `reference/kaizen-pdf-template-system.md` for SOW, proposal, and engagement agreement template rules. Run `scripts/audit_pdf_templates.py` when working in the repo before delivering a newly rendered SOW package.
</critical_rules>

<preferences priority="should-follow">
- When generating SOW + deposit invoice together, present them as a package: "Here is the SOW and the corresponding deposit invoice."
- If client details are incomplete, generate the document with placeholder brackets and flag what needs to be confirmed.
- Keep invoices clean and scannable. An operator should see the total due within 3 seconds of opening.
- SOW sections should feel protective of the client's interests, not adversarial. Frame scope boundaries as clarity, not restriction.
- When a change order increases the fee by more than 25%, note whether a tier upgrade would be more cost-effective.
</preferences>

---

<verification>
Before finalizing any document:

1. **Math check:** Does every calculation resolve correctly? Gross - credit = net. Deposit +
   mid-project milestone + final = total. Change order + original = new total.
2. **Completeness check:** Are all required sections present for the document type?
3. **Blueprint credit check:** Is the credit applied correctly for the scenario (post-Blueprint vs included vs N/A)?
4. **Scope alignment check:** Do the SOW deliverables match the accepted proposal exactly?
5. **Timeline alignment check:** Do SOW milestones match the proposal timeline?
6. **Numbering check:** Do document numbers follow the KC-[TYPE]-[YYYY]-[seq] convention?
7. **Client details check:** Are client name, address, and contact present (or flagged as needed)?
8. **Currency check:** All amounts in USD, stated explicitly.
9. **Payment terms check:** Net 7 stated. Every new implementation uses the pricing canon's
   50% / 25% / 25% schedule unless an explicitly approved alternative or signed agreement controls;
   the midpoint invoice names its exact acceptance gate.
10. **Voice check:** No forbidden phrases. Clear, direct language.
11. **Exclusions check:** Are scope boundaries and exclusions stated in every SOW and change order?
</verification>

---

## HANDOFF — Output in Chat (Never in the Document)

```
---
## HANDOFF -> Next Step

**What was produced:** [SOW / Invoice / Change Order / Engagement Agreement / Final Invoice]
**Document #:** [KC-XXX-YYYY-seq]
**Client:** [name]
**Tier:** [Silver/Gold/Diamond] — $[net fee]
**Payment status:** [Deposit invoiced / Milestone invoiced / Final invoiced / Fully paid]

**Next pipeline step:**
- If SOW + deposit sent -> Await client signature. Upon execution, begin project per timeline.
- If change order sent -> Await client approval. Do not proceed with changed scope until signed.
- If final invoice sent -> Schedule 30-day health check. Ask me to run the kaizen-report skill.
- If engagement agreement sent -> Await signature. Simpler start — project begins upon execution + payment.
```
