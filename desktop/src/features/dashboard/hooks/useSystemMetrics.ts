import { useEffect, useRef } from "react";
import { useSystemStore } from "@/shared/lib/stores";
import { useAuthStore } from "@/shared/lib/stores";

const POLL_INTERVAL_MS = 5_000;

export function useSystemMetrics() {
  const fetchAll = useSystemStore((s) => s.fetchAll);
  const serverUrl = useAuthStore((s) => s.serverUrl);

  const metricsHistory = useRef<{ cpu: number[]; vram: number[]; latency: number[] }>({
    cpu: [],
    vram: [],
    latency: [],
  });

  useEffect(() => {
    let mounted = true;

    const poll = async () => {
      if (!mounted) return;
      await fetchAll(serverUrl, "");

      // Collect real runtime data from store after fetch
      const state = useSystemStore.getState();
      const cpuValue = state.runtime.cpu;
      const vramValue = state.runtime.vramUsed;
      const latencyValue = state.runtime.latency;

      metricsHistory.current.cpu.push(cpuValue);
      metricsHistory.current.vram.push(vramValue);
      metricsHistory.current.latency.push(latencyValue);

      // Trim to last 20
      if (metricsHistory.current.cpu.length > 20) {
        metricsHistory.current.cpu.shift();
        metricsHistory.current.vram.shift();
        metricsHistory.current.latency.shift();
      }
    };

    poll();
    const interval = setInterval(poll, POLL_INTERVAL_MS);

    return () => {
      mounted = false;
      clearInterval(interval);
    };
  }, [fetchAll, serverUrl]);

  return metricsHistory.current;
}
