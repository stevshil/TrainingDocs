import tailwindcss from "@tailwindcss/vite";
import react from "@vitejs/plugin-react";
import { defineConfig } from "vitest/config";

const proxy = {
  "/peoplejson": {
    target: "http://localhost:3000",
    changeOrigin: true,
  },
};

export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    port: 5173,
    strictPort: true,
    proxy,
  },
  preview: { proxy },
  test: {
    environment: "jsdom",
    restoreMocks: true,
    unstubGlobals: true,
  },
});
