import { create } from "zustand";
import { kaosFetch } from "@/shared/api/kaos-client";

type SystemStatus = "online" | "degraded" | "offline";
type DriftLevel = "low" | "medium" | "high";

interface SystemServices {
  ollama: boolean;
  backend: boolean;
  qdrant: boolean;
  postgres: boolean;
  n8n: boolean;
  grafana: boolean;
  prometheus: boolean;
}

interface SystemState {
  status: SystemStatus;
  version: string;
  runtime: {
    activeModel: string;
    latency: number;
    vramUsed: number;
    vramTotal: number;
  };
  services: SystemServices;
  metrics: {
    vectorCount: number;
    tokenRate: number;
  };
  documentation: {
    coverage: number;
    driftLevel: DriftLevel;
    lastScan: number | null;
    missingCount: number;
    outdatedCount: number;
  };
  setStatus: (status: SystemStatus) => void;
  setRuntime: (runtime: Partial<SystemState["runtime"]>) => void;
  setService: (service: keyof SystemServices, up: boolean) => void;
  setMetrics: (metrics: Partial<SystemState["metrics"]>) => void;
  setDocumentation: (doc: Partial<SystemState["documentation"]>) => void;
  fetchAll: (serverUrl?: string, apiKey?: string) => Promise<void>;
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
    postgres: false,
    n8n: false,
    grafana: false,
    prometheus: false,
  },
  metrics: {
    vectorCount: 0,
    tokenRate: 0,
  },
  documentation: {
    coverage: 0,
    driftLevel: "low",
    lastScan: null,
    missingCount: 0,
    outdatedCount: 0,
  },

  setStatus: (status) => set({ status }),
  setRuntime: (runtime) =>
    set((s) => ({ runtime: { ...s.runtime, ...runtime } })),
  setService: (service, up) =>
    set((s) => ({ services: { ...s.services, [service]: up } })),
  setMetrics: (metrics) =>
    set((s) => ({ metrics: { ...s.metrics, ...metrics } })),
  setDocumentation: (doc) =>
    set((s) => ({ documentation: { ...s.documentation, ...doc } })),

  fetchAll: async (serverUrl = "http://localhost:8000", apiKey = "") => {
    try {
      const [healthRes, readinessRes, systemStatusRes, providerActiveRes] =
        await Promise.allSettled([
          kaosFetch(`${serverUrl}/health`, apiKey),
          kaosFetch(`${serverUrl}/health/readiness`, apiKey),
          kaosFetch(`${serverUrl}/api/system/status`, apiKey),
          kaosFetch(`${serverUrl}/api/setup/provider/active`, apiKey),
        ]);

      if (healthRes.status === "fulfilled" && healthRes.value.ok) {
        const data = await healthRes.value.json();
        set({ status: data.status === "ok" ? "online" : "degraded" });
      }

      if (readinessRes.status === "fulfilled" && readinessRes.value.ok) {
        const data = await readinessRes.value.json();
        set((s) => ({
          services: { ...s.services, ollama: data.services?.ollama ?? false },
        }));
      }

      if (systemStatusRes.status === "fulfilled" && systemStatusRes.value.ok) {
        const data = await systemStatusRes.value.json();
        set((s) => ({
          services: { ...s.services, ...data },
        }));
      }

      if (providerActiveRes.status === "fulfilled" && providerActiveRes.value.ok) {
        const data = await providerActiveRes.value.json();
        set((s) => ({
          runtime: { ...s.runtime, activeModel: data.model || s.runtime.activeModel },
        }));
      }
    } catch {
      // Silently fail — stores keep last known values
    }
  },
}));
