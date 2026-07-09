import { describe, it, expect, vi, beforeEach } from "vitest";
import { useHeatmapStore } from "@/features/documentation-ui/heatmap/heatmap-store";
import { kaosFetch } from "@/shared/api/kaos-client";

vi.mock("@shared/api/kaos-client", () => ({ kaosFetch: vi.fn() }));
const mockFetch = vi.mocked(kaosFetch);

const mockHeatmap = [
  { date: "2025-01-01", score: 80, level: "low", missingLinks: 2, sddMismatch: 1, codeVsVaultDiff: 3 },
  { date: "2025-01-02", score: 60, level: "medium", missingLinks: 5, sddMismatch: 3, codeVsVaultDiff: 7 },
];
const mockAnalysis = { coverageScore: 65, driftLevel: "medium", totalIssues: 12, suggestions: ["Add tests"], warnings: ["Low coverage"], generatedAt: "2025-01-02T00:00:00Z" };

describe("HeatmapStore", () => {
  beforeEach(() => {
    useHeatmapStore.setState({ history: [], currentScore: 0, archAnalysis: null, selectedDate: null });
    mockFetch.mockReset();
  });

  it("fetchHeatmap should populate history", async () => {
    mockFetch.mockResolvedValue(new Response(JSON.stringify(mockHeatmap), { status: 200 }));
    await useHeatmapStore.getState().fetchHeatmap();
    expect(useHeatmapStore.getState().history).toHaveLength(2);
    expect(useHeatmapStore.getState().currentScore).toBe(60);
  });

  it("fetchAnalysis should store analysis", async () => {
    mockFetch.mockResolvedValue(new Response(JSON.stringify(mockAnalysis), { status: 200 }));
    await useHeatmapStore.getState().fetchAnalysis();
    expect(useHeatmapStore.getState().archAnalysis?.coverageScore).toBe(65);
    expect(useHeatmapStore.getState().archAnalysis?.suggestions).toContain("Add tests");
  });

  it("setSelectedDate should update selection", () => {
    useHeatmapStore.getState().setSelectedDate("2025-01-01");
    expect(useHeatmapStore.getState().selectedDate).toBe("2025-01-01");
  });
});
