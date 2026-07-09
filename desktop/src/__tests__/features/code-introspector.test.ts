import { describe, it, expect } from "vitest";
import { CodeIntrospector } from "@/features/documentation-audit/auto-doc/code-introspector";

describe("CodeIntrospector", () => {
  it("scan should return categorized modules", () => {
    const result = CodeIntrospector.scan();
    expect(result.stores).toBeDefined();
    expect(result.routes).toBeDefined();
    expect(result.tools).toBeDefined();
    expect(Array.isArray(result.stores)).toBe(true);
  });
});
