import { describe, it, expect, vi, beforeEach } from "vitest";
import { useThemeStore } from "@/shared/lib/stores/theme-store";
import { kaosFetch } from "@/infrastructure/http";

vi.mock("@/infrastructure/http", () => ({ kaosFetch: vi.fn() }));
const mockFetch = vi.mocked(kaosFetch);

// Mock localStorage for theme
const store: Record<string,string> = {};
vi.stubGlobal("localStorage", {
  getItem: (k: string) => store[k] ?? null,
  setItem: (k: string, v: string) => { store[k] = v; },
  removeItem: (k: string) => { delete store[k]; },
  clear: () => { Object.keys(store).forEach(k => delete store[k]); },
  get length() { return Object.keys(store).length; },
  key: (i: number) => Object.keys(store)[i] ?? null,
});

describe("Theme Store", () => {
  beforeEach(() => {
    localStorage.clear();
    vi.stubGlobal("document", { documentElement: { style: { setProperty: vi.fn() } } });
  });

  it("should initialize with dark mode default", () => {
    const s = useThemeStore.getState();
    expect(s.mode).toBe("dark"); // default when localStorage empty
  });

  it("setMode should change mode", () => {
    useThemeStore.getState().setMode("light");
    expect(useThemeStore.getState().mode).toBe("light");
  });

  it("setAccentColor should change color", () => {
    useThemeStore.getState().setAccentColor("#8B5CF6");
    expect(useThemeStore.getState().accentColor).toBe("#8B5CF6");
  });

  it("loadFromBackend should fetch and apply", async () => {
    mockFetch.mockResolvedValue(new Response(JSON.stringify({ theme: "nordic", accent_color: "#10B981" }), { status: 200 }));
    await useThemeStore.getState().loadFromBackend();
    expect(useThemeStore.getState().mode).toBe("nordic");
    expect(useThemeStore.getState().accentColor).toBe("#10B981");
  });

  it("saveToBackend should PUT settings", async () => {
    useThemeStore.setState({ mode: "light", accentColor: "#EF4444" });
    mockFetch.mockResolvedValue(new Response(null, { status: 200 }));
    await useThemeStore.getState().saveToBackend();
    expect(mockFetch).toHaveBeenCalledWith("/api/settings", expect.any(String), expect.objectContaining({
      method: "PUT",
      body: expect.stringContaining("light"),
    }));
  });
});
