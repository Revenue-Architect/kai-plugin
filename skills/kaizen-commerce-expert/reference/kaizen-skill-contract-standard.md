# Kai Skill Contract Standard

Use this reference when maintaining Kai subskills or auditing whether a skill is complete.
This file is additive policy. It does not replace existing skill instructions.

## Additive Contract

Every Kai subskill should be able to answer these fields without relying on hidden context:

| Field | Requirement |
|---|---|
| Purpose | What business, technical, or operational job this skill performs. |
| Trigger | Exact user terms, workflow commands, or pipeline states that activate it. |
| Do not use | Clear cases where another skill or reference should own the request. |
| Required inputs | Minimum viable inputs and full-quality inputs. |
| Source dependencies | Current docs, MCP servers, client memory, transcripts, exports, logs, or references required before output. |
| Evidence requirement | What proof must support the output: files read, URLs, MCP docs, commands, screenshots, counts, logs, or calculations. |
| Success metrics | Observable quality thresholds for the skill's output. |
| Fail gates | Conditions that force `FAIL`, `NOT READY`, hold, re-scope, or user confirmation. |
| Output contract | Artifact type, required sections, verdicts, labels, and formatting rules. |
| Handoff fields | What downstream skill needs next, including unresolved risks and owner. |

## Maintenance Rules

- Add new contract material by appending a section. Do not compress or remove existing skill text.
- Keep bulky procedures in `reference/` and add short pointers from subskills.
- Keep the root `SKILL.md` as the hot router. Do not move full skill-contract procedures into it.
- Prefer one source of truth for repeated policy. Subskills should point here or to `kaizen-evidence-and-gates.md` instead of duplicating long checklists.
- Client-facing output should not expose internal framework names unless the operator explicitly asks for methodology language.

## Required Additive Sections

When upgrading a skill, append these sections if they are missing and relevant:

```markdown
## Success Metrics

- [Observable threshold]
- [Evidence or quality target]
- [Failure threshold or escalation trigger]

## Evidence And Gate Requirements

- Use `../reference/kaizen-evidence-and-gates.md` when this skill produces QA, validation, migration, audit, report, or decision output.
- Name files, sources, commands, counts, or logs used.
- Return a clear verdict when the output informs go/no-go, delivery readiness, or commercial action.
```

## Contract Audit Checklist

- Does the skill state when to use it and when not to use it?
- Does it separate confirmed facts, inferences, assumptions, and estimates where risk matters?
- Does it name the current source of truth for platform behavior?
- Does it define success in measurable terms?
- Does it have explicit fail gates rather than soft warnings?
- Does it pass a usable handoff to the next skill?
- Does it avoid creating a new persona that competes with Kai's voice?
