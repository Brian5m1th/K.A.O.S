import { useCallback, useEffect, useRef } from "react";
import { invoke } from "@tauri-apps/api/core";
import { listen, type UnlistenFn } from "@tauri-apps/api/event";
import { useUpdateStore } from "@/shared/lib/stores";
import { eventBus } from "@/shared/lib/event-bus";

interface UpdateResult {
  available: boolean;
  version?: string;
  date?: string;
  body?: string;
}

interface ProgressPayload {
  downloaded: number;
  total?: number;
}

/**
 * Hook que encapsula toda logica de IPC (invoke + listen) para o sistema de atualizacao.
 *
 * G-01: useRef<UnlistenFn[]> + clearListeners() para evitar acumulo de subscricoes.
 * G-04: useUpdateStore.getState() em vez de capturar estado do closure.
 */
export function useUpdaterService() {
  const unlistenersRef = useRef<UnlistenFn[]>([]);

  const clearListeners = useCallback(() => {
    unlistenersRef.current.forEach((fn) => fn());
    unlistenersRef.current = [];
  }, []);

  // G-01: cleanup ao desmontar
  useEffect(() => {
    return () => clearListeners();
  }, [clearListeners]);

  const checkForUpdates = useCallback(async () => {
    const store = useUpdateStore.getState();
    store.setPhase("checking");
    store.setError(null);
    console.log("[UpdaterService] Iniciando verificacao de atualizacoes...");
    try {
      const result = await invoke<UpdateResult>("check_for_update");
      console.log("[UpdaterService] Resposta do check_for_update:", result);
      store.setLastCheckAt(new Date().toISOString());
      if (result.available) {
        console.log(`[UpdaterService] Nova versao disponivel: v${result.version}`);
        store.setUpdate({
          version: result.version!,
          date: result.date!,
          body: result.body ?? "",
        });
        store.setPhase("available");
        eventBus.emit({
          type: "update:available",
          payload: { version: result.version!, date: result.date! },
        });
      } else {
        console.log("[UpdaterService] Nenhuma atualizacao disponivel.");
        store.setPhase("not-available");
      }
    } catch (e) {
      console.error("[UpdaterService] Erro ao verificar atualizacoes:", e);
      store.setError(String(e));
      store.setPhase("error");
      eventBus.emit({
        type: "update:error",
        payload: { phase: "check", message: String(e) },
      });
    }
  }, []);

  const downloadUpdate = useCallback(async () => {
    const store = useUpdateStore.getState();
    store.setPhase("downloading");
    store.setProgress(0);
    store.setError(null);
    clearListeners();
    console.log("[UpdaterService] Iniciando download da atualizacao...");

    try {
      const unlistenProgress = await listen<ProgressPayload>(
        "update:progress",
        (ev) => {
          const s = useUpdateStore.getState();
          if (ev.payload.total) {
            const pct = Math.round((ev.payload.downloaded / ev.payload.total) * 100);
            console.log(`[UpdaterService] Progresso do download: ${pct}% (${ev.payload.downloaded}/${ev.payload.total} bytes)`);
            s.setProgress(pct);
          } else {
            console.log(`[UpdaterService] Progresso do download: ${ev.payload.downloaded} bytes (total indefinido)`);
          }
        },
      );
      unlistenersRef.current.push(unlistenProgress);

      const unlistenReady = await listen("update:ready", () => {
        console.log("[UpdaterService] Download concluido com sucesso e pronto para instalacao.");
        useUpdateStore.getState().setPhase("ready");
        clearListeners();
      });
      unlistenersRef.current.push(unlistenReady);

      // G-01: tratar update:error como promise separada
      const unlistenError = await listen<{ message: string }>(
        "update:error",
        (ev) => {
          console.error("[UpdaterService] Erro emitido durante o download:", ev.payload.message);
          const s = useUpdateStore.getState();
          s.setError(ev.payload.message);
          s.setPhase("error");
          eventBus.emit({
            type: "update:error",
            payload: { phase: "download", message: ev.payload.message },
          });
          clearListeners();
        },
      );
      unlistenersRef.current.push(unlistenError);

      await invoke("download_and_install");
    } catch (e) {
      console.error("[UpdaterService] Erro ao chamar download_and_install:", e);
      const s = useUpdateStore.getState();
      s.setError(String(e));
      s.setPhase("error");
      eventBus.emit({
        type: "update:error",
        payload: { phase: "download", message: String(e) },
      });
      clearListeners();
    }
  }, [clearListeners]);

  const installUpdate = useCallback(async () => {
    console.log("[UpdaterService] Iniciando processo de instalacao do update...");
    try {
      await invoke("install_update");
      console.log("[UpdaterService] Comando de instalacao enviado ao backend Rust. O app deve reiniciar.");
    } catch (e) {
      console.error("[UpdaterService] Erro ao invocar install_update:", e);
    }
  }, []);

  return { checkForUpdates, downloadUpdate, installUpdate };
}
