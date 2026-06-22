import { useEffect, useRef } from "react";
import { useSystemStore } from "@/shared/lib/stores";
import { useWebSocket } from "@/shared/lib/use-websocket";

const WS_URL = "ws://localhost:8000/ws/metrics";

export function useSystemMetrics() {
  const setRuntime = useSystemStore((s) => s.setRuntime);
  const setService = useSystemStore((s) => s.setService);
  const setMetrics = useSystemStore((s) => s.setMetrics);
  const setStatus = useSystemStore((s) => s.setStatus);

  const wsConnected = useRef(false);
  const metricsHistory = useRef<{ cpu: number[]; vram: number[]; latency: number[] }>({
    cpu: [],
    vram: [],
    latency: [],
  });

  // Try WebSocket connection
  const wsHandlers = {
    onOpen: () => {
      wsConnected.current = true;
      setStatus("online");
    },
    onMessage: (data: unknown) => {
      const msg = data as Record<string, unknown>;
      if (msg.cpu !== undefined) metricsHistory.current.cpu.push(msg.cpu as number);
      if (msg.vram !== undefined) metricsHistory.current.vram.push(msg.vram as number);
      if (msg.latency !== undefined) metricsHistory.current.latency.push(msg.latency as number);

      // Trim to last 20
      if (metricsHistory.current.cpu.length > 20) {
        metricsHistory.current.cpu.shift();
        metricsHistory.current.vram.shift();
        metricsHistory.current.latency.shift();
      }

      setRuntime({
        vramUsed: (msg.vram_used as number) || 0,
        latency: (msg.latency as number) || 0,
        activeModel: (msg.active_model as string) || "",
      });
      setMetrics({
        vectorCount: (msg.vector_count as number) || 0,
        tokenRate: (msg.token_rate as number) || 0,
      });
      setService("ollama", (msg.ollama as boolean) ?? true);
      setService("backend", true);
      setService("qdrant", (msg.qdrant as boolean) ?? true);
    },
    onError: () => {
      wsConnected.current = false;
    },
  };

  useWebSocket({
    url: WS_URL,
    ...wsHandlers,
    maxRetries: 2,
  });

  // Fallback simulation when WebSocket isn't available
  useEffect(() => {
    if (wsConnected.current) return;

    const interval = setInterval(() => {
      const cpu = Math.round(Math.random() * 40 + 10);
      const vramUsed = Math.round(Math.random() * 8 + 2);
      const latency = Math.round(Math.random() * 60 + 20);

      setRuntime({ vramUsed, latency });
      setMetrics({
        vectorCount: Math.floor(Math.random() * 15000 + 5000),
        tokenRate: Math.floor(Math.random() * 500 + 100),
      });
      setService("ollama", Math.random() > 0.1);

      metricsHistory.current.cpu.push(cpu);
      metricsHistory.current.vram.push(vramUsed);
      metricsHistory.current.latency.push(latency);

      if (metricsHistory.current.cpu.length > 20) {
        metricsHistory.current.cpu.shift();
        metricsHistory.current.vram.shift();
        metricsHistory.current.latency.shift();
      }
    }, 2000);

    return () => clearInterval(interval);
  }, [setRuntime, setService, setMetrics, setStatus]);

  return metricsHistory.current;
}
