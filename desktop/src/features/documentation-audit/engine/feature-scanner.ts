import { kaosFetch } from "@/shared/api/kaos-client";

export interface FeatureEntry {
  id: string;
  name: string;
  phase: string;
  status: "planned" | "in-progress" | "done" | "missing";
  docs: string[];
  codeRefs: string[];
  lastCommit: string;
  createdAt: string;
  updatedAt: string;
}

export class FeatureScanner {
  static async listAll(): Promise<FeatureEntry[]> {
    try {
      const response = await kaosFetch("/api/audit/features", "");
      if (response.ok) {
        const data = await response.json();
        return data.features || [];
      }
    } catch {
    }
    return [];
  }

  static async getById(id: string): Promise<FeatureEntry | null> {
    try {
      const response = await kaosFetch(`/api/audit/features/${id}`, "");
      if (response.ok) {
        return await response.json();
      }
    } catch {
    }
    return null;
  }

  static filterByPhase(features: FeatureEntry[], phase: string): FeatureEntry[] {
    return features.filter(f => f.phase === phase);
  }

  static filterByStatus(features: FeatureEntry[], status: FeatureEntry["status"]): FeatureEntry[] {
    return features.filter(f => f.status === status);
  }

  static getMissingDocs(features: FeatureEntry[]): FeatureEntry[] {
    return features.filter(f => !f.docs || f.docs.length === 0);
  }

  static getDone(features: FeatureEntry[]): FeatureEntry[] {
    return features.filter(f => f.status === "done");
  }
}