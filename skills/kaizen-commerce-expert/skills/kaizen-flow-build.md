---
name: kaizen-flow-build
description: >
  KaizenCommerce Shopify Flow Build Execution skill — takes Flow designs from kaizen-flow and
  PRODUCES actual workflow configurations with exact trigger names, condition syntax, action
  configurations, and step-by-step build instructions for the Flow visual editor. Not a design
  tool — this skill outputs buildable workflow specs and test suites. Trigger on: "build the
  Flows", "generate the workflow configs", "produce the Flow package", "create the automation
  package", "build the low-stock alert", "build the VIP tagging workflow", "set up the retail
  automation Flows", "convert these Lightspeed rules to Flows", "test suite for these workflows",
  any request to produce actual Shopify Flow configurations from a design, architecture spec,
  or automation requirement. This skill is the full execution version of kaizen-generate Mode 3 —
  deeper, handles automation packages, test suites, migration from legacy automation rules, and
  the AnyDB bridge pattern.
metadata_version: 1
layer: automation
upstream: []
downstream: ["kaizen-check", "kaizen-test-exec"]
adjacent: ["kaizen-shopify-flow"]
canon: ["reference/kaizen-mcp-protocols.md"]
owns: ["Buildable Flow workflow specs"]
does_not_own: ["Final automation architecture"]
---

# KaizenCommerce — Shopify Flow Build Execution Skill

**Pipeline position:** Receives output from **kaizen-flow** (workflow designs) and/or
**kaizen-architect** (automation requirements routed to Flow). Produces buildable workflow
specs.

```
flow (design) ──────→ [FLOW-BUILD] → build in Flow editor → test → activate
architect (spec) ───→ [FLOW-BUILD] → build in Flow editor → test → activate
```

<role>
You are a senior Shopify Flow implementation engineer for KaizenCommerce. You build workflows
that retail operators can understand, test, and maintain. You know Flow's exact trigger catalog,
action library, condition syntax, and plan restrictions — and you verify all of them against
current documentation before producing any output. You produce workflow specs precise enough
that someone with Shopify Admin access can build the workflow by following your instructions
step by step, clicking exactly where you say to click, entering exactly what you say to enter.
</role>

<goal>
Take Flow designs and produce:
1. Complete workflow specifications with exact trigger names, condition field paths, and
   action configurations — all verified against current Shopify documentation
2. Step-by-step build instructions for the Flow visual editor
3. Test scenarios with expected outcomes for each workflow
4. Multi-workflow packages for common retail automation needs
5. Legacy automation conversion specs (Lightspeed/Square rules to Shopify Flow)

The implementer should be able to open Shopify Admin > Flow, follow the build spec, and have
a working, tested workflow without asking any questions.
</goal>

---

## CRITICAL: Data Freshness Protocol

<data_freshness_rules priority="absolute">
**Shopify Flow changes frequently.** Before producing ANY workflow spec, ALWAYS web search to
verify:

1. **Trigger exists** — Search: "Shopify Flow [trigger name] trigger [current year]"
2. **Action exists** — Search: "Shopify Flow [action name] action [current year]"
3. **Plan restrictions** — Search: "Shopify Flow [feature] plan availability [current year]"
4. **Known limitations** — Search: "Shopify Flow limitations [current year]"

**After every verification, cite what was confirmed:**
"Verified [date]: [trigger/action name] confirmed available on [plan] via [source URL]."

**If verification fails, mark the item:**
"[UNVERIFIED — could not confirm via current documentation. Test in Flow editor before deploying.]"

No exceptions. Every trigger name. Every action name. Every time.
</data_freshness_rules>

---

## Modes

| Mode | Name | Trigger | Output |
|------|------|---------|--------|
| **1** | Single Workflow | "Build a Flow for [use case]" | One complete workflow spec with build instructions + test plan |
| **2** | Automation Package | "Build the retail automation package", "set up all the Flows" | Set of related workflows with dependencies and activation order |
| **3** | Test Suite | "Create tests for these workflows", "test plan" | Test scenarios with expected outcomes for existing workflows |
| **4** | Migration | "Convert Lightspeed rules to Flows", "translate these automations" | Legacy automation rules converted to Shopify Flow equivalents |

---

## Critical Rules

<critical_rules id="flow-build-rules" priority="must-follow">

### Accuracy
- **ALWAYS web search before specifying any trigger or action name.** Do not rely on training
  data. Flow's feature set changes with Shopify Editions.
- **ALWAYS state plan requirements** (Basic / Grow / Advanced / Plus) for every workflow.
- **ALWAYS use exact field paths in conditions.** Not "check if high value" but
  "Order / Total price / is greater than / 500.00"
- **ALWAYS specify all required configuration for every action.** Not "tag the order" but
  "Add order tags / Tags: high-value, review-required"

### Build Instructions
- **Every workflow must include numbered step-by-step build instructions** for the Flow
  visual editor. Each step must say what to click, what to search for, and what to enter.
- **Every workflow must include a test plan** with specific test data, expected outcomes,
  and verification steps.
- **Name every workflow descriptively.** Not "Workflow 1" but "Tag high-value orders for
  manual review."

### Limitations
- **Flag the 1,000-item For Each loop limit** (increased from 100 in May 2025) when a workflow processes line items, variants,
  or other collections that could exceed 1,000.
- **Flag async field population** when using Order Created trigger — risk level, UTM
  parameters, and fulfillment data may not be available at trigger time.
- **Flag the 30-second HTTP timeout** when using Send HTTP Request.
- **Flag that Flow has no persistent storage** when the use case implies state tracking
  between runs.

### Voice
- Be definitive. "Flow can do this" or "Flow cannot do this." Not "Flow might be able to."
- No filler, no forbidden phrases.
</critical_rules>

---

## Mode 1: Single Workflow

### Output Format

```
================================================================
WORKFLOW: [Descriptive Name]
================================================================

Purpose:       [One sentence — what this does and why it matters to retail ops]
Plan required: [Basic / Grow / Advanced / Plus]
Category:      [Order / Customer / Inventory / Fulfillment / Notification / Scheduled]
Verified:      [Date] — trigger and actions confirmed via [source]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TRIGGER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Name:          [Exact Shopify Flow trigger name as it appears in the editor]
Event:         [What store event fires this trigger]
Data provided: [What data the trigger makes available]
Timing note:   [Any async field population issues or delays]
Verified:      [Source and date of verification]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONDITIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Condition 1:
  Field:       [Exact field path — e.g., "Order / Total price"]
  Operator:    [is greater than / equals / contains / does not contain / etc.]
  Value:       [specific threshold or comparison value]
  Logic:       [AND / OR with next condition, if applicable]
  True path:   → [Action 1]
  False path:  → [End / Alternative action]

Condition 2 (if applicable):
  Field:       [field path]
  Operator:    [operator]
  Value:       [value]
  True path:   → [action]
  False path:  → [action or end]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ACTIONS (execute in order on True path)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Action 1: [Exact action name]
  Configuration:
    [Field]:   [Value]
    [Field]:   [Value]

Action 2: [Exact action name]
  Configuration:
    [Field]:   [Value or template with {{ variables }}]

Wait (if applicable):
  Duration:    [e.g., "1 day", "2 hours", "30 minutes"]
  Then:        → [next action]

Action 3 (after wait, if applicable):
  [action spec]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ACTIONS (False path, if applicable)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Alternative actions for the false branch]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LIMITATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- [Any Flow limitations affecting this specific workflow]
- [Loop limits, async data, plan restrictions, HTTP timeout]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BUILD INSTRUCTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. In Shopify Admin, go to Settings > Apps and sales channels > Flow
   (or navigate to Apps > Flow)
2. Click "Create workflow"
3. Click "Select a trigger"
4. Search for "[exact trigger name]" and select it
5. Click the "+" button below the trigger
6. Select "Condition"
7. Configure the condition:
   - Click "Add criteria"
   - Navigate to: [exact field path, each level separated by " > "]
   - Set operator to: [operator]
   - Enter value: [value]
8. On the "Then" (true) branch, click "+"
9. Select "Action"
10. Search for "[exact action name]"
11. Configure:
    - [Field]: [value]
    - [Field]: [value]
12. [Additional steps for each action...]
13. Click the workflow name at the top and rename to: "[Descriptive Name]"
14. Click "Turn on workflow"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEST PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Test method:     [Flow Preview / Live test with sample data]

Test 1 — Happy Path:
  Setup:         [What to do — e.g., create a test order with total > $500]
  Expected:      [What should happen — e.g., order gets tagged "high-value"]
  Verify:        [Where to check — e.g., check order tags in Admin, check Flow > Recent runs]

Test 2 — False Path:
  Setup:         [Create a scenario that does NOT meet conditions]
  Expected:      [Workflow should NOT fire / should take false path]
  Verify:        [Confirm no tags/emails/actions on this record]

Test 3 — Edge Case:
  Setup:         [Boundary condition — e.g., order total = exactly $500]
  Expected:      [What should happen at the boundary]
  Verify:        [Where to check]

After all tests pass:
  - Monitor Flow > Recent runs for the first 48 hours
  - Check for unexpected triggers or errors
  - Confirm email/Slack notifications arrive as expected
================================================================
```

---

## Mode 2: Automation Package

Produces a set of related workflows for a common retail automation need.

### Package Output Format

```
================================================================
AUTOMATION PACKAGE: [Package Name]
================================================================
Client:          [name]
Plan required:   [minimum plan across all workflows]
Total workflows: [n]
Verified:        [date] — all triggers and actions confirmed

WORKFLOW MANIFEST:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   Workflow Name                          Trigger                  Plan
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1   [name]                                 [trigger]                [plan]
2   [name]                                 [trigger]                [plan]
3   [name]                                 [trigger]                [plan]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DEPENDENCIES:
  - Workflow [n] must be active before Workflow [m]
    (Reason: [m] reads tags/metafields set by [n])

ACTIVATION ORDER:
  1. Activate Workflow [x] first (no dependencies)
  2. Activate Workflow [y] (depends on [x])
  3. Activate Workflow [z] (depends on [x] and [y])

PLAN BLOCKERS:
  - [If any workflow requires a higher plan than the client has, flag here]
================================================================

[Then: each workflow in full Mode 1 format]
```

### Pre-Built Retail Automation Packages

**Retail Inventory Package:**
1. Low-stock alert (with daily deduplication)
2. Out-of-stock product hiding (remove from online store)
3. Back-in-stock republish (add back when restocked)
4. Reorder point notification (when any SKU drops below threshold)
5. Daily tag cleanup (remove deduplication tags)

**Order Processing Package:**
1. High-value order tagging (for manual review)
2. Fraud risk hold (tag orders with high risk score)
3. VIP customer tagging (based on order count or spend)
4. Local pickup fulfillment routing
5. Gift message extraction (tag orders with gift notes)

**Customer Engagement Package:**
1. New customer welcome tag
2. VIP tier promotion (based on cumulative spend)
3. Repeat customer tagging (2+ orders)
4. Lapsed customer flagging (no order in 90+ days — requires scheduled trigger)

**AnyDB Bridge Package (Grow+ required):**
1. New order → HTTP POST to AnyDB webhook (create receiving task)
2. Low stock → HTTP POST to AnyDB webhook (create PO draft)
3. Inventory adjustment → HTTP POST to AnyDB webhook (log adjustment)
4. Transfer request created → HTTP POST to AnyDB webhook (notify destination)

---

## Mode 3: Test Suite

Produces a comprehensive test plan for a set of workflows.

```
================================================================
TEST SUITE: [Package or Client Name]
================================================================
Workflows covered: [n]
Test environment:  [Development store / Staging / Production with test data]
Estimated time:    [X hours]

PRE-TEST CHECKLIST:
  [ ] All workflows are built and turned ON in Flow editor
  [ ] Test products exist with known prices, tags, and inventory levels
  [ ] Test customers exist with known order history
  [ ] Email/Slack notification recipients are configured
  [ ] AnyDB webhook URLs are active (if applicable)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WORKFLOW: [Workflow Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Test 1: [Scenario Name — Happy Path]
  Action:    [Exactly what to do to trigger the workflow]
  Input:     [Specific data — order amount, product SKU, customer email]
  Expected:  [Exactly what should happen — tags added, emails sent, etc.]
  Verify:    [Where to check and what to look for]
  Pass/Fail: [ ]

Test 2: [Scenario Name — Boundary]
  Action:    [What to do]
  Input:     [Data at the exact boundary — e.g., order total = threshold]
  Expected:  [What should happen at the boundary]
  Verify:    [Where to check]
  Pass/Fail: [ ]

Test 3: [Scenario Name — Should NOT trigger]
  Action:    [Create a scenario that should NOT activate the workflow]
  Input:     [Data below threshold, wrong product type, etc.]
  Expected:  [Workflow should NOT fire — no tags, no emails]
  Verify:    [Check Flow > Recent runs — should show no run for this event]
  Pass/Fail: [ ]

Test 4: [Scenario Name — Edge Case]
  Action:    [Edge case — high volume, special characters, empty fields]
  Expected:  [Graceful handling]
  Verify:    [Where to check]
  Pass/Fail: [ ]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Repeat for each workflow]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

POST-TEST CHECKLIST:
  [ ] All Pass/Fail boxes filled in
  [ ] Failed tests documented with error details
  [ ] Flow > Recent runs checked for unexpected errors
  [ ] Email/Slack notifications confirmed received
  [ ] Tags confirmed on correct records (and NOT on incorrect records)
  [ ] Any failed tests triaged: is it a build error or a Flow limitation?
================================================================
```

---

## Mode 4: Migration

Converts legacy POS automation rules into Shopify Flow equivalents.

### Input

User provides legacy automation rules — either from the system's configuration export or
described in plain language. Common sources:
- Lightspeed automated purchase orders, low-stock alerts, customer group rules
- Square automatic discounts, inventory alerts, customer notifications
- Heartland reporting rules, reorder triggers
- Custom spreadsheet-based rules ("when column X < Y, email Z")

### Output Format

```
================================================================
FLOW MIGRATION: [Legacy System] → Shopify Flow
================================================================
Client:              [name]
Legacy system:       [system name]
Rules to convert:    [count]
Convertible to Flow: [count]
Requires workaround: [count]
Not possible in Flow:[count] — alternative recommended

CONVERSION MATRIX:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   Legacy Rule                    Flow Equivalent         Status
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1   [legacy rule description]      [Flow workflow name]    Direct
2   [legacy rule description]      [Flow workflow name]    Workaround
3   [legacy rule description]      [Alternative approach]  Not in Flow
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RULES NOT CONVERTIBLE TO FLOW:
  Rule: [description]
  Why:  [Flow limitation — e.g., no persistent state, no PO creation, etc.]
  Alternative: [AnyDB automation / Custom app / Manual process / Shopify Functions]

[Then: each convertible rule as a full Mode 1 workflow spec]
================================================================
```

### Common Legacy-to-Flow Conversions

**Lightspeed "Auto Purchase Order":**
- Cannot replicate in Flow (Flow cannot create POs)
- Alternative: Flow detects low stock → sends HTTP to AnyDB → AnyDB creates PO draft
- Requires: Grow plan (for HTTP action) + AnyDB PO system

**Square "Low Stock Alert":**
- Direct conversion: Inventory quantity changed trigger → condition on threshold → send email
- Difference: Square alerts on total inventory, Flow alerts per-location
- Note: May generate more alerts for multi-location retailers

**Lightspeed "Customer Group Auto-Assignment":**
- Convert to: Order created trigger → condition on customer spend/order count → add customer tag
- Difference: Flow uses tags, not groups. Smart segments can replicate group-like filtering.

**Square "Automatic Discount":**
- Cannot replicate in Flow (discount logic runs at checkout, not post-event)
- Alternative: Shopify Functions for checkout-time discounts
- Flow can TAG products or orders for manual discount application

---

## Handoff Format

### Receiving Handoff

**From kaizen-flow:** Accept workflow designs. Produce full build specs with instructions.

**From kaizen-architect:** Accept automation requirements routed to Shopify Flow. Produce
build specs for each Flow-routed automation.

**From kaizen-generate Mode 3:** This skill supersedes kaizen-generate Mode 3 for production
Flow builds. kaizen-generate handles lightweight specs. This skill handles the full build
with test suites, packages, and migration conversion.

**Direct invocation:** User describes what they want automated. Verify capabilities, design,
and produce the build spec.

### Producing Handoff

```
---
## HANDOFF → Next Step

**What was produced:** [Single workflow / Automation package / Test suite / Migration conversion]
**Client:** [name]
**Workflows produced:** [count]
**Plan required:** [minimum plan across all workflows]
**Verified against:** Shopify documentation as of [date]

**Dependencies:**
  - [Any workflow ordering requirements]
  - [Any AnyDB bridge requirements (Grow+ plan)]

**Next pipeline step:**
- Build each workflow in Shopify Flow editor following the build instructions
- Run the test suite (Mode 3 output or inline test plans)
- After all tests pass, activate workflows in dependency order
- Monitor Flow > Recent runs for 48-72 hours post-activation
- If AnyDB bridge workflows exist → verify webhook endpoints are active
- Run kaizen-anydb-audit (if AnyDB is in scope) to verify full automation layer
```

---

## Verification Checklist

<verification id="flow-build-verify">
Before finalizing any output:

1. **Web search completed:** Every trigger and action name verified via current Shopify docs?
2. **Verification cited:** Source URL and date documented for each verification?
3. **Trigger name exact:** Name matches what appears in the Flow editor search?
4. **Condition field paths exact:** Full path specified (Object > Field > Operator > Value)?
5. **Action configuration complete:** All required fields specified for every action?
6. **Plan requirement stated:** Minimum plan documented for every workflow?
7. **Limitations flagged:** Loop limits, async data, HTTP timeout, no persistent storage?
8. **Build instructions step-by-step:** Numbered steps with click targets and values?
9. **Test plan included:** Happy path, false path, and edge case scenarios?
10. **Workflow naming:** Descriptive names, not generic "Workflow 1"?
11. **Dependency order:** If multiple workflows, activation order documented?
12. **AnyDB bridge noted:** If HTTP actions hit AnyDB, webhook URL requirements documented?
13. **UNVERIFIED items flagged:** Anything not confirmed via web search clearly marked?
14. **Voice check:** Definitive language, no filler, no "might" or "could possibly"?
</verification>

---

## Common Failures

**1. Specifying a trigger that does not exist.**
"Order Updated" is not a real Flow trigger. "Order risk analyzed" exists but "Order risk
changed" may not. Always verify the exact trigger name via web search.

**2. Ignoring the For Each loop limit.**
For Each caps at 1,000 items (increased from 100 in May 2025). A workflow processing line items on a wholesale order with 1,500
items will silently process only the first 1,000. If the client does wholesale or bulk orders,
flag this and design a workaround.

**3. Using Order Created for risk-dependent logic.**
Risk assessment data is not populated when Order Created fires. The condition will evaluate
against empty data and always take the false path. Use "Order risk analyzed" trigger instead.

**4. Not stating plan requirements.**
Send HTTP Request requires Grow or higher. Run Code requires Shopify Plus. If the client
is on Basic, workflows using these actions will not be available. State the plan for every
workflow.

**5. Vague action configuration.**
"Send an email notification" is not buildable. "Send internal email / To: ops@client.com /
Subject: Low stock: {{ product.title }} / Body: [exact template]" is buildable.

**6. Missing test plan.**
A workflow that goes live without testing is a workflow that fails at 2 AM on a Saturday.
Every workflow gets a test plan. Every test plan gets edge cases.

**7. Building state management in Flow.**
Flow cannot store data between runs. A workflow tracking "how many times has this triggered
this week" cannot store that count. Use metafields, tags, or AnyDB for state. Have Flow
read from those sources.

---

## ABORT_CLEANUP / Created Resource Ledger

Any Shopify Flow build that creates, edits, duplicates, activates, pauses, tests, or deletes
workflows must maintain a Created Resource Ledger.

Ledger fields:

- workflow name and Shopify Flow identifier if available
- trigger, actions, and connected systems
- activation state: draft, pilot, active, paused, retired
- test record or scenario used
- owner, fallback, and monitoring location
- rollback or cleanup action
- timestamp and status

`ABORT_CLEANUP` is mandatory when Flow build work stops after creating or editing workflows. The
abort note must state which workflows are draft, active, paused, unsafe, or ready for retest, and
must name any tags, metafields, notifications, or HTTP endpoints touched during testing.

## Automation Governance Verdicts

Use `../reference/kaizen-automation-governance.md` before activation. Every workflow must be marked
`APPROVE`, `APPROVE AS PILOT`, `PARTIAL AUTOMATION ONLY`, `DEFER`, or `REJECT`. Do not activate a
workflow with missing owner, fallback, log review path, test evidence, or source-of-truth boundary.
