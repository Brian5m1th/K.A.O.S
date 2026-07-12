/**
 * SecretsStore — Desktop store for user secrets (API keys, tokens).
 *
 * Communicates with K.A.O.S backend REST API.
 * NEVER imports or uses any crypto framework directly.
 *
 * API: POST /api/secrets/set, GET /api/secrets/status, DELETE /api/secrets/{provider}
 */

import { create } from "zustand";
import { kaosFetch } from "@/infrastructure";

interface SecretEntry {
  provider: string;
  configured: boolean;
  metadata?: Record<string, unknown>;
}

interface SecretsState {
  loading: boolean;
  error: string | null;
  configured: Record<string, boolean>;
  providers: Array<{ name: string; configured: boolean }>;

  // Actions
  checkStatus: (serverUrl?: string) => Promise<void>;
  setSecret: (provider: string, key: string, metadata?: Record<string, unknown>, serverUrl?: string) => Promise<boolean>;
  deleteSecret: (provider: string, serverUrl?: string) => Promise<boolean>;
  clearError: () => void;
}

const DEFAULT_URL = "http://localhost:8000";

export const useSecretsStore = create<SecretsState>((set) => ({
  loading: false,
  error: null,
  configured: {},
  providers: [],

  clearError: () => set({ error: null }),

  checkStatus: async (serverUrl = DEFAULT_URL) => {
    set({ loading: true, error: null });
    try {
      const res = await kaosFetch(`${serverUrl}/api/secrets/status`, "");
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();

      const configured: Record<string, boolean> = {};
      data.configured?.forEach((v: boolean, k: string) => { configured[k] = v; });
      const providers = data.providers || Object.entries(configured).map(([k, v]) => ({ name: k, configured: v }));

      set({ loading: false, configured, providers, error: null });
    } catch (e) {
      set({ loading: false, error: String(e) });
    }
  },

  setSecret: async (provider: string, key: string, metadata = {}, serverUrl = DEFAULT_URL) => {
    set({ loading: true, error: null });
    try {
      const res = await kaosFetch(`${serverUrl}/api/secrets/set`, "", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ provider, key, metadata }),
      });
      if (!res.ok) {
        const err = await res.json().catch(() => ({ detail: `HTTP ${res.status}` }));
        throw new Error(err.detail || `HTTP ${res.status}`);
      }
      // Refresh status
      await useSecretsStore.getState().checkStatus(serverUrl);
      return true;
    } catch (e) {
      set({ loading: false, error: String(e) });
      return false;
    }
  },

  deleteSecret: async (provider: string, serverUrl = DEFAULT_URL) => {
    set({ loading: true, error: null });
    try {
      const res = await kaosFetch(`${serverUrl}/api/secrets/${provider}`, "", { method: "DELETE" });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      await useSecretsStore.getState().checkStatus(serverUrl);
      return true;
    } catch (e) {
      set({ loading: false, error: String(e) });
      return false;
    }
  },
}));