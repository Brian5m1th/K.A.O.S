import { describe, it, expect, vi, beforeEach } from "vitest";
import { useHeatmapStore } from "@/features/documentation-audit/heatmap/heatmap-store";
import { kaosFetch } from "@/infrastructure/http";

vi.mock("@/infrastructure/http", () => ({ kaosFetch: vi.fn() }));
const mockFetch = vi.mocked(kaosFetch);

const mockHistoryResponse = {
  total: 2,
  history: [
    { date: "2025-01-01", score: 80, level: "low", missing_links: 2, sdd_mismatch: 1, code_vs_vault_diff: 3 },
    { date: "2025-01-02", score: 60, level: "medium", missing_links: 5, sdd_mismatch: 3, code_vs_vault_diff: 7 },
  ],
};
const mockAnalysis = { coverageScore: 65, driftLevel: "medium", totalIssues: 12, suggestions: ["Add tests"], warnings: ["Low coverage"], generatedAt: "2025-01-02T00:00:00Z" };

describe("HeatmapStore", () => {
  beforeEach(() => {
    useHeatmapStore.setState({ history: [], currentScore: null, analysis: null, isLoading: false, selectedDate: null });
    mockFetch.mockReset();
  });

  it("fetchHistory should populate history from /api/architecture/history", async () => {
    mockFetch.mockResolvedValue(new Response(JSON.stringify(mockHistoryResponse), { status: 200 }));
    await useHeatmapStore.getState().fetchHistory();
    expect(useHeatmapStore.getState().history).toHaveLength(2);
    expect(useHeatmapStore.getState().currentScore?.score).toBe(60);
    expect(useHeatmapStore.getState().history[0].date).toBe("2025-01-01");
    expect(useHeatmapStore.getState().history[1].score).toBe(60);
  });

  it("fetchHistory should handle empty history", async () => {
    mockFetch.mockResolvedValue(new Response(JSON.stringify({ total: 0, history: [] }), { status: 200 }));
    await useHeatmapStore.getState().fetchHistory();
    expect(useHeatmapStore.getState().history).toHaveLength(0);
    expect(useHeatmapStore.getState().currentScore).toBeNull();
  });

  it("fetchAnalysis should store analysis", async () => {
    const snakeAnalysis = { coverage_score: 65, drift_level: "medium", total_issues: 12, suggestions: ["Add tests"], warnings: ["Low coverage"], generated_at: "2025-01-02T00:00:00Z" };
    mockFetch.mockResolvedValue(new Response(JSON.stringify(snakeAnalysis), { status: 200 }));
    await useHeatmapStore.getState().fetchAnalysis();
    expect(useHeatmapStore.getState().analysis?.coverageScore).toBe(65);
    expect(useHeatmapStore.getState().analysis?.suggestions).toContain("Add tests");
  });

  it("setSelectedDate should update selection", () => {
    useHeatmapStore.getState().setSelectedDate("2025-01-01");
    expect(useHeatmapStore.getState().selectedDate).toBe("2025-01-01");
  });
});