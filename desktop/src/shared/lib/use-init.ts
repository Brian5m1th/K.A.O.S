import { useEffect } from "react";
import { useAuthStore, useUpdateStore } from "@/shared/lib/stores";
import { useUpdateCheck } from "@/features/auto-update/hooks/useUpdateCheck";
import { invoke } from "@tauri-apps/api/core";

export function useAppInit() {
  const checkSetupStatus = useAuthStore((s) => s.checkSetupStatus);
  useUpdateCheck();

  useEffect(() => {
    checkSetupStatus();
    
    // Iniciar automaticamente os serviços do Docker Compose
    const startDocker = async () => {
      console.log("[useAppInit] Iniciando contêineres Docker (Ollama, Postgres, etc.)...");
      try {
        await invoke("ensure_docker_services");
        console.log("[useAppInit] Comando Docker Compose disparado.");
      } catch (e) {
        console.error("[useAppInit] Erro ao iniciar serviços Docker:", e);
      }
    };
    void startDocker();

    // Buscar a versão real do binário do Tauri e atualizar o store
    const fetchRealVersion = async () => {
      try {
        const version = await invoke<string>("get_app_version");
        useUpdateStore.getState().setCurrentVersion(version);
        console.log(`[useAppInit] Dynamic version retrieved: ${version}`);
      } catch (e) {
        console.error("[useAppInit] Failed to get real app version:", e);
      }
    };
    void fetchRealVersion();
  }, [checkSetupStatus]);
}
