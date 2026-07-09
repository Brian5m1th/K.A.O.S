import { describe, it, expect, vi, beforeEach } from "vitest";
import { TauriStoreService } from "@/shared/api/tauri-store-service";

vi.mock("@/shared/api/ipc-bridge", () => ({
  isTauri: vi.fn(() => false),
}));

vi.mock("@tauri-apps/plugin-store", () => ({
  Store: {
    load: vi.fn().mockResolvedValue({
      get: vi.fn().mockResolvedValue("tauri-value"),
      set: vi.fn().mockResolvedValue(undefined),
      save: vi.fn().mockResolvedValue(undefined),
      entries: vi.fn().mockResolvedValue([
        ["key1", "val1"],
        ["key2", "val2"],
      ]),
    }),
  },
}));

import { isTauri } from "@/shared/api/ipc-bridge";

const STORE_PREFIX = "settings.json:";

describe("TauriStoreService", () => {
  beforeEach(() => {
    vi.mocked(isTauri).mockReturnValue(false);
    TauriStoreService.resetInstance();
    localStorage.clear();
  });

  describe("get", () => {
    it("should return null for missing keys", async () => {
      const result = await TauriStoreService.get("missing");
      expect(result).toBeNull();
    });

    it("should retrieve stored values", async () => {
      localStorage.setItem(STORE_PREFIX + "theme", JSON.stringify("dark"));
      const result = await TauriStoreService.get("theme");
      expect(result).toBe("dark");
    });

    it("should handle JSON parse gracefully", async () => {
      localStorage.setItem(STORE_PREFIX + "bad", "not-json");
      const result = await TauriStoreService.get("bad");
      expect(result).toBeNull();
    });
  });

  describe("set", () => {
    it("should store values", async () => {
      const ok = await TauriStoreService.set("key1", "value1");
      expect(ok).toBe(true);
      expect(localStorage.getItem(STORE_PREFIX + "key1")).toBe(JSON.stringify("value1"));
    });

    it("should overwrite existing values", async () => {
      await TauriStoreService.set("key", "first");
      await TauriStoreService.set("key", "second");
      const result = await TauriStoreService.get("key");
      expect(result).toBe("second");
    });
  });

  describe("getAll", () => {
    it("should return all stored entries", async () => {
      localStorage.setItem(STORE_PREFIX + "a", JSON.stringify(1));
      localStorage.setItem(STORE_PREFIX + "b", JSON.stringify(2));
      const all = await TauriStoreService.getAll();
      expect(all).toEqual({ a: 1, b: 2 });
    });

    it("should skip non-prefixed keys", async () => {
      localStorage.setItem("other", JSON.stringify("x"));
      localStorage.setItem(STORE_PREFIX + "y", JSON.stringify(42));
      const all = await TauriStoreService.getAll();
      expect(all).toEqual({ y: 42 });
    });

    it("should return empty object when no keys exist", async () => {
      const all = await TauriStoreService.getAll();
      expect(all).toEqual({});
    });

    it("should return empty object on error", async () => {
      vi.spyOn(localStorage as any, "getItem").mockImplementationOnce(() => {
        throw new Error("storage error");
      });
      const all = await TauriStoreService.getAll();
      expect(all).toEqual({});
    });
  });

  describe("resetInstance", () => {
    it("should allow re-initialization", async () => {
      await TauriStoreService.get("key1");
      TauriStoreService.resetInstance();
      const result = await TauriStoreService.get("key1");
      expect(result).toBeNull();
    });
  });

  describe("Tauri native mode", () => {
    beforeEach(() => {
      vi.mocked(isTauri).mockReturnValue(true);
      TauriStoreService.resetInstance();
    });

    it("should use Tauri store when in Tauri environment", async () => {
      TauriStoreService.resetInstance();
      const result = await TauriStoreService.get("key1");
      expect(result).toBe("tauri-value");
    });
  });
});