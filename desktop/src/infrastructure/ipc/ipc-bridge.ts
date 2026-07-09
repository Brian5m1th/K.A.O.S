export const isTauri = () => {
  return typeof window !== "undefined" && (window as any).__TAURI_INTERNALS__ !== undefined;
};

export async function invokeIpc<T>(cmd: string, args?: Record<string, any>): Promise<T> {
  if (isTauri()) {
    const { invoke } = await import("@tauri-apps/api/core");
    return invoke<T>(cmd, args);
  }
  
  console.log(`[IpcBridge] [Web/Electron Fallback] invoke: ${cmd}`, args);
  
  // Fallbacks para desenvolvimento web
  if (cmd === "get_app_version") {
    return "0.6.0-web" as unknown as T;
  }
  if (cmd === "check_for_update") {
    return { available: false } as unknown as T;
  }
  if (cmd === "check_docker") {
    // Em web, assumimos Docker disponivel (roda no servidor)
    return { available: true, version: "Docker Desktop (web fallback)" } as unknown as T;
  }
  if (cmd === "check_docker_engine") {
    return { running: true, info: "Engine running (web fallback)" } as unknown as T;
  }
  if (cmd === "check_backend_health") {
    return fetchHealth(args?.server_url || "http://localhost:8000") as unknown as T;
  }
  if (cmd === "get_bootstrap_state") {
    return fetchBootstrapState(args?.server_url || "http://localhost:8000") as unknown as T;
  }
  
  return undefined as unknown as T;
}

async function fetchHealth(serverUrl: string): Promise<{ reachable: boolean; status: string | null; error: string | null }> {
  try {
    const resp = await fetch(`${serverUrl}/health`);
    if (resp.ok) {
      const data = await resp.json();
      return { reachable: true, status: data.status || "ok", error: null };
    }
    return { reachable: true, status: `HTTP ${resp.status}`, error: null };
  } catch (e: any) {
    return { reachable: false, status: null, error: e.message || String(e) };
  }
}

async function fetchBootstrapState(serverUrl: string): Promise<{
  state: string; is_ready: boolean; degraded: boolean; boot_complete: boolean;
  stages: any[]; errors: string[]; total_elapsed_ms: number;
}> {
  try {
    const resp = await fetch(`${serverUrl}/api/system/bootstrap`);
    if (resp.ok) {
      return await resp.json();
    }
    return { state: "backend_error", is_ready: false, degraded: false, boot_complete: false, stages: [], errors: [`HTTP ${resp.status}`], total_elapsed_ms: 0 };
  } catch (e: any) {
    return { state: "backend_unreachable", is_ready: false, degraded: false, boot_complete: false, stages: [], errors: [e.message || String(e)], total_elapsed_ms: 0 };
  }
}

export async function listenIpc<T>(
  event: string,
  handler: (ev: { payload: T }) => void
): Promise<() => void> {
  if (isTauri()) {
    const { listen } = await import("@tauri-apps/api/event");
    const unlisten = await listen<T>(event, (e) => handler(e as any));
    return unlisten;
  }
  
  console.log(`[IpcBridge] [Web/Electron Fallback] listen: ${event}`);
  return () => {};
}
