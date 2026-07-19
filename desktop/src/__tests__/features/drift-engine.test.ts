import { describe, it, expect } from "vitest";
import { DriftEngine } from "@/features/documentation-audit/engine/drift-engine";

describe("DriftEngine", () => {
  it("should have static methods defined", () => {
    expect(DriftEngine.getReport).toBeDefined();
    expect(DriftEngine.getCoverage).toBeDefined();
    expect(DriftEngine.getMissingCount).toBeDefined();
  });

  it("getCoverage should return a number between 0 and 100", () => {
    const coverage = DriftEngine.getCoverage();
    expect(typeof coverage).toBe("number");
    expect(coverage).toBeGreaterThanOrEqual(0);
    expect(coverage).toBeLessThanOrEqual(100);
  });

  it("getMissingCount should return a non-negative integer", () => {
    const count = DriftEngine.getMissingCount();
    expect(typeof count).toBe("number");
    expect(count).toBeGreaterThanOrEqual(0);
    expect(Number.isInteger(count)).toBe(true);
  });

  it("getReport should return null or a valid DriftReport", () => {
    const report = DriftEngine.getReport();
    if (report !== null) {
      expect(typeof report.coverage).toBe("number");
      expect(typeof report.driftLevel).toBe("string");
      expect(Array.isArray(report.missing_features)).toBe(true);
      expect(Array.isArray(report.outdated_docs)).toBe(true);
    }
  });
});
