import { describe, it, expect } from "vitest";
import { CodeIntrospector } from "@/features/documentation-audit/auto-doc/code-introspector";

describe("CodeIntrospector", () => {
  it("scan should return categorized modules with expected structure", () => {
    const result = CodeIntrospector.scan();
    expect(result.stores).toBeDefined();
    expect(result.routes).toBeDefined();
    expect(result.tools).toBeDefined();
    expect(result.events).toBeDefined();
    expect(result.agents).toBeDefined();
    expect(result.providers).toBeDefined();
    expect(Array.isArray(result.stores)).toBe(true);
    expect(Array.isArray(result.routes)).toBe(true);
    expect(Array.isArray(result.tools)).toBe(true);
  });

  it("scan should return stores array with string entries", () => {
    const result = CodeIntrospector.scan();
    if (result.stores.length > 0) {
      expect(typeof result.stores[0]).toBe("string");
    }
  });

  it("scan should return routes array with string entries", () => {
    const result = CodeIntrospector.scan();
    if (result.routes.length > 0) {
      expect(typeof result.routes[0]).toBe("string");
    }
  });

  it("scan should return tools array with string entries", () => {
    const result = CodeIntrospector.scan();
    if (result.tools.length > 0) {
      expect(typeof result.tools[0]).toBe("string");
    }
  });
});
