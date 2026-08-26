# Vendored KaizenOS contract

`kaizenos-agent-tools.json` is copied from the canonical KaizenOS contract in
`Kaizen-Commerce/kaizen-skills` and is used only to source names, titles,
descriptions, actions, and destructive metadata for the plugin's named MCP
wrappers.

The KaizenOS app remains the source of truth. This plugin's allowlist in
`mcp/kaizenos.mjs` intentionally includes CRM and project-management tools plus
the reads needed to operate them. It excludes finance, Outlook sync,
discovery-email, quote-send, and other unrelated actions.

Refresh this file from the canonical contract before changing the allowlist,
then run `npm test`. Never add an invented `kai_*` name or edit the contract to
make a wrapper appear valid.
