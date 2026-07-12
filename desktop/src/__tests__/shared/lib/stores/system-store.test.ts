import { describe, it, expect, beforeEach } from "vitest";
import { useSystemStore } from "@/application/stores/system-store";
import { kaosFetch } from "@/infrastructure/http";
import { vi } from "vitest";

vi.mock("@/infrastructure/http", () => ({ kaosFetch: vi.fn() }));
const mockFetch = vi.mocked(kaosFetch);

describe("System Store", () => {
  beforeEach(() => {
    useSystemStore.setState({
      status: "offline", version: "0.5.0", setupStatus: "NOT_STARTED", setupStep: 0,
      runtime: { activeModel: "", latency: 0, cpu: 0, vramUsed: 0, vramTotal: 0 },
      services: { ollama: false, backend: false, qdrant: false, postgres: false, n8n: false, grafana: false, prometheus: false },
      metrics: { vectorCount: 0, tokenRate: 0 },
      documentation: { coverage: 0, driftLevel: "low", lastScan: null, missingCount: 0, outdatedCount: 0 },
    });
    mockFetch.mockReset();
  });

  it("should initialize with offline status", () => {
    expect(useSystemStore.getState().status).toBe("offline");
  });

  it("setStatus should update status", () => {
    useSystemStore.getState().setStatus("online");
    expect(useSystemStore.getState().status).toBe("online");
  });

  it("setSetupStatus should update setup", () => {
    useSystemStore.getState().setSetupStatus("COMPLETED");
    expect(useSystemStore.getState().setupStatus).toBe("COMPLETED");
  });

  it("setRuntime should partial merge", () => {
    useSystemStore.getState().setRuntime({ cpu: 45, latency: 120 });
    expect(useSystemStore.getState().runtime.cpu).toBe(45);
    expect(useSystemStore.getState().runtime.latency).toBe(120);
    expect(useSystemStore.getState().runtime.vramTotal).toBe(0);
  });

  it("setService should toggle service", () => {
    useSystemStore.getState().setService("ollama", true);
    expect(useSystemStore.getState().services.ollama).toBe(true);
  });

  it("setMetrics should partial merge", () => {
    useSystemStore.getState().setMetrics({ vectorCount: 42 });
    expect(useSystemStore.getState().metrics.vectorCount).toBe(42);
  });

  it("setDocumentation should partial merge", () => {
    useSystemStore.getState().setDocumentation({ coverage: 75, driftLevel: "medium" });
    expect(useSystemStore.getState().documentation.coverage).toBe(75);
    expect(useSystemStore.getState().documentation.driftLevel).toBe("medium");
  });

  it("fetchAll should query the consolidated dashboard endpoint", async () => {
    const mockDashboardData = {
      services: {
        backend: true,
        ollama: true,
        qdrant: true,
        postgres: true,
        n8n: false,
        grafana: false,
        prometheus: false,
      },
      runtime: {
        activeModel: "gpt-4",
        latency: 120,
        cpu: 50,
        vram: { used: 4, total: 16 }
      },
      metrics: {
        vectorCount: 15234,
        tokenRate: 42.3
      }
    };

    mockFetch.mockResolvedValueOnce(new Response(JSON.stringify(mockDashboardData), { status: 200 }));

    await useSystemStore.getState().fetchAll();

    expect(mockFetch).toHaveBeenCalledTimes(1);
    expect(useSystemStore.getState().services.backend).toBe(true);
    expect(useSystemStore.getState().runtime.activeModel).toBe("gpt-4");
  });
});
