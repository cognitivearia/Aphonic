import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.dirname(fileURLToPath(import.meta.url));
const viewer = path.resolve(root, "..");
const src = path.resolve(viewer, "../assets/mockups");
const dest = path.resolve(viewer, "public/assets");

fs.rmSync(dest, { recursive: true, force: true });
fs.mkdirSync(dest, { recursive: true });

for (const name of fs.readdirSync(src)) {
  // Skip huge x3 review dumps on Pages to keep the site lighter
  if (name.endsWith("-x3.png")) continue;
  fs.copyFileSync(path.join(src, name), path.join(dest, name));
}

fs.writeFileSync(path.resolve(viewer, "public/.nojekyll"), "");
console.log(`Synced mockup assets → public/assets (${fs.readdirSync(dest).length} files)`);
