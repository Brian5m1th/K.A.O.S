import { describe, it, expect } from "vitest";
import { DriftEngine } from "@/features/documentation-audit/engine/drift-engine";

describe("DriftEngine", () => {
  it("should have static methods defined", () => {
    expect(DriftEngine.getReport).toBeDefined();
    expect(DriftEngine.getCoverage).toBeDefined();
    expect(DriftEngine.getMissingCount).toBeDefined();
  });
});
