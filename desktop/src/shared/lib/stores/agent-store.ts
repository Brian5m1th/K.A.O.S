import { create } from "zustand";

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
  start: (id: string) => void;
  stop: (id: string) => void;
  pause: (id: string) => void;
  resume: (id: string) => void;
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

  start: (id) =>
    set((s) => ({
      agents: {
        ...s.agents,
        [id]: { ...s.agents[id], status: "starting", startedAt: Date.now() },
      },
    })),

  stop: (id) =>
    set((s) => ({
      agents: {
        ...s.agents,
        [id]: { ...s.agents[id], status: "stopped" },
      },
    })),

  pause: (id) =>
    set((s) => ({
      agents: {
        ...s.agents,
        [id]: { ...s.agents[id], status: "paused" },
      },
    })),

  resume: (id) =>
    set((s) => ({
      agents: {
        ...s.agents,
        [id]: { ...s.agents[id], status: "running" },
      },
    })),

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
