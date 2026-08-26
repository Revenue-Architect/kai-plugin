# Kaizen Specialist Registry

Shared registry for Kai and `kaizen-subagent-orchestrator`. Load this when the user explicitly
asks for subagents, delegation, parallel agent work, or the optimized Kaizen subagent workflow.

## Global Specialist Subagents

the operator's preferred KaizenCommerce workflow uses real global skills as specialist subagent
contracts when subagents make logical sense. These skills are installed globally, not embedded
inside this Kai bundle:

| Specialist | Installed skill path | Use for |
|---|---|---|
| `kaizen-subagent-orchestrator` | `~/.codex/skills/kaizen-subagent-orchestrator/SKILL.md` | splitting Kaizen work across bounded specialist subagents |
| `kaizen-retail-research` | `~/.codex/skills/kaizen-retail-research/SKILL.md` | merchant research, tech-stack detection, partner/app research, current-doc verification |
| `kaizen-retail-architecture` | `~/.codex/skills/kaizen-retail-architecture/SKILL.md` | source-of-truth design, build-vs-buy, POS/ERP/WMS architecture |
| `kaizen-anydb-schema` | `~/.codex/skills/kaizen-anydb-schema/SKILL.md` | AnyDB Types, Cells, formulas, Attach vs Reference, schema QA |
| `kaizen-shopify-migration` | `~/.codex/skills/kaizen-shopify-migration/SKILL.md` | migration strategy, API-first mapping, Matrixify fallback, cutover planning, historical import design |
| `kaizen-migration-qa` | `~/.codex/skills/kaizen-migration-qa/SKILL.md` | API job QA, Dry Run triage, import QA, reconciliation, discrepancy remediation |
| `kaizen-shopify-flow` | `~/.codex/skills/kaizen-shopify-flow/SKILL.md` | Shopify Flow capability checks, workflow design, Flow vs AnyDB boundary |
| `kaizen-frontend-audit` | `~/.codex/skills/kaizen-frontend-audit/SKILL.md` | storefront UX, merchandising, PDP/cart/BOPIS flow, theme audit |

## Model Policy

Prefer the parent model for Kaizen specialist subagents. This keeps quality aligned with the
main Kai session, including higher-quality parent models such as GPT-5.5 when that is what the
session is already using.

Only set an explicit model override when the user asks for one or the task has a clear
tradeoff:

| Case | Model guidance |
|---|---|
| high-stakes architecture, migration, AnyDB schema, or client-facing strategy | inherit parent model |
| broad retail research where source synthesis matters | inherit parent model unless user asks to economize |
| low-risk visual or frontend heuristic pass | `gpt-5.4-mini` is acceptable only when speed/cost matters more than depth |
| independent QA pass on migration evidence | inherit parent model unless the user explicitly asks for a cheaper checker |

Do not force a lower model just because a specialist exists. Token savings should mainly come
from narrower context and bounded prompts, not from weakening the reasoning model.

## When To Spawn

Use `kaizen-subagent-orchestrator` when the current request explicitly asks for subagents,
delegation, parallel agents, or the optimized Kaizen subagent workflow. The standing goal is to
reduce main-context token load without reducing quality. Do not spawn agents for every large
task by habit.

Good spawn candidates:
- independent research, QA, audit, or architecture slices that can run while Kai works locally
- workstreams with different evidence sources, such as retail research plus migration QA
- review passes where an independent specialist can catch mistakes before Kai ships the answer
- bounded implementation slices with non-overlapping file ownership

Keep local:
- the immediate blocking decision the next step depends on
- final client-facing synthesis, commercial positioning, scope, pricing, and verdicts
- tasks that are faster to complete than to delegate

## Delegation Rules

- Keep the immediate blocking task local when the next step depends on it right now.
- Delegate only bounded slices with clear ownership and a concrete deliverable.
- Do not spawn two agents with overlapping write responsibility.
- Do not ask one subagent to solve the entire engagement. Break by workstream.
- Reuse `Kai` as the integrating brain. Subagents gather evidence, implement bounded changes, or
  return a narrow recommendation.
- Prefer one to three subagents. More only when the write scopes or research questions are truly independent.

## Preferred Pairings

Use these defaults unless the task clearly needs a different split:

| Workstream | Specialist | Agent type |
|---|---|---|
| merchant or partner research | `kaizen-retail-research` | `default` |
| AnyDB schema or formula design | `kaizen-anydb-schema` | `worker` |
| migration mapping, API-first execution package, Matrixify fallback, or runbook | `kaizen-shopify-migration` | `worker` |
| API job evidence, Matrixify results, or reconciliation | `kaizen-migration-qa` | `worker` |
| storefront or UX audit | `kaizen-frontend-audit` | `default` |
| Flow design or verification | `kaizen-shopify-flow` | `worker` |
| system ownership or architecture critique | `kaizen-retail-architecture` | `worker` |

For coding subtasks, assign file or module ownership explicitly. Tell each worker it is not alone
in the codebase and must not revert others' work.

## Spawn Prompt Requirements

Every Kaizen specialist subagent prompt must explicitly name the global skill to use, for example
`Use $kaizen-retail-research` or `Use $kaizen-anydb-schema`, and must include the installed skill
path when precision matters. Give each subagent one bounded deliverable, the relevant input
facts, source requirements, and clear ownership boundaries.

Prefer the parent model for specialist subagents unless the user asks for a model override or
there is a clear task-specific reason to trade quality, speed, or cost. The orchestrator skill
contains the detailed split policy.

## Prompt Pattern

Use a structure like:

```text
Use subagents for this task.
Keep Kai / $kaizen-commerce-expert as the main orchestrator.

Spawn:
- one default agent using $kaizen-retail-research at
  ~/.codex/skills/kaizen-retail-research/SKILL.md for [bounded research responsibility]
- one worker agent using $kaizen-anydb-schema at
  ~/.codex/skills/kaizen-anydb-schema/SKILL.md for [bounded AnyDB responsibility]
- one worker agent using $kaizen-shopify-migration at
  ~/.codex/skills/kaizen-shopify-migration/SKILL.md for [bounded migration responsibility]

Model policy:
- specialist subagents inherit the parent model by default
- use gpt-5.4-mini only for low-risk frontend heuristic passes when speed/cost matters
- do not override the model for high-stakes architecture, migration, AnyDB, or final strategy
```

## File-Based Handoffs

For substantial delegated work, prefer file-backed outputs under a gated run folder instead of
message-only summaries:

```text
runs/[date]-[client]-[task]/agents/[agent-name]/
  findings.md
  evidence.jsonl
  files_read.txt
```

`findings.md` should be concise and structured. `evidence.jsonl` should preserve exact URLs,
file paths, line references, commands, or validation outputs that Kai may need to inspect.
`files_read.txt` should list important files or docs the agent relied on.

## Subagent Result Schema

When a file handoff is not necessary, ask subagents to return this shape:

```json
{
  "status": "COMPLETE | NEEDS_REVIEW | BLOCKED",
  "finding": "",
  "evidence": [],
  "files_read": [],
  "risks": [],
  "open_questions": [],
  "confidence": "high | medium | low",
  "recommended_kai_action": ""
}
```

## Output Contract

When this skill is active, the main agent should:
- state the delegation split briefly
- keep the orchestration concise
- integrate subagent results into one answer
- call out any unresolved conflicts between specialist outputs
