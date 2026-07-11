/**
 * KnowledgeStore — Desktop store for unified knowledge queries.
 *
 * Coalesces results from Graph, Memory, and Retrieval services.
 * NEVER imports Graphify, Mem0, Qdrant, or any framework directly.
 *
 * API: POST /api/knowledge/query
 *      GET  /api/knowledge/health
 */

import { create } from "zustand";
import { kaosFetch } from "@/infrastructure";

interface KnowledgeQueryResult {
  query: string;
  sources_queried: string[];
  results: Record<string, unknown>;
}

interface KnowledgeState {
  loading: boolean;
  error: string | null;
  lastQuery: KnowledgeQueryResult | null;

  query: (text: string, sources?: string[], serverUrl?: string) => Promise<KnowledgeQueryResult>;
}

const DEFAULT_URL = "http://localhost:8000";

export const useKnowledgeStore = create<KnowledgeState>((set) => ({
  loading: false,
  error: null,
  lastQuery: null,

  query: async (text, sources = ["graph", "retrieval", "memory"], serverUrl = DEFAULT_URL) => {
    set({ loading: true, error: null });
    try {
      const res = await kaosFetch(`${serverUrl}/api/knowledge/query`, "", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text, include_sources: sources }),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      set({ loading: false, lastQuery: data });
      return data;
    } catch (e) {
      set({ loading: false, error: String(e) });
      return { query: text, sources_queried: [], results: {} };
    }
  },
}));
