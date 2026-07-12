import { create } from "zustand";
import { persist } from "zustand/middleware";
import { kaosFetch } from "@/infrastructure";

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

// ── TTL cache to prevent redundant parallel requests ──
let _lastFetchTs = 0;
const FETCH_TTL_MS = 3_000;

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
        vramTotal: 0,
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
    // 3-second TTL throttle — skip redundant parallel requests
    const now = Date.now();
    if (now - _lastFetchTs < FETCH_TTL_MS) return;
    _lastFetchTs = now;

    try {
      const res = await kaosFetch(`${serverUrl}/api/system/dashboard`, apiKey);
      if (!res.ok) return;

      const data = await res.json();

      // ── Services ──
      const svc = data.services || {};
      set({
        status: svc.backend ? "online" : "offline",
        services: {
          ollama: svc.ollama ?? false,
          backend: svc.backend ?? false,
          qdrant: svc.qdrant ?? false,
          postgres: svc.postgres ?? false,
          n8n: svc.n8n ?? false,
          grafana: svc.grafana ?? false,
          prometheus: svc.prometheus ?? false,
        },
      });

      // ── Runtime ──
      const rt = data.runtime || {};
      // VRAM: null means CPU mode — store as 0.0/0.0 for display compatibility
      const vramUsed = rt.vram?.used ?? null;
      const vramTotal = rt.vram?.total ?? null;
      set((s) => ({
        runtime: {
          ...s.runtime,
          activeModel: rt.activeModel ?? s.runtime.activeModel,
          latency: rt.latency ?? s.runtime.latency,
          cpu: rt.cpu ?? s.runtime.cpu,
          vramUsed: vramUsed ?? 0.0,
          vramTotal: vramTotal ?? 0.0,
        },
      }));

      // ── Metrics ──
      const m = data.metrics || {};
      set((s) => ({
        metrics: {
          ...s.metrics,
          vectorCount: m.vectorCount ?? s.metrics.vectorCount,
          tokenRate: m.tokenRate ?? s.metrics.tokenRate,
        },
      }));
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
