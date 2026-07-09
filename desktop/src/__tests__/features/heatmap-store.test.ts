import { describe, it, expect, vi, beforeEach } from "vitest";
import { useHeatmapStore } from "@/features/documentation-audit/heatmap/heatmap-store";
import { kaosFetch } from "@/infrastructure/http";

vi.mock("@/infrastructure/http", () => ({ kaosFetch: vi.fn() }));
const mockFetch = vi.mocked(kaosFetch);

const mockEntry = { date: "2025-01-01", score: 80, level: "low" as const, missingLinks: 2, sddMismatch: 1, codeVsVaultDiff: 3 };
const mockEntry2 = { date: "2025-01-02", score: 60, level: "medium" as const, missingLinks: 5, sddMismatch: 3, codeVsVaultDiff: 7 };
const mockAnalysis = { coverageScore: 65, driftLevel: "medium", totalIssues: 12, suggestions: ["Add tests"], warnings: ["Low coverage"], generatedAt: "2025-01-02T00:00:00Z" };

describe("HeatmapStore", () => {
  beforeEach(() => {
    useHeatmapStore.setState({ history: [], currentScore: null, analysis: null, isLoading: false, selectedDate: null });
    mockFetch.mockReset();
  });

  it("fetchHistory should populate history", async () => {
    mockFetch.mockResolvedValue(new Response(JSON.stringify(mockEntry), { status: 200 }));
    await useHeatmapStore.getState().fetchHistory();
    expect(useHeatmapStore.getState().history).toHaveLength(1);
    expect(useHeatmapStore.getState().currentScore?.score).toBe(80);
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