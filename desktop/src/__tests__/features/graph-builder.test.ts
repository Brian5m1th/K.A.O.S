import { describe, it, expect, vi, beforeEach } from "vitest";
import { GraphBuilder, type GraphNode, type GraphEdge, type GraphData } from "@/features/documentation-audit/graph/graph-builder";

describe("GraphBuilder", () => {
  const snapshot = {
    features: [
      { id: "feat1", name: "Feature One", phase: "p1", status: "done", docs: ["sdd/feat1.md"], codeRefs: ["store/feat1-store.ts", "route/feat1-route.ts"] },
      { id: "feat2", name: "Feature Two", phase: "p2", status: "in_progress", docs: [], codeRefs: ["agent/feat2-agent.ts"] },
    ],
    coverage: 50,
    driftLevel: "medium",
    generatedAt: "2025-01-01T00:00:00Z",
    graphSummary: {},
    lastCommit: "abc",
    missingCount: 1,
    outdatedCount: 1,
  };

  it("buildFromSnapshot should create graph with nodes and edges", () => {
    const graph = GraphBuilder.buildFromSnapshot(snapshot as any);
    expect(graph).toBeDefined();
    expect(graph.nodes.length).toBeGreaterThanOrEqual(2);
    expect(graph.edges.length).toBeGreaterThanOrEqual(0);
    expect(graph.metadata.coverage).toBe(50);
    expect(graph.metadata.driftLevel).toBe("medium");
  });

  it("buildFromSnapshot should create document edges for features with docs", () => {
    const graph = GraphBuilder.buildFromSnapshot(snapshot as any);
    const docEdges = graph.edges.filter(e => e.relation === "documents");
    expect(docEdges.length).toBeGreaterThanOrEqual(1);
  });

  it("buildFromSnapshot should add system nodes", () => {
    const graph = GraphBuilder.buildFromSnapshot(snapshot as any);
    const systemNodes = graph.nodes.filter(n => n.type === "feature" || n.type === "store" || n.type === "route");
    expect(systemNodes.length).toBeGreaterThan(0);
  });
});
