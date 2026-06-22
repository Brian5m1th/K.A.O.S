import { create } from "zustand";

type SystemStatus = "online" | "degraded" | "offline";

interface SystemState {
  status: SystemStatus;
  version: string;
  runtime: {
    activeModel: string;
    latency: number;
    vramUsed: number;
    vramTotal: number;
  };
  services: {
    ollama: boolean;
    backend: boolean;
    qdrant: boolean;
  };
  metrics: {
    vectorCount: number;
    tokenRate: number;
  };
  setStatus: (status: SystemStatus) => void;
  setRuntime: (runtime: Partial<SystemState["runtime"]>) => void;
  setService: (service: keyof SystemState["services"], up: boolean) => void;
  setMetrics: (metrics: Partial<SystemState["metrics"]>) => void;
}

export const useSystemStore = create<SystemState>((set) => ({
  status: "offline",
  version: "0.5.0",
  runtime: {
    activeModel: "",
    latency: 0,
    vramUsed: 0,
    vramTotal: 16,
  },
  services: {
    ollama: false,
    backend: false,
    qdrant: false,
  },
  metrics: {
    vectorCount: 0,
    tokenRate: 0,
  },
  setStatus: (status) => set({ status }),
  setRuntime: (runtime) =>
    set((s) => ({ runtime: { ...s.runtime, ...runtime } })),
  setService: (service, up) =>
    set((s) => ({ services: { ...s.services, [service]: up } })),
  setMetrics: (metrics) =>
    set((s) => ({ metrics: { ...s.metrics, ...metrics } })),
}));
