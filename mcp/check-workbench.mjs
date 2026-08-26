import { readFile } from "node:fs/promises";

const html = await readFile(new URL("./workbench.html", import.meta.url), "utf8");
const scriptMatches = [...html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/gi)];
if (scriptMatches.length !== 1) {
  throw new Error(`Expected exactly one inline widget script, found ${scriptMatches.length}.`);
}

new Function(scriptMatches[0][1]);

for (const marker of [
  "ui/initialize",
  "ui/notifications/tool-result",
  "tools/call",
  "ui/message",
  "ui/update-model-context",
  "window.openai",
]) {
  if (!html.includes(marker)) throw new Error(`Missing widget contract marker: ${marker}`);
}

console.log(`Workbench widget check passed (${html.length} bytes).`);
