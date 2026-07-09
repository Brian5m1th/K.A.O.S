import { describe, it, expect, vi, beforeEach } from "vitest";
import { useDriftStore } from "@/features/documentation-audit/store/drift-store";
import { GraphBuilder } from "@/features/documentation-audit/graph/graph-builder";
import { useGraphStore } from "@/features/documentation-audit/graph/graph-store";
import { kaosFetch } from "@/infrastructure/http";

vi.mock("@/infrastructure/http", () => ({ kaosFetch: vi.fn() }));
const mockFetch = vi.mocked(kaosFetch);

const mockSnapshot = {
  features: [{ id: "f1", name: "Feature 1", phase: "p1", status: "done", docs: ["sdd/f1.md"], codeRefs: ["store/s1.ts"] }],
  coverage: 80, driftLevel: "low", lastCommit: "abc", graphSummary: {},
  missingCount: 0, outdatedCount: 0, generatedAt: "2025-01-01T00:00:00Z",
};

describe("Integration: Audit -> Graph Render", () => {
  beforeEach(() => {
    useDriftStore.setState({ driftReport: null, isLoading: false, lastScan: null });
    useGraphStore.setState({ graph: null, selectedNode: null, hoveredNode: null, zoom: 1, pan: { x: 0, y: 0 }, filterType: null, layout: "force" });
    mockFetch.mockReset();
  });

  it("should run audit, build graph, and populate graph store", async () => {
    // Run audit
    mockFetch.mockResolvedValue(new Response(JSON.stringify(mockSnapshot), { status: 200 }));
    await useDriftStore.getState().runAudit();
    expect(useDriftStore.getState().driftReport?.coverage).toBe(80);

    // Build graph
    const graph = GraphBuilder.buildFromSnapshot(mockSnapshot as any);
    expect(graph.metadata.driftLevel).toBe("low");

    // Populate graph store
    useGraphStore.getState().setGraph(graph);
    expect(useGraphStore.getState().graph?.nodes.length).toBeGreaterThanOrEqual(1);

    // Manipulate view
    useGraphStore.getState().selectNode(graph.nodes[0]);
    expect(useGraphStore.getState().selectedNode?.id).toBe(graph.nodes[0].id);
    useGraphStore.getState().setZoom(2);
    expect(useGraphStore.getState().zoom).toBe(2);
    useGraphStore.getState().setFilterType("feature");
    expect(useGraphStore.getState().filterType).toBe("feature");
  });
});
