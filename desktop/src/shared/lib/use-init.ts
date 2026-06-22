import { useEffect } from "react";
import { TauriStoreService } from "@/shared/api/tauri-store-service";
import { kaosFetch } from "@/shared/api/kaos-client";
import { useAuthStore, useSystemStore } from "@/shared/lib/stores";

const BACKEND_URL = "http://localhost:8000";

export function useAppInit() {
  const setApiKey = useAuthStore((s) => s.setApiKey);
  const setConnected = useAuthStore((s) => s.setConnected);
  const setStatus = useSystemStore((s) => s.setStatus);
  const setService = useSystemStore((s) => s.setService);

  useEffect(() => {
    TauriStoreService.get<string>("kaosApiKey").then((key) => {
      if (key) {
        setApiKey(key);
        verifyConnection(key);
      }
    });
  }, []);

  const verifyConnection = async (key: string) => {
    try {
      const res = await kaosFetch(`${BACKEND_URL}/health`, key);
      if (res.ok) {
        setConnected(true);
        setStatus("online");
        setService("backend", true);
      }
    } catch {
      setStatus("offline");
    }
  };
}
