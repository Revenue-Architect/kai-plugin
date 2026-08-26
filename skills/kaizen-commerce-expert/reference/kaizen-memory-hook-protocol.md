# Kai Memory Hook Protocol

Use this reference when client memory might matter but the operator did not explicitly say "recall
memory" or "update memory." This is a soft hook: automatic recall and automatic update proposals,
but no automatic authoritative writes.

## Purpose

Kai should feel automatic without becoming unsafe:

- recall known client memory before client-specific work
- draft memory update proposals after meaningful client work
- require explicit approval before applying any memory delta
- keep Kai as the only writer to authoritative memory

## Activation

Load this protocol when:

- the operator names a known client or merchant in `~/Documents/Codex/kaizen-memory` (override with `KAIZEN_MEMORY_ROOT`)
- a command or natural-language alias maps to `Prep Call`, `Post Call Update`, `Build Proposal`,
  `Resume Client`, `Sync Client`, `Migration QA`, `Close Client`, or `Build Blueprint`
- the operator says phrases such as "catch me up on Acme", "help me prep for my Acme call", "process
  these notes", "turn this call into next steps", or "save this to Acme memory"
- Antigravity, a subagent, or a workflow run produces durable client context

Do not use this protocol for casual brainstorming, generic Shopify/AnyDB questions, or one-off
drafting with no client state change.

## KaizenOS Boundary

Recall order for client work: KaizenOS record context first (`kai_search_context` →
`kai_get_record_context`), then file memory for narrative and preferences. Draft memory deltas
only for judgment-layer context; route record-shaped facts (stage moves, amounts, dates, contacts,
commitments) to KaizenOS writes per `reference/kaizen-kaizenos-integration-map.md`. Both lanes
stay approval-gated.

## Read Hook: Auto-Recall First

Before client-specific work:

1. Inspect `index/clients.json` or `index/active-clients.md` under the Kaizen memory root.
2. Match by exact client display name or slug. A "known client" means one exact match in the
   index or `clients/[slug]/`.
3. If exactly one known client matches, recall memory first:

```bash
./scripts/kaizen-memory-recall.py "Client Name"
```

4. Use the recalled profile, state, recent events, and recent decisions as source context.
5. If no known client matches, ask before creating memory unless the command is explicitly
   `New Deal`.
6. If multiple clients match, ask one short clarification question naming the candidates.

Do not broadly guess client identity from similar names. Do not load every client profile unless
the task is pipeline, pattern, or portfolio review.

## Write Hook: Draft, Do Not Apply

After meaningful client work, draft a memory update proposal when the output includes:

- client decisions
- confirmed stack changes
- call notes and follow-ups
- proposal, SOW, or pricing status
- pricing approvals or commercial exceptions
- migration lane decisions
- QA verdicts
- go-live or delivery updates
- post-go-live metrics
- QBR or account-health changes

Do not draft a memory update for:

- casual brainstorming
- generic Shopify/AnyDB advice
- unsent draft emails
- unsupported assumptions
- private raw data files
- secrets, credentials, tokens, or API keys

## Proposal Surface

When a memory update is warranted, show a compact chat block:

```text
Proposed Memory Update
Client: [client]
Why: [decision/call/proposal/QA/delivery update]
Updates: [fields/events/decisions/sources]
Evidence: [file/source/call note/log]
Risk checks: [conflicts, sensitive data, assumptions]
Approval phrase: "apply the memory update for [client]"
```

When a run folder exists, also draft:

```text
kai/context-delta.md
kai/memory_delta.json
```

`kai/context-delta.md` is the human-readable summary. `kai/memory_delta.json` is the structured
proposal to apply after approval.

## Approval Gate

Never apply a memory delta automatically.

Apply only after explicit approval such as:

- "apply the memory update for Acme"
- "save this to Acme memory"
- "approve the memory delta"

After approval:

```bash
./scripts/kaizen-memory-apply-delta.py path/to/kai/memory_delta.json
./scripts/kaizen-memory-consolidate.py --client "Client Name"
```

If the memory update is material to agency state, run full consolidation:

```bash
./scripts/kaizen-memory-consolidate.py
```

## Fail Gates

Return `NOT READY FOR MEMORY WRITE` when any of these are true:

- client identity is ambiguous
- the proposed update contains secrets, credentials, API tokens, or private keys
- the update tries to store raw exports, raw transcripts, or unnecessary bulk client data
- the update treats an unsent draft as a sent communication
- the update includes unapproved pricing, legal terms, or payment terms
- the update overwrites confirmed facts with inference
- evidence is missing for a decision, QA verdict, go-live, or commercial status
- the update conflicts with existing memory and the conflict is not called out

## Output Contract

For client-specific work, Kai should end with one of:

- `Memory recalled: [client]`
- `No known memory found: ask before create`
- `Memory update proposed: approval required`
- `No memory update needed`
- `NOT READY FOR MEMORY WRITE: [reason]`

Keep this concise in normal chat. Use full details in run-folder artifacts when available.
