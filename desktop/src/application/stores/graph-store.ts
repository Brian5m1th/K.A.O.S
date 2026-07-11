/**
 * GraphStore — Desktop store for code intelligence queries.
 *
 * Communicates with the K.A.O.S backend via REST API.
 * NEVER imports Graphify, NetworkX, or any framework directly.
 *
 * API: GET /api/graph/explain/{concept}
 *      GET /api/graph/path?source=&target=
 *      POST /api/graph/query
 *      GET /api/graph/health
 */

import { create } from "zustand";
import { kaosFetch } from "@/infrastructure";

interface NodeInfo {
  id: string;
  label: string;
  source_file: string;
  type: string;
  degree: number;
  community: string;
}

interface PathInfo {
  source: string;
  target: string;
  hops: number;
  description: string;
}

interface GraphQueryResult {
  nodes: NodeInfo[];
  total_found: number;
}

interface GraphState {
  // State
  loading: boolean;
  error: string | null;
  currentNode: NodeInfo | null;
  currentPath: PathInfo | null;
  queryResults: GraphQueryResult | null;

  // Actions
  explainConcept: (concept: string, serverUrl?: string) => Promise<NodeInfo | null>;
  findPath: (source: string, target: string, serverUrl?: string) => Promise<PathInfo | null>;
  queryGraph: (text: string, maxDepth?: number, serverUrl?: string) => Promise<GraphQueryResult>;
  checkHealth: (serverUrl?: string) => Promise<boolean>;
}

const DEFAULT_URL = "http://localhost:8000";

export const useGraphStore = create<GraphState>((set) => ({
  loading: false,
  error: null,
  currentNode: null,
  currentPath: null,
  queryResults: null,

  explainConcept: async (concept, serverUrl = DEFAULT_URL) => {
    set({ loading: true, error: null });
    try {
      const res = await kaosFetch(`${serverUrl}/api/graph/explain/${encodeURIComponent(concept)}`, "");
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      if (!data.found) {
        set({ loading: false, currentNode: null });
        return null;
      }
      const node: NodeInfo = {
        id: data.id,
        label: data.label,
        source_file: data.source_file,
        type: data.type,
        degree: data.degree,
        community: data.community,
      };
      set({ loading: false, currentNode: node });
      return node;
    } catch (e) {
      set({ loading: false, error: String(e) });
      return null;
    }
  },

  findPath: async (source, target, serverUrl = DEFAULT_URL) => {
    set({ loading: true, error: null });
    try {
      const params = new URLSearchParams({ source, target });
      const res = await kaosFetch(`${serverUrl}/api/graph/path?${params}`, "");
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      const path: PathInfo = {
        source: data.source,
        target: data.target,
        hops: data.hops,
        description: data.description,
      };
      set({ loading: false, currentPath: path });
      return path;
    } catch (e) {
      set({ loading: false, error: String(e) });
      return null;
    }
  },

  queryGraph: async (text, maxDepth = 3, serverUrl = DEFAULT_URL) => {
    set({ loading: true, error: null });
    try {
      const res = await kaosFetch(`${serverUrl}/api/graph/query`, "", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text, max_depth: maxDepth, max_results: 20 }),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      const results: GraphQueryResult = {
        nodes: data.nodes || [],
        total_found: data.total_found,
      };
      set({ loading: false, queryResults: results });
      return results;
    } catch (e) {
      set({ loading: false, error: String(e) });
      return { nodes: [], total_found: 0 };
    }
  },

  checkHealth: async (serverUrl = DEFAULT_URL) => {
    try {
      const res = await kaosFetch(`${serverUrl}/api/graph/health`, "");
      return res.ok;
    } catch {
      return false;
    }
  },
}));
