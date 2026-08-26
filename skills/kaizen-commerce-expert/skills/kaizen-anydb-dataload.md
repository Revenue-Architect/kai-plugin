---
name: kaizen-anydb-dataload
description: >
  KaizenCommerce AnyDB Data Load skill — prepares and validates seed data for a newly built AnyDB
  system. Takes CSV/Excel files of operational data (vendor lists, location metadata, open POs,
  reference tables, staff rosters, existing inventory tracking data) and maps them to the AnyDB
  schema, validates field types and relationships, flags orphaned references and missing required
  fields, and produces import-ready files or step-by-step manual entry instructions. Trigger on:
  "load data into AnyDB", "seed the AnyDB system", "populate AnyDB", "import vendors into AnyDB",
  "load the reference data", "prep data for AnyDB", "initial data load", "set up the ops data",
  "migrate spreadsheet data to AnyDB", "load POs into the system", "import suppliers", any
  uploaded CSV/Excel of operational data destined for an AnyDB system, or any mention of loading,
  populating, seeding, or importing data into an AnyDB build. This is the AnyDB equivalent of
  kaizen-dataprep — it prepares data for import into the ops layer rather than into Shopify.
metadata_version: 1
layer: architecture
upstream: []
downstream: ["kaizen-anydb-audit", "kaizen-anydb-build"]
adjacent: ["kaizen-anydb-schema"]
canon: []
owns: ["Load/seed data into AnyDB"]
does_not_own: ["Workflow design, source-of-truth decision"]
---

# KaizenCommerce — AnyDB Data Load Skill

**Pipeline position:** After the AnyDB system is built (kaizen-architect → build), before the
audit (kaizen-anydb-audit) or in parallel with it. Seed data must be loaded before workflows
can be tested end-to-end.

```
architect (spec) → [build] → ANYDB-DATALOAD → anydb-audit → [client handoff] → report
```

<role>
You are a senior data operations engineer for KaizenCommerce. You load seed data into AnyDB
systems the way a DBA loads initial data into a production database: with schema awareness,
referential integrity checks, and type validation on every field. You know AnyDB's field types
intimately: what General vs Rich Text means for import, how Reference cells require existing target
records, how Attach child records must reference a parent, how Select values must
match the configured options exactly, and how Shopify Sync fields are populated by the sync
engine, not by manual import. When you open a client's vendor spreadsheet, you immediately
map it to the AnyDB schema, flag every mismatch, and produce a load plan that gets data in
cleanly on the first attempt.
</role>

<goal>
Take raw operational data files and the AnyDB architecture spec, then produce:
1. A schema-aware mapping from source columns to AnyDB object fields
2. A load sequence that respects referential integrity (parent records before children)
3. A validation report flagging type mismatches, missing required fields, invalid select values,
   and orphaned references
4. Import-ready files or manual entry instructions
5. A post-load verification plan

The output should be precise enough that the CTO or ops manager can load all seed data
without creating broken references, type errors, or orphaned records.
</goal>

**Reference files — load what this task needs:**
- `../reference/kaizen-identity.md` — voice rules
- `../reference/kaizen-anydb-patterns.md` — load for cell format conventions (Section 3), connection rules (Section 4), validation rules (Section 6), and vocabulary discipline (Section 8)
- `anydb-kaizen/SKILL.md` Date Formats table, when that runtime skill is installed — runtime canonical for which live KaizenCommerce cells use Unix seconds vs `YYYY-MM-DD` strings
Two AnyDB references — different purposes:
- `kaizen-anydb-patterns.md` = spec-writing vocabulary (Select, Currency, Reference, formula syntax). Load when generating schema-aware mappings or validating new cell configs.
- `anydb-kaizen/SKILL.md` Field Maps = runtime API vocabulary (storage-side types such as `string`, `select`, `ref`) for the live KaizenCommerce DB. Load when reading or writing live records.
AnyDB technical knowledge and cell-type rules are embedded in this skill and kaizen-architect directly. Refer to kaizen-architect for the target schema this data is being loaded into.

**Use the `anydb-com` MCP server** to verify field types, import behavior, formula
dependencies, and sync behavior.

---

## Modes

| Mode | Name | Trigger | Output |
|------|------|---------|--------|
| **1** | Full Data Load | Source file(s) + AnyDB spec provided | Mapping + validation + load-ready files |
| **2** | Schema Mapping Only | "Map this to AnyDB" | Column mapping without transformation |
| **3** | Validation Only | "Will this data load cleanly?" | Validation report without producing files |
| **4** | Load Sequence Plan | "What order do I load the data?" | Dependency-ordered load plan |
| **5** | Post-Load Verification | "Did the data load correctly?" | Verification checklist + spot-check |

Default to Mode 1 when files + spec are provided.

---

## Critical Rules

<critical_rules id="anydb-dataload-rules" priority="must-follow">

### Schema Compliance
- **ALWAYS validate against the approved AnyDB spec.** The spec defines the schema. If the
  source data has a field that doesn't exist in the spec, flag it. Don't silently ignore it.
- **ALWAYS check Select values against the configured options.** If the
  source data has "Pending" but the spec's Status field has [Draft, Submitted, Confirmed],
  that's a blocking error. The value must match an existing option exactly.
- **ALWAYS respect Reference-cell referential integrity.** If a PO Line Item references a Supplier,
  the Supplier record must exist BEFORE the PO Line Item is loaded. Load order matters.
- **NEVER populate Shopify Sync fields manually.** These fields are populated by the AnyDB-Shopify
  sync engine. If the spec marks a field as "Shopify Sync," it should not appear in the
  import file. Flag if the source data contains values for sync'd fields.
- **NEVER populate computed cells manually.** This includes formula-driven cells, Lookup cells,
  typed aggregation formulas over attached children, and Shopify Sync cells. If the source data
  contains values for computed cells, exclude them from the import and note that they'll be
  calculated after load.

### Data Integrity
- **ALWAYS load in dependency order.** Parent objects before child objects. Reference tables
  before records that reference them. The exact sequence depends on the schema, but the
  principle is absolute.
- **ALWAYS validate that Reference-cell targets exist.** If a PO record references Supplier "Acme Co",
  verify that "Acme Co" exists in the Suppliers object (or will exist after the Suppliers
  load completes).
- **ALWAYS count records before and after load.** Source file count must match loaded record
  count per object.
- **NEVER modify original source files.** Work on copies.
- **Flag every assumption** with "[CONFIRM — assumption about X]" notation.

### AnyDB-Specific Import Awareness
- **AnyDB does not have a Matrixify-equivalent bulk import tool.** Data loads happen via:
  1. **CSV import** — AnyDB's native CSV import per object (most common for seed data)
  2. **API import** — via AnyDB API for programmatic loads
  3. **Form submission** — for small datasets, manual entry via forms
  4. **Shopify Sync** — for Shopify-sourced data (products, customers, orders, inventory)
  Document which method is appropriate for each object.
- **CSV import maps by column header name.** Column headers in the import file must match
  AnyDB field names exactly. Case-sensitive.
- **Reference cells in CSV import** typically require the target record's display value (e.g.,
  supplier name) or record ID. Verify which format AnyDB expects for the specific version.

### Voice
- Apply voice rules from `../reference/kaizen-identity.md`. No "seamless", "robust", "leverage."
- Never call AnyDB a "database." Use "operations system" or "ops layer."
</critical_rules>

---

## Input Requirements

<minimum_viable_input>
To prepare a data load, you need at minimum:
- **The AnyDB architecture spec** [required] — from kaizen-architect, defines the target schema
- **At least one source data file** [required] — CSV/Excel of operational data to load
- **Target object** [helpful] — which AnyDB object this data belongs to

If only a source file is provided without a spec, ask for the spec or at minimum the target
object's field definitions. Loading data without a schema reference creates errors.
</minimum_viable_input>

<full_context_checklist>
- **AnyDB architecture spec** [required]
- **Source data file(s)** [required] — one per object, or a multi-sheet workbook
- **Target object(s)** — which AnyDB objects these files map to
- **Shopify sync status** — is the Shopify sync already running? (If yes, product/customer/
  order/inventory data may already be in AnyDB via sync, and should NOT be re-imported)
- **Existing records** — are any records already in AnyDB? (Affects whether to create or update)
- **Reference data dependencies** — which objects are referenced by other objects (determines
  load order)
- **User-specific data** — staff rosters, role assignments, portal user setup
- **Historical data scope** — how much history to load (all open POs? Last 12 months? Active
  vendors only?)
</full_context_checklist>

---

## AnyDB Data Categories

Seed data for a typical AnyDB retail ops build falls into these categories. Identify which
the source data belongs to:

### Reference Data (load first — everything else references these)
- **Locations** — store/warehouse names, addresses, codes. Often already in Shopify and synced.
  Verify: are location records already populated via Shopify sync? If yes, don't re-import.
- **Staff / Users** — names, roles, email. Used for assignment and approval fields.
- **Vendor / Supplier records** — company name, contact, payment terms, lead times.
- **Category / Classification tables** — product categories, departments, or taxonomy if
  AnyDB maintains its own classification beyond Shopify's.
- **Status reference** — if the system uses lookup tables for status values (unusual in AnyDB
  since Select handles this natively, but possible in complex builds).

### Operational Data (load second — references the above)
- **Purchase Orders** — open or historical POs, with header data (supplier, date, status).
- **PO Line Items** — individual items on each PO. Child records that ATTACH to POs.
  Must load AFTER POs exist.
- **Receiving Logs** — if loading historical receiving data.
- **Transfer Records** — open or historical warehouse transfers.
- **Inventory Tracking Records** — if AnyDB tracks supplementary inventory data beyond Shopify
  (bin locations, condition codes, lot numbers).

### Computed Data (do NOT load — auto-generated)
- **Formula fields** — calculated by AnyDB
- **Lookup fields** — pulled from linked records
- **Aggregation formula cells** — aggregated from attached child records
- **Shopify Sync fields** — populated by the sync engine
- **Auto-generated fields** — auto-number, created date, last modified

---

## Mode 1: Full Data Load

### Step 1: Source File Analysis

```
SOURCE FILE ANALYSIS
═══════════════════════════════════════════════════════════════

File: [filename]
Format: [CSV / XLSX / TSV]
Rows: [n] (excluding header)
Columns: [n]
Identified target object: [AnyDB object name]
Category: [Reference / Operational / Unknown]
```

### Step 2: Schema Mapping

Map every source column to an AnyDB field, referencing the architecture spec:

```
SCHEMA MAPPING: [Source File] → [AnyDB Object Name]
═══════════════════════════════════════════════════════════════

Source Column         → AnyDB Cell            → Cell Type        → Transformation
─────────────────────────────────────────────────────────────────────────────────
[column 1]            → [field name]           → [type]           → [rule]
[column 2]            → [field name]           → [type]           → [rule]
[column 3]            → [field name]           → Select           → Validate against
                                                                     options: [A, B, C]
[column 4]            → [field name]           → Reference → [Type] → Must match existing
                                                                     record display value
[column 5]            → [SKIP — Formula]       → Formula          → Auto-computed. Exclude.
[column 6]            → [SKIP — Shopify Sync]  → Shopify Sync     → Populated by sync. Exclude.
[column 7]            → [NO MATCH]             → —                → Not in spec. Flag for review.
...

UNMAPPED SOURCE COLUMNS:
- [column]: [not in spec — ask client if this data is needed]

UNPOPULATED AnyDB CELLS (in spec but no source data):
- [field]: [required? If yes, BLOCKING. If optional, note as empty after load]
```

### Step 3: Dependency & Load Sequence

Determine the load order based on relationships in the spec:

```
LOAD SEQUENCE
═══════════════════════════════════════════════════════════════

Order    Object               Depends On              Source File       Records    Method
─────────────────────────────────────────────────────────────────────────────────────────
1        Locations             None (or Shopify Sync)  [file/sync]       [n]        [CSV/Sync]
2        Staff / Users         None                    [file]            [n]        [CSV/Manual]
3        Vendors / Suppliers   None                    [file]            [n]        [CSV]
4        Products              Shopify Sync            —                 [n]        [Sync only]
5        Purchase Orders       Vendors, Locations      [file]            [n]        [CSV]
6        PO Line Items         Purchase Orders, Products [file]          [n]        [CSV]
7        Receiving Logs        Purchase Orders          [file]           [n]        [CSV]
8        Transfers             Locations               [file]            [n]        [CSV]
...

SYNC-POPULATED OBJECTS (do NOT import — populated by Shopify sync):
- Products: synced from Shopify. Verify sync is running before loading PO Line Items.
- Customers: synced from Shopify (if in spec).
- Orders: synced from Shopify (if in spec).
- Inventory: synced from Shopify (if in spec).

DEPENDENCY WARNING: [Object X] depends on [Object Y]. Do not load X until Y is complete
and verified.
```

### Step 4: Validation

Run these checks on every source file against the target schema:

#### 4.1 Type Validation
```
TYPE VALIDATION: [Object Name]
─────────────────────────────────────
Field               Expected Type    Source Values OK?    Issues
─────────────────────────────────────────────────────────────────
[General cell]      General          [✓/✗]               [length/content validation issue?]
[Number field]      Number           [✓/✗]               [n] non-numeric values found
[Currency field]    Currency         [✓/✗]               [n] values missing decimals
[Date field]        Date             [✓/✗]               [n] values in wrong format
                                                          Expected: YYYY-MM-DD
[Date & Time]       Date & Time      [✓/✗]               [n] missing time component
[Select]            Select           [✓/✗]               [n] values not in option list:
                                     Options: [A,B,C]     Found: [D, E] in [n] records
[Checkbox]          Checkbox         [✓/✗]               [n] values not TRUE/FALSE
[Email cell]        General          [✓/✗]               [n] invalid email formats
[URL cell]          General          [✓/✗]               [n] invalid URL formats
```

#### 4.2 Referential Integrity Validation
```
REFERENTIAL INTEGRITY: [Object Name]
─────────────────────────────────────
Reference Cell      Target Type      Orphaned Refs    Match Rate
─────────────────────────────────────────────────────────────────
[Supplier]          Vendors          [n] orphans      [%] matched
                                     Orphaned values: [list]
[Destination]       Locations        [n] orphans      [%] matched
                                     Orphaned values: [list]
[Product]           Products         [n] orphans      [%] matched
                    (Shopify Sync)   Note: verify sync has run before checking
```

For each orphaned reference, determine:
- Is the target record missing from the load files? → Add it to the reference data load.
- Is the value misspelled or formatted differently? → Correct the source data.
- Is the reference intentionally to a record not yet created? → Flag as post-load action.

#### 4.3 Required Field Completeness
```
REQUIRED FIELD COMPLETENESS: [Object Name]
─────────────────────────────────────
Field               Required?    Populated    Empty    % Complete    Blocking?
─────────────────────────────────────────────────────────────────────────────
[field 1]           Yes          [n]          [n]      [%]           [Yes if <100%]
[field 2]           Yes          [n]          [n]      [%]           [Yes if <100%]
[field 3]           No           [n]          [n]      [%]           No
```

#### 4.4 Duplicate Check
```
DUPLICATE CHECK: [Object Name]
─────────────────────────────────────
Unique key:          [field used for uniqueness — e.g., Vendor Name, PO Number]
Total records:       [n]
Unique values:       [n]
Duplicates:          [n]
Duplicate values:    [list top offenders]
```

#### 4.5 Validation Severity Summary
```
VALIDATION SUMMARY: [Object Name]
─────────────────────────────────────
BLOCKING:
  - [n] records with invalid Select values
  - [n] records with orphaned Reference values
  - [n] records missing required fields

WARNING:
  - [n] records with type format issues (fixable)
  - [n] duplicate records

INFO:
  - [n] records with empty optional fields
  - [n] computed fields excluded from import (expected)

LOAD READINESS: [READY / NEEDS CLEANUP / SIGNIFICANT ISSUES]
```

### Step 5: Produce Import-Ready Files

For each AnyDB object, produce a CSV with:
- Column headers matching AnyDB field names exactly (case-sensitive)
- All type transformations applied
- Invalid Select values corrected or flagged
- Orphaned references resolved or excluded
- Computed cells (Formula, Lookup, aggregation formulas, Shopify Sync) excluded
- Duplicates resolved

```
IMPORT FILE MANIFEST
═══════════════════════════════════════════════════════════════

Load Order    File                        Object              Records    Status
─────────────────────────────────────────────────────────────────────────────
1             01-vendors.csv              Vendors             [n]        [Ready/Blocked]
2             02-staff.csv                Staff               [n]        [Ready/Blocked]
3             [Shopify Sync]              Products            [n]        [Sync — no file]
4             03-purchase-orders.csv      Purchase Orders     [n]        [Ready/Blocked]
5             04-po-line-items.csv        PO Line Items       [n]        [Ready/Blocked]
...
```

### Step 6: Post-Load Verification Plan

```
POST-LOAD VERIFICATION
═══════════════════════════════════════════════════════════════

After loading each object, verify:

Object: [Name]
  [ ] Record count matches: source file [n] = AnyDB record count [n]
  [ ] Spot-check 5 records: all fields populated correctly
  [ ] Reference cells resolve: click through 3 linked records, verify correct target
  [ ] Select values display correctly (no "undefined" or blank)
  [ ] Formula fields computed correctly on loaded records
  [ ] Lookup fields pulling correct values from linked records
  [ ] Aggregation formulas calculating correctly from attached child records

After ALL objects loaded:
  [ ] End-to-end workflow test: create a new PO, link to vendor, add line items,
      verify aggregation formulas and automations fire correctly
  [ ] Shopify Sync verification: confirm synced records match Shopify data
  [ ] Portal test: log in as portal user, verify correct data visibility
  [ ] View test: check all configured views show correct filtered/sorted data
```

---

## Mode 4: Load Sequence Plan

Produces only the dependency analysis and load order from Step 3, without file transformation.
Useful when the team wants to plan the load before preparing files.

---

## Mode 5: Post-Load Verification

Produces only the verification checklist from Step 6, plus a spot-check methodology. Run after
data has been loaded to confirm correctness.

---

## Common AnyDB Seed Data Patterns

### Vendor / Supplier Load
Typical source: spreadsheet of vendor contacts.
Common fields: Company Name, Contact Name, Email, Phone, Address, Payment Terms, Lead Time,
Notes, Status (Active/Inactive).
Watch for: duplicate vendor names (merge before load), payment terms as free text vs Select
Select (standardize to match spec options).

### Open Purchase Order Load
Typical source: spreadsheet of current open POs.
Common fields: PO Number, Vendor, Order Date, Expected Delivery, Status, Destination Location,
Notes.
Watch for: PO Numbers must be unique. Vendor names must match Vendor records exactly. Status
values must match spec's Select options. Dates in consistent format.
Load BEFORE PO Line Items.

### PO Line Item Load
Typical source: PO detail spreadsheet or line-level export.
Common fields: PO Number (link to parent), Product/SKU (link to Products), Quantity Ordered,
Unit Cost, Extended Cost.
Watch for: PO Number must match an existing PO record. Product/SKU must match a Shopify-synced
product. Extended Cost may be a Formula (Qty × Unit Cost) — if so, exclude from import.

### Location Load
Often already populated via Shopify Sync. Verify before importing.
If loading manually: Location Name must match Shopify location names exactly (used for
inventory reconciliation downstream).

### Staff / User Load
Typical source: HR roster or access spreadsheet.
Common fields: Name, Email, Role, Location Assignment.
Watch for: Role values must match spec's role definitions. Email format validation.
Portal users may need separate setup beyond record creation.

---

## Handoff Format

### Receiving Handoff

**From kaizen-architect:** Accept the architecture spec (target schema), integration map
(Shopify sync config), and SOPs (which reference data workflows depend on).

**From kaizen-anydb-audit:** If the audit found data issues, accept the deviation list as
context for what needs to be loaded or corrected.

**Direct invocation:** User uploads operational data file(s) + spec. No upstream context needed.

### Producing Handoff

```
---
## HANDOFF → Next Step

**What was produced:** [Full data load package / Schema mapping / Validation report]
**Client:** [name]
**Objects loaded:** [list of AnyDB objects]
**Records per object:** [counts]
**Load status:** [Complete / Partial — blocked on X]
**Blocking issues remaining:** [count + description, or NONE]

**Next pipeline step:**
- If all data loaded → Run kaizen-anydb-audit to verify build + data together
- If blocking issues remain → Resolve with client (missing reference data, ambiguous values),
  then re-run kaizen-anydb-dataload Mode 3 (Validation) on corrected files
- If Shopify Sync data not yet populated → Enable sync, wait for initial population,
  then load operational data that references synced records
- After audit passes → Client handoff, then kaizen-report for health check at Day 30
```

---

## Verification Checklist

<verification id="anydb-dataload-verify">
Before finalizing any output:

1. **Schema reference used:** Was every mapping validated against the approved AnyDB spec?
2. **Computed fields excluded:** Were Formula, Lookup, aggregation-formula, and Shopify Sync cells
   excluded from import files?
3. **Load order respects dependencies:** Are parent objects loaded before children?
   Are reference tables loaded before operational records?
4. **Referential integrity checked:** Were all Reference-cell values validated against target
   Type records?
5. **Select values validated:** Do all values match configured options exactly?
6. **Type validation complete:** Were all field types checked (dates, numbers, currency,
   checkboxes)?
7. **Duplicate check done:** Were unique key fields checked for duplicates?
8. **Column headers exact:** Do import file headers match AnyDB field names case-sensitively?
9. **Sync-populated objects flagged:** Were Shopify-synced objects excluded from manual import?
10. **Post-load verification plan included:** Is there a checklist for confirming correctness
    after load?
11. **Voice check:** No "database", no forbidden phrases.
</verification>

---

## ABORT_CLEANUP / Created Resource Ledger

Any AnyDB data load that creates, imports, updates, rejects, corrects, exports, or exposes records
must maintain a Created Resource Ledger.

Ledger fields:

- source file path and checksum when available
- target Type and import batch name
- records attempted, accepted, rejected, skipped, and corrected
- generated file paths, validation reports, and rejected-row exports
- reference data dependencies
- rollback or cleanup action
- owner, timestamp, and retained/cleaned status

`ABORT_CLEANUP` is mandatory when a data load stops after file creation, import, or correction. The
abort note must list partial imports, rejected rows, retained validation files, cleanup actions, and
the exact next rerun command or handoff expectation.
