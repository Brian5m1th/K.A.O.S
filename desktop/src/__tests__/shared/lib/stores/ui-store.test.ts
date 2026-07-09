import { describe, it, expect } from "vitest";
import { useUIStore } from "@/shared/lib/stores/ui-store";

describe("UI Store", () => {
  beforeEach(() => { useUIStore.setState({ sidebarCollapsed: false, commandPaletteOpen: false }); });

  it("should start with sidebar expanded", () => { expect(useUIStore.getState().sidebarCollapsed).toBe(false); });
  it("toggleSidebar should invert", () => { useUIStore.getState().toggleSidebar(); expect(useUIStore.getState().sidebarCollapsed).toBe(true); });
  it("setCommandPaletteOpen should set state", () => { useUIStore.getState().setCommandPaletteOpen(true); expect(useUIStore.getState().commandPaletteOpen).toBe(true); });
});
