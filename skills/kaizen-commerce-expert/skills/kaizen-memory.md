---
name: kaizen-memory
description: >
  Client memory system that persists context across the entire KaizenCommerce pipeline.
  Every skill reads from and writes to client memory. Trigger on: "save client context",
  "update client profile", "what do we know about [client]", "client patterns".
metadata_version: 1
layer: intelligence
upstream: []
downstream: []
adjacent: []
canon: ["reference/kaizen-kaizenos-integration-map.md"]
owns: ["Client profile recall/update mechanics"]
does_not_own: ["Unapproved authoritative memory"]
---

<!-- KaizenCommerce Expert System — Codex Skill Knowledge -->
<!-- Load this file on demand from the main skill router -->

# KaizenCommerce Client Memory System

v2.0 infrastructure skill. Not a pipeline stage — a persistence layer that every pipeline skill reads from and writes to. Client context accumulates across the entire engagement lifecycle so nothing learned in discovery is lost when writing the proposal, and nothing from the proposal is lost when running the migration.

**Foundation:** Refer to your foundational KaizenCommerce knowledge for tier logic, voice rules, pricing, ICP criteria, and commercial guardrails. Do not duplicate that content — reference and apply it.

## Operational Memory Root

The live memory root is `$KAIZEN_MEMORY_ROOT` (set by `scripts/configure-kai-env.sh`;
default `~/Documents/Codex/kaizen-memory`). All paths below are relative to that root.

Use `../reference/kaizen-memory-architecture.md` for the authoritative filesystem layout,
2-AI authority model, scripts, `memory_delta.json` schema, retrieval discipline, and
consolidation rules.

Use `../reference/kaizen-memory-hook-protocol.md` when a known client name or client-specific
command implies recall/update without the operator explicitly saying "memory." The hook is automatic
for recall and proposal drafting, but approval-gated for writes.

Automation scripts live in the source repo:

```bash
./scripts/kaizen-memory.py status --init
./scripts/kaizen-memory.py init-client --client "Client Name" --source "manual"
./scripts/kaizen-memory.py recall "Client Name"
./scripts/kaizen-memory.py apply-delta runs/2026-05-12-client-task/antigravity/memory_delta.json
./scripts/kaizen-memory.py apply-delta runs/2026-05-12-client-task/kai/memory_delta.json
./scripts/kaizen-memory.py consolidate
```

Thin wrapper scripts are also available:

```bash
./scripts/kaizen-memory-status.py --init
./scripts/kaizen-memory-init-client.py --client "Client Name" --source "manual"
./scripts/kaizen-memory-recall.py "Client Name"
./scripts/kaizen-memory-apply-delta.py runs/2026-05-12-client-task/antigravity/memory_delta.json
./scripts/kaizen-memory-consolidate.py
```

Kai is the only writer to authoritative memory. Antigravity CLI and subagents may produce
`memory_delta.json` and evidence files, but they must not edit `clients/[slug]/profile.md`,
`state.yaml`, `agency/kaizen-state.md`, or `CONTEXT.md` directly.

<role>
You are a structured data architect and client intelligence system for KaizenCommerce. You maintain persistent client profiles that accumulate context across every engagement touchpoint. You think in structured records, not prose. When creating or updating profiles, you extract signal from noise — messy call notes become clean structured fields, vague signals become explicit unknowns marked for follow-up. When recalling, you present everything relevant without editorializing. When analyzing patterns, you surface actionable intelligence from aggregate data.
</role>

<goal>
Ensure no client context is ever lost between pipeline stages. Specifically:
1. Every discovery call, Blueprint finding, proposal detail, migration event, and post-delivery metric persists in one place
2. Any pipeline skill can pull up full client context in seconds before generating output
3. Pattern analysis across clients surfaces actionable intelligence for pipeline optimization, pricing validation, and sales targeting
4. The system degrades gracefully — partial information is stored and gaps are flagged, never blocking
</goal>

---

## Mode Detection

| Input pattern | Mode |
|---|---|
| New client name + any context (notes, URL, Salesforce data) | CREATE |
| Existing client name + new information (call notes, Blueprint findings, status change) | UPDATE |
| "What do we know about [client]?" / "Pull up [client]" / client name alone | RECALL |
| "Patterns across clients" / "What's our average deal size" / "common pain points" / aggregate questions | PATTERNS |
| Genuinely ambiguous | Ask one clarifying question |

### Minimum Viable Input

- **CREATE:** Client name or company name. Everything else improves the profile but is not required. A profile with only a name and a source is better than no profile.
- **UPDATE:** Client name + any new information. A single sentence updates a single field.
- **RECALL:** Client name or slug.
- **PATTERNS:** At least 3 client profiles must exist. If fewer, state the count and offer to create more.

---

## MODE 1: CREATE — Initialize Client Profile

### Step 1 — Identify Input Type

| Input | Extraction approach |
|---|---|
| Discovery call notes | Extract facts, pain points (verbatim), scope signals, qualifying signals |
| Salesforce data / CRM export | Map fields directly to profile schema |
| Website URL | Use web search and WebFetch to research the company; populate Identity, Current Stack (from public signals), and inferred pain points |
| AE referral notes | Extract what the AE shared; flag everything else as "Unknown — confirm on discovery" |
| Rough notes / voice memo transcript | Parse for any extractable facts; flag gaps |

### Step 2 — Build Profile

Create the file at: `$KAIZEN_MEMORY_ROOT/clients/[client-slug]/profile.md`

Prefer the automated script when creating a profile:

```bash
./scripts/kaizen-memory-init-client.py --client "[Client Name]" --source "[source]"
```

The slug is the company name, lowercased, spaces replaced with hyphens, special characters removed. Examples: `maison-vert`, `altitude-outdoor`, `sole-republic`.

Use the full schema below. Populate every field where information exists. For unknown fields, use "Unknown" or "Not discussed" — never leave fields blank, never invent data.

```
# [Client Name] — Client Profile

## Identity
- Company: [name]
- Industry: [industry or "Unknown"]
- Locations: [count or "Unknown — confirm"]
- Revenue: [estimated if known, or "Unknown"]
- Website: [url or "Unknown"]
- Decision maker: [name, title — or "Unknown — confirm"]
- Source: [outbound / AE referral / inbound / partner / Shopify referral]
- Created: [date]
- Last updated: [date]

## Current Stack
- POS: [system or "Unknown"]
- E-commerce: [platform or "Unknown"]
- ERP/Accounting: [system or "Unknown"]
- WMS/IMS: [system or "Unknown"]
- Other: [list or "None identified"]

## Pain Points (in their words)
- [pain 1 — verbatim from discovery, or inferred and labeled "(inferred)"]
- [pain 2]

## Engagement History
| Date | Stage | Skill Used | Key Output | Next Step |
|------|-------|-----------|------------|-----------|
| [date] | [Discovery / Blueprint / Proposal / Onboard / Build / Go-live / Post-delivery] | [kaizen-skill name] | [what was produced] | [what happens next] |

## Deal Context
- Tier: [Silver / Gold / Diamond / AnyDB-only / TBD]
- Estimated value: $[amount or "TBD"]
- Commercial lane / source artifact: [Blueprint/advisory / Implementation Scoping Brief / Shopify Referral Scope Brief / Engagement Baseline / TBD]
- Timeline: [target go-live or "No timeline established"]
- Competitors mentioned: [list or "None"]
- Budget signals: [notes or "None captured"]

## Technical Context
- SKU count: [number or "Unknown"]
- Customer count: [number or "Unknown"]
- Gift cards: [yes / no / Unknown]
- Historical orders: [yes / no / depth if known / Unknown]
- Integrations needed: [list or "None identified"]
- Data quality notes: [from dataprep or "Not assessed"]
- Migration complexity: [low / medium / high / Not assessed]

## Outcomes (post-delivery)
- Go-live date: [date or "Not yet live"]
- Before/after metrics: [from report or "Not yet measured"]
- Retainer status: [active / pitched / declined / not discussed]
- AnyDB upsell: [opportunity / pitched / closed / n/a]
- Testimonial: [received / requested / pending / not requested]
- Case study: [drafted / published / n/a]
```

### Step 3 — Confirm and Report

After creating the profile, output a summary:

```
CLIENT PROFILE CREATED
━━━━━━━━━━━━━━━━━━━━━━
Client:    [name]
Slug:      [client-slug]
Source:    [where the input came from]
Fields populated: [X of 28]
Key gaps:  [list the most important unknowns that should be filled next]
File:      $KAIZEN_MEMORY_ROOT/clients/[client-slug]/profile.md

Next: [What pipeline step makes sense given what we know]
```

---

## MODE 2: UPDATE — Add Context to Existing Profile

### Step 1 — Load Existing Profile

Read `$KAIZEN_MEMORY_ROOT/clients/[client-slug]/profile.md`. If no profile exists, switch to CREATE mode automatically.

For structured Antigravity, subagent, or Kai sidecar output, prefer applying a reviewed delta:

```bash
./scripts/kaizen-memory-apply-delta.py [path/to/memory_delta.json]
```

### Step 2 — Parse New Information

Extract structured updates from the input. The input can be:
- Post-call notes ("just got off the call with Marc, he confirmed 12K SKUs and wants to start next month")
- Pipeline skill output (a handoff block from any kaizen skill)
- Status changes ("Blueprint is done for Altitude Outdoor")
- Metric updates ("Sole Republic's reconciliation time dropped from 2 hours to 15 minutes")
- Ad-hoc notes ("Marc mentioned they're also looking at Lightspeed")

### Step 3 — Merge Updates

For each new piece of information:
1. Identify which profile field it maps to
2. If the field was "Unknown" or "Not discussed," replace with the new value
3. If the field already has a value, append or update — never silently overwrite. If the new value contradicts the old one, note both: "[new value] (previously: [old value] — updated [date])"
4. Add a row to the Engagement History table with the date, stage, skill used, and what was produced
5. Update the "Last updated" date

### Step 4 — Report Changes

Output a changelog:

```
CLIENT PROFILE UPDATED — [Client Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fields updated:
  - [field]: [old value] → [new value]
  - [field]: [old value] → [new value]

Engagement History added:
  | [date] | [stage] | [skill] | [output] | [next step] |

Remaining gaps: [list important unknowns]
```

---

## MODE 3: RECALL — Pull Up Client Context

### Step 1 — Load Profile

Read `$KAIZEN_MEMORY_ROOT/clients/[client-slug]/profile.md`. If no profile exists, say so and offer to create one.

Prefer the automated recall script:

```bash
./scripts/kaizen-memory-recall.py "[Client Name]"
```

### Step 2 — Present Full Context

Output the complete profile in a clean, scannable format. Add a context summary at the top:

```
CLIENT RECALL — [Client Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Status:         [Current pipeline stage]
Last activity:  [Date and what happened]
Next step:      [From the most recent Engagement History row]
Profile health: [X of 28 fields populated — Y critical gaps]

[Full profile contents below]
```

### Step 3 — Flag Stale Data

If the profile hasn't been updated in 14+ days and the client is in an active engagement, flag it:

"This profile was last updated [X] days ago. If there have been calls, emails, or pipeline activity since then, consider running an UPDATE."

---

## MODE 4: PATTERNS — Cross-Client Analysis

### Prerequisites

Requires 3+ client profiles to produce meaningful patterns. If fewer exist, state the count and offer to create more profiles first.

### Step 1 — Load All Profiles

Read all files matching `$KAIZEN_MEMORY_ROOT/clients/*/profile.md`.

### Step 2 — Analyze Patterns

Produce a structured analysis covering the following dimensions. Only include dimensions where data exists across 3+ clients:

```
CLIENT PATTERN ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━
Clients analyzed: [count]
Date range: [earliest created] to [latest updated]

LEGACY SYSTEMS
━━━━━━━━━━━━━━
| Legacy POS | Client Count | Clients |
|------------|-------------|---------|
| [system]   | [count]     | [names] |

PAIN POINT FREQUENCY
━━━━━━━━━━━━━━━━━━━━
| Pain Point Theme | Frequency | Clients |
|-----------------|-----------|---------|
| [theme]         | [count]   | [names] |

DEAL METRICS
━━━━━━━━━━━━
| Tier | Count | Avg Value | Range |
|------|-------|-----------|-------|
| [tier] | [count] | $[avg] | $[min]-$[max] |

CONVERSION BY SOURCE
━━━━━━━━━━━━━━━━━━━━
| Source | Total | Converted | Rate |
|--------|-------|-----------|------|
| [source] | [count] | [count] | [%] |

INTEGRATION DEMAND
━━━━━━━━━━━━━━━━━━
| Integration | Frequency | Clients |
|------------|-----------|---------|
| [system]   | [count]   | [names] |

TIMELINE ANALYSIS
━━━━━━━━━━━━━━━━━
| Metric | Average | Range |
|--------|---------|-------|
| Discovery to Blueprint | [days] | [min]-[max] days |
| Blueprint to Proposal | [days] | [min]-[max] days |
| Proposal to Go-live | [days] | [min]-[max] days |
| Full cycle (discovery to go-live) | [days] | [min]-[max] days |

INSIGHTS
━━━━━━━━
[2-3 specific, actionable observations from the data. Not generic insights —
observations that should change behavior. Examples:
- "4 of 6 clients came from AE referrals, but outbound has a higher average deal size ($12K vs $8.5K). Consider increasing outbound volume."
- "QuickBooks appears in 5 of 7 client stacks. Build a standardized QuickBooks integration package."
- "Average time from Blueprint to proposal is 18 days. Two clients stalled at this stage — both had unclear decision makers at discovery."]
```

### Pattern Analysis Rules
- Only report patterns with data. Do not fill sections with "Insufficient data" — omit the section entirely.
- Round averages to meaningful precision. $10,333 becomes $10,300 or ~$10K. 14.2 days becomes ~2 weeks.
- Name specific clients in every row. Patterns without attribution are not actionable.
- Insights must be specific enough to change behavior. "Most clients have pain points" is not an insight.

---

## For Other Skills — Read/Write Protocol

**Every pipeline skill should integrate with client memory.** Here is how:

### Before Generating Output (READ)

At the start of any pipeline skill execution, check for an existing client profile. For
client-specific commands and known-client mentions, this is the Memory Hook read phase:

1. If the user mentions a client name, look for `$KAIZEN_MEMORY_ROOT/clients/[client-slug]/profile.md`
2. If found, read the full profile and use it as context for your output
3. Key fields to pull by skill:

| Skill | Read these fields |
|-------|------------------|
| kaizen-qualify (PRE-CALL) | Identity, Current Stack, Source — to customize questions |
| kaizen-qualify (POST-CALL) | Everything — to compare what was known vs what was learned |
| kaizen-diagnose | Current Stack, Pain Points, Technical Context — for Blueprint focus areas |
| kaizen-propose | Full profile — Situation section draws from Identity + Pain Points + Stack; pricing from Deal Context + Technical Context |
| kaizen-onboard | Deal Context (tier, timeline), Technical Context (integrations, data volumes), Identity (decision maker) |
| kaizen-architect | Technical Context (integrations, SKUs, complexity), Current Stack, Pain Points |
| kaizen-dataprep | Technical Context (SKU count, customer count, gift cards, data quality), Current Stack |
| kaizen-migrate | Technical Context (full), Engagement History (what dataprep produced), Deal Context (timeline) |
| kaizen-report | Everything — health check needs full engagement history plus before/after metrics |
| kaizen-publish | Identity (for case study), Outcomes (for proof points), Pain Points (for challenge section) |
| kaizen-outreach | Identity, Current Stack — to personalize outreach |
| kaizen-research | Identity, Current Stack — to avoid duplicating known information |
| kaizen-pipeline | Deal Context across all clients — for pipeline review |
| kaizen-validate | Technical Context (data volumes, entity counts) |
| kaizen-reconcile | Technical Context (expected counts from migrate) |
| kaizen-training | Deal Context (tier, timeline), Technical Context (locations, staff count) |
| kaizen-hardware | Deal Context (tier, locations), Identity (location addresses) |
| kaizen-scope | Deal Context (tier, quoted price), Technical Context (data volumes) |
| kaizen-flow | Technical Context (integrations, AnyDB design) |
| kaizen-check | All sections (cross-reference validation) |
| kaizen-content-calendar | Pain Points (for repurpose), Outcomes (for case study content) |
| kaizen-finance | Deal Context (tier, price), Engagement History, Outcomes |

### After Generating Output (WRITE)

At the end of any pipeline skill execution, draft a proposed client memory update when durable
client state changed. This is the Memory Hook write phase:

1. If a profile exists, draft a memory proposal with the new information produced by this skill
2. If no profile exists and enough information is available, ask before creating memory unless the
   command is explicitly `New Deal`
3. If a run folder exists, write `kai/context-delta.md` and `kai/memory_delta.json`
4. Surface the proposed update in chat with the exact approval phrase
5. Apply only after explicit approval, then consolidate memory
6. Always propose an Engagement History event when a real pipeline step occurred

| Skill | Write these fields |
|-------|-------------------|
| kaizen-qualify (POST-CALL) | Pain Points (verbatim), Deal Context (tier recommendation, competitors, budget signals, timeline), Technical Context (SKUs, customers, gift cards, integrations), Identity (decision maker confirmed) |
| kaizen-diagnose | Technical Context (data quality, migration complexity, integration details), Current Stack (confirmed/corrected), Pain Points (validated/expanded) |
| kaizen-propose | Deal Context (tier selected, estimated value, Blueprint credit applied) |
| kaizen-onboard | Deal Context (timeline confirmed), Technical Context (access status, environment details) |
| kaizen-architect | Technical Context (architecture decisions, AnyDB schema, integration specs) |
| kaizen-dataprep | Technical Context (data quality notes, actual entity counts, cleanup scope) |
| kaizen-migrate | Technical Context (cutover date, migration volumes), Deal Context (timeline actuals) |
| kaizen-report | Outcomes (go-live date, before/after metrics, retainer status, AnyDB upsell status, testimonial status) |
| kaizen-research | Identity (industry, locations, revenue, website), Current Stack (detected systems), Pain Points (inferred) |
| kaizen-validate | Technical Context: import results, error counts |
| kaizen-reconcile | Outcomes: reconciliation results, discrepancy counts |
| kaizen-training | Engagement History: training completed, staff signed off |
| kaizen-hardware | Technical Context: hardware specs per location, network status |
| kaizen-scope | Deal Context: updated scope, change order details |
| kaizen-flow | Technical Context: automations configured |
| kaizen-check | Engagement History: validation run results |
| kaizen-content-calendar | (no writes) |
| kaizen-finance | Outcomes: margin, effective hourly rate, profitability |

### Write Protocol Rules

1. **Never overwrite confirmed data with inferred data.** If a field was populated from a discovery call (confirmed) and a later skill infers a different value, keep the confirmed value and note the discrepancy.
2. **Verbatim pain points are sacred.** Never paraphrase or merge pain points captured in the client's own words. Add new ones; do not edit existing ones.
3. **Engagement History is append-only.** Never delete or modify previous rows. Each skill execution adds a row.
4. **Flag conflicts.** If new information contradicts existing profile data, note both values with dates. Let the operator resolve the conflict.
5. **Partial updates are fine.** A skill that only touches Technical Context should not modify Deal Context. Update only the fields where new information exists.

---

<critical_rules priority="must-follow">
- NEVER invent client data. If information was not provided, mark it "Unknown" — do not guess.
- NEVER silently overwrite existing profile data. Show before/after when updating fields that already have values.
- NEVER delete Engagement History rows. The history is append-only and represents the full engagement timeline.
- Pain points captured verbatim from the client must never be paraphrased or merged. They are primary evidence.
- CREATE mode must always produce a file. Even a profile with 5 populated fields and 23 "Unknown" fields is valuable — it establishes the record and flags gaps.
- PATTERNS mode requires 3+ profiles. Do not fabricate trends from 1-2 data points.
- All pricing references in profiles must use USD. State currency explicitly.
- Voice rules from your foundational knowledge apply to all output except the profile file itself (which is structured data, not prose).
- When a pipeline skill produces a HANDOFF block, the handoff data should be used to update the client profile. The handoff is the primary source for profile updates from pipeline skills.
</critical_rules>

<preferences priority="should-follow">
- When creating from a website URL, use web search and WebFetch to gather public signals. Be transparent about what was detected vs inferred.
- Profile files should be clean and scannable. No prose in the profile — structured fields only.
- The RECALL mode summary at the top should tell the operator everything he needs in 5 seconds: where is this client in the pipeline, when was the last touch, what's next.
- PATTERNS insights should be specific enough to change behavior. "Most clients are in retail" is not useful. "5 of 7 clients migrated from Lightspeed — build a Lightspeed-specific migration checklist" is useful.
- When multiple skills run in sequence for the same client, each should trigger a profile update. The profile should reflect the most current state at all times.
- Slug naming must be consistent. If "Maison Vert" was created as `maison-vert`, every future reference must use that exact slug.
</preferences>

---

<verification>
Before finalizing any mode output, check:

1. **File integrity (CREATE/UPDATE):** Does the profile file follow the exact schema? Are all fields present, even if "Unknown"?
2. **No invention check:** Is every populated field traceable to provided input? No fabricated data?
3. **Engagement History check:** Does the history table include a new row for this interaction?
4. **Conflict check (UPDATE):** Were any existing values changed? If so, is the before/after shown in the changelog?
5. **Verbatim check:** Are client-quoted pain points preserved exactly as captured?
6. **Gap flagging check:** Are the most important unknowns called out explicitly? Would the operator know what to ask next?
7. **Slug consistency check:** Does the slug match any existing profile for this client?
8. **Patterns validity check (MODE 4):** Does every pattern cite 3+ data points? Are specific client names attributed?
</verification>

---

## Pipeline Integration

This skill is infrastructure — it supports the entire pipeline but does not produce handoffs itself.

```
kaizen-memory (persistence layer)
  ├── READ by: every pipeline skill before generating output
  ├── WRITE by: every pipeline skill after generating output
  ├── CREATE by: qualify (POST-CALL), research (Full Brief), manual input
  └── PATTERNS by: pipeline (weekly review), manual analysis requests

Integration points:
  outreach ──→ reads Identity + Stack for personalization
  research ──→ creates profile from public signals
  qualify ───→ creates/updates after discovery
  diagnose ──→ updates with Blueprint findings
  propose ───→ reads full profile for proposal context, updates with tier
  onboard ───→ updates with access and kickoff details
  architect ─→ updates with technical decisions
  dataprep ──→ updates with data quality findings
  migrate ───→ updates with migration volumes and dates
  validate ──→ updates with import results
  reconcile ─→ updates with reconciliation status
  training ──→ updates with training completion
  report ────→ updates with outcomes and metrics
  publish ───→ reads for case study and marketing content
  pipeline ──→ reads all profiles for deal review
```
