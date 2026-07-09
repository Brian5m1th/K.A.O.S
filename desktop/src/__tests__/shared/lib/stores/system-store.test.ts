import { describe, it, expect, beforeEach } from "vitest";
import { useSystemStore } from "@/shared/lib/stores/system-store";
import { kaosFetch } from "@/infrastructure/http";
import { vi } from "vitest";

vi.mock("@/infrastructure/http", () => ({ kaosFetch: vi.fn() }));
const mockFetch = vi.mocked(kaosFetch);

describe("System Store", () => {
  beforeEach(() => {
    useSystemStore.setState({
      status: "offline", version: "0.5.0", setupStatus: "NOT_STARTED", setupStep: 0,
      runtime: { activeModel: "", latency: 0, cpu: 0, vramUsed: 0, vramTotal: 16 },
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
    expect(useSystemStore.getState().runtime.vramTotal).toBe(16);
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

  it("fetchAll should query multiple endpoints", async () => {
    mockFetch
      .mockResolvedValueOnce(new Response(JSON.stringify({ status: "ok" }), { status: 200 }))
      .mockResolvedValueOnce(new Response(JSON.stringify({ ready: true }), { status: 200 }))
      .mockResolvedValueOnce(new Response(JSON.stringify({ ollama: true, backend: true }), { status: 200 }))
      .mockResolvedValueOnce(new Response(JSON.stringify({ provider_id: "gpt-4" }), { status: 200 }))
      .mockResolvedValueOnce(new Response(JSON.stringify({ cpu: 50, vram_used: 4 }), { status: 200 }));

    await useSystemStore.getState().fetchAll();

    expect(mockFetch).toHaveBeenCalledTimes(5);
    expect(useSystemStore.getState().services.backend).toBe(true);
  });
});
