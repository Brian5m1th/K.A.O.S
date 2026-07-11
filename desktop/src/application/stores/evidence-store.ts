/**
 * EvidenceStore — Desktop store for architecture health evidence.
 *
 * Consumes the Evidence Engine REST API for architectural health reports.
 * NEVER imports Graphify, Git, or any evidence source directly.
 *
 * API: GET /api/evidence/report
 *      GET /api/evidence/metric/{name}
 *      GET /api/evidence/history/{name}
 *      GET /api/evidence/health
 */

import { create } from "zustand";
import { kaosFetch } from "@/infrastructure";

interface EvidenceMetric {
  name: string;
  value: number;
  level: "healthy" | "warning" | "critical" | "unknown";
  description: string;
  source: string;
}

interface EvidenceReport {
  generated_at: string;
  overall_score: number;
  level: string;
  sources_checked: string[];
  metrics: EvidenceMetric[];
  recommendations: string[];
}

interface EvidenceState {
  loading: boolean;
  error: string | null;
  report: EvidenceReport | null;

  fetchReport: (serverUrl?: string) => Promise<EvidenceReport | null>;
  fetchMetric: (name: string, serverUrl?: string) => Promise<EvidenceMetric | null>;
}

const DEFAULT_URL = "http://localhost:8000";

export const useEvidenceStore = create<EvidenceState>((set) => ({
  loading: false,
  error: null,
  report: null,

  fetchReport: async (serverUrl = DEFAULT_URL) => {
    set({ loading: true, error: null });
    try {
      const res = await kaosFetch(`${serverUrl}/api/evidence/report`, "");
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      set({ loading: false, report: data });
      return data;
    } catch (e) {
      set({ loading: false, error: String(e) });
      return null;
    }
  },

  fetchMetric: async (name, serverUrl = DEFAULT_URL) => {
    try {
      const res = await kaosFetch(`${serverUrl}/api/evidence/metric/${name}`, "");
      if (!res.ok) return null;
      const data = await res.json();
      return data.found ? data : null;
    } catch {
      return null;
    }
  },
}));
