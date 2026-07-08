import { useEffect } from "react";
import { useAuthStore, useUpdateStore } from "@/shared/lib/stores";
import { useUpdateCheck } from "@/features/auto-update/hooks/useUpdateCheck";
import { invokeIpc } from "@/shared/api/ipc-bridge";
import { DocSyncEngine } from "@/features/documentation-audit/auto-doc/doc-sync-engine";

export function useAppInit() {
  const checkSetupStatus = useAuthStore((s) => s.checkSetupStatus);
  const accessToken = useAuthStore((s) => s.accessToken);
  useUpdateCheck();

  useEffect(() => {
    if (accessToken) {
      console.log("[useAppInit] User authenticated, starting DocSyncEngine...");
      DocSyncEngine.start(60000);
    } else {
      console.log("[useAppInit] No user session, stopping DocSyncEngine...");
      DocSyncEngine.stop();
    }
    return () => {
      DocSyncEngine.stop();
    };
  }, [accessToken]);

  useEffect(() => {
    checkSetupStatus();
    
    // Iniciar automaticamente os serviços do Docker Compose
    const startDocker = async () => {
      console.log("[useAppInit] Iniciando contêineres Docker (Ollama, Postgres, etc.)...");
      try {
        await invokeIpc("ensure_docker_services");
        console.log("[useAppInit] Comando Docker Compose disparado.");
      } catch (e) {
        console.error("[useAppInit] Erro ao iniciar serviços Docker:", e);
        alert(`Erro de Infraestrutura: Falha ao iniciar os serviços locais do Docker.\n\nCertifique-se de que o Docker Desktop está aberto e rodando.\n\nDetalhes: ${String(e)}`);
      }
    };
    void startDocker();

    // Buscar a versão real do binário do Tauri e atualizar o store
    const fetchRealVersion = async () => {
      try {
        const version = await invokeIpc<string>("get_app_version");
        useUpdateStore.getState().setCurrentVersion(version);
        console.log(`[useAppInit] Dynamic version retrieved: ${version}`);
      } catch (e) {
        console.error("[useAppInit] Failed to get real app version:", e);
      }
    };
    void fetchRealVersion();
  }, [checkSetupStatus]);
}
