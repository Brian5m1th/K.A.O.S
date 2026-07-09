import { defineConfig } from "vitest/config";
import path from "path";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  define: {
    __APP_VERSION__: JSON.stringify("2.1.0"),
  },
  test: {
    globals: true,
    environment: "jsdom",
    setupFiles: ["./src/__tests__/setup.ts"],
    include: [
      "src/**/*.{test,spec}.{ts,tsx}",
      "src/__tests__/**/*.{test,spec}.{ts,tsx}",
    ],
    exclude: [
      "node_modules",
      "src-tauri",
      "src/__tests__/e2e/**",
      "src/__tests__/setup.ts",
    ],
    coverage: {
      provider: "v8",
      reporter: ["text", "json", "html", "lcov"],
      reportsDirectory: "./coverage",
      include: [
        "src/**/*.{ts,tsx}",
        "!src/**/*.d.ts",
        "!src/**/*.{test,spec}.{ts,tsx}",
        "!src/__tests__/**",
        "!src-tauri/**",
        "!src/vite-env.d.ts",
      ],
      thresholds: {
        lines: 10,
        functions: 40,
        branches: 50,
        statements: 10,
      },
    },
    mockReset: true,
    restoreMocks: true,
    clearMocks: true,
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
});