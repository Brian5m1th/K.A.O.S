import { kaosFetch } from "@/infrastructure";

export interface CommitEntry {
  hash: string;
  message: string;
  type: string;
  impact: string;
  scope: string | null;
  features: string[];
  timestamp: string;
  author: string;
}

export class CommitMapper {
  static async listAll(): Promise<CommitEntry[]> {
    try {
      const response = await kaosFetch("/api/audit/commit-map", "");
      if (response.ok) {
        const data = await response.json();
        return data.commits || [];
      }
    } catch {
    }
    return [];
  }

  static async scanLatest(limit: number = 200): Promise<CommitEntry[]> {
    try {
      const response = await kaosFetch(`/api/audit/scan-commits?limit=${limit}`, "", {
        method: "POST",
      });
      if (response.ok) {
        const data = await response.json();
        return data.commits || [];
      }
    } catch {
    }
    return [];
  }

  static filterByFeature(commits: CommitEntry[], feature: string): CommitEntry[] {
    return commits.filter(c => c.features.includes(feature));
  }

  static filterByImpact(commits: CommitEntry[], impact: string): CommitEntry[] {
    return commits.filter(c => c.impact === impact);
  }

  static getHighImpact(commits: CommitEntry[]): CommitEntry[] {
    return commits.filter(c => c.impact === "high");
  }

  static getLatest(commits: CommitEntry[]): CommitEntry | null {
    return commits.length > 0 ? commits[0] : null;
  }

  static groupByType(commits: CommitEntry[]): Record<string, CommitEntry[]> {
    const grouped: Record<string, CommitEntry[]> = {};
    for (const c of commits) {
      if (!grouped[c.type]) grouped[c.type] = [];
      grouped[c.type].push(c);
    }
    return grouped;
  }
}