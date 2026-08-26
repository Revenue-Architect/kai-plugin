# Kai Runtime Portability

Kai is optimized for Codex with local filesystem access. This reference defines graceful behavior
when Kai is used in runtimes with fewer tools.

## Runtime Tiers

| Runtime | Capabilities | Kai behavior |
|---|---|---|
| Codex runtime | Local files, scripts, memory root, install/status, run folders, shell validation | Use the full Kai operating system: memory scripts, run folders, audits, validation, install sync, and file-backed handoffs. |
| Chat-only runtime | No local writes, no shell, no durable run folders | Produce copyable memory deltas, proposed tasks, evidence manifests, and command outputs in chat. Do not claim files were written. |
| External agent runtime | File manifests or limited tool execution, but not Kai's local memory root | Use manifest contracts and explicit handoff fields. Do not assume local paths exist unless provided. |

## Local Path Policy

Shipped files use `~/...` home-relative paths (Codex-runtime defaults), never operator-specific absolute paths.
When a runtime cannot access them:

- say the local path is unavailable in this runtime
- provide the equivalent copyable artifact or command
- preserve the same approval gates
- avoid inventing file state

## Optional Local Helpers

Some Kai workflows can use local helper scripts when they exist, but they must not require
the operator-specific absolute paths. Document optional helpers as environment variables instead:

| Helper | Environment variable |
|---|---|
| Merchant file LangExtract parser | `KAIZEN_MERCHANT_PARSER` |
| Discovery-call LangExtract parser | `KAIZEN_DISCOVERY_PARSER` |

If the variable is unset or the file is unavailable, continue with the manual workflow and say the
automation helper was skipped.

## Memory Behavior By Runtime

- Codex runtime: recall and update through the memory scripts, with approval-gated
  `memory_delta.json`.
- Chat-only runtime: summarize known context from the conversation and produce a copyable proposed
  memory delta. Do not claim authoritative memory was updated.
- External agent runtime: return `memory_delta.json`, `context-delta.md`, and source manifest
  content for Kai review.

## Task Behavior By Runtime

- Codex runtime: accepted command-created tasks may be written through `scripts/kaizen-tasks.py`.
  Inferred tasks stay proposed until approved.
- Chat-only runtime: show a Proposed Tasks block with `userAccepted: false`.
- External agent runtime: write task proposals to the handoff manifest if file output is available.

## Validation Behavior By Runtime

- Codex runtime: run `./scripts/validate-all.sh`, `git diff --check`, runtime validation, and
  install/status checks when maintaining Kai.
- Chat-only runtime: provide a checklist and call out that validation was not executed.
- External agent runtime: preserve command outputs, file manifests, and failures for Kai review.
