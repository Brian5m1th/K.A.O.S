import { describe, it, expect } from "vitest";
import { FeatureScanner } from "@/features/documentation-audit/engine/feature-scanner";

describe("FeatureScanner", () => {
  it("should have static methods defined", () => {
    expect(FeatureScanner.listAll).toBeDefined();
    expect(FeatureScanner.getById).toBeDefined();
    expect(FeatureScanner.filterByPhase).toBeDefined();
    expect(FeatureScanner.filterByStatus).toBeDefined();
  });

  it("listAll should return an array", () => {
    const all = FeatureScanner.listAll();
    expect(Array.isArray(all)).toBe(true);
  });

  it("filterByStatus should work with valid status", () => {
    const completed = FeatureScanner.filterByStatus("done");
    expect(Array.isArray(completed)).toBe(true);
  });

  it("filterByPhase should return array for valid phase", () => {
    const phase1 = FeatureScanner.filterByPhase(1);
    expect(Array.isArray(phase1)).toBe(true);
  });
});
