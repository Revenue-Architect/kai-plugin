---
name: kaizen-proactive
description: >
  KaizenCommerce Proactive Suggestions Engine — a REFERENCE skill, not directly invoked. Defines
  the logic for contextual next-step suggestions that other skills embed in their handoff blocks.
  After every skill output, the system should append intelligent suggestions for the logical next
  action based on pipeline position, client context, and engagement stage. This skill contains the
  complete suggestion logic table, the suggestion block format, and the rules for generating
  context-aware recommendations. Other skills reference this pattern in their handoff sections.
  Do NOT trigger this skill directly. It is loaded as a reference when building or updating
  handoff blocks in other skills.
metadata_version: 1
layer: intelligence
upstream: []
downstream: []
adjacent: ["kaizen-check"]
canon: ["reference/kaizen-kaizenos-integration-map.md"]
owns: ["Next-step suggestion"]
does_not_own: ["Marking inferred tasks accepted"]
---

# KaizenCommerce — Proactive Suggestions Engine (Reference Skill)

**This skill is NOT directly invoked.** It defines a pattern that other skills follow. The
suggestion logic here should be embedded into the handoff block of every pipeline skill's output.

The purpose: instead of waiting for the user to know which skill to invoke next, the system
suggests the logical next step based on what was just produced and where the client sits in the
engagement lifecycle.

---

## How This Skill Works

1. Every pipeline skill produces output + a handoff block
2. The handoff block includes a "Suggested Next Steps" section
3. That section is generated using the rules in this file
4. The suggestions are context-aware — they consider the skill that just ran, the client's
   pipeline position, and what information is now available

**The brain's composition rules should treat this file as a reference pattern.** Skills do not
need to `read` this file at runtime. The pattern is baked into how handoff blocks are written.

---

## Suggestion Block Format

Append this block after every skill's handoff section:

```
================================================================
SUGGESTED NEXT STEPS
================================================================

Based on [what was just produced] + [client pipeline position]:

1. [PRIORITY] [Specific action with client context]
   WHY: [Concrete reason derived from the output just produced]
   RUN: "Use kaizen-[skill] to [specific task with specific inputs]"

2. [RECOMMENDED] [Specific action]
   WHY: [Reason tied to pipeline logic or engagement timing]
   RUN: "Use kaizen-[skill] to [specific task]"

3. [OPTIONAL] [Specific action]
   WHY: [Reason — usually efficiency or upsell opportunity]
   RUN: "Use kaizen-[skill] to [specific task]"
================================================================
```

### Priority Levels

| Level | Meaning | When to use |
|---|---|---|
| PRIORITY | Must happen next. Blocks progress if skipped. | The next pipeline step, a blocker that needs resolution, or a time-sensitive action |
| RECOMMENDED | Should happen soon. Improves quality or captures value. | Quality checks, memory saves, upsell timing, parallel workstreams |
| OPTIONAL | Good to do when time allows. Adds polish or future value. | Content repurposing, advanced optimizations, nice-to-have documentation |

### Suggestion Rules

- **Maximum 3 suggestions per handoff.** More than 3 creates decision paralysis.
- **Every suggestion must reference a specific skill by name** with a concrete task description.
  Not "consider running a data prep" but "Use kaizen-dataprep to audit the Lightspeed product
  export (4,200 records) and produce a migration-ready output for the selected lane."
- **Suggestions must be informed by the output just produced.** If the architect spec identified
  12 AnyDB automations, the suggestion should reference that count. If the data audit found
  847 duplicate SKUs, the suggestion should reference that finding.
- **Never suggest a skill that has already been run for this client** unless there is new input
  that changes the output (e.g., "re-run kaizen-dataprep with the corrected customer export").
- **Always include one suggestion that saves context** when a significant deliverable was produced.
  This is usually "Save engagement details to client memory with kaizen-memory."

---

## Complete Suggestion Logic Table

This table defines what to suggest after each skill completes. The suggestions should be
adapted with specifics from the actual output — client name, record counts, identified issues,
tier, timeline details.

### After kaizen-outreach completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | PRIORITY | Run kaizen-qualify in pre-call mode to prep discovery questions for [prospect name] | Outreach generated a meeting. Discovery prep before the call maximizes the 30-minute window. |
| 2 | RECOMMENDED | Create client memory entry with kaizen-memory for [prospect name] | Capture the outreach context (channel, message, response) so discovery has full background. |
| 3 | OPTIONAL | Check kaizen-pipeline to see where this prospect fits against monthly targets | Helps prioritize this opportunity against others in the funnel. |

### After kaizen-qualify completes (post-call)

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1a | PRIORITY (if Blueprint accepted) | Generate Blueprint scope with kaizen-diagnose using the discovery findings | Client said yes to Blueprint. Generate the diagnostic report while the call context is fresh. |
| 1b | PRIORITY (if ready for proposal) | Generate proposal with kaizen-propose using discovery findings and tier recommendation | Discovery indicates the client is ready to move forward. Strike while the intent is hot. |
| 2 | RECOMMENDED | Save discovery findings to client memory with kaizen-memory | Preserve the pain points, quotes, and qualification score for future reference. |
| 3 | OPTIONAL | If competitor was mentioned, run kaizen-competebot (via brain routing) for battle card | Competitive intel strengthens the follow-up conversation. |

### After kaizen-diagnose completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | PRIORITY | Generate proposal with kaizen-propose based on the Blueprint findings | Blueprint is complete. The proposal should follow within 3-5 business days while findings are top of mind. |
| 2 | RECOMMENDED | If AnyDB is in scope, start architecture planning with kaizen-architect | The Blueprint identified operational gaps that need AnyDB. Getting the spec started now saves time post-signature. |
| 3 | RECOMMENDED | Run quality check on the Blueprint report before sending to client | Verify the report meets KaizenCommerce quality standards. Check assumptions, verify data accuracy, confirm voice. |

### After kaizen-propose completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | PRIORITY | Run quality check on the proposal before sending | Verify pricing math, scope alignment with Blueprint findings, and commercial guardrails. |
| 2 | RECOMMENDED (if signed) | Run kaizen-onboard to generate kickoff materials and access checklist | Proposal accepted. Kickoff within 48 hours maintains momentum. |
| 3 | RECOMMENDED | Save engagement details (tier, value, scope, timeline) to client memory with kaizen-memory | Engagement record is the foundation for all downstream tracking. |

### After kaizen-onboard completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | PRIORITY | Run kaizen-hardware to produce hardware plan and procurement list | Hardware has lead times. Start procurement now to avoid blocking go-live. |
| 2 | PRIORITY | Start kaizen-architect for technical architecture and integration design | Architecture drives everything downstream. The spec must be approved before build begins. |
| 3 | OPTIONAL | Update kaizen-pipeline with engagement status (moved to "In Progress") | Keep pipeline tracking current with the new active engagement. |

### After kaizen-architect completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1a | PRIORITY (if POS migration in scope) | Run kaizen-dataprep to audit the legacy data export and produce field mappings | Architecture is approved. Data prep is the next delivery step for the POS migration track. |
| 1b | PRIORITY (if AnyDB in scope) | Run kaizen-generate Mode 2 to produce the AnyDB schema config from the spec | The spec has [N] objects and [N] fields. Generate the build guide so the implementer can start. |
| 2 | RECOMMENDED (if Flows identified) | Run kaizen-generate Mode 3 to produce Flow workflow specs for the [N] automations routed to Flow | The architecture spec identified [N] automations for Shopify Flow. Generate build-ready specs. |
| 3 | RECOMMENDED | Run quality check on the architecture spec before sharing with the build team | Verify schema completeness, relationship accuracy, and automation logic. |

### After kaizen-dataprep completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | PRIORITY | Run kaizen-generate Mode 1 to produce Matrixify import CSVs from the field mapping | Data is audited and mapped. Generate the actual import files. |
| 2 | RECOMMENDED (if multiple entities) | Upload the next entity export and run kaizen-dataprep again | [Entity] is prepped. [N] more entity files remain: [list them]. |
| 3 | RECOMMENDED | Run kaizen-generate Mode 4 to produce sample data for lane-specific validation | Test the import pipeline with realistic sample data before running the full import. |

### After kaizen-migrate completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | PRIORITY | Run kaizen-training to produce the staff training plan | Training must be scheduled before cutover. The runbook has the cutover date — work backward from it. |
| 2 | RECOMMENDED | Verify training is scheduled [N] days before cutover date of [date] | Timeline check: training must complete before staff uses the new system on day one. |
| 3 | RECOMMENDED | Run kaizen-hardware to confirm all devices are procured, configured, and tested | Hardware validation before go-live. A perfect data migration fails if the iPad can't reach the printer. |

### After kaizen-validate completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1a | PRIORITY (if errors found) | Run kaizen-dataprep Mode 4 to fix the [N] errors found in validation | [N] records failed import. Fix the source data and re-run validation before proceeding. |
| 1b | PRIORITY (if clean) | Run kaizen-reconcile to compare legacy data against the Shopify import | Validation is clean. Reconciliation confirms the data actually matches — counts, totals, completeness. |
| 2 | RECOMMENDED | Save validation results to client memory with kaizen-memory | Document the validation state for the engagement record. |

### After kaizen-reconcile completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1a | PRIORITY (if clean) | Proceed to cutover per the kaizen-migrate runbook | Reconciliation passed. Green light for live migration. |
| 1b | PRIORITY (if discrepancies) | Investigate [N] discrepancies before proceeding to cutover | [specific discrepancies]. Resolve before live migration to avoid data integrity issues post-go-live. |
| 2 | RECOMMENDED | Confirm cutover day resources: staff availability, hardware readiness, rollback plan reviewed | Final pre-cutover checklist. |

### After kaizen-training completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | PRIORITY | Run kaizen-hardware validation — confirm all devices are configured and network-tested before go-live | Training complete. Hardware is the last physical dependency before cutover. |
| 2 | RECOMMENDED | Verify cutover date is [N] days away and all prerequisites are met | Timeline check against the kaizen-migrate runbook. |

### After kaizen-report completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | PRIORITY | Run kaizen-finance Mode 1 to calculate engagement P&L for [client] | Engagement is complete. Calculate profitability while hours and costs are fresh. |
| 2 | RECOMMENDED | Run kaizen-publish to repurpose the case study for LinkedIn and marketing | The health check / case study is written. Turn it into content while the results are current. |
| 3 | OPTIONAL (if upsell identified) | Run kaizen-qualify with the AnyDB upsell context from the health check | The report identified [specific operational gap]. This is the AnyDB upsell trigger — run discovery. |

### After kaizen-publish completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | RECOMMENDED | Post the content to LinkedIn and update the content calendar status | Content is produced. Distribution is the value step. |
| 2 | OPTIONAL | Share the case study with AE contacts via kaizen-outreach as a warm touchpoint | Case studies are the best referral-generation tool. Send to [N] active AE contacts. |

### After kaizen-generate completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1a | PRIORITY (if migration artifact) | Run the lane-specific validation gate from kaizen-migrate with the generated artifact | Migration artifact is ready. Validation catches errors before live import. |
| 1b | PRIORITY (if AnyDB config) | Begin AnyDB build following the schema config. Run kaizen-anydb-audit after build is complete. | Schema config is the build guide. Audit validates the build matches the spec. |
| 1c | PRIORITY (if Flow spec) | Build workflows in the Shopify Flow editor following the build instructions | Flow specs are ready. Build, test with preview, activate. |
| 2 | RECOMMENDED (if sample data) | Use the sample data for lane-specific validation before generating production import files | Test the pipeline with sample data first. Production files after validation passes. |
| 3 | RECOMMENDED (if script) | Run the script against actual data in dry-run mode, review output, then run for real | Scripts have dry-run mode. Preview before committing. |

### After kaizen-finance completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | PRIORITY (if pricing issue found) | Update proposal templates in kaizen-propose with adjusted pricing | Pricing analysis shows [tier] is underpriced by [amount]. Adjust before the next proposal. |
| 2 | RECOMMENDED | Run kaizen-pipeline to connect financial health to current deal pipeline | Financial review informs pipeline priorities. If margins are thin, prioritize higher-tier deals. |
| 3 | OPTIONAL (if retainer issue) | Schedule retainer client touchpoints for at-risk accounts this week | [N] retainer clients flagged for churn risk. Proactive outreach prevents revenue loss. |

### After kaizen-scope completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | PRIORITY | Get client approval on the change order before continuing work | Scope change documented. No additional work until the change order is signed. |
| 2 | RECOMMENDED | Update client memory with scope change details via kaizen-memory | Document the scope change for engagement history. |
| 3 | RECOMMENDED | Run kaizen-finance Mode 1 to recalculate engagement P&L with the scope change | The change order affects profitability. Recalculate to confirm margins are still healthy. |

### After kaizen-anydb-dataload completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | PRIORITY | Run kaizen-anydb-audit to verify the loaded data matches the spec | Data is loaded. Audit confirms record counts, field population, and relationship integrity. |
| 2 | RECOMMENDED | Test AnyDB automations with the loaded data | Automations need real data to validate. Run through each automation workflow manually. |

### After kaizen-anydb-audit completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1a | PRIORITY (if issues found) | Fix the [N] audit findings before proceeding | [specific issues]. Resolve before staff training or go-live. |
| 1b | PRIORITY (if clean) | Run kaizen-training to prepare staff training on the AnyDB system | Build is verified. Staff needs training before they start using it. |
| 2 | RECOMMENDED | Verify Flow-AnyDB integrations are working end-to-end | If Flows send data to AnyDB via HTTP, test the full chain with real events. |

### After kaizen-research completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | PRIORITY | Run discovery prep with kaizen-qualify using this merchant brief | Research produced a full brief. Discovery prep customizes questions using the research findings so the call is maximally productive. |
| 2 | RECOMMENDED | Save this research to client memory with kaizen-memory | Capture the research findings (industry, stack, inferred pain points) so downstream skills have full context. |
| 3 | OPTIONAL | Draft a cold outreach sequence with kaizen-email-exec using the research findings | If no meeting is booked yet, outreach informed by research converts better than generic templates. |

### After kaizen-check completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1a | PRIORITY (if FAIL) | Fix the issues identified, then re-run kaizen-check | Validation found issues. Resolve them before delivering the document to the client. |
| 1b | PRIORITY (if PASS) | Render as styled PDF with kaizen-render for client delivery | Document passed validation. Render for professional delivery. |
| 2 | RECOMMENDED | Update client memory with validation results | Document the validation state for the engagement record. |

### After kaizen-content-calendar completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | PRIORITY | Generate the first piece of content with kaizen-publish | Calendar is planned. Producing the first piece creates momentum and validates the content strategy. |
| 2 | RECOMMENDED | Schedule the calendar items in your posting tool | Content planned but not scheduled is content that doesn't ship. Lock in the dates. |

### After kaizen-matrixify-exec completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | PRIORITY | Run the selected validation gate using kaizen-test-exec or kaizen-validate | Migration files are generated. Validation catches errors before live import. |
| 2 | RECOMMENDED | Update client memory with data volumes from the generated files | Record the entity counts and file sizes for the engagement record and downstream reconciliation. |

### After kaizen-anydb-build completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | PRIORITY | Build the schema in AnyDB following the config sequence | Build guide is ready. Execute the schema creation in the correct object order to respect dependencies. |
| 2 | RECOMMENDED | Run kaizen-anydb-audit after build to verify against spec | Audit confirms the build matches the architecture spec — catches missing fields, wrong types, broken relationships. |

### After kaizen-flow-build completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | PRIORITY | Build workflows in Shopify Flow following the step-by-step instructions | Flow specs are ready. Build each workflow, test with preview, then activate. |
| 2 | RECOMMENDED | Run the test suite from kaizen-test-exec to verify each workflow | Automated tests catch edge cases that manual testing misses. Run the full suite before go-live. |

### After kaizen-email-exec completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | PRIORITY | Review and send the emails | Emails are drafted. Review for accuracy, personalize final touches, then send. |
| 2 | RECOMMENDED | Update client memory with outreach sent date and content | Track outreach timing and content for engagement history and follow-up sequencing. |

### After kaizen-invoice-exec completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | PRIORITY | Send the SOW/invoice to the client for signature | Contract is generated. Send promptly — delays lose deal momentum. |
| 2 | RECOMMENDED | Update client memory with deal status and contract details | Record the contract value, terms, and sent date for pipeline tracking. |

### After kaizen-shopify-config completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | PRIORITY | Run hardware validation with kaizen-test-exec before staff training | Shopify is configured. Verify hardware connects properly before training staff on a system that might not work at their location. |
| 2 | RECOMMENDED | Generate staff training materials with kaizen-training | Configuration is complete. Training materials should reference the actual settings and workflows configured. |

### After kaizen-test-exec completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1a | PRIORITY (if all pass) | Proceed to controlled cutover per kaizen-migrate runbook | All tests passed. Green light for live migration. |
| 1b | PRIORITY (if failures) | Fix issues, re-run failed tests | Test failures must be resolved before cutover. Address each failure and re-validate. |
| 2 | RECOMMENDED | Update client memory with test results | Document test pass/fail status, error counts, and resolution notes for the engagement record. |

### After kaizen-report-exec completes

| # | Level | Suggestion | Reason |
|---|---|---|---|
| 1 | PRIORITY | Send the report to the client | Report is complete. Deliver while the engagement results are fresh and relevant. |
| 2 | RECOMMENDED | Repurpose the case study via kaizen-content-calendar | The report contains proof points. Turn them into marketing content while the data is current. |
| 3 | OPTIONAL | Run kaizen-finance engagement P&L with the real data | Engagement is complete. Calculate actual profitability against the quoted price. |

---

## Embedding Suggestions in Skill Outputs

When writing or updating a skill's handoff block, follow this pattern:

```
---
## HANDOFF → Next Step

**What was produced:** [output description]
**Client:** [name]
[...standard handoff fields...]

================================================================
SUGGESTED NEXT STEPS
================================================================

Based on [specific output produced] for [client name]:

1. [PRIORITY] [Action — informed by the specific output]
   WHY: [Reason referencing specific data from the output]
   RUN: "Use kaizen-[skill] to [task with specific parameters]"

2. [RECOMMENDED] [Action]
   WHY: [Reason]
   RUN: "Use kaizen-[skill] to [task]"

3. [OPTIONAL/RECOMMENDED] [Action]
   WHY: [Reason]
   RUN: "Use kaizen-[skill] to [task]"
================================================================
```

### Adaptation Rules

The suggestion logic table above provides the template. When generating actual suggestions:

1. **Replace bracketed placeholders** with real data from the output. "[N] errors" becomes
   "23 errors". "[client]" becomes "Montreal Bike Co."
2. **Reference specific findings.** If the architect spec identified 8 AnyDB objects, say
   "8 AnyDB objects." If the data audit found 847 duplicate SKUs, say "847 duplicate SKUs."
3. **Adjust priority based on timeline.** If cutover is 5 days away, training jumps to
   PRIORITY even if it would normally be RECOMMENDED.
4. **Skip suggestions that don't apply.** If the engagement doesn't include AnyDB, don't
   suggest kaizen-architect. If the client is on Basic plan, don't suggest Flows that
   require Grow.
5. **Add kaizen-finance suggestion after any completed engagement.** Engagement P&L should
   be calculated for every completed project.

---

## Common Failures in Suggestions

**1. Generic suggestions without context.**
"Consider running data prep" is useless. "Run kaizen-dataprep on the Lightspeed product export
(4,200 records, 847 duplicate SKUs identified in the audit)" is actionable.

**2. Too many suggestions.**
Four or five suggestions create decision paralysis. Three maximum. If more actions are needed,
the PRIORITY one should subsume or sequence the others.

**3. Suggesting skills that already ran.**
If kaizen-dataprep already processed the product export, don't suggest it again unless there
is new data or corrections to apply. Reference the specific new input that warrants a re-run.

**4. Missing the finance suggestion post-engagement.**
Every completed engagement should trigger an engagement P&L suggestion. This is how the agency
learns whether its pricing is correct. Skipping it means flying blind on margins.

**5. Not adjusting for timeline pressure.**
Suggestions should reflect urgency. If cutover is in 3 days, hardware validation is PRIORITY,
not OPTIONAL. The suggestion engine must be aware of timeline context when available.

---

## Verification

<verification id="proactive-verify">
When reviewing suggestions appended to any skill output:

1. **Maximum 3 suggestions:** No more. Trim to the highest-impact three.
2. **Every suggestion references a specific skill:** Not "consider next steps" but
   "Use kaizen-[skill] to [specific task]."
3. **Suggestions use specific data from the output:** Record counts, client names,
   issue counts, tier names, dates.
4. **Priority levels are correct:** PRIORITY = blocks progress. RECOMMENDED = should do soon.
   OPTIONAL = nice to have.
5. **No duplicate skill suggestions:** Each skill appears at most once in the suggestion block.
6. **Finance P&L suggested after completed engagements:** Every time.
7. **Memory save suggested after major deliverables:** Blueprint reports, proposals,
   architecture specs, completed migrations.
8. **Timeline-aware:** If cutover date or deadline is known, suggestions reflect urgency.
9. **Inapplicable suggestions excluded:** No AnyDB build suggestions when AnyDB has been
   explicitly ruled out. For DTC/B2B commerce systems, consider the AnyDB operating-layer
   opportunity before deciding it is out of scope. No Grow-plan Flow suggestions if client is on Basic.
10. **Voice check:** Suggestions are direct and actionable, not vague or padded.
</verification>
