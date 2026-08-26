import { access, readFile } from "node:fs/promises";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const pluginRoot = join(fileURLToPath(new URL("..", import.meta.url)));
const manifestPath = join(pluginRoot, ".codex-plugin", "plugin.json");
const appManifestPath = join(pluginRoot, ".app.json");
const manifest = JSON.parse(await readFile(manifestPath, "utf8"));

try {
  await access(appManifestPath);
} catch {
  console.log("ChatGPT app mapping: not configured yet (expected until Developer Mode creates a plugin_asdk_app connection).");
  process.exit(0);
}

const appManifest = JSON.parse(await readFile(appManifestPath, "utf8"));
if (!appManifest.apps || typeof appManifest.apps !== "object" || Array.isArray(appManifest.apps)) {
  throw new Error(".app.json must contain an apps object.");
}
if (manifest.apps !== "./.app.json") {
  throw new Error("plugin.json must point apps to ./.app.json when the mapping exists.");
}

const entries = Object.entries(appManifest.apps);
if (entries.length === 0) throw new Error(".app.json apps must contain at least one registered app.");
for (const [name, value] of entries) {
  if (!value || typeof value !== "object" || typeof value.id !== "string" || !value.id.trim()) {
    throw new Error(`.app.json app ${name} must contain a non-empty id.`);
  }
}

console.log(`ChatGPT app mapping: configured (${entries.map(([name]) => name).join(", ")}).`);
