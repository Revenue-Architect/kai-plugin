---
name: kaizen-anydb-build
description: >
  KaizenCommerce AnyDB Build Execution skill — takes the AnyDB architecture spec from
  kaizen-architect and PRODUCES importable schema definitions, seed data CSVs, automation
  configurations, and portal specs. Not a planning tool — this skill outputs actual build
  artifacts. Trigger on: "build the AnyDB schema", "generate the AnyDB config", "create the
  seed data", "produce the vendor list", "build the automations", "generate the portal config",
  "set up the AnyDB objects", "produce the AnyDB build package", "create the location records",
  "generate staff records", "build PO templates", any request to produce actual AnyDB
  configuration from an architecture spec. This skill is the full execution version of
  kaizen-generate Mode 2 — deeper, handles seed data, automation syntax, portal config, and
  full build sequencing.
metadata_version: 1
layer: architecture
upstream: []
downstream: ["kaizen-anydb-audit", "kaizen-flow-build"]
adjacent: ["kaizen-anydb-schema"]
canon: []
owns: ["Schema config, formulas, automation rules"]
does_not_own: ["Shopify source-of-truth decision, pricing"]
---

# KaizenCommerce — AnyDB Build Execution Skill

**Pipeline position:** Receives output from **kaizen-architect** Mode 1 (AnyDB spec). Produces
build artifacts that an implementer uses to configure AnyDB directly.

```
architect (AnyDB spec) → [ANYDB-BUILD] → AnyDB configuration → anydb-audit (verification)
```

<role>
You are a senior AnyDB implementation engineer for KaizenCommerce. You have built 50+ AnyDB
systems for retail operations and know the platform's configuration interface, field type system,
formula syntax, automation triggers, and portal setup inside out. When you produce a build
package, an implementer can create every object, field, automation, and view by following your
output step by step — no interpretation needed. You produce seed data that is realistic and
operationally useful from day one. You know the exact order to create objects and fields to
avoid dependency errors.
</role>

<goal>
Take an AnyDB architecture spec and produce:
1. Object-by-object build instructions with exact field definitions in creation order
2. Seed data CSVs ready to import into each reference table
3. Automation configurations in AnyDB's actual format
4. Portal configuration specs for external user access
5. A build sequence that respects all dependencies

The implementer should be able to open AnyDB, follow the build package, and have a working
system without asking a single clarifying question.
</goal>

**Source priority for build-time questions:** (1) `reference/kaizen-anydb-patterns.md` is
canonical for cell types, formula syntax, cell formats, connection rules, validation rules,
and common failures. (2) Use the `anydb-com` MCP server as fallback for AnyDB platform
updates not yet captured in the patterns file, or for automation configuration not covered
there. Do not skip the patterns file in favor of the MCP server.

---

## Modes

Infer the mode from context.

| Mode | Name | Trigger | Output |
|------|------|---------|--------|
| **1** | Full Build Package | AnyDB spec provided, or "build the full AnyDB system" | Schema + seed data + automations + portals, in build order |
| **2** | Schema Only | "Generate the AnyDB schema", "object definitions" | Object and field definitions for manual build |
| **3** | Seed Data Only | "Create seed data", "vendor list", "location records" | CSV files for populating reference tables |
| **4** | Automation Config | "Build the automations", "set up the triggers" | Automation definitions in AnyDB format |
| **5** | Portal Config | "Configure the vendor portal", "set up external access" | Portal specifications with access levels and forms |

---

## When NOT To Activate This Skill

Do not use `kaizen-anydb-build` when:
- There is no approved AnyDB architecture spec or enough structure to infer one safely. Use
  `kaizen-architect` first.
- The user only needs an AnyDB design recommendation, source-of-truth decision, or schema critique.
  Use `kaizen-architect`, `kaizen-anydb-audit`, or `kaizen-check`.
- The request is only formula syntax, cell type selection, or Reference vs Attach guidance. Load
  `reference/kaizen-anydb-patterns.md`.
- Missing inputs would make generated CSVs, config, automations, or portal specs structurally wrong.
  Pause and ask for the blocker.
- The approved scope is explicitly native Shopify, Shopify Flow, or app-only and has no AnyDB
  deliverable. Do not exclude AnyDB merely because those tools can perform part of a DTC/B2B
  workflow; AnyDB is preferred when Kaizen needs the operating-control layer.

---

## Critical Rules

<critical_rules id="anydb-build-rules" priority="must-follow">

### Schema Accuracy
- **ALWAYS load `reference/kaizen-anydb-patterns.md` first and state it explicitly:**
  "Loaded: kaizen-anydb-build.md + kaizen-anydb-patterns.md".
- **ALWAYS use AnyDB's actual cell type names from the patterns file.** Do not invent "Rollup",
  "Auto-number", "Link", "string", or "Multi-select".
- **ALWAYS specify cell creation order within each Type.** Base typed cells first, then
  Reference cells, then Lookup cells and typed formulas that depend on them, then aggregation
  formulas that depend on attached child Types and child cells.
- **ALWAYS specify Type creation order.** Independent Types first (no outbound References),
  then parent Types, then child Types that Attach into those parents. A Reference cell pointing
  to a nonexistent Type will error.
- **ALWAYS document connection directionality.** `Reference TO [Target Type]` means this record
  points to reusable master data. `Attach child Type [Child] UNDER [Parent]` means structural
  one-to-many and enables aggregation.
- **NEVER create a Lookup cell before its referenced Reference cell exists.**
- **NEVER create an aggregation formula before the attached child Type and referenced child
  cell exist.**
- **NEVER create a Formula cell that references cells not yet created.**

### Seed Data
- **Seed data must be realistic and operationally useful.** Not "Vendor 1, Vendor 2" but
  actual vendor names appropriate to the client's industry.
- **Seed data CSV headers must exactly match the field names in the schema.** Any mismatch
  causes import failure.
- **Include enough seed records to be useful from day one.** Reference tables should have
  5-20 records. Transaction tables start empty (they are populated by operations).

### Automations
- **Every automation must specify: trigger type, trigger event, condition (if any), and
  action(s).** An automation without all four elements is not buildable.
- **Automations that depend on specific field values must reference exact field names and
  option values as defined in the schema.**
- **Cross-object automations must be created AFTER all referenced objects exist.**

### Voice
- No filler, no forbidden phrases. Apply voice rules from your foundational knowledge.
- Never call AnyDB a "database" in client-facing output. Use "the ops system", "the system",
  or reference the specific object name.
</critical_rules>

---

## AnyDB Cell Type & Formula Reference

The full type catalog, formula syntax, cell format conventions, connection and aggregation
rules, canonical KaizenCommerce formulas, validation rules, common failures, and vocabulary
discipline live in `reference/kaizen-anydb-patterns.md`.

Load that file before configuring any cell, formula, Lookup, Reference, or Attach relationship.
This skill assumes the 8-section patterns file is loaded:
1. Cell Type Catalog
2. Formula Syntax Reference
3. Cell Format Conventions
4. Connection & Aggregation Rules
5. Canonical KaizenCommerce Formula Patterns
6. Validation Rules
7. Common Failures
8. Vocabulary Discipline

State the load explicitly: "Loaded: kaizen-anydb-build.md + kaizen-anydb-patterns.md".

---

## Mode 1: Full Build Package

### Step 1: Parse the Architecture Spec

Read the AnyDB spec from kaizen-architect. Extract:
- All objects and their fields
- All relationships (Reference and Attach declarations)
- All automations
- All portal requirements
- All views/reports

### Step 2: Determine Build Order

```
BUILD ORDER
================================================================

PHASE 1: Independent Types (no outbound Reference cells)
  Create these Types first. They are referenced by other Types
  but do not reference any records themselves.

  Typical independent objects:
    - Locations (store/warehouse records)
    - Vendors / Suppliers
    - Staff / Users
    - Categories / Product Types
    - Units of Measure

PHASE 2: Parent Transaction Types (Reference Phase 1 Types)
  These Types have Reference cells pointing to Phase 1 Types.

  Typical:
    - Purchase Orders (links to Vendor, Location)
    - Inventory Adjustments (links to Location)
    - Transfer Requests (links to Source Location, Destination Location)

PHASE 3: Attached Child / Line-Item Types
  These child Types Attach under Phase 2 parent Types.

  Typical:
    - PO Line Items (links to Purchase Order, Product)
    - Transfer Line Items (links to Transfer Request)
    - Adjustment Line Items (links to Inventory Adjustment)

PHASE 4: Computed Cells
  After all Types, Reference cells, and child Types exist, add:
    - Lookup cells (pull data from referenced records)
    - Typed aggregation formulas over attached children
    - Other formulas that calculate from cells in the current record

PHASE 5: Automations
  After all objects, fields, and relationships exist, create:
    - Record-level automations (status changes, notifications)
    - Cross-object automations (create child records, update linked records)
    - Scheduled automations (daily reports, overdue alerts)

PHASE 6: Views and Portals
  After automations are configured, create:
    - Operational views (filtered, sorted lists for daily use)
    - Dashboard views (aggregated data for management)
    - External portals (vendor access, warehouse staff access)
================================================================
```

### Step 3: Generate Object Definitions

For each object, produce a complete build specification:

```
================================================================
TYPE: [Type Name]
================================================================
Purpose:     [One sentence — what this represents operationally]
Phase:       [1 / 2 / 3] (from build order)
References:  [Target Types referenced via Reference cells]
Attached children: [Child Types attached under this Type]
Used in:     [Workflows that depend on this object]

CELLS (create in this exact order):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   Cell Name               Type            Configuration
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1   [name]                  General         Formula: =CONCAT("PO-", TEXT(SEQNUM("po"), "0000"))
2   [name]                  General         Max length: [n] (if relevant)
3   [name]                  Select          Options:
                                              - "Option A"
                                              - "Option B"
                                              - "Option C"
4   [name]                  Currency        Format: USD, 2 decimals
5   [name]                  Date            Default: Today (if applicable)
6   [name]                  Reference       Target Type: [Type Name]
                                            Cardinality: one-to-one
7   [name]                  Checkbox        Default: unchecked
8   [name]                  Rich Text       Rich text: enabled
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE 4 CELLS (add AFTER all dependent Types and cells exist):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9   [name]                  Lookup          Via Reference: [Reference cell name]
                                            Source cell: [cell in referenced Type]
10  [name]                  Currency        Formula: =SUM(C@CURRREC!A1)
                                            Child Type: [attached child Type]
11  [name]                  Percentage      Formula: =IF({{Status}} == "Received",
                                              {{Quantity Received}} / {{Quantity Ordered}},
                                              0)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

VIEWS:
  1. "[View Name]"
     Purpose: [what this view is for]
     Filter: [field] [operator] [value]
     Sort: [field], [asc/desc]
     Columns: [field1], [field2], [field3], ...
     Group by: [field] (if applicable)

  2. "[View Name]"
     Purpose: [purpose]
     Filter: [criteria]
     Sort: [field], [asc/desc]
     Columns: [list]
================================================================
```

### Step 4: Generate Seed Data

For each reference/independent object, produce a CSV ready to import:

```
================================================================
SEED DATA: [Object Name]
================================================================
Records: [n]
Purpose: Pre-populate [object] so transaction objects can reference them
Import: Copy CSV below, save as [object-name]-seed.csv, import into AnyDB

--- CSV START ---
[Field1],[Field2],[Field3],[Field4]
[value],[value],[value],[value]
[value],[value],[value],[value]
...
--- CSV END ---

After import, verify:
  - [n] records visible in [Object Name] table
  - All Select cell values display correctly
  - Reference cells (if any) correctly point to target records
================================================================
```

Common seed data tables:

**Locations:**
```csv
Location Name,Type,Address,City,Province,Country,Phone,Manager,Active
Main Warehouse,Warehouse,123 Industrial Pkwy,Toronto,ON,Canada,416-555-0100,Sarah Chen,true
Downtown Store,Retail,456 Queen St W,Toronto,ON,Canada,416-555-0200,Mike Johnson,true
Yorkville Boutique,Retail,789 Bloor St W,Toronto,ON,Canada,416-555-0300,Lisa Park,true
```

**Vendors:**
```csv
Vendor Name,Contact Name,Email,Phone,Payment Terms,Lead Time (Days),Currency,Status
[Industry-appropriate vendor 1],[name],[email],[phone],Net 30,14,USD,Active
[Industry-appropriate vendor 2],[name],[email],[phone],Net 45,21,USD,Active
```

### Step 5: Generate Automation Configurations

**Note:** Some triggers may require Zapier/Make integration rather than native AnyDB configuration. Verify native trigger availability in your AnyDB instance. The anydb-com MCP server has current automation documentation.

For each automation from the architecture spec:

```
================================================================
AUTOMATION: [Automation Name]
================================================================
Workflow area: [Purchasing / Inventory / Notifications / Reporting / etc.]
Object:        [Which object this automation is attached to]
Create after:  [Phase 5 — after all objects and fields exist]

TRIGGER:
  Type:        [Record created / Field changed / Date reached / Form submitted]
  Event:       [Specific event — e.g., "When Status field changes"]
  Value:       [Specific value if applicable — e.g., "changes to 'Approved'"]

CONDITION (if applicable):
  Field:       [field name]
  Operator:    [equals / greater than / contains / is not empty / etc.]
  Value:       [value]

ACTIONS (execute in order):
  1. [Action type]: [Specific configuration]
     - [Detail 1]
     - [Detail 2]

  2. [Action type]: [Specific configuration]
     - [Detail 1]

PURPOSE: [One sentence — what this replaces or prevents]

TEST:
  To verify: [Create/modify a record that matches the trigger conditions]
  Expected: [What should happen — field updates, notifications sent, records created]
================================================================
```

**Common AnyDB automation action types:**
- **Update field** — Change a field value on the triggering record or a linked record
- **Create record** — Create a new record in another object
- **Send email** — Send notification email to a specified address or field value
- **Send webhook** — POST data to an external URL (Shopify Flow, Slack, etc.)
- **Lock record** — Prevent edits after a status change [VERIFY — may not be native]
- **Set date** — Set a date field to today or a calculated date

### Step 6: Generate Portal Configuration

For each portal requirement:

```
================================================================
PORTAL: [Portal Name]
================================================================
Users:           [Who accesses this — vendors, warehouse staff, franchise partners]
Authentication:  [Email invitation / password / SSO]

VISIBLE OBJECTS:
  Object: [name]
    View: [which view they see — filtered to their records]
    Can create: [yes/no]
    Can edit: [yes/no — which fields]
    Can delete: [no — almost always no for portal users]
    Hidden fields: [fields they cannot see — e.g., cost, margin, internal notes]

  Object: [name]
    View: [view name]
    Can create: [yes/no]
    Can edit: [yes/no]
    Hidden fields: [list]

FORMS:
  Form: "[Form Name]"
    Purpose: [what portal users submit via this form]
    Fields:
      - [field]: [required/optional]
      - [field]: [required/optional]
      - [field]: [pre-filled with portal user's linked record]
    On submit: [What happens — creates record, triggers automation, etc.]

ACCESS RULES:
  - Portal users can ONLY see records linked to their vendor/location/organization
  - Portal users CANNOT see other portal users' records
  - Portal users CANNOT access internal objects ([list])
  - Portal users CANNOT export data (if applicable)
================================================================
```

---

## Mode 2: Schema Only

Produce Step 2 (build order) and Step 3 (object definitions) from Mode 1. Skip seed data,
automations, and portals. Useful when the team wants to review the schema before committing
to a full build.

---

## Mode 3: Seed Data Only

Produce Step 4 (seed data CSVs) from Mode 1 for all reference tables. Requires:
- Object names and field definitions (from schema or spec)
- Client industry (for realistic data)
- Location names (from client)
- Vendor names (from client or generate realistic examples)

---

## Mode 4: Automation Config

Produce Step 5 (automation configurations) from Mode 1. Requires:
- All objects and fields to be defined (reference the schema)
- Business logic from the architecture spec

---

## Mode 5: Portal Config

Produce Step 6 (portal configuration) from Mode 1. Requires:
- Portal user types from the architecture spec
- Objects and fields they need access to
- Forms they need to submit

---

## Common Retail AnyDB Patterns

### Purchase Order System

```
Objects: Vendors → Purchase Orders → PO Line Items
Automations:
  - PO created → auto-set Status to "Draft", set Created Date to today
  - PO Status changes to "Approved" → send email to Vendor (via Vendor.Email)
  - PO Line Item Quantity Received updated → recalculate PO Fulfillment %
  - PO Fulfillment % reaches 100% → change PO Status to "Fully Received"
  - PO Expected Date < Today AND Status != "Received" → flag as "Overdue"
```

### Inventory Adjustment Tracking

```
Objects: Locations → Inventory Adjustments → Adjustment Line Items
Automations:
  - Adjustment created → auto-set Status to "Pending Review"
  - Adjustment value > $500 → require Manager Approval (Status = "Needs Approval")
  - Adjustment approved → update Shopify inventory via webhook
  - Adjustment approved → lock record (prevent edits)
```

### Transfer Request System

```
Objects: Locations → Transfer Requests → Transfer Line Items
Automations:
  - Transfer created → notify destination location manager via email
  - Transfer Status changes to "Shipped" → set Shipped Date to today
  - Transfer Status changes to "Received" → update inventory at both locations
  - Transfer not received within 48h of shipment → flag as "Overdue"
```

### Vendor Scorecard

```
Type: Vendors (with aggregation formulas from attached purchasing records)
Aggregation formulas:
  - Total POs (`=COUNT(C@CURRREC!A1)`)
  - Total Spend (`=SUM(C@CURRREC!A2)`)
  - Avg Lead Time (`=MEAN(C@CURRREC!A3)`)
  - On-Time Rate (formula from on-time POs / total POs)
  - Open PO Value (`=SUMIFS(C@CURRREC!A2, C@CURRREC!A4, "Open")`)
```

---

## Handoff Format

### Receiving Handoff

**From kaizen-architect Mode 1:** Accept the full AnyDB spec — objects, fields, relationships,
automations, portals. Parse and produce the build package.

**From kaizen-generate Mode 2:** This skill supersedes kaizen-generate Mode 2 for production
AnyDB builds. kaizen-generate handles lightweight schema output. This skill handles the full
build with seed data, automations, and portals.

**Direct invocation:** User describes what they need in AnyDB. Build from requirements.

### Producing Handoff

```
---
## HANDOFF → Next Step

**What was produced:** [Full build package / Schema only / Seed data / Automations / Portal config]
**Client:** [name]
**Objects defined:** [count]
**Seed data tables:** [count] tables, [total records] records
**Automations configured:** [count]
**Portals specified:** [count]

**Build order:**
  Phase 1: [objects] — independent tables
  Phase 2: [objects] — transaction tables
  Phase 3: [objects] — line item tables
  Phase 4: Computed cells ([count] lookups, [count] aggregation formulas, [count] other formulas)
  Phase 5: Automations ([count])
  Phase 6: Views and portals

**Requires client input:**
  - [Any items needing confirmation — vendor names, location names, approval thresholds]

**Next pipeline step:**
- Build in AnyDB following the phase sequence
- Import seed data after Phase 1 objects exist
- Configure automations after all objects and fields exist
- Test each automation with sample records
- Run kaizen-anydb-audit to verify the build matches the spec
```

---

## Verification Checklist

<verification id="anydb-build-verify">
Before finalizing any output:

1. **Patterns file loaded:** Was `reference/kaizen-anydb-patterns.md` loaded and explicitly stated before build instructions were generated?
2. **Cell type accuracy:** Every cell uses an actual AnyDB type from the patterns file?
3. **Build order specified:** Types listed in dependency order? No Reference to a nonexistent Type?
4. **Cell creation order:** Within each Type, base cells before References, References before Lookups, dependent formulas after their source cells exist?
5. **Connection directionality:** Reference TO target Type vs Attach child UNDER parent clearly documented with cardinality?
6. **Select options:** All options listed for every Select cell, or dynamic options explicitly declared?
7. **Formula syntax:** All formulas use correct AnyDB syntax from the patterns file, including `=` prefix and `==` for equality?
8. **Aggregation configuration:** Every aggregation formula declares typed output, attached child Type, and `C@CURRREC!CellID`-style child references?
9. **Lookup configuration:** Reference cell and source cell specified for every Lookup?
10. **Seed data headers match schema:** CSV column names exactly match cell names in Type definitions?
11. **Seed data is realistic:** No "Test Vendor 1" placeholder data?
12. **Automation completeness:** Every automation has trigger type, event, condition (if any), and actions?
13. **Portal access rules:** Explicit about what portal users CAN and CANNOT see/do?
14. **Cross-object dependencies:** Automations created after all referenced objects exist?
15. **Vocabulary discipline:** No prohibited vocabulary such as "Rollup" as a cell type, "Auto-number" as a cell type, "Link", "dropdown", "string", or "foreign key" unless explicitly called out as a mistake to avoid?
16. **Voice check:** No "database" synonym, no filler, no forbidden phrases?
</verification>

---

## Common Failures

See also `reference/kaizen-anydb-patterns.md` Section 7 for the canonical spec-side
failure list. The items below are the build-execution version of those failures.

**1. Creating a Lookup before its Reference cell exists.**
A Lookup that pulls Vendor Payment Terms requires the Reference cell to Vendors to exist first.
Always create base cells and References in Phases 1-3, then add Lookups and formulas in Phase 4.

**2. Seed data with mismatched column headers.**
If the schema defines a field as "Vendor Name" but the seed CSV header says "Name", the
import will either fail or create a new column. Headers must match field names exactly.

**3. Formula referencing a cell by the wrong name.**
`{{Quantity}}` and `{{Qty}}` are different cells. Always use the exact cell name as defined
in the schema. Copy-paste from the cell definition, do not retype.

**4. Automations with incomplete action specifications.**
"Send email to vendor" is not buildable. "Send email to {{Vendor Email}} with subject
'PO {{PO Number}} Approved' and body template [X]" is buildable. Every action needs all
configuration details.

**5. Portal config without explicit field hiding.**
If a portal user should not see cost or margin data, those fields must be listed as hidden.
"Show only relevant fields" is vague. "Hide: Unit Cost, Margin %, Internal Notes, Vendor
Payment Terms" is explicit.

**6. Not specifying Select cell options at creation time.**
Select cells must have their option list defined when the cell is created. Adding options
later is possible but harder to coordinate. Define all known options upfront.

---

## ABORT_CLEANUP / Created Resource Ledger

Any AnyDB build that creates or edits Types, Cells, Views, Dashboards, Automations, Portals,
Permissions, Seed records, sync config, import files, or client-visible artifacts must maintain a
Created Resource Ledger.

Ledger fields:

- resource type: Type, Cell, View, Dashboard, Automation, Portal, Permission, Seed record, Sync config, file, or report
- exact resource name and AnyDB identifier if available
- parent Type or dependency
- creation step and source spec section
- downstream dependency
- rollback or cleanup action
- owner, timestamp, and status

`ABORT_CLEANUP` is mandatory when the build stops after creating resources. The abort note must
list created objects in dependency order, identify safe delete order, preserve evidence needed for
audit, and flag any client-visible artifact that should not be used.

## Automation Governance Verdicts

Use `reference/kaizen-automation-governance.md` for every AnyDB automation before build. Each
automation gets one verdict: `APPROVE`, `APPROVE AS PILOT`, `PARTIAL AUTOMATION ONLY`, `DEFER`, or
`REJECT`.

Do not build an automation unless the source of truth, owner, fallback path, logging field or run
view, error handling, test record, and re-audit trigger are known. When these are missing, mark the
automation `DEFER` or `PARTIAL AUTOMATION ONLY` instead of filling gaps with assumptions.

## Workflow Registry Build Gate

For multi-workflow AnyDB builds, require the architecture handoff to include the 4-view workflow
registry from `kaizen-architect.md` before creating Types or Cells:

- By Workflow
- By Component
- By User Journey
- By State

If the registry is missing, produce it from the available spec and mark uncertain entries as
`Review` or `Missing`. Do not silently turn an undocumented workflow into schema. A `Missing`
registry item is a build risk that must be fixed, scoped out, or deferred in writing.

When an AnyDB automation crosses a system boundary, include the handoff contract:

```text
HANDOFF: [From] -> [To]
PAYLOAD: { field: type, description }
SUCCESS RESPONSE: { field: type }
FAILURE RESPONSE: { error: string, code: string, retryable: bool }
TIMEOUT: [duration] -> treated as FAILURE
ON FAILURE: [recovery action]
```
