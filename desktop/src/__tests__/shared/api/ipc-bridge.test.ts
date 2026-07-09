import { describe, it, expect, vi, beforeEach } from "vitest";
import { isTauri, invokeIpc, listenIpc } from "@/infrastructure/ipc";

describe("ipc-bridge", () => {
  beforeEach(() => {
    vi.unstubAllGlobals();
    vi.stubGlobal("fetch", vi.fn());
  });

  afterEach(() => {
    vi.unstubAllGlobals();
  });

  describe("isTauri", () => {
    it("should return true when __TAURI_INTERNALS__ is defined", () => {
      vi.stubGlobal("window", { __TAURI_INTERNALS__: {} });
      expect(isTauri()).toBe(true);
    });

    it("should return false when __TAURI_INTERNALS__ is undefined", () => {
      vi.stubGlobal("window", {});
      expect(isTauri()).toBe(false);
    });
  });

  describe("invokeIpc web fallback", () => {
    beforeEach(() => { vi.stubGlobal("window", {}); });

    it("should return web version for get_app_version", async () => {
      const result = await invokeIpc("get_app_version");
      expect(result).toBe("0.6.0-web");
    });

    it("should return no update for check_for_update", async () => {
      const result = await invokeIpc("check_for_update");
      expect(result).toEqual({ available: false });
    });

    it("should check backend health via fetch", async () => {
      vi.mocked(fetch).mockResolvedValue(
        new Response(JSON.stringify({ status: "ok" }), { status: 200 })
      );
      const result = await invokeIpc("check_backend_health", { server_url: "http://localhost:8000" });
      expect(result).toEqual({ reachable: true, status: "ok", error: null });
    });

    it("should return undefined for unknown command", async () => {
      const result = await invokeIpc("unknown_cmd");
      expect(result).toBeUndefined();
    });
  });

  describe("listenIpc", () => {
    it("should return no-op unlisten in web environment", async () => {
      vi.stubGlobal("window", {});
      const handler = vi.fn();
      const unlisten = await listenIpc("some-event", handler);
      expect(typeof unlisten).toBe("function");
      expect(() => unlisten()).not.toThrow();
      expect(handler).not.toHaveBeenCalled();
    });
  });
});