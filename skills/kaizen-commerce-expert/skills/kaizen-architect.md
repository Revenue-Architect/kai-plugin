<!-- KaizenCommerce Expert System — Codex Skill Knowledge -->
<!-- Load this file on demand from the main skill router -->

---
name: kaizen-architect
description: >
  KaizenCommerce Architecture skill — stage 4 in the pipeline. Three modes: (1) AnyDB Spec —
  generate a 10–15 page technical architecture specification for developers and implementers, (2) Integration Map — map
  systems, source-of-truth ownership, data flow, sync design, AnyDB role, (3) SOP Builder —
  convert architecture and integration outputs into role-based Standard Operating Procedures.
  Trigger on: "build an AnyDB spec", "architecture doc", "design the ops system", "map the
  integrations", "integration mapping", "how do systems connect", "build SOPs", "create
  procedures", "write the ops manual". Input can be rough notes, transcripts, workflow
  descriptions, Blueprint output, or handoff from kaizen-propose or kaizen-diagnose.
metadata_version: 1
layer: architecture
upstream: []
downstream: ["kaizen-anydb-build", "kaizen-dataprep"]
adjacent: ["kaizen-anydb-schema", "kaizen-retail-architecture"]
canon: ["reference/kaizen-mcp-protocols.md"]
owns: ["Source-of-truth, build-vs-buy, integration map, SOPs"]
does_not_own: ["Pricing, sales close, final migration QA"]
---

# KaizenCommerce — Architecture Skill (3 Modes)

**Pipeline position:** qualify → diagnose → propose → **architect** → publish

This skill merges three capabilities into one. Infer the mode from context:

| Mode | Name | Trigger Phrases | Output |
|------|------|-----------------|--------|
| **1** | AnyDB Spec | "build an AnyDB spec", "architecture doc", "design the ops system", "operations system spec" | 10–15 page technical architecture specification (developer/implementer audience) |
| **2** | Integration Map | "map the integrations", "integration mapping", "how do systems connect", "data flow design" | Structured integration mapping package |
| **3** | SOP Builder | "build SOPs", "create procedures", "write the ops manual", "operating procedures" | Role-based Standard Operating Procedures |

If the mode is ambiguous, ask. If the input implies a sequence (e.g., "full architecture build"), run Mode 1 → Mode 2 → Mode 3 in order.

## Shared Foundation

**Reference files — load what this task needs:**
- `reference/kaizen-pricing.md` — tier logic, pricing, commercial guardrails
- `reference/kaizen-identity.md` — voice rules, ICP, company identity
- `reference/kaizen-design-system.md` — design system tokens
- `reference/kaizen-data-freshness.md` — data freshness protocols, source-of-truth heuristics
- `reference/kaizen-surface-complexity.md` — merchant profile classification; load at start of Mode 2 to drive source-of-truth decisions
- `reference/kaizen-build-vs-buy.md` — 4-verdict framework (NATIVE / THIRD-PARTY / CUSTOM / RETAIN); assign one verdict per system in Mode 2 Integration Map
- `reference/kaizen-erp-patterns.md` — ERP connector patterns, data flows, Last 10% edge cases; load when ERP integration is confirmed in scope
- `reference/kaizen-anydb-patterns.md` — AnyDB cell types, formula syntax, cell formats, connection rules, canonical patterns; mandatory load at the start of Mode 1 before writing any cell, formula, lookup, Reference, or Attach relationship
- `reference/kaizen-shopify-commerce-systems.md` — DTC/B2B commerce system lanes, AnyDB-first commerce lens, and non-POS source-of-truth patterns
AnyDB role patterns, API-first migration boundaries, and Matrixify fallback knowledge are embedded
in this skill directly.

**Use Shopify Dev MCP for:** Shopify Admin API, GraphQL, CLI, custom data, POS UI, Liquid,
Hydrogen, Functions, Polaris, or version-sensitive Shopify behavior. Start with
`learn_shopify_api`, search with `search_docs_chunks`, and validate generated GraphQL with
`validate_graphql_codeblocks`. Shopify Dev MCP is the source of truth for Shopify developer/API
behavior.

**Use the `anydb-com` MCP server for:** field-level AnyDB detail, formula syntax, automation configuration, API behavior. Search the MCP server for the specific topic you need (e.g., "formula functions", "automation triggers", "Shopify sync configuration"). Fallback: read the anydb-com MCP server if the MCP server is unavailable.

**Use the `matrixify-app` MCP server for Matrixify lane work only:** Matrixify field-level detail, import/export configuration, edge-case handling. Search the MCP server for the specific topic you need (e.g., "gift card migration", "historical orders import", "Dry Run protocol", "inventory by location"). Fallback: read the matrixify-app MCP server if the MCP server is unavailable.

Do NOT duplicate tier logic, pricing, voice rules, or company identity from the reference files. Reference them.

---

## When NOT To Activate This Skill

Do not use `kaizen-architect` when:
- The ask is a tactical Shopify setting, POS configuration, hardware question, or staff-permission
  question. Use `kaizen-retail-expert-v2`, `kaizen-shopify-config`, or `kaizen-hardware`.
- The user only needs AnyDB formula syntax, cell type names, or Reference vs Attach guidance. Load
  `reference/kaizen-anydb-patterns.md`.
- The request is to produce actual build files, seed CSVs, portal config, or automation config from
  an approved spec. Use `kaizen-anydb-build`.
- The merchant only needs a proposal or commercial scope. Use `kaizen-propose`.
- The right answer depends on current vendor API behavior that has not been verified. Research or
  MCP lookup comes before architecture commitment.

---

## Decision Quality Gate

Before finalizing an architecture, source-of-truth decision, AnyDB role, integration map, or SOP
sequence, run this gate silently and preserve the results in assumptions, risks, open questions,
or recommendation rationale.

1. **Evidence separation:** Treat provided systems, workflows, exports, and client statements as
   Confirmed. Treat source-of-truth logic, workflow fragility, and ownership deductions as
   Inferred unless directly confirmed. Treat missing vendor capabilities, sync cadence, field
   mappings, and operational owners as Assumed. Treat record counts, effort, and timing guesses
   as Estimated.
2. **Kill conditions:** Name what would invalidate the architecture. Examples: the workflow is
   simple enough that the operator accepts a native/app-only lower-control path, ERP must remain source
   of truth for the entity, API support is not available, sync latency breaks store operations,
   or staff cannot maintain the proposed workflow after handoff.
3. **AnyDB anti-overbuild:** AnyDB should have a specific job: workflow state, approvals,
   exception management, portal collection, orchestration, or reporting. If it is only a passive
   copy of Shopify or ERP data, redesign.
   For DTC/B2B commerce systems, consider AnyDB first for operating control before native-only or
   app-only architecture. Shopify native B2B and apps can own transaction surfaces while AnyDB
   owns account onboarding, approvals, exceptions, reporting, portal state, or reconciliation.
4. **Source-of-truth discipline:** Every critical entity needs one owner or an explicit split.
   Never let two systems appear to own the same write path without a conflict rule.
5. **Runner-up option:** When rejecting native Shopify, a third-party app, or retaining a legacy
   system, explain the operational reason it loses. Do not let custom build win by default.

---

# ============================================================
# MODE 1 — ANYDB SPEC
# ============================================================

## Mode 1: AnyDB Technical Architecture Spec Generator

Produces a technical architecture specification that gives developers and implementers everything
they need to build, configure, and validate the AnyDB system. This is a build brief — precise
enough to execute from, complete enough to QA against.

<goal>
Produce a specification that:
1. Gives a developer every object, field, type, relationship, formula, and automation needed to build without follow-up questions
2. Ties the architecture to specific workflows so implementers understand the intent behind each design decision
3. Documents integration points with enough precision that an engineer can configure syncs correctly
4. Is implementation-ready from first read — no hand-waving, no deferred decisions
Target: 10–15 pages. Every section required. At least 5 visual exhibits.
</goal>

<critical_rules id="mode1-rules" priority="must-follow">
- Required reading — non-negotiable before generating output: Before writing any cell, formula, lookup, Reference, or Attach relationship, you must have loaded `reference/kaizen-anydb-patterns.md`. State the load explicitly in your first response: "Loaded: kaizen-architect.md + kaizen-anydb-patterns.md". If you have not loaded it, stop and load it. Do not infer cell types or formula syntax from memory.
- NEVER use "database" as a synonym for AnyDB in client-facing sections. Use "your operations
  system", "the ops layer", or "the system."
- NEVER use: "leverage", "seamless", "robust", "scalable" (generically).
- NEVER simplify the schema to save space. The schema section is one of the highest-value sections.
- ALWAYS include at least 5 visual exhibits (diagrams, tables, matrices, maps).
- ALWAYS include the System Architecture Overview diagram (Figure 1) — it is mandatory.
- ALWAYS flag assumptions clearly with "[Assumption — confirm before build]" notation.
- ALWAYS explain WHY each design choice matters operationally, not just how it's configured.
- Every automation must be complete enough for a developer to implement without clarification — trigger, condition, actions, and purpose all documented.
</critical_rules>

<preferences priority="should-follow">
- Workflow mapping should give developers enough context to understand why an object or field exists, not just that it exists.
- Design principles should explain build consequences — what breaks or degrades if the principle is violated.
- Schema field definitions should be complete. Expect 6–12 objects for a typical retail ops build.
- Automations written with enough precision for implementation: trigger type, condition logic, action sequence, and any system dependency.
- If the input is sparse, make reasonable assumptions and flag them clearly.
</preferences>

### Mode 1 — Input Requirements

<minimum_viable_input>
To generate a credible spec, you need at minimum:
- Client name / company
- Core operational problem AnyDB is solving
- Key objects / entities in their business (or enough context to infer them)

If you have these three, you can generate the spec. Flag everything inferred as an assumption.
</minimum_viable_input>

<full_extraction_checklist>
Extract from input. Ask ONLY for items marked [required] if missing:

- **Client name / company** [required]
- **Core operational problem** AnyDB is solving [required]
- **Key objects / entities** [required — e.g. Purchase Orders, Suppliers, Transfers, Locations,
  Products, Staff. Can be inferred from business type if not stated explicitly.]
- **Workflows that need to be supported** — what does the team actually do day to day?
- **Data that needs to come from or push to Shopify** — products, inventory, orders, customers
- **Other external integrations** — 3PL, accounting, ERP, email, etc.
- **Who will use the system** — operators, warehouse staff, managers, vendors (portal users?)
- **Automations or triggers** — what should happen automatically vs. manually
- **Reporting needs** — what does leadership need to see that they can't see today?
- **Approval or control requirements** — who approves purchases, transfers, adjustments?
- **Role-specific needs** — what different users need to see, edit, submit, or approve
- **Build constraints** — timeline, bandwidth, migration concerns, phased rollout needs
</full_extraction_checklist>

### Mode 1 — Document Structure (14 Sections)

Target: **10–15 pages.** Every section required.

#### 1. Cover Page (1 page)
- Client name
- Document title: "AnyDB Operations Architecture — System Specification"
- Version: v1.0
- Date
- Prepared by: KaizenCommerce
- Note: "This document is a working specification. Confirm flagged assumptions before build begins."
- Optional subtitle: "Workflow Design, Data Model, Automation Logic, and Build Priorities"

#### 2. Technical Summary (1 page)
2–3 paragraphs. Written for the technical lead or lead developer picking up the build.

Cover:
- What operational problem this system solves and why the architecture was designed this way
- What the system is (AnyDB as a structured ops layer — explain the data model structure, Shopify integration points, and automation approach at a high level)
- What the system enables at the workflow level — the key outcomes a correct build will produce
- The most important architectural constraint or design decision the implementer needs to understand before touching anything

No business-case language. No ROI framing. This section orients the builder, not the buyer.

#### 3. System Overview (1–1.5 pages)
Technical explanation of how the system is structured — before schema detail.

Write as: "This system is built around [X] core objects. Here is how they relate to each other,
how data flows between them, and what each layer is responsible for."

Then describe architecture in 3–5 sentences covering:
- Primary objects and their relationships (Reference vs. Attach)
- Where Shopify data enters (sync direction, trigger type) and exits (write-back conditions)
- Which objects are user-driven vs. automation-driven
- Where approvals, status gates, or validation logic control the flow

**System Diagram (MANDATORY):**
- Core objects as labeled boxes
- Arrows indicating data flow and relationships (label direction)
- Shopify as an external node with directional arrows and sync type noted
- Any other integration nodes (3PL, accounting, etc.) with connection type
- Label: "Figure 1 — System Architecture Overview"

#### 4. Design Principles (0.75–1 page)
Explain the logic behind the architecture choices so implementers understand what they are
building toward — and what breaks if the principle is violated. 4–6 principles such as:
- Single source of truth by workflow area
- Clear ownership and status visibility
- Minimal duplicate data entry
- Approval and exception handling where needed
- Shopify remains system of record for commerce-facing data
- Reporting designed around decisions, not raw data exposure

Write each principle with 1–2 sentences on the build consequence: what specifically is
implemented differently because of this principle, and what would break without it.

#### 5. Workflow Mapping (1–1.5 pages)
Map real-world workflows to the system design so developers understand the intent behind each
object, field, and automation — and can make correct implementation decisions when the spec
doesn't anticipate every edge case.

For each workflow (purchasing, receiving, inventory adjustments, transfers, vendor coordination,
reorder planning, reporting / exception review):
- What triggers it (user action, schedule, system event)
- Which objects are involved and in what sequence
- Which fields change state and what those state changes mean downstream
- What automations fire and when
- What the correct end state looks like (so QA can verify)

Include a visual workflow diagram for at least one major process. Label as a figure.

#### 6. Schema: Objects & Fields (2.5–4 pages)
For each Type, produce:

```
TYPE: [Type Name]
Purpose: [One sentence — what this Type represents and why it exists]
Connects to: [Related Types with connection type — Reference or Attach]
Used in workflows: [Which operational workflows depend on this object]

Cells:
  [Cell Name]          [Type]        [Notes — purpose, options, formula logic]
  [Cell Name]          [Type]        [Notes]
  ...

Shopify Sync: [Yes / No — if yes, what syncs and in which direction]
```

**Cell types, formula syntax, cell formats:** Use only the vocabulary and patterns defined in
`reference/kaizen-anydb-patterns.md`. Do not invent type names. Do not write formula
syntax from memory. Every cell declaration in the spec must match a cell type from the
patterns file catalog. Every formula must use the patterns file syntax.

**Connection conventions:**
- `Reference`: associative connection to another record in the same database. Declare target
  Type. Reference is one-to-one per AnyDB's model.
- `Attach`: structural parent-child relationship. Declare parent Type, child Type, and
  one-to-many direction explicitly. Use Attach when the parent needs aggregation across
  children.
- If aggregation is required, use Attach plus a typed formula with `C@CURRREC!CellID`.
  Do not specify a Rollup cell.

Include all Types. For typical retail ops: 6–12 core Types. Do not simplify to save space.

#### 7. Role & Access Model (0.75–1 page)
Document how different users interact with the system.

**Role & Access Matrix** covering:
- What each role can view
- What each role can create or edit
- What each role can approve
- What each role cannot access

Roles to consider: Owner/leadership, Ops manager, Inventory/warehouse staff, Store managers,
Finance/accounting, Vendors/portal users.

#### 8. Automation Logic (1.5–2 pages)
For each automation:

```
AUTOMATION: [Name]
Workflow Area: [Purchasing / Inventory / Reporting / Notifications / etc.]
Trigger: [What starts it — record created, field changed, date reached, form submitted]
Condition: [If applicable — what must be true for it to fire]
Actions:
  1. [What happens first]
  2. [What happens next]
  3. [etc.]
Purpose: [One sentence — why this exists, what it replaces]
```

Group by workflow area. Write in plain English.
Flag Shopify-dependent automations: [Requires Shopify integration].
Add an **Automation Map** visual showing major triggers, handoffs, and outputs.

#### 9. Portal Configuration (0.5–1 page)
If external users access the system (vendors, warehouse staff, franchise partners):

```
PORTAL: [Name]
Who uses it: [Persona]
Access level: [View only / Submit forms / Edit own records / Full access]
What they see: [Objects or views they can access]
What they can do: [Forms, records they can create/edit]
What they cannot see: [Explicitly state hidden fields/objects]
```

If no portal needed, note briefly and move on.

#### 10. Integration Points (1–1.25 pages)
For each integration:

```
INTEGRATION: [System name — e.g. Shopify, QuickBooks, ShipStation]
Type: [Native sync / Webhook / API / Manual export]
Direction: [Shopify → AnyDB / AnyDB → Shopify / Bidirectional]
What syncs:
  - [Field or object and what it maps to]
Frequency: [Real-time / On trigger / Scheduled / Manual]
Notes: [Constraints, limitations, build requirements]
```

Always include Shopify. Flag custom-build requirements: [Requires custom build].
Add a short note on why each integration matters operationally.

#### 11. Reporting & Views (1–1.25 pages)
For each key view/report:

```
VIEW / REPORT: [Name]
Object: [Which table it's built on]
Who uses it: [Persona]
What it shows: [Plain description — filtered, sorted, grouped how]
Business purpose: [What decision or action it supports]
```

4–8 views. Clarify which support frontline execution, management review, exception surfacing,
and leadership decision-making.

#### 12. Build Phasing & Priorities (0.75–1 page)
Separate launch requirements from follow-on improvements.

- **Phase 1 / MVP:** core objects, critical automations, essential views, minimum integrations
- **Phase 2:** quality-of-life improvements, advanced reporting, secondary portals
- **Phase 3 (optional):** future enhancements

For each phase: what's included, why it belongs there, dependencies or prerequisites.

#### 13. Flagged Assumptions (0.5–0.75 page)

| # | Assumption | Section | Action Required |
|---|---|---|---|
| 1 | [What was assumed] | [Section reference] | [Confirm / Decide / Provide data] |

Be honest. A spec with clear assumptions is more useful than one that hides its gaps.

#### 14. Next Steps (0.5 page)
Three numbered actions:
1. Review flagged assumptions (Section 13) and confirm or correct before the build call
2. Share any source documents, templates, or workflow examples needed to finalize field mapping
3. We'll schedule the build kickoff within 48 hours of assumption sign-off

### Mode 1 — Visual Requirements

Include **at least 5 visual exhibits**, selected from:
- Figure 1 — System Architecture Overview (MANDATORY)
- Workflow diagram for a core process
- Role & Access Matrix
- Automation Map
- Integration map
- Reporting hierarchy / dashboard stack
- Build phase roadmap
- Systems-to-workflow mapping table
- Data ownership or source-of-truth matrix

Rules:
- Every visual must clarify structure, data flow, responsibility, or decision logic
- Tables count as visual exhibits if they synthesize the design meaningfully
- Include at least one visual tied to workflows and one tied to governance/access
- Diagrams should be implementation-readable — a developer should be able to look at Figure 1 and know what to build first

### Mode 1 — Output Instructions

#### Pre-Step: Architecture Diagram First (Mandatory)

Before generating the full PDF spec, always produce the system architecture diagram as a
standalone Mermaid file. This is a required gate — do not proceed to the full PDF until the
diagram has been reviewed and approved.

**Why:** The architecture diagram is the foundation of the spec. If the object model, data flow,
or integration structure is wrong in the diagram, the entire spec will be wrong. Catching it at
diagram stage costs minutes. Catching it after a 15-page PDF costs hours.

**Diagram output format:**

Produce a `.mermaid` file using Mermaid graph syntax. The diagram must show:
- All core objects as nodes
- Relationships between Types (Reference or Attach, labeled)
- Shopify as an external node with directional arrows and sync type (→ bidirectional, → one-way)
- Any other external system nodes (accounting, 3PL, etc.)
- Data flow direction on all arrows

**File naming:** `kaizen-anydb-diagram-[clientname]-[date].mermaid`

After producing the diagram file, pause and explicitly ask:
> "Here is the system architecture diagram. Review it before I generate the full spec — does
> the object model, data flow, and integration structure look correct? Any objects missing,
> wrong relationships, or incorrect sync directions?"

Only proceed to the full PDF spec after explicit confirmation that the diagram is approved.

If draw.io is preferred over Mermaid, produce the same diagram as a draw.io-compatible XML file
instead: `kaizen-anydb-diagram-[clientname]-[date].drawio`

---

#### Full Spec Output

1. Produce as a styled PDF document
2. File naming: `kaizen-anydb-spec-[clientname]-[date].pdf`

**PDF Styling — render via `kaizen-render`:** Follow `reference/kaizen-ds-v2.html`,
`reference/kaizen-design-system.md`, and `reference/kaizen-design-tokens.json`; do not
define tokens here. Architect-specific deltas: object/automation/portal blocks are flat bento
cells; field definitions/IDs may use monospace; system diagrams sit in bounded boxes; assumption
callouts stay flat; target length is **10–15 pages**.

### Mode 1 — Voice Rules

- Technical Summary is written for the developer picking up the build — orient them to the architecture, not the business case.
- System Overview explains object relationships and data flow before introducing field-level detail.
- Design Principles explain build consequences — what breaks if the principle is not followed.
- Workflow Mapping gives developers enough context to make correct implementation decisions on edge cases the spec didn't anticipate.
- Schema section is the highest-value section — complete, precise, no deferred decisions.
- Automation section must be implementation-complete: trigger type, condition, action sequence, and any system dependency all documented.
- Never use "database" as a synonym for AnyDB — call it "the ops layer", "the system", or reference the specific object by name.
- Never use "leverage", "seamless", "robust", or "scalable" generically.
- Flagged assumptions are implementation blockers — write them with enough specificity that the builder knows exactly what to confirm.
- The document is a build contract, not a pitch deck. Write for the person who will be staring at it at 11pm trying to figure out what a field is supposed to do.

<verification id="mode1-verify">
Before finalizing Mode 1 output, check every item:

1. **Diagram gate test:** Was the Mermaid or draw.io diagram produced and approved before the full spec was generated? If not, produce the diagram first.
2. **Terminology test:** Search for "database" in the spec. Replace with "ops layer" or the specific object name. Search for "leverage", "seamless", "robust", "scalable" — remove or replace.
3. **Schema completeness test:** Are all objects documented with full field definitions? Could a developer build every object, configure every field type, and set every relationship from this section alone — without asking a single question?
4. **Workflow intent test:** Would a developer reading the Workflow Mapping section understand why each object and field exists, and be able to make a correct implementation decision on an edge case the spec didn't explicitly cover?
5. **Assumption test:** Are all inferred items flagged as "[Assumption — confirm before build]"? Is the Flagged Assumptions table complete with specific action items?
6. **Automation completeness test:** Does every automation have trigger type, condition, full action sequence, and system dependency documented? Could an implementer configure it from the spec alone?
7. **Design logic test:** Does each principle state the build consequence — what breaks or degrades without it?
8. **Length test:** Is the spec 10–15 pages? If under 10, the schema section is likely too thin.
9. **Section count:** All 14 sections present?
10. **Patterns file load test:** Did the first response explicitly state `Loaded: kaizen-architect.md + kaizen-anydb-patterns.md` before any schema writing started?
11. **Cell type test:** Does every cell use a type from Section 1 of `kaizen-anydb-patterns.md`?
12. **Formula syntax test:** Do all formulas use Section 2 syntax, including `=` prefix, curly-brace cell refs where named refs are used, and AnyDB function names?
13. **Cell format test:** Does every Currency, Percentage, Number, Date, Date & Time, Time, and auto-incrementing ID declaration include the format details required by Section 3?
14. **Reference test:** Does every Reference declare the target Type and one-to-one behavior?
15. **Attach test:** Does every Attach declaration specify parent Type, child Type, and one-to-many structural direction?
16. **Aggregation test:** Does every aggregation formula declare the attached child Type and use `C@CURRREC!CellID` or the equivalent child-Type-qualified form? Are aggregation parents using Attach, never Reference?
17. **Lookup test:** Does every Lookup declare the Reference cell it traverses and the source cell on the referenced record?
18. **Vocabulary discipline test:** Search for prohibited schema vocabulary in the spec: "dropdown", "string", "foreign key", "fk", "join", "Rollup" as a cell type, "Auto-number" as a cell type, and "Link". Remove or replace.
19. **Decision-quality test:** Does the spec name architecture kill conditions and prove AnyDB has a specific operational job beyond copying data?
</verification>

---

## Common Failures — Mode 1

**1. Schema section too thin.**
The spec lists Type names and a few key cells but defers the rest to "implementation."
Every cell must have: name, type, options (if Select), formula logic (if applicable),
connection target and direction (if Reference/Attach), and whether it's required, optional,
or computed. A developer should never need to make a design decision the spec didn't make.

**2. Automations described narratively instead of specified.**
"When a PO is received, update the status" is not a spec. The automation needs: trigger type
(record update, button, scheduled), trigger condition (Status field changes to "Received"),
action sequence (step 1: update PO Status to "Closed", step 2: create Inventory Adjustment
record linked to PO, step 3: send notification to Warehouse Manager), and system dependency
(requires Shopify inventory sync to be active).

**3. "Database" used instead of "ops layer" or "system."**
Client-facing output that calls AnyDB a "database" undermines the positioning. Search the
final output for "database" and replace every instance.

**4. Diagram skipped or deferred.**
Mode 1 has a mandatory diagram-first gate. The system architecture overview diagram must be
produced and reviewed before the full spec is written. Skipping this means the spec may not
reflect the actual system relationships correctly.

**5. Assumptions buried in prose instead of flagged.**
An assumption mentioned in paragraph 3 of the Workflow Mapping section will be missed. Every
assumption must also appear in the Flagged Assumptions table with a specific action item and
owner. Inline "[Assumption — confirm before build]" markers AND the summary table, not one
or the other.

**6. Metaobject vs. metafield confusion.**
Metafields are key-value pairs attached to existing Shopify resources. Metaobjects are
standalone structured content objects. They have different creation methods, different API
endpoints, and different Matrixify support (metafields importable, metaobjects not). If the
spec references either, it must use the correct term and note the import implication.

---

## Examples — Mode 1

<examples>

<example name="mode1-schema-excerpt">
**CONTEXT:** Gold-tier POS migration + AnyDB Standard Build for a 6-location outdoor gear retailer
migrating from Lightspeed. AnyDB scope: vendor PO management and receiving reconciliation. 23
active vendors, ~40 POs per month, stock received at a central warehouse and distributed to stores.

**WHAT A STRONG SCHEMA SECTION LOOKS LIKE (excerpt — Vendors and Purchase Orders objects only):**

```
## 7. Schema — Object & Field Definitions

### Type: Vendors

Purpose: Master vendor/supplier record. Source of truth for vendor contact info,
payment terms, and performance tracking. One Vendor record per supplier relationship.

| Cell Name         | Cell Code | Type               | Options / Logic                                                       | Required | Notes |
|-------------------|-----------|--------------------|-----------------------------------------------------------------------|----------|-------|
| Company Name      | V-01      | General            | —                                                                     | Yes      | Primary identifier. Must be unique. |
| Contact Name      | V-02      | General            | —                                                                     | No       | Primary contact at the vendor. |
| Email             | V-03      | General            | Validate with `=ISEMAIL({{Email}})`                                   | Yes      | Used for PO delivery via automation. |
| Phone             | V-04      | General            | Validate with `=ISPHONE({{Phone}})`                                   | No       | E.164 preferred. |
| Payment Terms     | V-05      | Select             | Net 15 / Net 30 / Net 45 / Net 60 / COD / Prepaid                    | Yes      | Drives PO payment tracking. [Assumption — confirm option list with client before build] |
| Lead Time (days)  | V-06      | Number             | Integer, min 0                                                        | No       | Average fulfillment lead time. Used in reorder calculations. |
| Status            | V-07      | Select             | Active / Inactive / On Hold                                           | Yes      | Inactive vendors hidden from PO creation form. |
| Notes             | V-08      | Rich Text          | —                                                                     | No       | Internal notes. Not visible on portal. |
| Open PO Count     | V-09      | Number             | `=COUNTIF(C@CURRREC!A2, "Open")`                                      | Auto     | Aggregates attached purchasing records. |
| Open PO Value     | V-10      | Currency           | `=SUMIFS(C@CURRREC!A1, C@CURRREC!A2, "Open")`                         | Auto     | CAD or client currency. |
| Purchase Orders   | V-11      | Attach             | Child Type: Purchase Orders                                           | Auto     | Vendor is parent. POs are children. |

### Type: Purchase Orders

Purpose: Tracks the lifecycle of each purchase order from draft through close.
One PO per vendor order. Contains header-level data; line items are in an attached child Type.

| Cell Name          | Cell Code | Type               | Options / Logic                                                       | Required | Notes |
|--------------------|-----------|--------------------|-----------------------------------------------------------------------|----------|-------|
| PO Number          | PO-01     | General            | `=CONCAT("PO-", TEXT(SEQNUM("po"), "0000"))`                          | Auto     | System-generated. Unique. |
| Vendor             | PO-02     | Reference          | Target Type: Vendors                                                  | Yes      | Parent vendor record. |
| Status             | PO-03     | Select             | Draft / Submitted / Acknowledged / Partially Received / Received / Closed / Cancelled | Yes | Drives automation triggers and view filtering. |
| Order Date         | PO-04     | Date               | —                                                                     | Yes      | Date PO was submitted to vendor. |
| Expected Delivery  | PO-05     | Date               | —                                                                     | No       | Vendor-provided ETA. |
| Destination        | PO-06     | Reference          | Target Type: Locations                                                | Yes      | [Assumption — confirm location names match Shopify location names exactly] |
| Subtotal           | PO-07     | Currency           | `=SUM(C@CURRREC!A1)`                                                  | Auto     | Sum across attached line items. |
| Shipping Cost      | PO-08     | Currency           | Manual entry                                                          | No       | — |
| Total Value        | PO-09     | Currency           | `={{Subtotal}} + {{Shipping Cost}}`                                   | Auto     | Header-level total. |
| Items Ordered      | PO-10     | Number             | `=SUM(C@CURRREC!A2)`                                                  | Auto     | — |
| Items Received     | PO-11     | Number             | `=SUM(C@CURRREC!A3)`                                                  | Auto     | — |
| Receiving Variance | PO-12     | Number             | `={{Items Ordered}} - {{Items Received}}`                             | Auto     | 0 = fully received. >0 = short. <0 = over-received. |
| Notes              | PO-13     | Rich Text          | —                                                                     | No       | Internal notes. |
| Line Items         | PO-14     | Attach             | Child Type: PO Line Items                                             | Auto     | PO is parent. Line items are children. |
| Created By         | PO-15     | User               | —                                                                     | Auto     | Audit trail. |
| Last Modified      | PO-16     | Date & Time        | System-generated, UTC                                                 | Auto     | — |
```

**WHAT MAKES THIS STRONG:**
- Every field has a code (V-01, PO-12) so the builder can reference fields unambiguously.
- Types are exact (`Select`, not "dropdown"). Options are listed in full.
- Aggregation formulas and other formulas show the complete logic, not just "calculates total."
- Relationships state direction and type (`Reference` vs `Attach`, parent-child direction, which Type is the parent).
- Assumptions are flagged inline with "[Assumption — confirm...]" and would also appear in the Flagged Assumptions table.
- Required vs. Auto vs. Optional is explicit for every field.
- The Notes column explains operational significance, not just data format.
- A developer could build both objects from this table without asking a single follow-up question.

**WHAT A WEAK VERSION LOOKS LIKE (avoid this):**

```
### Vendors
- Company Name
- Contact info (name, email, phone)
- Payment terms
- Status (active/inactive)
- Related purchase orders

### Purchase Orders
- PO number (auto-generated)
- Linked to vendor
- Status tracking
- Line items
- Totals
```

**WHY IT FAILS:** No field codes. No types. No formula logic. No relationship direction. No options for Select cells. A developer reading this would need to make 20+ design decisions the spec should have made. This is a feature list, not a build spec.
</example>

</examples>

---

# ============================================================
# MODE 2 — INTEGRATION MAP
# ============================================================

## Mode 2: Integration Mapping

Converts discovery inputs into a reusable integration mapping package for commerce and retail
operations. Turns a client's stack, entities, business processes, and operational constraints into
a clear integration design that can guide scoping, implementation, QA, and SOP creation.

<goal>
Produce a concise but complete integration mapping document with:
- Executive context
- Systems in scope
- Source-of-truth matrix
- Integration map
- Entity and field mapping notes
- Data refresh protocol
- Exception and reconciliation handling
- AnyDB role definition (when applicable)
- Risks and open questions
- Build recommendation
</goal>

<critical_rules id="mode2-rules" priority="must-follow">
- Never invent vendor capabilities, API endpoints, or business facts not in the provided materials.
- Mark uncertain ownership, transformations, or frequencies as assumptions.
- Distinguish clearly between event-driven syncs, scheduled syncs, manual updates, and reconciliation jobs.
- When AnyDB is in scope, explain its role explicitly rather than treating it as a generic database.
- Prefer one clear recommended approach over a long list of equal options.
- Preserve contradictions and unresolved issues in an open-questions section.
- Name the source of truth for each critical entity.
- Specify direction and cadence for each integration.
- State refresh protocol and validation approach.
- Identify failure ownership for every integration path.
</critical_rules>

### Mode 2 — When to Use

Use when the task involves:
- Mapping data flows between Shopify, POS, ERP, WMS, accounting, CRM, 3PL, marketplaces, or AnyDB
- Defining system ownership for entities (products, inventory, customers, orders, payments, vendors, locations, financial states)
- Producing field mapping, sync logic, refresh policy, exception handling, or implementation recommendation
- Turning discovery notes into a technical-but-client-readable blueprint

Do NOT use for: writing SOPs as the main deliverable (use Mode 3), generic product comparisons, or implementation steps requiring verified vendor API details not in the task materials.

**Delivery OS handoff:** When this Integration Map is the engine for a Mixed Commerce Systems engagement (two or more active commerce surfaces with cross-surface source-of-truth or sequencing dependencies), the Mode 2 outputs — surface inventory, build-vs-buy verdicts, and the cross-surface source-of-truth matrix — feed the `delivery-os/templates/mixed-commerce-baseline-brief.md` producer, which records them into the Engagement Baseline plus its Mixed extension and adds the launch sequence and cross-surface risk gates Mode 2 does not own.

### Mode 2 — Required Inputs

Collect or infer before drafting:
- Systems in scope and their roles
- Core entities in scope
- Business processes being supported
- Pain points, constraints, and known failure modes
- Desired reporting or reconciliation outcomes
- Whether AnyDB is in scope and in what role

If critical inputs are missing, state assumptions explicitly and create an open-questions section.

### Mode 2 — Workflow Sequence

#### Step 1: System Inventory
Create a plain-language inventory of each system:
- Role in the business
- What data it creates
- What data it updates
- What it should never overwrite
- Operational owner

#### Step 1b: Merchant Surface-Complexity Classification (Mode 2 Gate)

Before assigning source-of-truth, classify the merchant using `reference/kaizen-surface-complexity.md`:
- **Simple Retail** (1–2 locations, no ERP, < 5K SKUs) → Shopify-native for most domains
- **Growing Multi-Location** (3–10 locations, possible ERP) → evaluate each domain against the reference table
- **Complex Multi-Surface** (10+ locations or ERP as backbone) → external systems likely own product, inventory, and/or customer domains

State the classification at the top of the integration map output. Every source-of-truth decision that follows should be consistent with it.

**Build-vs-Buy verdict:** For each system in the client's stack, assign one of four verdicts from `reference/kaizen-build-vs-buy.md`: NATIVE / THIRD-PARTY / CUSTOM BUILD / RETAIN & INTEGRATE. Add a Verdict column to the Systems in Scope table.

If an ERP is confirmed or inferred (from signal inference chains — see `reference/kaizen-signal-inference.md`), load `reference/kaizen-erp-patterns.md` and use it to define data flows, sync frequency, and the source-of-truth matrix for product, inventory, order, customer, and pricing domains.

#### Step 2: Source-of-Truth Assignment
Assign ownership at the entity level, not at the platform level.

Use this logic (from `reference/kaizen-data-freshness.md` heuristics):
1. Prefer the system where the business event originates
2. Prefer the system of record that downstream teams already reconcile against
3. System with cleanest keys and lowest manual overwrite risk
4. System downstream teams trust for audit/finance
5. If no single source stable, declare split ownership explicitly

Separate creation ownership from enrichment ownership when needed.
If ownership changes by lifecycle stage, state that explicitly.

Common split examples:
- Product core data from ERP, channel merchandising from ecommerce platform
- Customer master from ecommerce or CRM, loyalty enrichment elsewhere
- Order capture from commerce platform, fulfillment state from WMS, accounting state from finance system

#### Step 3: Integration Path Definition
For each path, document:
- From system
- To system
- Entities moved
- Trigger
- Frequency or cadence
- Required transformations
- Validation rules
- Failure handling
- Monitoring owner

#### Step 4: Field Mapping Detail
Map only the fields that matter operationally. Group fields by entity and note:
- Required fields
- Derived fields
- Lookup dependencies
- Defaults
- Formatting rules
- ID strategy
- Backfill requirements

#### Step 5: Refresh Protocol
For each critical entity or sync, assign all five elements:

**1. Update type:**
- Event-driven: updates immediately from a business event
- Scheduled: updates on a set cadence
- Batch reconciliation: verifies or repairs prior updates
- Manual: changes only by reviewed user action

**2. Freshness target** (plain language):
- Immediate, Near real-time, Hourly, Daily, End of day, Weekly
- Only assign a tighter target if the business process actually needs it

**3. Validation layer** — how freshness and correctness are checked:
- Record counts, Updated-at comparison, Status comparison, Financial tie-out
- Exception queue review, Sample-based audit

**4. Repair path** — what happens when data is stale or inconsistent:
- Automatic retry, Requeue, Manual review in AnyDB, Daily reconciliation job
- Escalation to implementation owner

**5. Business rationale** — why the chosen refresh rule exists

Reference data freshness defaults from `reference/kaizen-data-freshness.md`:

| Entity | Default Update Type | Freshness Target | Validation | Repair Path |
|---|---|---|---|---|
| Orders | Event-driven | Immediate / near real-time | Record arrival + status checks | Retry, requeue, manual review |
| Payments & Refunds | Event-driven + reconciliation | Immediate + daily tie-out | Financial status comparison | Retry, reconcile, escalate |
| Inventory | Event-driven + reconciliation | Near real-time | Quantity + location comparison | Retry, queue exceptions, daily balance |
| Shipments | Event-driven | Near real-time | Tracking + status comparison | Retry, carrier-status review |
| Products & Variants | Scheduled or event-driven | Hourly to daily | Changed record comparison | Reprocess changed records |
| Price/Cost data | Scheduled | Hourly to daily | Changed field audit | Re-run batch or manual correction |
| Customers | Event-driven + dedupe | Near real-time | Identity + key match review | Merge review, exception handling |
| Payouts/Accounting | Scheduled + reconciliation | Daily / end-of-day | Tie-out + completeness | Re-export, reconcile, finance review |
| Vendor/PO reference | Scheduled | Daily to weekly | Count + change review | Re-run batch |

#### Step 6: Exceptions and Reconciliation
Document what happens when:
- A record is missing
- A key mismatch occurs
- A sync fails
- A user edits the wrong system
- Timing creates temporary mismatches

Always include: failure owner, detection method, first response, business-safe fallback, reconciliation cadence for high-risk entities.

High-risk entities: inventory availability, orders, payments/refunds, payouts, accounting exports.

#### Step 7: AnyDB Decision Branch
Treat AnyDB as an explicit architectural choice, not a default add-on.

**Choose AnyDB when:**
- The client needs a shared operational workspace across departments
- The process requires structured records, forms, formulas, or workflow automation
- Exceptions, approvals, or task states need visibility outside the source applications
- The business needs a lightweight operational layer without turning the ERP or ecommerce platform into a workflow tool

**Do NOT recommend AnyDB as the primary source of truth for everything by default.**

If AnyDB is included, assign one of these roles:
1. **Operational Control Layer** — shared records across departments, approval + task status, push validated changes downstream
2. **Exception Queue** — one record per exception, track triage and closure by status
3. **Approval Workflow Layer** — separate proposed from approved values, automate downstream only after approval
4. **Shared Reference Hub** — mapping keys, location metadata, custom taxonomies, protected from casual edits
5. **Supplemental Reporting Workspace** — snapshots, calculated fields, exception flags, not write-back unless governance explicit

For each AnyDB role, document:
- What records live in AnyDB
- Which systems write into it
- Which users act in it
- Which formulas or automations matter
- Which records sync back out and under what controls

#### Step 8: Recommendation
Recommend the simplest viable design:
- Native connector when requirements are straightforward and low-risk
- Middleware when transformations, branching, or retries matter
- AnyDB when structured operations, approvals, exception handling, workflow visibility, or shared operational records are needed
- Custom API work only when requirements cannot be met reliably another way

### Mode 2 — Integration Archetypes

**Event-driven sync** — best for records affecting live operations: orders, payments, refunds, inventory deltas, shipment events.

**Scheduled sync** — best for data that changes less often or tolerates delay: product enrichment, vendor records, cost updates, reference tables, historical reporting loads.

**Batch reconciliation** — best for trust-but-verify: finance tie-outs, inventory balance checks, missing-record detection, corrective backfills.

**Manual controlled update** — best for sensitive administrative changes: approved master-data corrections, mapping override tables, exception resolution, sign-off steps.

### Mode 2 — Output Templates

**Systems in Scope:**

| System | Role | Verdict | Creates | Updates | Must not overwrite | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| [System] | [Role] | NATIVE / THIRD-PARTY / CUSTOM / RETAIN | [Records] | [Records] | [Records] | [Team] |

**Source-of-Truth Matrix:**

| Entity | System of truth | Secondary systems | Notes |
| --- | --- | --- | --- |
| Products | [System] | [Systems] | [Notes] |
| Inventory | [System] | [Systems] | [Notes] |
| Customers | [System] | [Systems] | [Notes] |
| Orders | [System] | [Systems] | [Notes] |
| Payments | [System] | [Systems] | [Notes] |

**Integration Map:**

| From | To | Entity | Trigger | Frequency | Transformations | Validation | Failure handling |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Source] | [Target] | [Entity] | [Trigger] | [Cadence] | [Logic] | [Method] | [Repair path] |

**Refresh Protocol:**

| Entity or sync | Update type | Freshness target | Validation layer | Repair path | Business rationale |
| --- | --- | --- | --- | --- | --- |
| [Entity] | [Type] | [Target] | [Check] | [Repair] | [Why] |

**AnyDB Role Definition:**

| Question | Answer |
| --- | --- |
| Is AnyDB in scope? | [Yes/No] |
| Recommended role | [Operational control layer / exception queue / approval workflow layer / shared reference hub / supplemental reporting workspace / not recommended] |
| Main records in AnyDB | [Records] |
| Who works in it | [Teams] |
| What writes into it | [Systems/processes] |
| What writes back out | [Systems/processes] |
| Key formulas or automations | [Needed logic] |
| Governance note | [Controls] |

**Risks and Open Questions:**

### Risks
- [Risk]: [Why it matters] -> [Mitigation]

### Open questions
- [Question]

**Recommendation Block:**

### Recommended approach
[One clear recommendation in plain language.]

### Why this approach fits
- [Reason]

### What to validate before build
- [Validation item]

<verification id="mode2-verify">
Before finalizing Mode 2 output:

1. **Surface-complexity test:** Is the merchant classified (Simple Retail / Growing Multi-Location / Complex Multi-Surface) and does every source-of-truth decision align with that classification?
2. **Build-vs-buy test:** Does every system in the Systems in Scope table have a verdict (NATIVE / THIRD-PARTY / CUSTOM / RETAIN)? No system should be listed without one.
3. **ERP test:** If ERP is confirmed or inferred, were patterns loaded from `reference/kaizen-erp-patterns.md`? Are the Last 10% edge cases surfaced in risks?
4. **Source-of-truth test:** Is every critical entity assigned an owner? Are splits explicitly declared?
5. **Direction test:** Does every integration path state direction and cadence?
6. **Refresh protocol test:** Does every entity or sync have all five elements (update type, freshness target, validation, repair, rationale)?
7. **Failure ownership test:** Is there a named failure owner for every integration path?
8. **AnyDB clarity test:** If AnyDB is included, is its role named explicitly? Are records, users, automations, and governance documented?
9. **Assumption test:** Are uncertain items marked as assumptions and preserved in open questions?
10. **Recommendation test:** Is there one clear recommended approach, not a list of equal options?
11. **Template test:** Are all relevant templates from the output section populated?
12. **Decision-quality test:** Does the integration recommendation preserve source-of-truth discipline, stress-test the runner-up option, and name what would change the recommendation?
</verification>

---

# ============================================================
# MODE 3 — SOP BUILDER
# ============================================================

## Mode 3: SOP Builder

Converts an approved workflow, integration map, or operating model into clear, role-based SOPs
for commerce and retail operations. Turns a defined future-state process into practical procedures
that teams can follow, audit, train on, and maintain.

<goal>
Produce a practical SOP document or SOP set with:
- SOP title and purpose
- Trigger and scope
- Roles and responsibilities
- Systems used
- Step-by-step procedure
- Exception handling
- Reconciliation or quality checks
- Escalation path
- Review and maintenance cadence
- Open questions or assumptions
</goal>

<critical_rules id="mode3-rules" priority="must-follow">
- Never invent system capabilities, governance rules, or business facts not present in the provided materials.
- Write procedures in plain language that an operator can follow without interpretation.
- Separate standard flow from exception flow.
- Assign clear ownership to each action where possible.
- When AnyDB is included, state exactly how it is used — table name, fields, statuses, views, automations, downstream actions.
- Preserve unresolved gaps in an assumptions or open-questions section.
- Include at least one control or review step in every SOP.
- State maintenance cadence for every SOP.
</critical_rules>

### Mode 3 — When to Use

Use when:
- Converting an approved integration design into operational procedures
- Writing SOPs for store operations, ecommerce operations, warehouse, finance, customer service, or admin teams
- Documenting exception handling, reconciliation, approvals, data corrections, or onboarding processes
- Translating AnyDB-supported workflows into step-by-step operating guidance

Do NOT use for: deciding system architecture from scratch (use Mode 1 or 2), producing a technical integration mapping spec as the primary output, or writing policy/HR/compliance documents requiring legal review.

### Mode 3 — Required Inputs

Collect or infer before drafting:
- Approved workflow, integration map, or future-state process
- Roles involved and who owns each step
- Trigger events for the procedure
- Systems or tools used in each step
- Exception cases and escalation paths
- Review cadence and success checks
- Whether AnyDB is part of the workflow and what users do inside it

### Mode 3 — Default SOP Types

#### Daily Operations SOP
Use when the process is routine and recurring.
Examples: daily order review, daily inventory verification, daily fulfillment checks, daily queue management.

#### Exception Handling SOP
Use when triggered by a failure, mismatch, or blocked workflow.
Examples: failed sync review, missing customer record, inventory discrepancy, payment mismatch.

#### Reconciliation SOP
Use when validating records match across systems.
Examples: end-of-day sales reconciliation, payout review, accounting export verification, inventory balance checks.

#### Data Correction SOP
Use when authorized users must fix records safely.
Examples: correcting product metadata, repairing location assignments, fixing mapping keys, updating customer merge issues.

#### Onboarding SOP
Use when bringing on a new store, location, workflow, or user group.
Examples: new location setup, new staff onboarding, new integration handoff, new queue or approval process rollout.

### Mode 3 — SOP Assembly Sequence

#### Step 1: Define the SOP Frame
Document:
- Title
- Purpose
- Trigger
- Scope
- Primary owner
- Supporting roles
- Systems used
- Success condition

#### Step 2: Map the Standard Flow
Write the default path as a sequence of clear actions. Each step answers:
- Who acts?
- In which system?
- What do they do?
- What output or status confirms completion?

#### Step 3: Add Decision Points
For any branch, make the condition explicit:
- If payment status is missing, move to exception handling
- If location data is incomplete, hold the record for review
- If approval is required, route to the approver before proceeding

#### Step 4: Document Exception Handling
For each likely failure mode:
- Trigger condition
- Detection method
- Owner
- First response
- Safe fallback
- Escalation path

#### Step 5: Add Checks and Reconciliation
Define the control layer that prevents silent failure:
- End-of-day checks
- Record-count comparisons
- Queue review
- Financial tie-outs
- Spot audits
- Approval logs

#### Step 6: Add Maintenance Guidance
State:
- How often the SOP should be reviewed
- What changes require updating the SOP
- Which metrics or issues signal the SOP is outdated

Default review guidance:
- Review high-change SOPs monthly
- Review stable SOPs quarterly
- Update immediately after system changes, new approval logic, or major process failures

### Mode 3 — AnyDB Procedure Branch

When AnyDB is in scope, define its role precisely. Do not write "update AnyDB" without saying what the user is updating and why.

Possible AnyDB activities: create a record, update status, assign a task, review an exception queue, attach or review documents, approve or reject a proposed change, monitor automation outcomes, use formulas or views to confirm next actions.

For each AnyDB step, document:
- Table or record type
- Required fields
- Status changes
- Who owns the step
- What happens next
- Whether another system must also be updated

Good AnyDB-linked SOP components:
- Exception triage queue
- Approval workflow
- Shared task list
- Document collection and review
- Reference-table maintenance
- Status-driven handoff process

For AnyDB steps, specify: table name or record category, required fields, status vocabulary, view or filter used, approval rule if any, automation expectation if any, what external system action follows.

### Mode 3 — Control Point Guidance

Include a control point when:
- Data affects money, inventory, customer communication, or compliance
- A user could update the wrong system
- A sync might silently fail
- A status change triggers downstream work
- Multiple teams rely on the same record

Useful control methods: daily review queue, required approval step, four-eyes check, record count comparison, exception report, dashboard spot check, weekly audit sample.

### Mode 3 — SOP Design Principles

1. Write for the person doing the work, not just the person designing the process
2. Prefer observable actions over abstract instructions
3. Keep one step to one action when possible
4. Name systems and statuses explicitly
5. Distinguish standard flow, exception flow, and escalation
6. Include review cadence so the SOP stays current

### Mode 3 — Output Templates

**SOP Header:**

| Field | Value |
| --- | --- |
| SOP title | [Title] |
| Purpose | [Why this exists] |
| Trigger | [Event or cadence] |
| Scope | [Included workflow boundary] |
| Primary owner | [Role] |
| Supporting roles | [Roles] |
| Systems used | [Systems] |
| Success condition | [Observable outcome] |
| Review cadence | [Monthly / quarterly / after change] |

**Procedure Steps:**

| Step | Role | System | Action | Output or completion signal |
| --- | --- | --- | --- | --- |
| 1 | [Role] | [System] | [Action] | [Result] |

**Decision Points:**

| Condition | Action | Owner | Escalation if unresolved |
| --- | --- | --- | --- |
| [Condition] | [Action] | [Role] | [Escalation] |

**Exception Handling:**

| Exception | Detection method | First response | Owner | Safe fallback | Escalation |
| --- | --- | --- | --- | --- | --- |
| [Issue] | [How detected] | [First action] | [Role] | [Fallback] | [Escalation] |

**Reconciliation or Quality Checks:**

| Check | Cadence | Owner | Method | Pass criteria | Failure response |
| --- | --- | --- | --- | --- | --- |
| [Check] | [Cadence] | [Role] | [Method] | [Pass] | [Failure action] |

**AnyDB Procedure Detail:**

| Question | Answer |
| --- | --- |
| Is AnyDB in scope? | [Yes/No] |
| Record type or table | [Table] |
| Main user actions | [Create/update/approve/assign/review] |
| Required fields | [Fields] |
| Status values | [Statuses] |
| View or filter used | [View] |
| Automation expectation | [Automation] |
| Downstream action | [What happens next] |

**Maintenance Note:**
- Review this SOP every [cadence].
- Update it when [system/process change] occurs.
- Escalate SOP maintenance to [owner] when [signal] appears.

<verification id="mode3-verify">
Before finalizing Mode 3 output:

1. **Operator test:** Could a frontline operator follow the instructions without interpreting vague language?
2. **Separation test:** Are standard flow and exception flow clearly separated?
3. **Ownership test:** Does every action have a named role?
4. **System test:** Does every step name the system where the action happens?
5. **Control test:** Is there at least one quality control or review step?
6. **AnyDB precision test:** If AnyDB is in scope, does every AnyDB step specify table, fields, statuses, views, and downstream actions?
7. **Maintenance test:** Does every SOP state review cadence and update triggers?
8. **Assumption test:** Are unresolved items preserved in open questions?
9. **Decision-quality test:** Do SOPs avoid assigning work to staff, systems, or roles whose ownership was only inferred unless that assumption is flagged?
</verification>

---

# ============================================================
# EXAMPLES
# ============================================================

## Example 1 — AnyDB Spec (Mode 1)

**Input:**
"We're working with Hype Supply Co., a multi-brand streetwear distributor. They have 3 warehouses, purchase orders done in spreadsheets, no receiving reconciliation, inventory transfers tracked via WhatsApp, and Shopify for e-commerce. They need an AnyDB build to manage purchasing, receiving, transfers, and vendor coordination."

**Expected output structure:**
- Cover page with "AnyDB Operations Architecture — System Specification" for Hype Supply Co.
- Technical Summary (no "database" language, written for the lead developer):

> "This specification defines an AnyDB operations layer for Hype Supply Co. — a multi-brand
> streetwear distributor running three warehouses and a Shopify e-commerce store. The system
> is built around eight objects: Suppliers, Purchase Orders, PO Line Items, Receiving Logs,
> Inventory Transfers, Transfer Line Items, Locations, and Products (synced read-only from Shopify).
>
> The core architectural constraint to understand before building: Products is a read-only sync
> object — it pulls from Shopify and must never be written back to. All procurement records
> reference Products for line-item lookups, but inventory quantity changes are pushed back to
> Shopify only after a Receiving Log is reconciled and approved. Build the approval gate first;
> everything downstream depends on it.
>
> Spreadsheet-based PO tracking is being replaced entirely. There is no legacy data to migrate
> into this system — the build starts clean. Initial seed data required before go-live: Suppliers
> table and Locations table must be populated manually."

- System Overview with Figure 1 showing: Products (synced from Shopify), Suppliers, Purchase Orders, PO Line Items, Receiving Logs, Transfers, Locations, Staff
- Schema with full field definitions for 7–8 objects. Example:

```
OBJECT: Purchase Orders
Purpose: Tracks every order placed with a supplier — from request through delivery and
reconciliation. This is the starting point of the procurement workflow.
Connects to: Suppliers (Reference), PO Line Items (Attach child), Locations (Reference)
Used in workflows: Purchasing, Receiving, Reorder Planning

Fields:
  PO Number          General        Auto-generated. Format: PO-[YYYY]-[sequential]
  Supplier           Reference      Links to Suppliers Type
  Destination        Reference      Links to Locations Type — where stock is being sent
  Status             Select         [Draft, Submitted, Confirmed, Shipped, Received, Closed]
  Order Date         Date           Date PO was submitted to supplier
  Expected Delivery  Date           Estimated arrival — drives receiving queue
  Total Value        Currency       Formula from attached PO Line Items
  Notes              Rich Text      Internal notes — not visible to supplier portal
  Approved By        Reference      Links to Staff — required before status moves to Submitted
  Shopify Sync       No

Shopify Sync: No — purchase orders are internal operations. Product data is pulled from Shopify
into AnyDB via the Products object sync.
```

- At least 5 visual exhibits including mandatory Figure 1
- All 14 sections populated
- Flagged assumptions table with clear action items

**Anti-pattern to avoid:**
"This document outlines the database architecture for Hype Supply Co.'s new system. The database
will leverage AnyDB's robust features to seamlessly integrate with their existing Shopify setup
and provide a scalable solution for their growing needs."
Fails because: calls it "database" (forbidden), uses "leverage", "robust", "seamlessly", "scalable".

---

## Example 2 — Integration Mapping (Mode 2)

**Input:**
"Client is a 6-location furniture retailer. Shopify POS in stores, Shopify e-commerce online. They use QuickBooks for accounting, ShipStation for e-commerce fulfillment, and a spreadsheet for vendor PO tracking. Inventory is managed in Shopify but they have no reconciliation process. They want to add AnyDB for vendor management and purchase orders."

**Expected output structure:**

**Systems in Scope:**

| System | Role | Creates | Updates | Must not overwrite | Owner |
| --- | --- | --- | --- | --- | --- |
| Shopify (Online + POS) | Commerce platform, inventory master | Products, orders, customers | Inventory levels, order status | Product handles, historical orders | Ecommerce + Store Ops |
| QuickBooks | Accounting system of record | Journal entries, invoices | Payment status, payout reconciliation | GL codes, closed periods | Finance |
| ShipStation | E-commerce fulfillment | Shipping labels, tracking | Fulfillment status on orders | Order amounts | Ops / Warehouse |
| AnyDB | Vendor management + PO ops layer | Purchase orders, vendor records, receiving logs | PO status, receiving reconciliation | Shopify inventory (read-only sync) | Ops Manager |
| Spreadsheets (legacy) | To be replaced by AnyDB | PO tracking (current) | N/A — being deprecated | N/A | Ops Manager |

**Source-of-Truth Matrix:**

| Entity | System of truth | Secondary systems | Notes |
| --- | --- | --- | --- |
| Products | Shopify | AnyDB (read-only sync) | Shopify is master for catalog. AnyDB reads product data for PO line items |
| Inventory | Shopify | AnyDB (monitoring) | Shopify tracks available qty. AnyDB tracks expected incoming from POs |
| Orders | Shopify | QuickBooks (accounting), ShipStation (fulfillment) | Order captured in Shopify, fulfilled via ShipStation, reconciled in QB |
| Vendors | AnyDB | None | New entity — no current structured system. AnyDB becomes master |
| Purchase Orders | AnyDB | None | Replacing spreadsheets. AnyDB is the sole PO system |
| Payments/Payouts | QuickBooks | Shopify (source data) | QB is accounting SOT. Shopify provides payout data for reconciliation |

**AnyDB Role: Operational Control Layer** — shared PO and vendor records, approval workflow for purchase orders, receiving reconciliation queue, product data synced read-only from Shopify for PO line item lookups.

---

# ============================================================
# HANDOFF FORMAT
# ============================================================

When a mode completes, always append:

```
---
## HANDOFF — Next Step

**What was produced:** [AnyDB Spec / Integration Map / SOPs]
**Client:** [name]
**Mode used:** [1/2/3]

**Next pipeline step:**
- After AnyDB Spec → To continue, say: "Now run the kaizen-architect` in Integration Map mode to define system connections
- After Integration Map → To continue, say: "Now run the kaizen-architect` in SOP mode to build operational procedures
- After SOPs → To continue, say: "Now run the kaizen-publish` for client-facing content or training materials
- Full build sequence: AnyDB Spec → Integration Map → SOPs (run all three in order for complete architecture)
```

When receiving handoff FROM another skill:
- From the kaizen-propose skill or the kaizen-diagnose skill — extract client context, systems, entities, pain points, and begin the appropriate mode
- From Mode 1 (AnyDB Spec) into Mode 2 — use the spec's schema, integration points, and design principles as input
- From Mode 2 (Integration Map) into Mode 3 — use the integration map's source-of-truth matrix, refresh protocols, and AnyDB role as input

---

# ============================================================
# CROSS-MODE RULES
# ============================================================

<critical_rules id="global-rules" priority="must-follow">
- Each mode works independently with full quality. Never sacrifice depth for consolidation.
- Apply voice rules from `reference/kaizen-identity.md` across all modes.
- Never call AnyDB a "database" in any client-facing output.
- Never use: "leverage", "seamless", "robust", "scalable" (generically), "holistic", "cutting-edge", "game-changing", "transformative".
- Flag all inferred information as assumptions.
- When AnyDB is in scope in ANY mode, explain its role explicitly — table names, fields, statuses, views, automations, downstream actions.
- Every output must end with a handoff block in the chat response. Never embed handoff blocks inside client-facing PDF specs or SOP documents.
- If running multiple modes in sequence, carry context forward — do not re-ask for information already provided.
</critical_rules>

---

## Automation Governance Verdicts

When architecture includes AnyDB automations, Shopify Flow workflows, API syncs, scheduled jobs,
webhooks, or integration logic, apply `reference/kaizen-automation-governance.md` before
recommending build or activation.

Every automation recommendation must return one internal verdict:

- `APPROVE`: source of truth, owner, fallback, logging, error handling, and test evidence are clear.
- `APPROVE AS PILOT`: low-risk automation can run with limited scope, short monitoring window, and rollback owner.
- `PARTIAL AUTOMATION ONLY`: automate the safe portion and keep human review for ambiguity, money movement, inventory risk, or client-visible messaging.
- `DEFER`: business rule, source data, owner, or test path is not stable enough yet.
- `REJECT`: automation would create unacceptable risk, overwrite a source of truth, hide errors, or bypass required approval.

Architecture outputs that include automation must name the source of truth, human owner, fallback
path, log location, test evidence required, and re-audit trigger. Do not bury these in prose.

## Workflow Registry And Boundary Contracts

Before designing AnyDB tables, Shopify syncs, or integration workflows, create a 4-view workflow
registry when the engagement includes more than one workflow, system, or actor.

Required registry views:

1. **By Workflow:** `Workflow | Spec file | Status | Trigger | Primary actor | Last reviewed`
   with status limited to `Approved`, `Review`, `Draft`, `Missing`, or `Deprecated`.
2. **By Component:** every AnyDB Type, Cell, formula, view, automation, Shopify object, Flow
   workflow, or integration endpoint mapped to the workflows that touch it.
3. **By User Journey:** merchant journeys, Kaizen PM journeys, and system-to-system journeys.
4. **By State:** `State | Entered by | Exited by | Workflows that can trigger exit`.

`Missing` means implementation exists without an approved spec. Treat it as a red flag that must
be scoped, deferred in writing, or fixed before build starts.

For each system boundary, define the handoff contract:

```text
HANDOFF: [From] -> [To]
PAYLOAD: { field: type, description }
SUCCESS RESPONSE: { field: type }
FAILURE RESPONSE: { error: string, code: string, retryable: bool }
TIMEOUT: [duration] -> treated as FAILURE
ON FAILURE: [recovery action]
```

For each major workflow state, describe what each party sees:

```text
State: [workflow status]
Merchant sees: [POS, email, portal, or staff-facing signal]
Kaizen PM sees: [AnyDB, task, report, or QA signal]
AnyDB: [record status, fields, dates, owner]
Shopify: [tag, metafield, order state, inventory state, Flow action]
```

## Success Metrics

A successful architecture output:

- identifies the source of truth for every critical entity before proposing workflows
- keeps Shopify as the commerce execution layer and AnyDB as the operational/spec layer unless evidence proves otherwise
- marks every inferred field, status, threshold, or integration behavior as an assumption
- includes a 4-view workflow registry before multi-workflow AnyDB or integration builds
- defines boundary handoff contracts with success, failure, timeout, and recovery behavior
- includes build order, ownership, failure handling, and handoff fields for each major system
- uses automation verdicts for every AnyDB, Flow, API, webhook, or integration automation
- gives the next builder enough detail to configure the system without re-discovering requirements

## Output Quality References

For AnyDB architecture, integration maps, SOPs, automation architecture, or architecture review,
load:

- `reference/kaizen-output-quality-standard.md`
- `reference/kaizen-judgment-rubrics.md`

Use the `kaizen-architect` criteria and Architecture Rubric. If the work starts with tables before
workflows, states, owners, and source-of-truth boundaries, revise the architecture.

## Pattern And Example References

For deeper architecture judgment, load as needed:

- `reference/kaizen-retail-ops-patterns.md`
- `reference/kaizen-anydb-use-case-library.md`
- `examples/kaizen-anydb-architecture-examples.md`

Use these when deciding whether AnyDB belongs in scope, when mapping workflow states, or when the
spec risks becoming table-first instead of workflow-first.
