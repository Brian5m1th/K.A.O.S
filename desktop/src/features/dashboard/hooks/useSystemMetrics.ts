import { useEffect, useRef } from "react";
import { useSystemStore } from "@/shared/lib/stores";
import { kaosFetch } from "@/shared/api/kaos-client";

const POLL_INTERVAL_MS = 5_000;
const API_KEY = "";
const SERVER_URL = "http://localhost:8000";

export function useSystemMetrics() {
  const fetchAll = useSystemStore((s) => s.fetchAll);

  const metricsHistory = useRef<{ cpu: number[]; vram: number[]; latency: number[] }>({
    cpu: [],
    vram: [],
    latency: [],
  });

  useEffect(() => {
    let mounted = true;

    const poll = async () => {
      if (!mounted) return;
      await fetchAll(SERVER_URL, API_KEY);

      // Collect runtime data from store after fetch
      const state = useSystemStore.getState();
      metricsHistory.current.cpu.push(Math.round(state.runtime.latency / 10));
      metricsHistory.current.vram.push(state.runtime.vramUsed);
      metricsHistory.current.latency.push(state.runtime.latency);

      // Trim to last 20
      if (metricsHistory.current.cpu.length > 20) {
        metricsHistory.current.cpu.shift();
        metricsHistory.current.vram.shift();
        metricsHistory.current.latency.shift();
      }
    };

    // Immediate first poll
    poll();

    const interval = setInterval(poll, POLL_INTERVAL_MS);

    return () => {
      mounted = false;
      clearInterval(interval);
    };
  }, [fetchAll]);

  return metricsHistory.current;
}
