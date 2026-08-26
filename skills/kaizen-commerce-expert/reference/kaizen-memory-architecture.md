# Kaizen Memory Architecture

Load this file when working with Kai's persistent client memory, 2-AI handoffs, Antigravity
`memory_delta.json`, or cross-session engagement state.

## Default Memory Root

Kai's durable filesystem memory lives outside the skill repo:

```text
~/Documents/Codex/kaizen-memory/   (override with KAIZEN_MEMORY_ROOT)
```

Override with `KAIZEN_MEMORY_ROOT` only when testing or running in a temporary workspace.

## Directory Layout

```text
kaizen-memory/
  README.md
  agency/
    kaizen-state.md
  clients/
    [client-slug]/
      profile.md
      state.yaml
      summary.md
      events.jsonl
      decisions.jsonl
      sources.jsonl
      memory-deltas/
  runs/
    [date]-[client]-[task]/
      TASK.md
      antigravity/
        manifest.json
        memory_delta.json
        evidence/
        outputs/
      kai/
        REVIEW.md
        context-delta.md
        memory_delta.json
      APPROVAL.md
  tasks/
    schema.json
    active/
      task_[timestamp]_[slug].json
    archive/
      YYYY/
        MM/
  index/
    clients.json
    active-clients.md
```

## Authority Model

Kai is the only writer to authoritative memory.

Antigravity CLI may produce:

- `manifest.json`
- `memory_delta.json`
- evidence files
- output artifacts

Antigravity must not edit `clients/[client-slug]/profile.md`, `state.yaml`, `agency/kaizen-state.md`,
or `CONTEXT.md`. Kai reviews Antigravity output, validates artifacts and sources, then applies the
delta with `scripts/kaizen-memory-apply-delta.py`.

Use `reference/kaizen-memory-hook-protocol.md` for soft-hook behavior: auto-recall known client
memory before client-specific work, auto-draft memory proposals after meaningful client work, and
require explicit approval before applying any authoritative write.

## Scope Boundary With KaizenOS

KaizenOS MCP is the system of record for merchants, contacts, deals, stages, projects, tasks,
invoices, activity, and evidence sources (`reference/kaizen-kaizenos-integration-map.md`). File
memory does not compete with it:

- **File memory holds** judgment narrative, operator preferences, style calibration, discovery
  nuance, and cross-client patterns — context KaizenOS records cannot hold.
- **File memory must not hold** record-shaped facts as authority: deal stages, amounts, dates,
  contact details, owners, or commitments. Capture those through `kai_log_activity`,
  `kai_update_deal`, `kai_create_task`, and the other named KaizenOS tools instead.
- **Precedence:** on conflict, current KaizenOS record state wins. Memory narrative annotates and
  challenges; it never overrides. When memory looks fresher than the record, propose a KaizenOS
  update — do not treat the memory file as the newer truth.
- **Migration and lint:** `./scripts/kaizen-memory.py export-facts [--client NAME] [--out FILE]`
  walks client memory and emits a reviewable, approval-gated batch of proposed KaizenOS writes
  (structured events/decisions/state) plus flagged record-shaped profile lines. It never writes
  anywhere; the operator applies approved items through named KaizenOS tools with `dryRun=true`
  first. Re-run it periodically as a lint for facts that leaked back into file memory.

## Memory Layers

| Layer | File | Purpose |
|---|---|---|
| Client profile | `clients/[slug]/profile.md` | Current known truth about the client |
| Orchestrator state | `clients/[slug]/state.yaml` | Current phase, step, gates, blockers, next action |
| Events | `clients/[slug]/events.jsonl` | Append-only activity history |
| Decisions | `clients/[slug]/decisions.jsonl` | Source-of-truth choices, migration lane, pricing approvals, scope calls |
| Sources | `clients/[slug]/sources.jsonl` | URLs, files, docs, Shopify Dev MCP checks, Exa findings |
| Run evidence | `runs/[date]-[client]-[task]/` | Temporary handoff artifacts for Antigravity and Kai review |
| Task ledger | `tasks/active/`, `tasks/archive/` | Open, blocked, completed, and auto-detected Kaizen tasks |
| Index | `index/clients.json`, `index/active-clients.md` | Fast client lookup and dashboard |
| Agency state | `agency/kaizen-state.md` | Consolidated active-client state |

## Scripts

Run from the kaizen-skills checkout (default `~/Documents/Codex/kaizen-skills`; override with `KAIZEN_SKILLS_ROOT`). Installed runtime wrapper scripts
forward to this source checkout; set `KAIZEN_SKILLS_ROOT` or `KAI_SOURCE_ROOT` if the checkout
lives somewhere else.

```bash
./scripts/kaizen-memory.py status --init
./scripts/kaizen-memory.py init-client --client "Client Name" --source "manual"
./scripts/kaizen-memory.py recall "Client Name"
./scripts/kaizen-memory.py apply-delta runs/2026-05-12-client-task/antigravity/memory_delta.json
./scripts/kaizen-memory.py apply-delta runs/2026-05-12-client-task/kai/memory_delta.json
./scripts/kaizen-memory.py consolidate
./scripts/kaizen-memory.py export-facts --out /tmp/kaizenos-migration-batch.json
./scripts/kaizen-workflow.py new-deal "Client Name" --website "https://example.com"
./scripts/kaizen-workflow.py doctor
./scripts/kaizen-workflow.py start-my-day
./scripts/kaizen-workflow.py evidence-research "Research topic" --client "Client Name"
./scripts/kaizen-workflow.py priorities
./scripts/kaizen-workflow.py review-workspace
./scripts/kaizen-workflow.py close-client "Client Name"
./scripts/kaizen-tasks.py list --client "Client Name"
```

Thin wrapper scripts are also available:

```bash
./scripts/kaizen-memory-status.py --init
./scripts/kaizen-memory-init-client.py --client "Client Name" --source "manual"
./scripts/kaizen-memory-recall.py "Client Name"
./scripts/kaizen-memory-apply-delta.py runs/2026-05-12-client-task/antigravity/memory_delta.json
./scripts/kaizen-memory-apply-delta.py runs/2026-05-12-client-task/kai/memory_delta.json
./scripts/kaizen-memory-consolidate.py
```

Use `--root /path/to/test-memory` for tests. The default root is the durable Kaizen memory
folder above.

## Task Ledger

Task files are stored in `tasks/active/` until their status is `done` or `archived`, then moved
under `tasks/archive/YYYY/MM/`. Each task is a JSON file with:

- `id`
- `title`
- `description`
- `client`
- `client_slug`
- `status`
- `priority`
- `labels`
- `links`
- `source`
- `created_at`
- `updated_at`
- `due_date`
- `userAccepted`

Rules:

- explicit command-created tasks use `userAccepted: true`
- auto-detected tasks from notes, transcripts, Antigravity manifests, or evidence reviews use
  `userAccepted: false`
- task titles are short, verb-first, and merchant-free
- task descriptions preserve source file, run folder, transcript, or evidence references
- no secrets, credentials, API keys, or raw private exports should be stored in task files

Commands:

```bash
./scripts/kaizen-tasks.py add --client "Client Name" --title "Gather Outlook evidence" --user-accepted
./scripts/kaizen-tasks.py list --client "Client Name"
./scripts/kaizen-tasks.py status task_20260512123000_client-name done
```

## memory_delta.json Schema

Antigravity or Kai-reviewed sidecar work should return this shape when memory should be updated.
Antigravity-authored deltas live under `antigravity/memory_delta.json`. Kai-authored deltas live under
`kai/memory_delta.json`.

```json
{
  "client": "Client Name",
  "client_slug": "client-name",
  "source": "antigravity | kai | subagent | manual",
  "summary": "One sentence describing what changed.",
  "profile_updates": {
    "Identity": {
      "Industry": "Retail"
    },
    "Current Stack": {
      "POS": "Square"
    },
    "Pain Points (in their words)": [
      "Exact client quote or clearly labeled inferred pain point"
    ],
    "Technical Context": {
      "SKU count": "12000"
    }
  },
  "state_updates": {
    "current_phase": "3",
    "current_step": "3.6",
    "gates_pending": "Migration Package Ready"
  },
  "events": [
    {
      "date": "2026-05-12",
      "stage": "Migration",
      "skill": "kaizen-api-migration-exec",
      "key_output": "Prepared API payload manifest",
      "next_step": "Kai review"
    }
  ],
  "decisions": [
    {
      "decision": "Use api_to_api migration lane",
      "rationale": "Source and target APIs are controllable",
      "confidence": "high"
    }
  ],
  "sources": [
    {
      "type": "file | url | mcp | command",
      "ref": "exact path, URL, MCP check, or command",
      "note": "why it matters"
    }
  ],
  "notes": []
}
```

## Retrieval Discipline

- Read `index/active-clients.md` or `index/clients.json` before broad client lookup.
- Read one client's `profile.md` and `state.yaml` before client-specific deliverables.
- Read `events.jsonl`, `decisions.jsonl`, and `sources.jsonl` only when the task needs audit
  history or provenance.
- Use `summary.md` after consolidation for quick re-entry.
- Never load every client profile unless running PATTERNS mode or pipeline review.
- For known-client command work, recall becomes a required preflight. If exactly one known client
  matches the request, recall memory before writing the client-specific output.

## Consolidation

Run consolidation after a major session, after applying Antigravity deltas, or before resuming a
stale engagement:

```bash
./scripts/kaizen-memory-consolidate.py
```

Consolidation is deterministic. It does not discard history. It writes:

- per-client `summary.md`
- `index/clients.json`
- `index/active-clients.md`
- `agency/kaizen-state.md`

## Safety Rules

- Do not store secrets, tokens, passwords, production credentials, or private API keys in memory.
- Do not let Antigravity write authoritative memory files directly.
- Preserve verbatim client pain points.
- Keep `events.jsonl`, `decisions.jsonl`, and `sources.jsonl` append-only.
- Never replace confirmed data with inferred data. If a delta conflicts, preserve the previous
  value in the profile line and let the operator resolve the conflict.
