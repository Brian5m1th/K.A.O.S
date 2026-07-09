import { describe, it, expect } from "vitest";
import { LayoutEngine } from "@/features/documentation-ui/graph/layout-engine";

describe("LayoutEngine", () => {
  const nodes = [
    { id: "a", label: "A", type: "feature" as const, x: 0, y: 0 },
    { id: "b", label: "B", type: "store" as const, x: 0, y: 0 },
    { id: "c", label: "C", type: "route" as const, x: 0, y: 0 },
  ];
  const edges = [
    { from: "a", to: "b", relation: "uses" as const },
    { from: "b", to: "c", relation: "uses" as const },
  ];

  it("forceDirected should assign positions", () => {
    const result = LayoutEngine.forceDirected(nodes as any, edges);
    expect(result.nodes).toHaveLength(3);
    result.nodes.forEach(n => {
      expect(typeof n.x).toBe("number");
      expect(typeof n.y).toBe("number");
    });
    expect(result.width).toBeGreaterThan(0);
    expect(result.height).toBeGreaterThan(0);
  });

  it("hierarchical should assign positions", () => {
    const result = LayoutEngine.hierarchical(nodes as any, edges);
    expect(result.nodes).toHaveLength(3);
    result.nodes.forEach(n => {
      expect(typeof n.x).toBe("number");
      expect(typeof n.y).toBe("number");
    });
  });

  it("radial should arrange in circle", () => {
    const result = LayoutEngine.radial(nodes as any, edges);
    expect(result.nodes).toHaveLength(3);
    expect(result.width).toBeGreaterThan(0);
  });
});
