import { create } from "zustand";
import { persist } from "zustand/middleware";
import { kaosFetch } from "@/shared/api/kaos-client";

type SystemStatus = "online" | "degraded" | "offline";
type DriftLevel = "low" | "medium" | "high";
type SetupStatus = "NOT_STARTED" | "IN_PROGRESS" | "COMPLETED";

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
  setupStatus: SetupStatus;
  setupStep: number;
  runtime: {
    activeModel: string;
    latency: number;
    cpu: number;
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
  setSetupStatus: (status: SetupStatus) => void;
  setSetupStep: (step: number) => void;
  setRuntime: (runtime: Partial<SystemState["runtime"]>) => void;
  setService: (service: keyof SystemServices, up: boolean) => void;
  setMetrics: (metrics: Partial<SystemState["metrics"]>) => void;
  setDocumentation: (doc: Partial<SystemState["documentation"]>) => void;
  fetchAll: (serverUrl?: string, apiKey?: string) => Promise<void>;
}

export const useSystemStore = create<SystemState>()(
  persist(
    (set) => ({
      status: "offline",
      version: "0.5.0",
      setupStatus: "NOT_STARTED" as SetupStatus,
      setupStep: 0,
      runtime: {
        activeModel: "",
        latency: 0,
        cpu: 0,
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
      setSetupStatus: (setupStatus) => set({ setupStatus }),
      setSetupStep: (setupStep) => set({ setupStep }),
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
      const [healthRes, readinessRes, systemStatusRes, providerActiveRes, systemMetricsRes] =
        await Promise.allSettled([
          kaosFetch(`${serverUrl}/health`, apiKey),
          kaosFetch(`${serverUrl}/health/readiness`, apiKey),
          kaosFetch(`${serverUrl}/api/system/status`, apiKey),
          kaosFetch(`${serverUrl}/api/setup/provider/active`, apiKey),
          kaosFetch(`${serverUrl}/api/system/metrics`, apiKey),
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

      if (systemMetricsRes.status === "fulfilled" && systemMetricsRes.value.ok) {
        const data = await systemMetricsRes.value.json();
        set((s) => ({
          runtime: {
            ...s.runtime,
            cpu: data.cpu ?? s.runtime.cpu,
            vramUsed: data.vram?.used ?? s.runtime.vramUsed,
            vramTotal: data.vram?.total ?? s.runtime.vramTotal,
          },
        }));
      }
    } catch {
      // Silently fail — stores keep last known values
    }
  },
}),
    {
      name: "kaos-system-store",
      partialize: (state) => ({
        setupStatus: state.setupStatus,
        setupStep: state.setupStep,
      }),
    },
  ),
);
