import { describe, it, expect } from "vitest";
import { GraphExport } from "@/features/documentation-ui/graph/graph-export";

describe("GraphExport", () => {
  const graphData = {
    nodes: [{ id: "a", label: "A", type: "feature" as const, phase: "p1", status: "done", x: 0, y: 0 }],
    edges: [{ from: "a", to: "b", relation: "uses" as const }],
    metadata: { totalNodes: 1, totalEdges: 1, nodeTypes: { feature: 1 }, coverage: 50, driftLevel: "medium" },
    width: 800, height: 600,
  };

  it("toJSON should serialize correctly", () => {
    const json = GraphExport.toJSON(graphData as any);
    const parsed = JSON.parse(json);
    expect(parsed.nodes).toHaveLength(1);
    expect(parsed.metadata.coverage).toBe(50);
  });

  it("toGraphML should generate valid XML", () => {
    const xml = GraphExport.toGraphML(graphData as any);
    expect(xml).toContain("<?xml");
    expect(xml).toContain("<graphml");
    expect(xml).toContain("node");
    expect(xml).toContain("edge");
  });

  it("toSVG should generate valid SVG", () => {
    const svg = GraphExport.toSVG(graphData as any);
    expect(svg).toContain("<svg");
    expect(svg).toContain("</svg>");
  });
});
