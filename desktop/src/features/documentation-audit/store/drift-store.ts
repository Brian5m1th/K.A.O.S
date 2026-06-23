import { create } from "zustand";
import { kaosFetch } from "@/shared/api/kaos-client";

interface FeatureEntry {
  id: string;
  name: string;
  phase: string;
  status: string;
  docs: string[];
  codeRefs: string[];
  lastCommit: string;
  createdAt: string;
  updatedAt: string;
}

interface DriftReport {
  coverage: number;
  driftLevel: "low" | "medium" | "high";
  missing_features: string[];
  outdated_docs: string[];
  inconsistent_phases: string[];
  orphaned_sdds: string[];
  undocumented_code: string[];
  coverageHistory: { date: string; coverage: number }[];
  driftHistory: { date: string; level: string; missing: number }[];
}

interface DriftSnapshot {
  features: any[];
  coverage: number;
  driftLevel: string;
  lastCommit: string;
  graphSummary: any;
  missingCount: number;
  outdatedCount: number;
  generatedAt: string;
}

interface DriftState {
  driftReport: DriftReport | null;
  isLoading: boolean;
  lastScan: number | null;
  runAudit: () => Promise<void>;
  loadSnapshot: () => Promise<void>;
}

export const useDriftStore = create<DriftState>((set) => ({
  driftReport: null,
  isLoading: false,
  lastScan: null,

  runAudit: async () => {
    set({ isLoading: true });
    try {
      const response = await kaosFetch("/api/audit/run", "", { method: "POST" });
      if (response.ok) {
        const data = await response.json();
        set({
          driftReport: data,
          isLoading: false,
          lastScan: Date.now(),
        });
      } else {
        set({ isLoading: false });
      }
    } catch {
      set({ isLoading: false });
    }
  },

  loadSnapshot: async () => {
    try {
      const response = await kaosFetch("/api/audit/snapshot", "");
      if (response.ok) {
        const data = await response.json();
        set({
          driftReport: data,
          lastScan: data.timestamp ? new Date(data.timestamp).getTime() : null,
        });
      }
    } catch {
    }
  },
}));

export function useDriftReport() {
  return useDriftStore((state) => state.driftReport);
}

export function useDriftLoading() {
  return useDriftStore((state) => state.isLoading);
}

export function useDriftActions() {
  return useDriftStore((state) => ({
    runAudit: state.runAudit,
    loadSnapshot: state.loadSnapshot,
  }));
}

export type { FeatureEntry, DriftSnapshot };