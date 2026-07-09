import { describe, it, expect, vi, beforeEach } from "vitest";
import { useDriftStore } from "@/features/documentation-audit/store/drift-store";
import { kaosFetch } from "@/infrastructure/http";

vi.mock("@/infrastructure/http", () => ({ kaosFetch: vi.fn() }));
const mockFetch = vi.mocked(kaosFetch);

const mockSnapshot = {
  features: [],
  coverage: 45.5,
  driftLevel: "medium",
  lastCommit: "abc123",
  graphSummary: { totalNodes: 10, totalEdges: 5 },
  missingCount: 3,
  outdatedCount: 2,
  generatedAt: "2025-06-15T10:00:00Z",
};

describe("DriftStore", () => {
  beforeEach(() => {
    useDriftStore.setState({
      driftReport: null, isLoading: false, lastScan: null,
    });
    mockFetch.mockReset();
  });

  it("should initialize with null report", () => {
    const s = useDriftStore.getState();
    expect(s.driftReport).toBeNull();
    expect(s.isLoading).toBe(false);
  });

  it("runAudit should POST and update report", async () => {
    mockFetch.mockResolvedValue(new Response(JSON.stringify(mockSnapshot), { status: 200 }));
    await useDriftStore.getState().runAudit();
    const s = useDriftStore.getState();
    expect(s.driftReport?.coverage).toBe(45.5);
    expect(s.driftReport?.driftLevel).toBe("medium");
    expect(s.lastScan).toBeGreaterThan(0);
  });

  it("loadSnapshot should GET snapshot", async () => {
    mockFetch.mockResolvedValue(new Response(JSON.stringify(mockSnapshot), { status: 200 }));
    await useDriftStore.getState().loadSnapshot();
    expect(useDriftStore.getState().driftReport?.coverage).toBe(45.5);
  });
});
