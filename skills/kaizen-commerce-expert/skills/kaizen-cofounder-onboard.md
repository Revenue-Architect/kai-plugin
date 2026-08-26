---
name: kaizen-cofounder-onboard
description: Guide a KaizenCommerce cofounder through Claude or Gemini setup, personal KaizenOS MCP access, and safe read/write verification.
metadata_version: 1
layer: founder-operations
upstream: []
downstream: []
adjacent: []
canon: ["reference/kaizen-kaizenos-integration-map.md"]
owns: ["cofounder runtime onboarding and attributed access verification"]
does_not_own: ["shared credential rotation or founder-specific configuration replacement"]
---

# Kaizen Cofounder Onboarding

Use this route when a cofounder says "onboard me", "set up Kai", "connect KaizenOS", or asks whether
their Claude or Gemini setup is complete. Lead the flow one verified step at a time. Do not dump the
whole checklist unless the operator asks.

## Non-negotiable boundaries

- KaizenOS remains the operating source of truth. Never create a second CRM, task list, or client
  record store.
- Preserve every existing runtime, MCP server, credential, operator file, and the operator-specific
  configuration. Do not reset, overwrite, remove, or rename an existing setup automatically.
- Each cofounder gets a personal KaizenOS Agent API key owned by their real KaizenOS profile.
  Never share the operator's key or the shared MCP bearer.
- Never ask the operator to paste a raw key into chat, place it in the repository, or record it in
  onboarding state. The local setup script accepts it with hidden terminal input.
- All KaizenOS writes remain preview-first: `dryRun=true`, show the exact proposed fields, require
  explicit approval, then commit once with a stable `idempotencyKey`.

## Resumable state

The non-secret state file is `~/.kaizen/cofounder-onboarding.json`. Resolve the bundled
`../scripts/cofounder-onboarding.py` from this skill file into `KAI_COFUNDER_STATE_TOOL`, then use:

```bash
python3 "$KAI_COFUNDER_STATE_TOOL" status
```

Mark a step complete only after its evidence check passes:

```bash
python3 "$KAI_COFUNDER_STATE_TOOL" complete STEP
```

Allowed steps are `operator_profile`, `skill_discovery`, `personal_agent_key`, `mcp_connection`,
`read_check`, `dry_run_check`, and `attribution_check`.

## Guided flow

1. Read `~/.kaizen/operator.md` and the onboarding state. If either is missing, guide the operator
   through the repository bootstrap for their runtime; do not infer their name or email.
2. Verify skill discovery:
   - Claude: start a fresh Claude Code session and invoke
     `/kaizen-commerce-expert Onboard me as a KaizenCommerce cofounder`.
   - Gemini: run `/skills reload`, then `/skills list`, confirm `kaizen-commerce-expert`, explicitly
     ask Gemini to use that skill for cofounder onboarding, and approve the activation prompt.
   - A generic clarification asking what "cofounder onboarding" means proves Kai did not activate.
     Do not mark `skill_discovery` complete; repair discovery or invoke the skill explicitly.
3. Ask a KaizenOS admin to create a key in **Settings → Agent API keys** with:
   - owner: this cofounder's real profile;
   - source: `Claude` or `Gemini`, matching their runtime;
   - scopes: `read` and `write` by default; add `finance` or `sync` only for an agreed need.
   The raw key is shown once. Do not collect it in chat.
4. Have the cofounder run this locally; it prompts for the key with hidden input and preserves any
   MCP server already named `kaizenos`:

   ```bash
   KAI_RUNTIME=claude ~/.kaizen/kaizen-skills/scripts/configure-kaizenos-mcp.sh
   ```

   Use `KAI_RUNTIME=gemini` for Gemini CLI. Restart the runtime afterward.
5. Verify a live read using `kai_get_priorities` or `kai_search_context`. Report the returned live
   KaizenOS state; do not substitute sample or cached data.
6. Verify write authority with a harmless, named write using `dryRun=true`. Show the preview and do
   not commit it as part of onboarding.
7. Verify attribution in KaizenOS Agent API audit: the call must show this cofounder's owner and
   the correct `Claude` or `Gemini` source. If not, stop and fix identity before real work.
8. Report completion, remaining optional scopes, and how to revoke the key. Do not expose key
   material in the report.

## Failure handling

- Prompt was entered in claude.ai, Claude chat/desktop, gemini.google.com, or Gemini mobile:
  filesystem skills are unavailable there. Continue in Claude Code CLI or Gemini CLI.
- Existing `kaizenos` MCP entry: preserve it and inspect with the operator. Never auto-remove it.
- Read succeeds but attribution is wrong: treat onboarding as incomplete and do not perform writes.
- Write preview is denied: have the admin adjust this personal key's scopes; do not switch to a
  shared or admin credential.
- Hosted MCP lacks personal-key support: report deployment drift between the KaizenOS app and
  `agent-mcp`; do not create an alternate database or local shadow state.
