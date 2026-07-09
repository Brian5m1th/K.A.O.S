import { create } from "zustand";
import { kaosFetch } from "@/infrastructure";

export type AgentStatus =
  | "idle"
  | "starting"
  | "running"
  | "paused"
  | "error"
  | "stopped";

export interface AgentConfig {
  id: string;
  name: string;
  model: string;
  systemPrompt: string;
  temperature: number;
  topP: number;
}

export interface AgentInstance {
  config: AgentConfig;
  status: AgentStatus;
  error?: string;
  startedAt?: number;
  memoryContext?: string[];
}

interface AgentState {
  agents: Record<string, AgentInstance>;
  register: (config: AgentConfig) => void;
  unregister: (id: string) => void;
  start: (id: string) => Promise<void>;
  stop: (id: string) => Promise<void>;
  pause: (id: string) => Promise<void>;
  resume: (id: string) => Promise<void>;
  setError: (id: string, error: string) => void;
  updateConfig: (id: string, config: Partial<AgentConfig>) => void;
}

export const useAgentStore = create<AgentState>((set) => ({
  agents: {},

  register: (config) =>
    set((s) => ({
      agents: {
        ...s.agents,
        [config.id]: { config, status: "idle" },
      },
    })),

  unregister: (id) =>
    set((s) => {
      const { [id]: _, ...rest } = s.agents;
      return { agents: rest };
    }),

  start: async (id) => {
    set((s) => ({
      agents: {
        ...s.agents,
        [id]: { ...s.agents[id], status: "starting", startedAt: Date.now() },
      },
    }));
    try {
      const agent = useAgentStore.getState().agents[id];
      await kaosFetch(`/api/agents/${id}/start`, "", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(agent.config),
      });
      set((s) => ({
        agents: {
          ...s.agents,
          [id]: { ...s.agents[id], status: "running" },
        },
      }));
    } catch (e) {
      console.error("[agent-store] start failed:", e);
      set((s) => ({
        agents: {
          ...s.agents,
          [id]: { ...s.agents[id], status: "error", error: "Failed to start on backend" },
        },
      }));
    }
  },

  stop: async (id) => {
    set((s) => ({
      agents: {
        ...s.agents,
        [id]: { ...s.agents[id], status: "stopped" },
      },
    }));
    try {
      await kaosFetch(`/api/agents/${id}/stop`, "", { method: "POST" });
    } catch (e) {
      console.error("[agent-store] stop failed:", e);
    }
  },

  pause: async (id) => {
    set((s) => ({
      agents: {
        ...s.agents,
        [id]: { ...s.agents[id], status: "paused" },
      },
    }));
    try {
      await kaosFetch(`/api/agents/${id}/pause`, "", { method: "POST" });
    } catch (e) {
      console.error("[agent-store] pause failed:", e);
    }
  },

  resume: async (id) => {
    set((s) => ({
      agents: {
        ...s.agents,
        [id]: { ...s.agents[id], status: "running" },
      },
    }));
    try {
      await kaosFetch(`/api/agents/${id}/resume`, "", { method: "POST" });
    } catch (e) {
      console.error("[agent-store] resume failed:", e);
    }
  },

  setError: (id, error) =>
    set((s) => ({
      agents: {
        ...s.agents,
        [id]: { ...s.agents[id], status: "error", error },
      },
    })),

  updateConfig: (id, config) =>
    set((s) => ({
      agents: {
        ...s.agents,
        [id]: {
          ...s.agents[id],
          config: { ...s.agents[id].config, ...config },
        },
      },
    })),
}));
