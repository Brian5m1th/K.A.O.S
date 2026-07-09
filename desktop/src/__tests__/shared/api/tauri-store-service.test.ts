import { describe, it, expect, vi, beforeEach, afterEach } from "vitest";
import { TauriStoreService } from "@/shared/api/tauri-store-service";

// Mock isTauri do ipc-bridge
vi.mock("@/shared/api/ipc-bridge", () => ({
  isTauri: vi.fn(() => false),
}));

import { isTauri } from "@/shared/api/ipc-bridge";

describe("TauriStoreService", () => {
  beforeEach(() => {
    vi.mocked(isTauri).mockReturnValue(false);
    TauriStoreService.resetInstance();
    localStorage.clear();
  });

  afterEach(() => {
    TauriStoreService.resetInstance();
    localStorage.clear();
  });

  describe("get", () => {
    it("should return null for non-existent key in localStorage fallback", async () => {
      const result = await TauriStoreService.get("non-existent");
      expect(result).toBeNull();
    });

    it("should return stored value from localStorage", async () => {
      localStorage.setItem(
        'settings.json:api-key',
        JSON.stringify("my-api-key-123")
      );

      const result = await TauriStoreService.get("api-key");
      expect(result).toBe("my-api-key-123");
    });

    it("should return parsed object from localStorage", async () => {
      const config = { theme: "dark", accent: "#3B82F6" };
      localStorage.setItem("settings.json:theme-config", JSON.stringify(config));

      const result = await TauriStoreService.get("theme-config");
      expect(result).toEqual(config);
    });

    it("should return null when JSON is malformed", async () => {
      localStorage.setItem("settings.json:broken", "not-json{{{");

      const result = await TauriStoreService.get("broken");
      expect(result).toBeNull();
    });
  });

  describe("set", () => {
    it("should store value in localStorage with prefix", async () => {
      const result = await TauriStoreService.set("api-key", "key-456");

      expect(result).toBe(true);
      expect(localStorage.getItem("settings.json:api-key")).toBe(
        JSON.stringify("key-456")
      );
    });

    it("should store complex objects", async () => {
      const settings = { theme: "light", fontSize: 14 };
      await TauriStoreService.set("settings", settings);

      const stored = localStorage.getItem("settings.json:settings");
      expect(JSON.parse(stored!)).toEqual(settings);
    });
  });

  describe("getAll", () => {
    it("should return all stored values without prefix", async () => {
      localStorage.setItem("settings.json:key1", JSON.stringify("val1"));
      localStorage.setItem("settings.json:key2", JSON.stringify("val2"));
      localStorage.setItem("other:key3", JSON.stringify("val3"));

      const all = await TauriStoreService.getAll();

      expect(all).toEqual({
        key1: "val1",
        key2: "val2",
      });
      expect(all).not.toHaveProperty("key3");
    });

    it("should return empty object when no keys exist", async () => {
      const all = await TauriStoreService.getAll();
      expect(all).toEqual({});
    });

    it("should return empty object on error", async () => {
      // Simula erro no localStorage
      vi.spyOn(Object.getPrototypeOf(localStorage), "getItem").mockImplementationOnce(
        () => {
          throw new Error("storage error");
        }
      );

      const all = await TauriStoreService.getAll();
      expect(all).toEqual({});
    });
  });

  describe("resetInstance", () => {
    it("should allow re-initialization", async () => {
      await TauriStoreService.get("key1");

      TauriStoreService.resetInstance();

      // Após reset, deve funcionar novamente
      const result = await TauriStoreService.get("key1");
      expect(result).toBeNull();
    });
  });

  describe("Tauri native mode", () => {
    beforeEach(() => {
      vi.mocked(isTauri).mockReturnValue(true);

      // Mock do Store do Tauri
      const mockStoreInstance = {
        get: vi.fn().mockResolvedValue("tauri-value"),
        set: vi.fn().mockResolvedValue(undefined),
        save: vi.fn().mockResolvedValue(undefined),
        entries: vi.fn().mockResolvedValue([
          ["key1", "val1"],
          ["key2", "val2"],
        ]),
      };

      vi.mock("@tauri-apps/plugin-store", () => ({
        Store: {
          load: vi.fn().mockResolvedValue(mockStoreInstance),
        },
      }));
    });

    it("should use Tauri store when in Tauri environment", async () => {
      const result = await TauriStoreService.get("key1");
      expect(result).toBe("tauri-value");
    });
  });
});