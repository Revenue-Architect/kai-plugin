---
name: kaizen-subagent-orchestrator
description: >
  KaizenCommerce delegation wrapper for subagent-based execution. Use when the user explicitly
  wants subagents or parallel agent work and the task should be split across Kaizen specialist
  skills installed globally under ~/.codex/skills. Keeps Kai as the
  integrating brain while specialist skills handle bounded sidecar work.
---

# Kaizen Subagent Orchestrator

Thin global wrapper that standardizes how KaizenCommerce work is split across specialist
subagents. This skill does not replace `Kai` or `kaizen-commerce-expert`. It tells the main
agent how to delegate bounded slices cleanly when the user explicitly asks for subagents,
delegation, or parallel agent work.

## Load Order

Always load:
- `../kaizen-commerce-expert/SKILL.md`
- `../kaizen-commerce-expert/reference/kaizen-specialist-registry.md`

State the load explicitly when using this skill:
`Loaded: kaizen-subagent-orchestrator + kaizen-commerce-expert + kaizen-specialist-registry`

## Activation Rule

Use this skill only when the user explicitly asks for one of:
- subagents
- delegation
- parallel agent work
- splitting the task across agents
- optimized Kaizen subagent workflow

If the user does not explicitly ask for delegation, do not spawn subagents just because the task
is large. Work locally or use `Kai` normally.

## Role

`Kai` remains the main orchestrator. Specialist subagents own narrow execution slices. The main
agent decides the split, spawns only the non-overlapping sidecar work, and integrates the result
back into one answer.

## Registry Source

The full specialist paths, parent-model policy, preferred pairings, spawn prompt pattern,
file-based handoff convention, and result schema live in:

`../kaizen-commerce-expert/reference/kaizen-specialist-registry.md`

Use that file as the single source of truth. Do not duplicate specialist tables or model-policy
details in this wrapper.

## Execution Pattern

1. Read the user request and decide what the main agent should keep locally.
2. Split only the parallelizable sidecar work.
3. Spawn each specialist with:
   - the matching global skill named explicitly in the prompt
   - the installed skill path from `reference/kaizen-specialist-registry.md`
   - the parent model unless the registry model policy justifies an override
   - one bounded deliverable
   - ownership boundaries if code changes are involved
4. Continue local work immediately instead of waiting by reflex.
5. Integrate returned results into one KaizenCommerce answer or implementation.

## Delegation Boundary

Keep local:
- the immediate blocking decision the next step depends on
- final client-facing synthesis
- commercial positioning, scope, pricing, and verdicts
- migration lane decisions and source-of-truth architecture
- tasks faster to complete than to delegate

Delegate:
- independent research, QA, audit, or architecture slices
- workstreams with different evidence sources
- bounded implementation slices with non-overlapping file ownership
- review passes where an independent specialist can catch mistakes before Kai ships the answer

Prefer one to three subagents. More only when the write scopes or research questions are truly
independent.

## Output Contract

When this skill is active, the main agent should:
- state the delegation split briefly
- keep orchestration concise
- use the result schema from the specialist registry when practical
- integrate subagent results into one answer
- call out unresolved conflicts between specialist outputs
