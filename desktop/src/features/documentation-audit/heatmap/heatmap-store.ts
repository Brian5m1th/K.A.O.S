import { create } from "zustand";

export interface HeatmapEntry {
  date: string;
  score: number;
  level: "low" | "medium" | "high" | "critical";
  missingLinks: number;
  sddMismatch: number;
  codeVsVaultDiff: number;
}

export interface ArchAnalysis {
  coverageScore: number;
  driftLevel: string;
  totalIssues: number;
  suggestions: string[];
  warnings: string[];
  generatedAt: string;
}

interface HeatmapState {
  history: HeatmapEntry[];
  currentScore: HeatmapEntry | null;
  analysis: ArchAnalysis | null;
  isLoading: boolean;
  selectedDate: string | null;
  fetchHeatmap: () => Promise<void>;
  fetchAnalysis: () => Promise<void>;
  fetchHistory: () => Promise<void>;
  setSelectedDate: (date: string | null) => void;
}

export const useHeatmapStore = create<HeatmapState>((set) => ({
  history: [],
  currentScore: null,
  analysis: null,
  isLoading: false,
  selectedDate: null,

  fetchHeatmap: async () => {
    try {
      const response = await fetch("/api/architecture/heatmap");
      if (response.ok) {
        const data = await response.json();
        set({
          currentScore: {
            date: data.generated_at?.split("T")[0] || new Date().toISOString().split("T")[0],
            score: data.score || 0,
            level: data.level || "low",
            missingLinks: data.missing_links || 0,
            sddMismatch: data.sdd_mismatch || 0,
            codeVsVaultDiff: data.code_vs_vault_diff || 0,
          },
        });
      }
    } catch {
    }
  },

  fetchAnalysis: async () => {
    try {
      const response = await fetch("/api/architecture/analysis");
      if (response.ok) {
        const data = await response.json();
        set({
          analysis: {
            coverageScore: data.coverage_score || 0,
            driftLevel: data.drift_level || "low",
            totalIssues: data.total_issues || 0,
            suggestions: data.suggestions || [],
            warnings: data.warnings || [],
            generatedAt: data.generated_at || "",
          },
        });
      }
    } catch {
    }
  },

  fetchHistory: async () => {
    set({ isLoading: true });
    try {
      const response = await fetch("/api/architecture/heatmap");
      if (response.ok) {
        const data = await response.json();
        const entry: HeatmapEntry = {
          date: data.generated_at?.split("T")[0] || new Date().toISOString().split("T")[0],
          score: data.score || 0,
          level: data.level || "low",
          missingLinks: data.missing_links || 0,
          sddMismatch: data.sdd_mismatch || 0,
          codeVsVaultDiff: data.code_vs_vault_diff || 0,
        };
        set((state) => {
          const existing = state.history.findIndex((h) => h.date === entry.date);
          const newHistory = existing >= 0
            ? state.history.map((h, i) => (i === existing ? entry : h))
            : [...state.history, entry].sort((a, b) => a.date.localeCompare(b.date));
          return { history: newHistory, currentScore: entry, isLoading: false };
        });
      } else {
        set({ isLoading: false });
      }
    } catch {
      set({ isLoading: false });
    }
  },

  setSelectedDate: (date) => set({ selectedDate: date }),
}));

export function useHeatmapHistory() {
  return useHeatmapStore((s) => s.history);
}

export function useCurrentScore() {
  return useHeatmapStore((s) => s.currentScore);
}

export function useArchAnalysis() {
  return useHeatmapStore((s) => s.analysis);
}

export const levelColors: Record<string, string> = {
  low: "bg-green-500",
  medium: "bg-yellow-500",
  high: "bg-red-500",
  critical: "bg-purple-600",
};

export const levelBgColors: Record<string, string> = {
  low: "bg-green-50 border-green-200",
  medium: "bg-yellow-50 border-yellow-200",
  high: "bg-red-50 border-red-200",
  critical: "bg-purple-50 border-purple-600",
};

export const levelTextColors: Record<string, string> = {
  low: "text-green-800",
  medium: "text-yellow-800",
  high: "text-red-800",
  critical: "text-purple-800",
};

export const levelLabels: Record<string, string> = {
  low: "Baixo",
  medium: "Medio",
  high: "Alto",
  critical: "Critico",
};
