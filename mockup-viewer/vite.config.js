import { defineConfig } from "vite";
import path from "node:path";
import { fileURLToPath } from "node:url";
import fs from "node:fs";

const root = path.dirname(fileURLToPath(import.meta.url));
const mockups = path.resolve(root, "../assets/mockups");

// Relative base so GitHub Pages works for user/org or project sites
export default defineConfig({
  base: "./",
  publicDir: "public",
  build: {
    outDir: "dist",
    emptyOutDir: true,
    assetsDir: "assets-built",
  },
  server: {
    host: "0.0.0.0",
    port: 3847,
    strictPort: true,
    fs: { allow: [root, path.resolve(root, "..")] },
  },
  plugins: [
    {
      name: "serve-mockup-assets-dev",
      configureServer(server) {
        // Dev: read live from ../assets/mockups
        server.middlewares.use((req, res, next) => {
          if (!req.url?.startsWith("/assets/")) return next();
          const file = path.resolve(
            mockups,
            decodeURIComponent(req.url.slice("/assets/".length).split("?")[0]),
          );
          if (!file.startsWith(mockups) || !fs.existsSync(file)) {
            res.statusCode = 404;
            res.end("missing");
            return;
          }
          const ext = path.extname(file);
          res.setHeader(
            "Content-Type",
            ext === ".png"
              ? "image/png"
              : ext === ".json"
                ? "application/json"
                : "application/octet-stream",
          );
          fs.createReadStream(file).pipe(res);
        });
      },
    },
  ],
});
