/**
 * MemoryStore — Desktop store for agent/user memory operations.
 *
 * Communicates with K.A.O.S backend REST API.
 * NEVER imports Mem0, Graphiti, or any memory framework directly.
 *
 * API: POST /api/memory/store
 *      POST /api/memory/search
 *      GET  /api/memory/{id}
 *      DELETE /api/memory/{id}
 *      GET  /api/memory/health
 */

import { create } from "zustand";
import { kaosFetch } from "@/infrastructure";

interface MemoryEntry {
  id?: string;
  type: string;
  content: string;
  metadata: Record<string, unknown>;
}

interface MemorySearchResult {
  matches: MemoryEntry[];
  total_found: number;
}

interface MemoryState {
  loading: boolean;
  error: string | null;
  searchResults: MemorySearchResult | null;

  storeEntry: (entry: MemoryEntry, serverUrl?: string) => Promise<string | null>;
  searchMemory: (text: string, serverUrl?: string) => Promise<MemorySearchResult>;
  getMemory: (id: string, serverUrl?: string) => Promise<MemoryEntry | null>;
  deleteMemory: (id: string, serverUrl?: string) => Promise<boolean>;
}

const DEFAULT_URL = "http://localhost:8000";

export const useMemoryStore = create<MemoryState>((set) => ({
  loading: false,
  error: null,
  searchResults: null,

  storeEntry: async (entry, serverUrl = DEFAULT_URL) => {
    set({ loading: true, error: null });
    try {
      const res = await kaosFetch(`${serverUrl}/api/memory/store`, "", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(entry),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      set({ loading: false });
      return data.id;
    } catch (e) {
      set({ loading: false, error: String(e) });
      return null;
    }
  },

  searchMemory: async (text, serverUrl = DEFAULT_URL) => {
    set({ loading: true, error: null });
    try {
      const res = await kaosFetch(`${serverUrl}/api/memory/search`, "", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text, max_results: 10 }),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      const result: MemorySearchResult = {
        matches: data.matches || [],
        total_found: data.total_found,
      };
      set({ loading: false, searchResults: result });
      return result;
    } catch (e) {
      set({ loading: false, error: String(e) });
      return { matches: [], total_found: 0 };
    }
  },

  getMemory: async (id, serverUrl = DEFAULT_URL) => {
    try {
      const res = await kaosFetch(`${serverUrl}/api/memory/${id}`, "");
      if (!res.ok) return null;
      const data = await res.json();
      return data.found ? (data as MemoryEntry) : null;
    } catch {
      return null;
    }
  },

  deleteMemory: async (id, serverUrl = DEFAULT_URL) => {
    try {
      const res = await kaosFetch(`${serverUrl}/api/memory/${id}`, "", { method: "DELETE" });
      if (!res.ok) return false;
      const data = await res.json();
      return data.deleted === true;
    } catch {
      return false;
    }
  },
}));
