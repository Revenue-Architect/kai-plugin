# Kai Context Load Profiles

Use this reference when deciding how much Kai context to load for a task or when maintaining the
skill architecture. The goal is not smaller knowledge. The goal is loading the right knowledge at
the right time.

## Target Profiles

| Profile | Use when | Default load |
|---|---|---|
| Router-only quick answer | Quick Read, sanity check, simple take, command recognition | `SKILL.md` only, then answer or route |
| Normal execution | One clear workflow or deliverable | `SKILL.md` + one primary skill + zero to one supporting reference |
| Complex execution | Architecture, migration, proposal, QA, or source-of-truth work with real stakes | `SKILL.md` + one primary skill + one to two targeted references |
| Deep appendix | A task needs a long example, platform appendix, field mapping, or template | Load only the specific appendix section or example after the primary skill says it is needed |
| Full engagement orchestration | Multi-phase client work, resume, closeout, or pipeline status | [`kaizen-command-palette.md`](kaizen-command-palette.md) or [`kaizen-orchestrate.md`](../skills/kaizen-orchestrate.md) + the current phase reference only |

## Load Budget Targets

- Router: under 350 lines.
- Standard primary skill target: under 600 active lines when possible.
- Oversized skills may remain, but must include a `Lean Load Contract`.
- Command references should route to category references instead of forcing a monolithic load.
- Examples should load only when output taste, formatting, or failure comparison matters.

## Oversized Skill Rule

For any sub-skill over 600 lines, add a `Lean Load Contract` near the top. The contract must name:

- the minimum sections to read first
- mode or phase jumps
- optional appendices and when to load them
- example-loading rules
- supporting references that override embedded shortcuts

Do not delete or compress the existing skill content during the contract pass. The contract is a
navigation layer for the current content.

## Command Palette Rule

Use `reference/kaizen-command-palette.md` as the command index. When a command category is obvious,
load the relevant category reference:

- command categories (daily/status, pipeline intake, execution/QA/closeout, vendor freshness
  and operating hooks): `reference/kaizen-command-palette.md` category sections

## Failure Signs

- A simple answer requires several skills before the first recommendation.
- A migration task loads proposal, training, hardware, and reporting before the lane is selected.
- A daily briefing loads migration package details.
- A proposal answer uses stale pricing because it relied on embedded values instead of the pricing
  reference.
- A variant only names a chain and does not change the judgment.
