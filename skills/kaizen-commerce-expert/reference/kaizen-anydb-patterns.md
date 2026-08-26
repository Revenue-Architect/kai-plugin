---
name: kaizen-anydb-patterns
description: >
  KaizenCommerce shared AnyDB reference — cell type catalog, formula syntax, cell format
  conventions, relationship and aggregation rules, canonical formula patterns, validation
  rules, common failures, and vocabulary discipline. Sourced from anydb.com docs
  (verified 2026-04-22). Load before writing any AnyDB cell, formula, reference, or
  attachment in specs, builds, audits, or data loads.
---

# KaizenCommerce — AnyDB Patterns Reference

Single source of truth for AnyDB spec-writing vocabulary. Load this file before writing
any cell, formula, reference, lookup, or attachment relationship in any kaizen-architect,
kaizen-anydb-build, kaizen-anydb-audit, or kaizen-anydb-dataload context.

**AnyDB domain model (use these words, not synonyms):**
- **Database** — top-level container; references only work within the same database.
- **Type** — schema/template that defines which cells a record has. What other systems call
  a "table" or "object definition" is a Type in AnyDB.
- **Record** — an instance of a Type. The AnyDB docs sometimes use "object" and "record"
  interchangeably for the instance.
- **Cell** — the unit of data within a record. What other systems call a "field" is a Cell
  in AnyDB. Do not say "field."

---

## Section 1: AnyDB Cell Type Catalog

These are the 15 supported cell types per anydb.com/support/user-docs/templates/cell%20types/cell-types-overview.
Use these exact names. No synonyms.

```
AnyDB CELL TYPES (core 15 per Overview)
================================================================

TEXT / CONTENT:
  General          — Plain text or mixed content (single-line strings, codes, short values).
                     Use for email/phone/URL storage; enforce format via validation functions.
  Rich Text        — Multi-line text with formatting support (descriptions, notes, docs).

NUMERIC:
  Number           — Numeric values with optional formatting (integer or decimal).
  Currency         — Monetary values with symbol/code support.
  Percentage       — Display and calculate percentage values.

TEMPORAL:
  Date             — Calendar date only (no time component).
  Date & Time      — Date with time included.
  Time             — Time of day only.

SELECTION:
  Select           — Single value from a predefined list of options.
                     No native "Multi-select" cell type exists.
                     Options can be static (defined at cell creation) or dynamic
                     (computed from a formula returning an array of strings).
  Checkbox         — Yes/No, True/False toggle.

RELATIONSHIP & FILES:
  Reference        — Link to another record in the SAME database.
                     Connection type is one-to-one (see Section 4).
  File             — Upload and attach a file to the cell (document, image).
  Attachments      — Displays child records attached to the current record.
                     This is NOT file upload. See Section 4 for attach relationship mechanics.
  User             — Reference to a team member.
  Signature        — User-drawn or uploaded signature.

```

The list above is the official core overview page. Do not extend this catalog unless the
specific cell type has its own AnyDB doc page and is explicitly in scope. QR Code, for
example, has a separate doc page, but it is not part of the 15-type core overview list.

### Separately documented specialized cell types

These are documented by AnyDB on their own cell-type pages, but are not part of the
15-type core overview list above. Use them when the build actually needs them.

```
AnyDB SPECIALIZED CELL TYPES (separately documented)
================================================================

Lookup           — Display data from a linked record inside the current record.
                   Uses a Reference cell under the hood via DYNREF().

Report           — Wrapper around REPORT() for counts, sums, averages, terms, and
                   lightweight embedded dashboards/charts.

Chart            — Inline visualization cell for Line / Bar / Pie charts using array data.

Barcode          — Renders a machine-readable barcode from a referenced value.

QR Code          — Renders a QR code from a referenced value.

Clock            — Displays a live clock, including timezone-specific time displays.

Comments         — Displays record or cell comments for collaboration inside the record.

AI               — Runs AI prompts against local cells, linked records, attached child
                   records, and supported files.
```

### What does NOT exist as a cell type

Do not specify these — they are not valid AnyDB cell types. Use the stated alternative:

| Not a cell type | Use instead |
|---|---|
| "Rollup" | Formula cell aggregating attached children (Section 4 + Section 5) |
| "Auto-number" | Formula cell using `=SEQNUM("type-id")` |
| "Email" | General cell + `ISEMAIL()` validation |
| "Phone" | General cell + `ISPHONE()` validation |
| "URL" | General cell + `ISURL()` validation |
| "Formula" (as a cell type) | Any cell type can have a formula — set the cell's type first (Number/Currency/General/etc.), then add a formula that returns that type |
| "Multi-select" | Select cell with dynamic options formula, OR use Attachments of a small "tag" type |
| "Long text" | `Rich Text` |
| "Text" | `General` |
| "Link" | `Reference` |
| "Percent" | `Percentage` |
| "Date and time" | `Date & Time` |

---

## Section 2: Formula Syntax Reference

Source: anydb.com/support/user-docs/templates/formulas

### Entry and cell references

- Formulas start with `=`. Example: `=A1 + B1`.
- Cells can be referenced by position (`A1`, `B2`) or by name with double curly braces (`{{Price}}`).
- **Function names and references are case-sensitive.** Use `SUM`, not `sum`. Use `A1`, not `a1`.

### Operators

```
Arithmetic:   + - * / ^ !         (! is factorial)
Grouping:     ( )
Array index:  [ ]                  (0-based: A1[0] is the first element)
Range:        :                    (A1:A10)
Comparison:   == != > < >= <=
Logical:      and  or  not         (words, not && || !)
Conditional:  IF(cond, a, b)  OR  cond ? a : b
```

### Record-level references

```
Current record:             CURRREC
Record name:                M@NAME
Assigned user:              M@ASSIGNED
Follow-up date:             M@FOLLOWUP
Status (open/closed):       M@STATUS
Type name:                  M@TYPENAME
Type ID:                    M@TYPEID
Badge value:                B@BADGE_NAME
Cell property:              A1!P@BACKGROUND_COLOR
```

### Aggregation across attached child records

This is how AnyDB does rollups. There is no Rollup cell — use formulas with child references.

```
All children of current record:           C@CURRREC!CellID
Children of a specific Type only:         C@CURRREC!N@TypeName!CellID
Children of a specific record by ID:      C@RecordID!CellID
Parents of current record:                A@CURRREC!CellID

Aggregate with functions:
  =SUM(C@CURRREC!A1)                       — sum cell A1 across children
  =MEAN(C@CURRREC!A1)                      — average (there is no AVG)
  =COUNT(C@CURRREC!A1)                     — count
  =MAX(C@CURRREC!A1), =MIN(...)
  =SUMIFS(C@CURRREC!A1, C@CURRREC!A2, ">100")
  =COUNTIF(C@CURRREC!A2, "Open")
```

### Cross-record lookups (for Reference cells)

```
=DYNREF(A7, A1)                            — pulls cell A1 from the record A7 references
```
Lookup cells wrap this pattern with a UI so you don't write the formula manually.

### Key function names (partial — load anydb.com docs for full list)

```
Text:       LEN, CONCAT, TRIM, LEFT, RIGHT, MID, REPLACE, SUBSTITUTE,
            UPPER, LOWER, PROPER, TEXT
Math:       SUM, MAX, MIN, MEAN, POWER, ROUND, SQRT, FLOOR, CEILING, PMT
Date:       TODAY, DATEADD, DATESUBTRACT, DATEDIF, DAYS, DAY, MONTH, YEAR,
            WORKDAY, FORMATDATE, DATEVALUE, READABLEDATE, READABLEDATETIME
Logic:      IF, IFERROR, COUNTIF, COUNTIFS, SUMIFS, COUNTNIF, FILTER,
            MAXBY, SUMBY, GROUPBYSUM
Validate:   ISEMAIL, ISPHONE, ISURL, ISPOSTALCODE, ISCREDITCARD, ISIP,
            ISMACADDRESS, ISNUMERIC, ISALPHANUMERIC, ISPASSPORTNUMBER, ISODATE
Lookup:     DYNREF, VLOOKUP
Sequence:   SEQNUM              — use for auto-incrementing IDs
Reports:    REPORT
Advanced:   GETONCE, MAP
```

### Common syntax mistakes

- `IF({{Status}} = "Approved", ...)` → wrong — equality is `==`.
- `CONCATENATE(...)` → wrong — the function is `CONCAT`.
- `AVG(...)` → wrong — the function is `MEAN`.
- `{{Total}} && {{Qty}}` → wrong — logical AND is `and` (word).
- `=A1 & "-" & B1` → unverified; prefer `=CONCAT(A1, "-", B1)`.

---

## Section 3: Cell Format Conventions

**Currency**
- Declare symbol/code explicitly. Default: CAD for KaizenCommerce internal records. USD for US-based client records.
- Standard 2 decimals unless a client's accounting requires more (e.g., FX rates).
- Example spec line: `Currency — CAD, 2 decimals`

**Percentage**
- Displayed as a percentage. Store the decimal value.
- Declare precision (typically 2 decimals).

**Number**
- Declare integer vs decimal and precision explicitly.
- Do not use Number for monetary values — use Currency.
- Example: `Number — integer, min 0`

**Date** (calendar date only)
- Display format: `YYYY-MM-DD` (ISO 8601).
- Runtime serialization for the live KaizenCommerce AnyDB DB may use Unix seconds — see `anydb-kaizen/SKILL.md` Date Formats table. Do not assume; confirm per cell.

**Date & Time**
- Timezone must be declared. Default: UTC for system-generated cells. Client-local for user-facing cells (appointments, submission timestamps).

**Time**
- Declare 12h vs 24h format.

**Auto-incrementing IDs** (no Auto-number cell type)
- Implement via a General or Number cell with a Formula of `=SEQNUM("type-id")`.
- For prefixed IDs (e.g., `PO-0001`), wrap in CONCAT: `=CONCAT("PO-", TEXT(SEQNUM("po"), "0000"))`.
- KaizenCommerce prefix conventions:
  - Purchase Orders: `PO-`
  - Invoices: `INV-`
  - Credit memos: `CR-`
  - Defects/deductions: `DEF-`
  - Delivery/transfer: `DL-`
- Sequence width: 4 digits minimum.

**Email / Phone / URL** (all stored in General cells)
- Apply validation via formulas:
  - Email: `=ISEMAIL(A1)`
  - Phone: `=ISPHONE(A1)` — E.164 format recommended (+15141234567)
  - URL: `=ISURL(A1)`
- Do not specify "Email cell" or "Phone cell" — those don't exist.

**Select**
- List all options at cell creation, OR use a dynamic options formula that returns an array of strings.
- For lists tied to another record's children: `=C@CURRREC!CellID`.
- For lookups that return a list: use `=COUNTRIES("name")`, `=LANGUAGES()`, etc.

---

## Section 4: Connection & Aggregation Rules

AnyDB has exactly **two connection types**. Use the right one.

### Attach (structural, parent-child)

- Places a record **inside** another as a child. One-to-many by structure.
- Parent deletion removes the attached child (unless the child is attached to other parents).
- **Supports aggregation (rollups) via formulas using `C@CURRREC!CellID`.**
- **A child can be attached to multiple parents** — this does not duplicate the child; it appears in multiple contexts.
- Use when: the child does not make sense without the parent (order lines, tasks inside a project, quality checks, maintenance logs).

### Reference (Link, associative)

- One record points to another. **One-to-one by definition.**
- Referenced record exists independently; not deleted with the referrer.
- **Supports lookups via Lookup cells or `DYNREF()`.**
- **Does NOT support rollups/aggregation.**
- **Only works within the same database.**
- Use when: the target is reusable master data (customers, vendors, products, locations, categories).

### Decision rule

> "Should this record still exist if the parent is deleted?"
> If **no** → Attach. If **yes** → Reference.

### Aggregation must use Attach

Any time a spec says "rollup", "sum across children", "count of linked records", or similar:
- The relationship must be **Attach**, not Reference.
- The aggregation cell is a Formula cell (typed as Number/Currency/etc.) using `=SUM(C@CURRREC!A1)` or equivalent.
- There is no Rollup cell type. Stating one in a spec is a CRITICAL error.

### Build order dependency (non-negotiable)

1. Parent Type must exist before the child Type that attaches to it.
2. Target Type of a Reference must exist before the cell that references it is created.
3. Any cell used in a Formula or Lookup must exist before the Formula/Lookup cell that names it.

---

## Section 5: Canonical KaizenCommerce Formula Patterns

All patterns use AnyDB syntax (curly-brace cell names, `=` prefix, `==` equality, `C@CURRREC!` for children).

| Pattern | Formula |
|---|---|
| Margin % | `=({{Sale Price}} - {{Cost}}) / {{Sale Price}}` |
| Stock aging in days | `=DAYS(TODAY(), {{Date Received}})` |
| Reorder trigger flag | `=IF({{Qty On Hand}} <= {{Reorder Point}}, "REORDER", "OK")` |
| Days since last order | `=DAYS(TODAY(), {{Last Order Date}})` |
| Variance % | `=({{Counted}} - {{Expected}}) / {{Expected}}` |
| SLA breach flag | `=IF(TODAY() > {{SLA Deadline}}, "BREACH", "ON TRACK")` |
| Weighted pipeline value | `={{Deal Value}} * {{Close Probability}}` |
| Churn risk score | `=IF({{Days Since Last Order}} > 90, "HIGH", IF({{Days Since Last Order}} > 60, "MEDIUM", "LOW"))` |
| Currency conversion | `={{USD Amount}} * {{FX Rate}}` |
| Sum of child record values (e.g., PO total from line items) | `=SUM(C@CURRREC!A1)` |
| Count of child records | `=COUNT(C@CURRREC!A1)` |
| Filtered child count (e.g., open POs) | `=COUNTIF(C@CURRREC!A2, "Open")` |
| Filtered child sum (e.g., open PO value) | `=SUMIFS(C@CURRREC!A1, C@CURRREC!A2, "Open")` |
| Prefixed auto-number (e.g., PO-0001) | `=CONCAT("PO-", TEXT(SEQNUM("po"), "0000"))` |
| Lookup from referenced record (parent pattern) | `=DYNREF(A7, A1)` — or a Lookup cell |

---

## Section 6: Validation Rules

Source: anydb.com/support/user-docs/templates/cell-validation_required

**Required cells**
- Any cell can be marked Required. Records cannot be saved with empty Required cells.
- Required cells are marked with `*` in the UI.

**Conditional required**
- Required state can itself be a formula returning true/false.
- Example: make Age required only when Subject is Biology:
  `=B2 == "Biology" ? true : false`

**Custom error messages**
- When a cell fails validation, a formula-driven error message can be displayed.
- Example: `Need to be 20 to take biology`

**Format validation via functions**
- `ISEMAIL`, `ISPHONE`, `ISURL`, `ISPOSTALCODE`, `ISCREDITCARD`, `ISIP`, `ISMACADDRESS`, `ISNUMERIC`, `ISALPHANUMERIC`, `ISPASSPORTNUMBER`, `ISODATE`
- Applied as validation formulas on General cells.

**Unique constraints**
- Not a built-in cell-level flag. Enforce via:
  - `=SEQNUM("type-id")` for guaranteed-unique auto IDs
  - Automations that check for duplicates on save
  - Downstream reconciliation in AnyDB views or reports
- Document the enforcement mechanism explicitly in the spec.

**Select options**
- Define all static options at cell creation, OR bind to a dynamic options formula.
- Formula must return an array of strings.
- Never leave a Select with an empty options list.

---

## Section 7: Common Failures

**1. Specifying a "Rollup" cell in a spec.**
Rollup is not a cell type. Write a Formula cell (typed as Number/Currency/etc.) that aggregates attached children via `C@CURRREC!CellID`. A spec that lists "Rollup" cells is a CRITICAL deviation from AnyDB's actual model.

**2. Using Reference when aggregation is needed.**
Reference is one-to-one and does NOT support aggregation. If the spec needs a parent to sum/count values across children, the relationship must be Attach, not Reference. This is a CRITICAL error — Rollup formulas silently fail on Reference cells.

**3. Specifying "Auto-number" as a cell type.**
No such cell type exists. Use a General or Number cell with `=SEQNUM("type-id")`, wrap in CONCAT for prefixes.

**4. Specifying "Email", "Phone", or "URL" as cell types.**
Those don't exist. Use General cells with ISEMAIL/ISPHONE/ISURL validation.

**5. Specifying "Multi-select".**
No such cell type. Use a Select cell with a dynamic options formula, or model as Attachments of a "Tag" Type.

**6. Formula using `=` instead of `==` for equality.**
`IF({{Status}} = "Approved", ...)` is wrong. Equality is `==`. Case-sensitive.

**7. Using `CONCATENATE` or `AVG`.**
Wrong function names. Use `CONCAT` and `MEAN`.

**8. Lower-case function names or cell references.**
AnyDB formulas are case-sensitive. `sum(a1)` fails. Must be `SUM(A1)`.

**9. Referencing a record in a different database.**
Reference cells and DYNREF only work within the same database. Cross-database linking is not supported via cells — requires integration.

**10. Confusing Attachments cell with File cell.**
The Attachments cell displays child records attached to the current record. The File cell uploads a file. Specifying "Attach a PDF to the PO" needs a File cell. Specifying "PO has line items" needs Attach relationship + (optionally) an Attachments cell to display them.

**11. Cardinality mislabeling on Reference.**
Reference is one-to-one per AnyDB docs. Writing "Reference — many-to-many" or "one-to-many" in a spec is a terminology error. Many-to-one relationships are fine from the "many" side's perspective (each line item references one product). For one-to-many/many-to-many structural relationships, use Attach (children can have multiple parents).

---

## Section 8: Vocabulary Discipline

**Cell type names:** Use exact names from Section 1 only. Never use:

| Don't say | Say |
|---|---|
| "dropdown" | `Select` |
| "string" | `General` or `Rich Text` |
| "text field" | `General` |
| "long text" | `Rich Text` |
| "fk" or "foreign key" | `Reference` |
| "join" | `Reference` (for display) or `Attach` (for structure) |
| "rollup" (as cell type) | Formula with `C@CURRREC!` aggregation |
| "multi-select" | Select with dynamic options, or Attach of tag records |
| "auto-number" | `=SEQNUM("type-id")` formula |
| "link" | `Reference` when you mean the cell type. In AnyDB's relationship docs, "Link" is the concept implemented by a Reference cell. |
| "object" (as schema) | `Type` |
| "table" | `Type` |
| "field" | `Cell` |
| "row" | `Record` |
| "column" | `Cell` (across records of a Type) |

**Formula syntax discipline:**
- All formulas start with `=`.
- Comparison uses `==` (never `=`).
- Cell refs are case-sensitive: `A1`, `{{Price}}`, not `a1` or `{{price}}`.
- Function names are case-sensitive: `SUM`, `IF`, `CONCAT`, `MEAN`.
- Logical operators are words: `and`, `or`, `not`.
- Child aggregation uses `C@CURRREC!CellID`; parent reference uses `A@CURRREC!CellID`.

**Relationship declarations — every cell, every time:**
- Every Reference cell: declare target Type.
- Every Attach relationship: declare parent Type and child Type.
- Every Lookup cell: declare the Reference cell it traverses AND the source cell on the referenced record.
- Every aggregation Formula: declare the typed output (Number/Currency/etc.) AND the child Type whose cells it aggregates.

**Required vs Optional vs Computed:** State one of these for every cell. Never leave it implicit.

**Two AnyDB reference files — different purposes:**
- `kaizen-anydb-patterns.md` (this file) = spec-writing vocabulary sourced from anydb.com. Load when generating schema, cell configs, auditing builds, or preparing data loads.
- `anydb-kaizen/SKILL.md` Field Maps = legacy runtime API vocabulary for old AnyDB-backed KaizenCommerce records. Storage-side type names may differ. Do not conflate with current KaizenOS MCP records.

**KaizenOS source boundary:** KaizenOS MCP, not AnyDB, is the current CRM/project-management source
for KaizenCommerce. Use this AnyDB reference for AnyDB platform behavior and client workflow-system
builds, not for live deal/project status.
