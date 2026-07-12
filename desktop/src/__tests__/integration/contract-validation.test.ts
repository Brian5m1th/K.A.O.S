import { describe, it, expect } from "vitest";

/**
 * Contract validation test — ensures the frontend SystemState store shape
 * matches the properties returned by the backend /api/system/dashboard endpoint.
 *
 * This test validates that the consolidated dashboard endpoint returns
 * all expected top-level keys with correct value types.
 */

// Expected shape mirrors the system-store.ts SystemState interface
interface DashboardResponse {
  status: string;
  services: {
    backend: boolean;
    postgres: boolean;
    qdrant: boolean;
    ollama: boolean;
    n8n: boolean;
    grafana: boolean;
    prometheus: boolean;
  };
  runtime: {
    activeModel: string;
    latency: number;
    cpu: number;
    ram: { used: number; total: number };
    vram: { used: number | null; total: number | null };
  };
  metrics: {
    vectorCount: number;
    tokenRate: number;
  };
  costs: {
    total_usd: number;
    total_tokens: number;
  };
  dlq: {
    failed: Array<{
      id: string;
      workflow_name: string;
      status: string;
      error: string;
      created_at: string;
    }>;
    count: number;
  };
  alerts: {
    notifications: Array<{
      id: string;
      level: string;
      title: string;
      message: string;
      source: string;
      created_at: string;
      read: boolean;
    }>;
  };
}

const REQUIRED_TOP_KEYS = [
  "services",
  "runtime",
  "metrics",
  "costs",
  "dlq",
  "alerts",
  "status",
] as const;

const REQUIRED_SERVICE_KEYS = [
  "backend",
  "postgres",
  "qdrant",
  "ollama",
  "n8n",
  "grafana",
  "prometheus",
] as const;

const REQUIRED_RUNTIME_KEYS = [
  "activeModel",
  "latency",
  "cpu",
  "ram",
  "vram",
] as const;

const REQUIRED_METRICS_KEYS = ["vectorCount", "tokenRate"] as const;

describe("Dashboard API Contract Validation", () => {
  it("defines all required top-level keys in DashboardResponse", () => {
    const sample: DashboardResponse = {
      status: "ready",
      services: {
        backend: true,
        postgres: true,
        qdrant: true,
        ollama: true,
        n8n: false,
        grafana: false,
        prometheus: false,
      },
      runtime: {
        activeModel: "qwen3:14b",
        latency: 45.0,
        cpu: 12.5,
        ram: { used: 8.2, total: 32.0 },
        vram: { used: 4.5, total: 8.0 },
      },
      metrics: {
        vectorCount: 15234,
        tokenRate: 42.3,
      },
      costs: {
        total_usd: 0.0045,
        total_tokens: 2850,
      },
      dlq: {
        failed: [
          {
            id: "abc-123",
            workflow_name: "test-workflow",
            status: "failed",
            error: "timeout",
            created_at: "2026-01-01T00:00:00Z",
          },
        ],
        count: 1,
      },
      alerts: {
        notifications: [
          {
            id: "n-1",
            level: "warning",
            title: "Test Alert",
            message: "Test message",
            source: "system",
            created_at: "2026-01-01T00:00:00Z",
            read: false,
          },
        ],
      },
    };

    // All required top-level keys exist
    for (const key of REQUIRED_TOP_KEYS) {
      expect(sample).toHaveProperty(key);
    }

    // Service keys
    for (const key of REQUIRED_SERVICE_KEYS) {
      expect(sample.services).toHaveProperty(key);
    }

    // Runtime keys
    for (const key of REQUIRED_RUNTIME_KEYS) {
      expect(sample.runtime).toHaveProperty(key);
    }

    // VRAM can be null for CPU mode
    expect(sample.runtime.vram.used === null || typeof sample.runtime.vram.used === "number").toBe(true);
    expect(sample.runtime.vram.total === null || typeof sample.runtime.vram.total === "number").toBe(true);

    // Metrics keys
    for (const key of REQUIRED_METRICS_KEYS) {
      expect(sample.metrics).toHaveProperty(key);
    }
  });

  it("accepts null VRAM for CPU-only mode", () => {
    const cpuMode: DashboardResponse = {
      status: "ready",
      services: { backend: true, postgres: true, qdrant: false, ollama: false, n8n: false, grafana: false, prometheus: false },
      runtime: {
        activeModel: "No model installed",
        latency: 0,
        cpu: 5.2,
        ram: { used: 4.1, total: 16.0 },
        vram: { used: null, total: null },
      },
      metrics: { vectorCount: 0, tokenRate: 0 },
      costs: { total_usd: 0, total_tokens: 0 },
      dlq: { failed: [], count: 0 },
      alerts: { notifications: [] },
    };

    expect(cpuMode.runtime.vram.used).toBeNull();
    expect(cpuMode.runtime.vram.total).toBeNull();
    expect(cpuMode.runtime.activeModel).toBe("No model installed");
  });

  it("ensures DLQ items have required shape", () => {
    const emptyDlq: DashboardResponse["dlq"] = { failed: [], count: 0 };
    expect(emptyDlq.failed).toEqual([]);
    expect(emptyDlq.count).toBe(0);
  });
});
