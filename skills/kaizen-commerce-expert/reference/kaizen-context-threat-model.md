# Kai V3 Context Threat Model

Load this file when maintaining Kai's skill architecture, investigating quality regressions, or
planning further context-engineering changes.

## Context Risks

| Risk | How it appears in Kai | Mitigation |
|---|---|---|
| lost-in-middle | Critical rules sit in the middle of a long router and get missed during complex tasks. | Keep `SKILL.md` as the hot router; move large policies to named references and keep critical rules at the top and end. |
| context distraction | Loading several skill files, references, and examples for a simple answer creates attention competition. | Use response depth modes and route to one primary skill plus zero to two supporting references. |
| context clash | API-first, Matrixify fallback, Shopify Dev MCP, Exa, and legacy migration habits can conflict. | Keep migration lane defaults in the router and full MCP rules in `reference/kaizen-mcp-protocols.md`. |
| supervisor bottleneck | Kai receives too many subagent summaries and must synthesize every detail from memory. | Use bounded subagents, file-based handoffs, and structured result schemas from `reference/kaizen-specialist-registry.md`. |
| telephone-game loss | Antigravity or subagent output gets paraphrased before Kai reviews exact evidence. | Prefer manifests, evidence files, exact paths, URLs, and line references. |
| stale technical behavior | Shopify API, CLI, POS UI, Liquid, Functions, Polaris, or AnyDB behavior changes after skill text is written. | Use Shopify Dev MCP for Shopify developer/API truth and MCP/docs fallback rules for other platforms. |
| stale commercial defaults | Old pricing or scope defaults survive in examples and get emitted as current facts. | Load `reference/kaizen-pricing.md` for commercial documents and keep `[NEED: approved price]` when numbers are not confirmed. |
| registry drift | Kai and subagent orchestrator list different specialists or model policies. | Use `reference/kaizen-specialist-registry.md` as the single source of truth. |

## Context Budget Targets

- Main Kai router: 300 to 350 lines.
- Subagent orchestrator: 100 to 120 lines.
- Default load: router only.
- Standard task load: router + one primary skill + zero to two references.
- Delegated task load: router + orchestrator + specialist registry + bounded specialist prompt.

## Optimization Strategy

1. Preserve stable critical rules in the router.
2. Move large but important bodies into named references.
3. Make references grep-friendly with precise headings and exact trigger strings.
4. Avoid loading multiple deep references before choosing the primary route.
5. Use file handoffs for substantial delegated work.
6. Run v3 audits after any material router, registry, MCP, or delegation change.
