import { useDriftStore } from "../store/drift-store";

export interface DriftReport {
  coverage: number;
  driftLevel: "low" | "medium" | "high";
  missingFeatures: string[];
  outdatedDocs: string[];
  inconsistentPhases: string[];
  orphanedSDDs: string[];
  undocumentedCode: string[];
  lastScan: number | null;
}

export class DriftEngine {
  static getReport(): DriftReport | null {
    const state = useDriftStore.getState();
    if (!state.driftReport) return null;

    return {
      coverage: state.driftReport.coverage,
      driftLevel: state.driftReport.driftLevel,
      missingFeatures: state.driftReport.missingFeatures || [],
      outdatedDocs: state.driftReport.outdatedDocs || [],
      inconsistentPhases: state.driftReport.inconsistentPhases || [],
      orphanedSDDs: state.driftReport.orphanedSDDs || [],
      undocumentedCode: state.driftReport.undocumentedCode || [],
      lastScan: state.lastScan,
    };
  }

  static getCoverage(): number {
    return useDriftStore.getState().driftReport?.coverage || 0;
  }

  static getMissingCount(): number {
    return useDriftStore.getState().driftReport?.missingFeatures?.length || 0;
  }

  static async runAudit(): Promise<void> {
    await useDriftStore.getState().runAudit();
  }

  static async loadSnapshot(): Promise<void> {
    await useDriftStore.getState().loadSnapshot();
  }
}