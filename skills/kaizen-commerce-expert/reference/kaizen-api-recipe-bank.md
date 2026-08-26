# Kaizen API Recipe Bank — Migration Core (Dev-MCP-Verified)

Load this reference when building migration runbooks, execution packages, or API-lane plans.
Every recipe carries: API version · verified date (Shopify Dev MCP schema validation) · recheck
interval · required scopes · retry/rollback behavior · usage class.

**Usage classes (hard rule):**
- `proposal-safe` — may inform client-facing capability statements
- `planning-safe` — runbook/architecture planning; do not promise behavior to clients from it
- `execution (verify live first)` — re-validate against the target shop (API version, plan
  gating, app approval) before any live run

**Freshness protocol:** verified means *schema-validated via Shopify Dev MCP on the date shown*
— not load-tested on a store. Past the recheck interval, re-validate before reuse
(`validate_graphql_codeblocks`) and update the date. A recipe past recheck used in an execution
artifact without re-validation is a vendor-freshness gate failure.

**Bank status:** verified 2026-06-10 against Admin GraphQL **2026-04** · recheck interval:
**90 days or any API-version bump in the target shop, whichever first** · recheck due:
**2026-09-08**.

---

## R1 — Product import (productSet, async)

- **Class:** planning-safe · **Scopes:** `write_products, read_products`
- **Why this shape:** `productSet` is the migration upsert — idempotent on repeated runs with the
  same identifier (rerun-safe), handles options/variants in one payload; async mode
  (`synchronous: false`) returns a `productSetOperation` to poll instead of blocking.
- **Limits that bite migrations:** variant creation throttles after a store crosses 50K variants
  (~1,000 new variants/day) — front-load catalog volume checks in Phase 1; products land
  unpublished by default — publication is a separate explicit step (`publishablePublish`).
- **Retry:** poll the operation id; on userErrors, fix payload and re-run the same identifiers
  (upsert semantics). **Rollback:** ledger every created product id; `productDelete` reversal.

```graphql
mutation MigrateProductSet($input: ProductSetInput!) {
  productSet(input: $input, synchronous: false) {
    productSetOperation { id status userErrors { field message } }
    userErrors { field message }
  }
}
```

## R2 — Bulk import lane (staged upload → bulk mutation)

- **Class:** planning-safe · **Scopes:** per the wrapped mutation
- **Shape:** upload JSONL via `stagedUploadsCreate`, then `bulkOperationRunMutation` wrapping the
  per-row mutation; poll status. One bulk mutation runs at a time per shop — serialize entities.
- **Retry:** failed rows land in `partialDataUrl` output — reprocess only failures; never re-run
  the full file without idempotent payloads. **Rollback:** the JSONL file IS the created-resource
  ledger; keep it.

```graphql
mutation MigrateStagedUpload($input: [StagedUploadInput!]!) {
  stagedUploadsCreate(input: $input) {
    stagedTargets { url resourceUrl parameters { name value } }
    userErrors { field message }
  }
}
```
```graphql
mutation MigrateBulkImport($mutation: String!, $stagedUploadPath: String!) {
  bulkOperationRunMutation(mutation: $mutation, stagedUploadPath: $stagedUploadPath) {
    bulkOperation { id status }
    userErrors { field message }
  }
}
```
```graphql
query MigrateBulkStatus {
  bulkOperations(first: 1, reverse: true, query: "type:mutation") {
    nodes { id status errorCode objectCount fileSize url partialDataUrl }
  }
}
```

## R3 — Customer import

- **Class:** planning-safe · **Scopes:** `write_customers, read_customers`
- **Note:** `Customer.email` is deprecated in selections — use `defaultEmailAddress.emailAddress`.
  Dedupe by email/phone BEFORE import; Shopify enforces uniqueness and the failure mode is
  userErrors mid-batch.
- **Retry:** userErrors row-level; safe to retry failures after dedupe fix. **Rollback:**
  ledger ids; `customerDelete` works only with no order history — delete window closes once
  orders import. Sequence customers → orders, and reconcile BEFORE orders begin.

```graphql
mutation MigrateCustomer($input: CustomerInput!) {
  customerCreate(input: $input) {
    customer { id defaultEmailAddress { emailAddress } }
    userErrors { field message }
  }
}
```

## R4 — Inventory opening counts (inventorySetQuantities)

- **Class:** planning-safe · **Scopes:** `write_inventory, read_inventory`
- **Why this shape:** sets absolute quantities (the migration semantic — "opening count is X"),
  not deltas; per-location in one input; supports `reason` for the audit trail.
- **Sequence:** products must exist and be stocked at locations first; activate inventory at
  each location before setting. **Retry:** idempotent — re-setting the same absolute value is
  safe. **Rollback:** previous values are gone once overwritten; capture a pre-import snapshot
  query per location as the rollback reference.

```graphql
mutation MigrateInventory($input: InventorySetQuantitiesInput!) {
  inventorySetQuantities(input: $input) {
    inventoryAdjustmentGroup { createdAt reason }
    userErrors { field message }
  }
}
```

## R5 — Historical order import (orderCreate)

- **Class:** execution (verify live first) · **Scopes:** `write_orders, read_orders` (validator
  also reports `read_marketplace_orders, read_quick_sale` on the selection set)
- **Hard constraints (Dev-MCP doc, 2026-06-10):** offline token apps only · dev/trial stores cap
  at ~5 orders/minute · one discount code max per order; line-level/multiple discounts are NOT
  replicated — historical totals must be imported as captured amounts, not re-derived.
- **Migration posture:** import as closed/archived with original dates via options; never let
  historical orders trigger fulfillment, payment capture, or customer notifications — verify
  notification suppression live on a test order before batch.
- **Retry:** NOT idempotent — duplicate runs create duplicate orders. Tag every imported order
  with a migration batch tag; dedupe-check by source order id (stored as note attribute/tag)
  before any retry. **Rollback:** ledger + batch tag enables targeted cleanup; order deletion is
  restricted — treat order import as the point of no easy return and gate it hardest.

```graphql
mutation MigrateOrder($order: OrderCreateOrderInput!, $options: OrderCreateOptionsInput) {
  orderCreate(order: $order, options: $options) {
    order { id name }
    userErrors { field message }
  }
}
```

## R6 — Gift cards with balances

- **Class:** execution (verify live first) · **Scopes:** `write_gift_cards, read_gift_cards`
- **Financial tie-out is mandatory:** sum of created balances must equal the legacy liability
  export to the cent (QA gate in kaizen-migrate). Codes: Shopify generates codes unless
  supplied — supplying legacy codes preserves customer-held cards; verify code-format
  acceptance live first.
- **Retry:** NOT idempotent — duplicates create liability. Ledger every created card id +
  amount; reconcile count AND sum before any retry. **Rollback:** disable created cards
  (`giftCardDeactivate`), never silent deletion — liability records must stay auditable.

```graphql
mutation MigrateGiftCard($input: GiftCardCreateInput!) {
  giftCardCreate(input: $input) {
    giftCard { id balance { amount currencyCode } }
    userErrors { field message }
  }
}
```
```graphql
query MigrateGiftCardBalances($cursor: String) {
  giftCards(first: 250, after: $cursor) {
    nodes { id balance { amount currencyCode } }
    pageInfo { hasNextPage endCursor }
  }
}
```

## R7 — Metafields / custom data

- **Class:** planning-safe · **Scopes:** `write_metaobjects, read_metaobjects` (metaobjects);
  metafieldsSet inherits the owner resource's scope
- **Shape:** `metafieldsSet` is the bulk-friendly upsert (25 per call); `metaobjectUpsert` is
  idempotent by handle — both rerun-safe. Define metafield definitions BEFORE the data lands so
  values are typed and admin-visible.

```graphql
mutation MigrateMetafields($metafields: [MetafieldsSetInput!]!) {
  metafieldsSet(metafields: $metafields) {
    metafields { id key }
    userErrors { field message }
  }
}
```
```graphql
mutation MigrateMetaobject($metaobject: MetaobjectUpsertInput!, $handle: MetaobjectHandleInput!) {
  metaobjectUpsert(handle: $handle, metaobject: $metaobject) {
    metaobject { id handle }
    userErrors { field message }
  }
}
```

## R8 — Reconciliation counts (Phase 5 verification)

- **Class:** planning-safe · **Scopes:** `read_products, read_customers, read_orders`
- Pair with the Phase-1 export baseline; gift card SUM comes from paginating R6's balance query.

```graphql
query MigrateReconcileCounts {
  productsCount { count }
  customersCount { count }
  ordersCount { count }
}
```

---

## Adding recipes

New recipes enter only after `validate_graphql_codeblocks` passes against the current stable
version, with all six required fields filled. Recipes used in execution artifacts past their
recheck date must be re-validated first — no exceptions. Matrixify-lane equivalents live with
the Matrixify lane variant and verify against the matrixify-app MCP instead.
