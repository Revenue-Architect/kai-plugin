# KaizenCommerce Antigravity CLI Delegation Reference

Reference file for the kaizen-commerce-expert skill. `SKILL.md` keeps only the compact
Antigravity routing table. This file carries the full Antigravity CLI task contract, delegation
recommendation logic, review loop, and token economics.

Load this file when the operator asks whether to use Antigravity CLI vs Codex subagents, asks for an
Antigravity CLI prompt, reports Antigravity CLI output, or asks for corrected Antigravity instructions.

---

## Core Model

KaizenCommerce uses a deliberate split:

- **Kai / Codex / ChatGPT:** architect, strategist, reviewer, source-of-truth decision maker,
  client-facing voice, pricing guardrail, and final QA.
- **Codex subagents:** explicit specialist or parallel agents for higher-reasoning research,
  architecture, review, QA, MCP-backed docs checks, and independent workstreams.
- **Antigravity CLI:** explicit-only execution lane for bounded local execution, research gathering,
  script work, data cleanup, API payload prep, log parsing, and migration artifact preparation
  in a terminal workspace.

Antigravity CLI is never invoked automatically. Kai may discuss or recommend it when the operator asks
for Antigravity, Antigravity CLI, an Antigravity prompt, usage-saving options, or a recommendation that
specifically compares Antigravity against subagents. An Antigravity CLI task block is output only when
the operator explicitly asks to use Antigravity/Antigravity CLI or asks for the Antigravity prompt.

When the operator explicitly requests delegated execution, try `agy` first. If Antigravity is
unavailable, unusable, or quota-blocked, use Grok Build CLI (`grok`) before built-in subagents. Never
claim that either CLI ran without actual output from that CLI.

## Recommendation vs Invocation

Keep these behaviors separate:

- A **recommendation** tells the operator which lane fits the task. It does not output an Antigravity CLI
  task block unless he asked for the actual Antigravity prompt.
- An **invocation** outputs a paste-ready `ANTIGRAVITY CLI TASK` block for the operator to run in the
  Antigravity CLI.

When the operator asks for subagents, parallel agents, or the optimized Kaizen specialist workflow
without naming Antigravity, first apply the explicit external-lane order above. If neither `agy`
nor `grok` is usable, use the global Kaizen specialist subagent workflow; do not silently invoke an
external CLI without the operator's explicit delegation request.

### Delegation Recommendation

Use this compact format when the operator asks which lane to use:

```markdown
### Delegation Recommendation
**Recommended lane:** Antigravity CLI / Codex subagent / Kai only / Hybrid
**Why:** [task-specific reason]
**Usage impact:** [OpenAI/Codex usage implication]
**Risk:** [what could go wrong]
**Next action:** [recommendation only, or exact Antigravity CLI block if explicitly requested]
```

### Decision Model

Recommend **Antigravity CLI** when the task is local, bounded, execution-heavy, research-gathering,
or easy to verify: file edits from a clear plan, CSV/data cleanup, API payload preparation,
local ETL scripts, source documentation collection, test runs, scaffolding, repetitive
transformations, log parsing, smoke tests, or implementation grunt work. This is the default
usage-saving recommendation because it shifts execution away from OpenAI/Codex usage and
toward Antigravity/Google agent quota usage.

Recommend **Codex/ChatGPT subagents** when the task benefits from stronger reasoning,
parallel investigation, specialist Kaizen skills, MCP-backed docs, code review, ambiguity
handling, architecture analysis, security/test-gap review, or multiple independent
workstreams. Call out that this consumes more OpenAI/Codex usage than Antigravity CLI but is the
better quality choice for reasoning-heavy work.

Recommend **Kai only** when the task is strategic, commercial, client-facing,
pricing-related, source-of-truth architecture, final synthesis, or quality verdict work.

Recommend **Hybrid** for larger workflows: Kai plans, Antigravity CLI executes bounded work, Kai
validates, and Codex subagents are used only for high-risk review or specialist analysis.

## Antigravity CLI Task Contract

When the operator explicitly asks for Antigravity CLI execution, output one task block per bounded job.
Make every decision before writing the block. Antigravity CLI should not infer architecture,
broaden scope, change unrelated files, invent requirements, or silently skip validation.

```markdown
=== ANTIGRAVITY CLI TASK - [client/project] - [task title] ===
**Working directory:** [absolute path]
**Goal:** [one sentence]
**Allowed files/paths:** [exact paths Antigravity may read/write]
**Do not touch:** [unrelated files, secrets, git history, production systems]
**Context:** [minimum facts Antigravity needs]
**Instructions:**
1. [specific step]
2. [specific step]
3. [specific step]
**Commands to run:** [exact commands, or "none"]
**Validation required:** [exact checks/tests]
**Output back to Kai:** [exact response structure]
**Stop conditions:** [when to stop instead of guessing]
=== END ANTIGRAVITY CLI TASK ===
```

After outputting an invocation block, end with:

```markdown
the operator: run `agy --sandbox --dangerously-skip-permissions --print` from the stated working
directory with the task block above as the prompt. When it finishes, paste Antigravity's
summary and any changed file list back here, and I'll verify it.
```

### CLI Invocation Preference

the operator's current default is to use Antigravity CLI through `agy`, including
`--dangerously-skip-permissions` for fewer interruptions. Kai may include that flag in
Antigravity handoffs, but the task contract still must narrow allowed paths, forbid secrets,
forbid production writes, and require reviewable output. Prefer this command shape:

```bash
agy --sandbox --dangerously-skip-permissions --print "$(cat TASK.md)"
```

Use `--add-dir /absolute/path` only when a bounded task genuinely needs another directory.
Do not use permission flags as a substitute for scope discipline.

### Required Prompt Discipline

Every Antigravity CLI task must include:

1. **Exact working directory.** Use an absolute path.
2. **Allowed files/paths.** Name the only files or directories Antigravity may read or edit.
3. **Do-not-touch list.** Include unrelated files, secrets, git history, production systems,
   and any client data that should not be modified.
4. **Specific instructions.** Avoid "clean this up" or "map appropriately." State exact
   mappings, steps, edge cases, and expected behavior.
5. **Validation commands.** Tell Antigravity exactly what to run and what to do if a check fails.
6. **Output contract.** Require a concise summary, changed file list, commands run, test
   results, and blockers.
7. **Stop conditions.** Antigravity must stop when scope is unclear, required files are missing,
   tests need credentials, commands would touch production, or it would need to modify files
   outside the allowed paths.

## What Antigravity CLI May Do

Good Antigravity CLI tasks:

- Create or edit files from a Kai-approved implementation plan.
- Run local tests, checks, builds, scripts, and smoke tests.
- Clean or transform CSV/data files with exact mapping rules.
- Prepare API payload JSONL, retry files, normalized staging data, or local ETL scripts from a
  Kai-approved migration spec.
- Gather raw research evidence, source URLs, and short excerpts for Kai to verify.
- Parse logs or generated reports and summarize the concrete findings.
- Scaffold low-risk helper scripts or fixtures.
- Perform repetitive changes across a bounded file set.
- Produce a structured `manifest.json` for Kai review.

Do not use Antigravity CLI for:

- Client-facing final writing.
- Pricing, tier, scope, ROI, or commercial recommendations.
- Shopify/AnyDB/source-of-truth architecture decisions.
- Migration lane selection. Kai decides whether the lane is `api_to_api`, `matrixify_csv`,
  `shopify_admin_csv`, or `hybrid`.
- Final migration verdicts or QA sign-off.
- Ambiguous implementation where the plan still needs real reasoning.
- Anything that requires secrets, production credentials, production writes, destructive git
  operations, or broad filesystem access.
- Updating `CONTEXT.md` or making the result authoritative without Kai review.

For KaizenCommerce web research, prefer Kai with the approved research tools and current docs.
Use Antigravity CLI for web work only if the operator explicitly asks for Antigravity to gather raw evidence,
or if Kai is writing a bounded evidence-collection task. Require source URLs, short exact
snippets where useful, confidence flags, and a verification summary for Kai to review.

## Gated Run Folder Workflow

Use this structure for larger Antigravity-assisted work:

```text
runs/[date]-[client]-[task]/
  TASK.md
  antigravity/
    manifest.json
    memory_delta.json
    evidence/
    outputs/
  kai/
    REVIEW.md
    context-delta.md
  APPROVAL.md
```

Antigravity returns `manifest.json`, not a prose-only summary:

```json
{
  "status": "COMPLETE | NEEDS_REVIEW | BLOCKED",
  "migration_lane": "api_to_api | matrixify_csv | shopify_admin_csv | hybrid",
  "files_processed": [],
  "files_changed": [],
  "api_surfaces": [],
  "shopify_dev_mcp_checks_needed": [],
  "commands_run": [],
  "validation_results": [],
  "sources": [],
  "blockers": [],
  "notes_for_kai": []
}
```

When the work creates durable client or engagement context, Antigravity also returns
`memory_delta.json` using the schema from `reference/kaizen-memory-architecture.md`. Antigravity
must not edit authoritative memory directly. Kai reviews the manifest, inspects artifacts,
calls Shopify Dev MCP or Exa where needed, applies the reviewed memory delta with
`scripts/kaizen-memory-apply-delta.py`, and returns PASS / PASS WITH NOTES / FAIL.

Minimal `memory_delta.json` shape:

```json
{
  "client": "Client Name",
  "client_slug": "client-name",
  "source": "antigravity",
  "summary": "One sentence describing what changed.",
  "profile_updates": {},
  "state_updates": {},
  "events": [],
  "decisions": [],
  "sources": [],
  "notes": []
}
```

## Reviewing Antigravity CLI Output

When the operator pastes Antigravity CLI output back into the conversation, do not trust it by default.
Review it before consuming any result:

1. **Check the summary.** Antigravity should report changed files, commands run, validation
   results, skipped steps, and blockers. If this is missing, ask for that summary before
   trusting the work.
2. **Inspect the actual files or output artifacts** whenever available in the local
   workspace.
3. **Inspect `memory_delta.json`** when present. Confirm it contains no secrets, does not
   contradict known client memory, and only proposes updates Kai can verify.
4. **Run relevant checks directly** when the environment allows it.
5. **Apply approved memory deltas** with `scripts/kaizen-memory-apply-delta.py`, then run
   `scripts/kaizen-memory-consolidate.py` when the engagement state changed materially.
6. **Give a verdict inline:**
   - **PASS** - usable as-is.
   - **PASS WITH NOTES** - usable, but caveats need to be called out.
   - **FAIL** - do not use; output a corrective Antigravity CLI task block if Antigravity should fix it.

For migration or data tasks, spot-check critical mappings before PASS:

- Migration lane matches Kai's approved lane.
- Handle generation is URL-safe, lowercase, and hyphenated.
- Variant grouping uses the intended option names and values.
- SKU, barcode, phone, and email formatting are preserved.
- Metafield namespace, key, type, and value format match the plan.
- Row counts, dropped rows, and confidence flags are reported.
- API payloads have idempotency keys, retry/dead-letter behavior, validation outputs, and no
  secrets or production credentials.

## Correction Blocks

If Antigravity CLI gets it wrong, write a new `ANTIGRAVITY CLI TASK` block for the same working
directory. The correction must state:

- The exact failure.
- The exact file, row, field, command, or behavior that is wrong.
- The expected correction.
- The allowed files/paths.
- The validation command Antigravity must rerun.
- The required output summary.

Do not let Antigravity make a second attempt from vague feedback like "try again" or "fix the
mapping." It needs concrete instructions.

## Feedback Loop

```text
Kai outputs recommendation, if asked
Kai outputs ANTIGRAVITY CLI TASK, only when explicitly requested
the operator runs task in Antigravity CLI
the operator pastes Antigravity output back to Kai
Kai inspects and validates locally where possible
Kai returns PASS / PASS WITH NOTES / FAIL
If FAIL, Kai outputs a corrective ANTIGRAVITY CLI TASK
```

## Token Economics

The split exists to conserve OpenAI/Codex usage without lowering quality:

| Without Antigravity CLI | With Antigravity CLI |
|---|---|
| Kai spends tokens doing repetitive local execution or raw evidence gathering | Kai writes a tight task block and validates the result |
| Codex subagents consume OpenAI tokens for low-judgment grunt work | Antigravity handles bounded execution when quality risk is low |
| Main thread fills with logs and intermediate noise | Antigravity returns a distilled summary for Kai to verify |

## API Migration Task Example

```markdown
=== ANTIGRAVITY CLI TASK - [client/project] - API payload prep ===
**Working directory:** [absolute path]
**Goal:** Build normalized API payload files from the approved source export.
**Allowed files/paths:** [source export copy], [output directory], [script path]
**Do not touch:** secrets, production systems, git history, files outside the allowed paths
**Context:** Kai selected `api_to_api` as the migration lane. Shopify API operation details must
be verified by Kai through Shopify Dev MCP before production use.
**Instructions:**
1. Read the source export copy only.
2. Generate normalized JSONL payloads using the provided field mapping and idempotency keys.
3. Write failed or ambiguous records to `retry_queue.jsonl` with row numbers and reasons.
4. Write `manifest.json` using the required schema.
**Commands to run:** [exact local test commands]
**Validation required:** count source rows, output rows, retry rows, duplicate idempotency keys,
and required-field completeness.
**Output back to Kai:** changed files, commands run, validation results, blockers, and
`manifest.json`.
**Stop conditions:** missing required fields, unclear merge keys, need for credentials, or any
production write.
=== END ANTIGRAVITY CLI TASK ===
```

Use Codex subagents anyway when the task needs stronger reasoning, specialist skills, or
parallel analysis. Saving usage is not worth outsourcing judgment-heavy Kaizen decisions.

## Skill Routing Additions

| User says | Action |
|---|---|
| "should I use Antigravity or a subagent", "recommend a delegation lane", "what saves Codex usage here" | Output the Delegation Recommendation format only |
| "delegate this to Antigravity", "use Antigravity CLI", "give me an Antigravity CLI prompt", "have Antigravity handle this" | Output an `ANTIGRAVITY CLI TASK` block |
| "here's what Antigravity returned", "Antigravity is done, here's the output" | Review the output and give PASS / PASS WITH NOTES / FAIL |
| "Antigravity got it wrong, fix the instructions" | Output a corrective `ANTIGRAVITY CLI TASK` block |
| "what would you send Antigravity for this" | Draft a preview `ANTIGRAVITY CLI TASK` block without assuming it has been run |
