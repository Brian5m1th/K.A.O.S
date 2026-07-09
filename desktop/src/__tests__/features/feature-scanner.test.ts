import { describe, it, expect } from "vitest";
import { FeatureScanner } from "@/features/documentation-ui/engine/feature-scanner";

describe("FeatureScanner", () => {
  it("should have static methods defined", () => {
    expect(FeatureScanner.listAll).toBeDefined();
    expect(FeatureScanner.getById).toBeDefined();
    expect(FeatureScanner.filterByPhase).toBeDefined();
    expect(FeatureScanner.filterByStatus).toBeDefined();
  });
});
