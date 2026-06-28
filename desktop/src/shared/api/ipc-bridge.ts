export const isTauri = () => {
  return typeof window !== "undefined" && (window as any).__TAURI_INTERNALS__ !== undefined;
};

export async function invokeIpc<T>(cmd: string, args?: Record<string, any>): Promise<T> {
  if (isTauri()) {
    const { invoke } = await import("@tauri-apps/api/core");
    return invoke<T>(cmd, args);
  }
  
  console.log(`[IpcBridge] [Web/Electron Fallback] invoke: ${cmd}`, args);
  
  if (cmd === "get_app_version") {
    return "0.6.0-web" as unknown as T;
  }
  if (cmd === "check_for_update") {
    return { available: false } as unknown as T;
  }
  
  return undefined as unknown as T;
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
