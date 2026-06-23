import { useDriftStore } from "../store/drift-store";

export interface DriftReport {
  coverage: number;
  driftLevel: "low" | "medium" | "high";
  missing_features: string[];
  outdated_docs: string[];
  inconsistent_phases: string[];
  orphaned_sdds: string[];
  undocumented_code: string[];
  lastScan: number | null;
}

export class DriftEngine {
  static getReport(): DriftReport | null {
    const state = useDriftStore.getState();
    if (!state.driftReport) return null;

    return {
      coverage: state.driftReport.coverage,
      driftLevel: state.driftReport.driftLevel,
      missing_features: state.driftReport.missing_features || [],
      outdated_docs: state.driftReport.outdated_docs || [],
      inconsistent_phases: state.driftReport.inconsistent_phases || [],
      orphaned_sdds: state.driftReport.orphaned_sdds || [],
      undocumented_code: state.driftReport.undocumented_code || [],
      lastScan: state.lastScan,
    };
  }

  static getCoverage(): number {
    return useDriftStore.getState().driftReport?.coverage || 0;
  }

  static getMissingCount(): number {
    return useDriftStore.getState().driftReport?.missing_features?.length || 0;
  }

  static async runAudit(): Promise<void> {
    await useDriftStore.getState().runAudit();
  }

  static async loadSnapshot(): Promise<void> {
    await useDriftStore.getState().loadSnapshot();
  }
}
