# Kaizen Vendor Freshness Protocol

Use this reference when Kai depends on current Shopify, AnyDB, Matrixify, or vendor-platform
behavior. This is a freshness and verification layer, not a replacement for MCP-backed source
checks.

## Purpose

Kai can keep local indexed notes for navigation and recent-change awareness, but current vendor
truth still comes from canonical sources at answer time.

The freshness layer has three jobs:

1. Point Kai to the right current source quickly.
2. Surface recent vendor changes that may affect Kaizen recommendations.
3. Block or qualify answers when local knowledge is stale, ambiguous, or version-sensitive.

## Source Priority

| Domain | Primary source | Local index role | Live validation required when |
|---|---|---|---|
| Shopify developer/API behavior | Shopify Dev MCP and `shopify.dev` canonical docs | Navigation, recent changelog awareness | Any schema, mutation, field, scope, API version, CLI command, component, extension target, POS UI, Functions, Liquid, Hydrogen, Polaris, or custom data claim is generated or validated |
| Shopify merchant/admin behavior | `help.shopify.com`, `changelog.shopify.com`, and Shopify Admin evidence when available | Merchant-facing change feed and feature availability notes | Plan/tier availability, rollout, tax, payments, Markets, POS, checkout, customer accounts, or settings behavior affects a recommendation |
| AnyDB behavior | AnyDB MCP/docs, `anydb.com/support/releasenotes`, `anydb.com/support/roadmap`, and AnyDB community release posts | Release notes, roadmap awareness, and Kaizen-specific watchlist | Cell types, formulas, references, rollups, import/export behavior, workflow triggers, Shopify sync, roadmap claims, or build instructions are used |
| Matrixify behavior | Matrixify docs and app evidence | Lane-specific reminders only | Column names, import limits, dry-run behavior, errors, or entity support affects a migration package |

## Required Freshness Gate

Before finalizing non-casual work involving Shopify, AnyDB, Matrixify, or integration automation,
Kai must answer these questions internally:

1. Is this claim vendor-current or just local memory?
2. Is the behavior version-sensitive, plan-sensitive, rollout-sensitive, or API-schema-sensitive?
3. Does `reference-content/` show a recent changelog or release item that could affect this answer?
4. If yes, was the canonical source checked live or was the answer clearly qualified?
5. If the local index is stale or missing, did Kai use MCP/web validation instead of guessing?

If any answer is unsafe, use `NOT READY`, `DEFER`, `[UNVERIFIED]`, or a plain-language caveat
depending on the output contract.

## Vendor Freshness Auto-Gate

This protocol is also a soft hook. Kai should load it automatically when the user asks about:

- current Shopify developer or merchant behavior
- AnyDB build behavior, formulas, releases, roadmap, workflows, or Shopify sync
- Matrixify-supported entities, columns, limits, dry-run behavior, or import errors
- automation safety where current platform behavior could change the answer

The hook does not require the operator to say `Vendor Freshness Check`. If freshness materially affects
the answer, Kai checks the local index first, then validates against the canonical live source when
the work is client-facing, build-ready, version-sensitive, plan-sensitive, or rollout-sensitive.

If live validation cannot be done in the current run, Kai must say so directly and treat the
platform-specific claim as provisional rather than final.

Exact fallback contract when live validation is unavailable:

- Start the answer with `[VERIFY]`.
- Do not state a definitive yes/no capability verdict from memory.
- Name the canonical source or MCP that must be checked and the operational decision that remains
  blocked until verification.

## Curated Change Radar

The generated index says what changed. It does not say what it means for KaizenCommerce. Items that
move a recommendation, a scope, or a build-vs-buy verdict get promoted by hand into
`reference/kaizen-platform-change-radar.md`, with a date, a canonical source, a confidence mark, and
a Kaizen action. Load the radar during scoping, Blueprint, architecture, build-vs-buy, and
pre-launch QA. Run the sweep protocol at the bottom of that file monthly and before any proposal.

## Local Index

Generated vendor notes live under:

```text
reference-content/
  _freshness-manifest.json
  _changelog-state.json
  _needs-merge.md
  shopify-dev/
  shopify-help/
  anydb/
```

The index is a navigation surface. It can say "this changed recently" or "check this canonical
source." It must not be treated as authoritative when the final answer depends on exact current
behavior.

## Update Command

Run from the source repo:

```bash
python3 skills/kaizen-commerce-expert/scripts/update_vendor_knowledge.py
```

The script fetches:

- Shopify merchant changelog RSS: `https://changelog.shopify.com/feed.xml`
- Shopify developer changelog RSS: `https://shopify.dev/changelog/feed.xml`
- AnyDB releases category JSON: `https://www.anydb.com/community/c/releases/6.json`
- AnyDB roadmap page metadata: `https://www.anydb.com/support/roadmap/`
- AnyDB official release notes: `https://www.anydb.com/support/releasenotes/`

First run uses a 30-day lookback. Later runs catch up from the last successful fetch and dedupe
against `reference-content/_changelog-state.json`.

Each source carries its own fetch timestamp, advanced only on a run where that source succeeded.
A source that is failing therefore keeps its backlog in range and picks it up when it recovers,
instead of losing the outage window to the other sources advancing a shared cutoff.

To recover a window that was already missed, rescan one source without touching the others:

```bash
python3 skills/kaizen-commerce-expert/scripts/update_vendor_knowledge.py \
  --backfill shopify-dev --lookback-days 75
```

`--backfill` is repeatable and takes `shopify-dev`, `shopify-help`, or `anydb`. Already-seen entries
stay deduped, so a wide window is safe. Add `--dry-run` first to see what it would pull.

**Check `errors` before trusting a thin result.** `_freshness-manifest.json` carries an `errors`
object. A fetch or parse failure leaves the snapshot date looking current while that source
contributes nothing, so a quiet week and a broken feed look identical from the outside. The
vendor-freshness audit warns on any non-empty `errors`.

## Conservative Auto-Curation

The updater may append unambiguous entries to generated section files, such as:

- new Shopify API version feature
- deprecated or removed Shopify behavior
- new extension target or component migration guide
- Shopify merchant feature rollout
- AnyDB release affecting cell types, views, formulas, workflows, imports, or Shopify sync

Ambiguous items are not merged into section notes. They are flagged in:

```text
reference-content/_needs-merge.md
```

Examples of ambiguous items:

- phased rollout with unclear account eligibility
- preview, beta, early access, or "coming soon"
- plan-tier or country availability not fully clear
- roadmap item without shipped status
- vendor wording that affects Kaizen commercial claims

## Kai Behavior

When a freshness command is used:

- `Vendor Freshness Check` reports state, new items, stale areas, and items needing merge.
- `Update Kai Vendor Knowledge` runs or instructs the updater, then reports what changed.
- `Check Shopify Freshness` focuses on Shopify developer and merchant surfaces.
- `Check AnyDB Freshness` focuses on AnyDB releases, roadmap, and AnyDB-specific build risks.

When answering client-facing or high-stakes work:

- Do not cite local generated files as final proof if a canonical vendor URL or MCP validation is
  available.
- Do cite the canonical Shopify, AnyDB, or Matrixify source that was checked.
- If a generated changelog item is relevant but unreviewed, state that it needs review before the
  recommendation is treated as final.

## Fail Gates

Use a hard gate when:

- Shopify GraphQL, CLI, POS UI, Functions, Liquid, Hydrogen, Polaris, or extension behavior was
  not validated through Shopify Dev MCP.
- AnyDB formula, cell, import, workflow, or Shopify sync behavior was not validated through AnyDB
  docs/MCP for a build-ready artifact.
- A recent changelog/release item directly affects the recommendation and is marked
  `[NEEDS-MERGE]`.
- The local freshness manifest shows the relevant source has not been updated in more than 14 days
  and no live validation was performed.
- The answer depends on plan, country, rollout, or beta availability and that availability is not
  confirmed.

## Output Snippet

Use this compact note when freshness materially affects an answer:

```text
Freshness check:
- Local index checked: [yes/no, timestamp if available]
- Canonical source checked: [Shopify Dev MCP / Shopify changelog / help.shopify.com / AnyDB docs / Matrixify docs / none]
- Verdict: [current / current with caveat / needs live verification / not ready]
- Reason: [one sentence]
```
