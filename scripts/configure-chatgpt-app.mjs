import { readFile, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const pluginRoot = join(fileURLToPath(new URL("..", import.meta.url)));
const manifestPath = join(pluginRoot, ".codex-plugin", "plugin.json");
const appManifestPath = join(pluginRoot, ".app.json");
const appId = process.argv[2]?.trim();

if (!appId) {
  console.error("Usage: npm run configure:chatgpt -- plugin_asdk_app_<id>");
  process.exit(1);
}

const manifest = JSON.parse(await readFile(manifestPath, "utf8"));
manifest.apps = "./.app.json";
await writeFile(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`);

const appManifest = {
  apps: {
    "kaizen-knowledge": {
      id: appId,
      category: "Business",
    },
  },
};
await writeFile(appManifestPath, `${JSON.stringify(appManifest, null, 2)}\n`);
console.log(`Configured .app.json for ${appId}. Refresh the plugin in ChatGPT and start a new chat.`);
