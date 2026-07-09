import { describe, it, expect } from "vitest";
import { FeatureExtractor } from "@/features/documentation-audit/auto-doc/feature-extractor";

describe("FeatureExtractor", () => {
  it("extract should infer feature name from path", () => {
    const features = FeatureExtractor.extract(["store/agent-store.ts", "route/chat-route.ts"]);
    expect(features.length).toBeGreaterThanOrEqual(2);
    features.forEach(f => {
      expect(f.id).toBeDefined();
      expect(f.confidence).toMatch(/high|medium|low/);
    });
  });

  it("should extract from API response", () => {
    const response = { stores: ["store/a.ts"], routes: ["route/b.ts"], tools: [], events: [], agents: [], providers: [] };
    const features = FeatureExtractor.extractFromApiResponse(response);
    expect(features.length).toBeGreaterThanOrEqual(2);
  });
});
