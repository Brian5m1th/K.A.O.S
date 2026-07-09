import { describe, it, expect, vi, beforeEach } from "vitest";
import { isTauri, invokeIpc, listenIpc } from "@/shared/api/ipc-bridge";

describe("ipc-bridge", () => {
  beforeEach(() => {
    vi.unstubAllGlobals();
    vi.restoreAllMocks();
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

    it("should return false in non-window environment", () => {
      // @ts-expect-error - testing no window
      const orig = globalThis.window;
      // @ts-expect-error - testing no window
      delete globalThis.window;
      expect(isTauri()).toBe(false);
      globalThis.window = orig;
    });
  });

  describe("invokeIpc", () => {
    describe("web fallback", () => {
      beforeEach(() => {
        vi.stubGlobal("window", {});
      });

      it("should return web version for get_app_version", async () => {
        const result = await invokeIpc("get_app_version");
        expect(result).toBe("0.6.0-web");
      });

      it("should return no update for check_for_update", async () => {
        const result = await invokeIpc("check_for_update");
        expect(result).toEqual({ available: false });
      });

      it("should return docker available for check_docker", async () => {
        const result = await invokeIpc("check_docker");
        expect(result).toEqual({
          available: true,
          version: "Docker Desktop (web fallback)",
        });
      });

      it("should return engine running for check_docker_engine", async () => {
        const result = await invokeIpc("check_docker_engine");
        expect(result).toEqual({
          running: true,
          info: "Engine running (web fallback)",
        });
      });

      it("should check backend health via fetch", async () => {
        vi.mocked(fetch).mockResolvedValue(
          new Response(JSON.stringify({ status: "ok" }), { status: 200 })
        );

        const result = await invokeIpc("check_backend_health", {
          server_url: "http://localhost:8000",
        });

        expect(fetch).toHaveBeenCalledWith("http://localhost:8000/health");
        expect(result).toEqual({
          reachable: true,
          status: "ok",
          error: null,
        });
      });

      it("should handle backend health failure", async () => {
        vi.mocked(fetch).mockRejectedValue(new Error("Connection refused"));

        const result = await invokeIpc("check_backend_health", {
          server_url: "http://localhost:8000",
        });

        expect(result).toEqual({
          reachable: false,
          status: null,
          error: "Connection refused",
        });
      });

      it("should fetch bootstrap state", async () => {
        const bootstrapData = {
          state: "ready",
          is_ready: true,
          degraded: false,
          boot_complete: true,
          stages: [],
          errors: [],
          total_elapsed_ms: 1500,
        };
        vi.mocked(fetch).mockResolvedValue(
          new Response(JSON.stringify(bootstrapData), { status: 200 })
        );

        const result = await invokeIpc("get_bootstrap_state", {
          server_url: "http://localhost:8000",
        });

        expect(fetch).toHaveBeenCalledWith(
          "http://localhost:8000/api/system/bootstrap"
        );
        expect(result).toEqual(bootstrapData);
      });

      it("should return undefined for unknown command", async () => {
        const result = await invokeIpc("non_existent_command");
        expect(result).toBeUndefined();
      });
    });

    describe("Tauri mode", () => {
      it("should attempt to call Tauri invoke when in Tauri", async () => {
        vi.stubGlobal("window", { __TAURI_INTERNALS__: {} });

        // Mock import dinâmico do @tauri-apps/api/core
        const mockInvoke = vi.fn().mockResolvedValue("tauri-result");
        vi.stubGlobal(
          "__TAURI_INVOKE_MOCK__",
          vi.fn(() => "tauri-result")
        );

        const result = await invokeIpc("some_command", { arg: 1 });
        expect(result).toBe("tauri-result");
      });
    });
  });

  describe("listenIpc", () => {
    it("should return unlisten function in Tauri environment", async () => {
      vi.stubGlobal("window", { __TAURI_INTERNALS__: {} });
      const mockListen = vi.fn(() => Promise.resolve(() => {}));

      const unlisten = await listenIpc("some-event", () => {});
      expect(typeof unlisten).toBe("function");
    });

    it("should return no-op unlisten in web environment", async () => {
      vi.stubGlobal("window", {});

      const handler = vi.fn();
      const unlisten = await listenIpc("some-event", handler);

      expect(typeof unlisten).toBe("function");
      // Calling the unlisten function should not throw
      expect(() => unlisten()).not.toThrow();
      // Handler should never have been called
      expect(handler).not.toHaveBeenCalled();
    });
  });
});