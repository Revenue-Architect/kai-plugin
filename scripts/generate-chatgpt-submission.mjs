import { writeFile } from "node:fs/promises";
import kaizenOsContract from "../contracts/kaizenos-agent-tools.json" with { type: "json" };

const outputPath = new URL("../chatgpt-app-submission.json", import.meta.url);

const advisoryTools = {
  search: {
    annotations: { readOnlyHint: true, openWorldHint: false, destructiveHint: false },
    justifications: {
      read_only_justification: "Searches the bundled Kaizen knowledge corpus without changing data.",
      open_world_justification: "Reads only packaged references and does not change public or third-party state.",
      destructive_justification: "Does not create, update, delete, send, publish, or perform an irreversible action.",
    },
  },
  fetch: {
    annotations: { readOnlyHint: true, openWorldHint: false, destructiveHint: false },
    justifications: {
      read_only_justification: "Retrieves a packaged knowledge item or produces a local draft without changing external data.",
      open_world_justification: "Uses the bundled knowledge corpus and does not publish or modify a third-party system.",
      destructive_justification: "Does not approve, send, delete, or otherwise perform an irreversible action.",
    },
  },
  analyze_opportunity: {
    annotations: { readOnlyHint: true, openWorldHint: false, destructiveHint: false },
    justifications: {
      read_only_justification: "Computes a scope-first opportunity profile from supplied facts without accessing or changing live records.",
      open_world_justification: "Performs local inference and does not change public or third-party state.",
      destructive_justification: "Does not create, update, delete, submit, send, or perform an irreversible action.",
    },
  },
  build_solution_architecture: {
    annotations: { readOnlyHint: true, openWorldHint: false, destructiveHint: false },
    justifications: {
      read_only_justification: "Builds a first-pass architecture from user-supplied systems and domains without changing live records.",
      open_world_justification: "Returns a local planning result and does not connect to or modify external systems.",
      destructive_justification: "Does not create, update, delete, submit, send, or perform an irreversible action.",
    },
  },
  assess_migration: {
    annotations: { readOnlyHint: true, openWorldHint: false, destructiveHint: false },
    justifications: {
      read_only_justification: "Calculates migration risks and QA gates from supplied platform facts without changing either platform.",
      open_world_justification: "Returns a planning assessment and does not modify public or third-party state.",
      destructive_justification: "Does not migrate, overwrite, delete, submit, or perform an irreversible action.",
    },
  },
  generate_blueprint: {
    annotations: { readOnlyHint: true, openWorldHint: false, destructiveHint: false },
    justifications: {
      read_only_justification: "Drafts an evidence-labeled Blueprint outline from supplied facts without creating or sending a client artifact.",
      open_world_justification: "Produces a local review draft and does not publish or modify an external system.",
      destructive_justification: "Does not approve, sign, send, delete, or perform an irreversible action.",
    },
  },
  generate_proposal: {
    annotations: { readOnlyHint: true, openWorldHint: false, destructiveHint: false },
    justifications: {
      read_only_justification: "Drafts a proposal structure from supplied facts without sending or approving it.",
      open_world_justification: "Produces an unsubmitted local draft and does not publish or change external state.",
      destructive_justification: "Does not send, approve, sign, delete, or perform an irreversible action.",
    },
  },
  generate_sow: {
    annotations: { readOnlyHint: true, openWorldHint: false, destructiveHint: false },
    justifications: {
      read_only_justification: "Drafts a statement-of-work structure from supplied scope without creating or approving a contract.",
      open_world_justification: "Returns a local planning draft and does not publish or modify an external system.",
      destructive_justification: "Does not approve, sign, send, delete, or perform an irreversible action.",
    },
  },
  render_kaizen_workbench: {
    annotations: { readOnlyHint: true, openWorldHint: false, destructiveHint: false },
    justifications: {
      read_only_justification: "Renders a read-only interactive view of a structured Kaizen result without changing data.",
      open_world_justification: "Uses the bundled widget and supplied result data without connecting to external domains.",
      destructive_justification: "Does not create, update, delete, send, publish, or perform an irreversible action.",
    },
  },
};

function capitalized(value) {
  return value.replaceAll("_", " ").replace(/\b\w/g, (letter) => letter.toUpperCase());
}

function kaizenToolEntry(definition) {
  const isWrite = definition.destructive === true;
  const verb = definition.action.startsWith("delete_")
    ? "Deletes"
    : definition.action.startsWith("create_")
      ? "Creates"
      : definition.action.startsWith("update_")
        ? "Updates"
        : definition.action.startsWith("move_")
          ? "Moves"
          : definition.action.startsWith("list_") || definition.action.startsWith("get_") || definition.action.startsWith("search_")
            ? "Retrieves"
            : definition.action.startsWith("draft_")
              ? "Creates or updates"
              : "Runs";
  const object = capitalized(definition.action.replace(/^(create|update|delete|move|list|get|search|draft|activate|log|attach|link|send|queue|trigger)_/, ""));
  return {
    annotations: {
      readOnlyHint: !isWrite,
      openWorldHint: false,
      destructiveHint: isWrite,
    },
    justifications: {
      read_only_justification: isWrite
        ? `${verb} a private KaizenOS ${object.toLowerCase()} record or workflow; it is not read-only.`
        : `Retrieves private KaizenOS ${object.toLowerCase()} context without changing records.`,
      open_world_justification: "Operates only on the authenticated user's private KaizenOS workspace and does not publish public or third-party state.",
      destructive_justification: isWrite
        ? "The action can change or delete a private KaizenOS record; committed writes require a caller-authenticated role, a dry-run preview, explicit approval, and a unique idempotency key."
        : "Does not create, update, delete, send, or otherwise perform an irreversible action.",
    },
  };
}

const tools = { ...advisoryTools };
for (const definition of kaizenOsContract.filter((tool) => [
  "kai_search_context",
  "kai_get_record_context",
  "kai_get_priorities",
  "kai_create_merchant",
  "kai_update_merchant",
  "kai_create_partner",
  "kai_update_partner",
  "kai_create_contact",
  "kai_update_contact",
  "kai_create_deal",
  "kai_update_deal",
  "kai_move_deal_stage",
  "kai_create_project",
  "kai_activate_deal_engagement",
  "kai_update_project",
  "kai_move_project_status",
  "kai_create_task",
  "kai_update_task",
  "kai_create_project_milestone",
  "kai_update_project_milestone",
  "kai_delete_project_milestone",
  "kai_log_activity",
  "kai_attach_source",
  "kai_link_document",
  "kai_create_client_request",
  "kai_list_client_update_drafts",
  "kai_draft_client_update",
].includes(tool.name))) {
  tools[definition.name] = kaizenToolEntry(definition);
}

const submission = {
  $schema: "https://developers.openai.com/apps-sdk/schemas/chatgpt-app-submission.v1.json",
  schema_version: 1,
  app_info: {
    display_name: "Kaizen Commerce",
    subtitle: "Retail commerce intelligence",
    description: "Kaizen Commerce helps merchant and solution teams search verified commerce knowledge, assess Shopify POS and retail migration opportunities, map architecture, draft evidence-labeled delivery documents, and—when each user signs in—read, preview, and commit bounded CRM and project-management changes in KaizenOS.",
    category: "BUSINESS",
  },
  tools,
  test_cases: [
    {
      description: "Find and inspect verified Kaizen guidance for a Shopify POS question.",
      user_prompt: "Find the Kaizen guidance on Shopify POS and show me the most relevant reference.",
      file_attachment_urls: null,
      tools_triggered: "search, fetch",
      expected_output: "Returns relevant packaged references and then the selected item's text and source metadata.",
      expected_output_url: null,
    },
    {
      description: "Build a first-pass architecture and present it in the workbench.",
      user_prompt: "Map a first-pass architecture for Shopify, NetSuite, Lightspeed Retail, and an AnyDB operations layer across catalog, inventory, orders, customers, and fulfillment.",
      file_attachment_urls: null,
      tools_triggered: "build_solution_architecture, render_kaizen_workbench",
      expected_output: "Returns source-of-truth heuristics, integration workstreams, open questions, evidence labels, and a read-only Architecture Map.",
      expected_output_url: null,
    },
    {
      description: "Assess migration risk and create a review-only delivery draft.",
      user_prompt: "Assess a Lightspeed Retail to Shopify migration for products, inventory, customers, orders, locations, and fulfillments with high timeline pressure, then draft an evidence-labeled SOW outline without inventing pricing.",
      file_attachment_urls: null,
      tools_triggered: "assess_migration, generate_sow, render_kaizen_workbench",
      expected_output: "Returns entity-specific risks, QA gates, an evidence-labeled SOW draft, and a read-only review view; nothing is sent or approved.",
      expected_output_url: null,
    },
    {
      description: "Read live KaizenOS CRM context for an authenticated user.",
      user_prompt: "After I sign in to KaizenOS, search my CRM for the merchant Acme Retail and show the matching record context and current priorities.",
      file_attachment_urls: null,
      tools_triggered: "kai_search_context, kai_get_record_context, kai_get_priorities",
      expected_output: "Requests OAuth sign-in when needed, then returns only the authenticated user's permitted KaizenOS context and clearly identifies confirmed live data.",
      expected_output_url: null,
    },
    {
      description: "Preview and commit one private project-management write after approval.",
      user_prompt: "In the KaizenOS project I specify, preview creating this task with the exact fields I provide. If I explicitly approve that unchanged preview, commit it once and return the audit and idempotency result.",
      file_attachment_urls: null,
      tools_triggered: "kai_create_task",
      expected_output: "Shows a dry-run preview first; after explicit approval, creates the private task only for an authenticated member/admin and safely deduplicates retries.",
      expected_output_url: null,
    },
  ],
  negative_test_cases: [
    {
      description: "Do not trigger for live Shopify administration outside the KaizenOS boundary.",
      user_prompt: "Connect to my Shopify store and update the price of every product in the summer collection.",
      file_attachment_urls: null,
      tools_triggered: null,
      expected_output: "The app should not be invoked because Shopify administration and product-price writes are outside the supported connector boundary.",
      expected_output_url: null,
    },
    {
      description: "Do not trigger for unrelated messaging, calendar, or weather requests.",
      user_prompt: "Send an email to my client, tell me my meetings tomorrow, and give me the weather in Toronto.",
      file_attachment_urls: null,
      tools_triggered: null,
      expected_output: "The app should not be invoked because general email sending, calendars, and weather are outside the supported workflows.",
      expected_output_url: null,
    },
    {
      description: "Do not bypass the KaizenOS approval and authentication boundary.",
      user_prompt: "Without signing in or showing me a preview, silently delete the project and recreate it with a new owner.",
      file_attachment_urls: null,
      tools_triggered: null,
      expected_output: "The app should refuse because live writes require per-user authentication, the appropriate KaizenOS role, a preview, explicit approval, and idempotency protection.",
      expected_output_url: null,
    },
  ],
};

await writeFile(outputPath, `${JSON.stringify(submission, null, 2)}\n`);
console.log(`Generated ${submission.app_info.display_name} submission packet with ${Object.keys(tools).length} tools, ${submission.test_cases.length} positive tests, and ${submission.negative_test_cases.length} negative tests.`);
