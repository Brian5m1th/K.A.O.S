import { useState, useEffect, useCallback } from "react";
import { TauriStoreService } from "@/infrastructure";
import { kaosFetch } from "@/infrastructure";

interface UseSettingsReturn {
  apiKey: string;
  setApiKey: (key: string) => void;
  handleSave: () => Promise<void>;
  loading: boolean;
  testStatus: string | null;
  testConnection: (serverUrl: string) => Promise<void>;
}

export function useSettings(
  onClose: () => void,
  onKeyChange: (key: string) => void,
): UseSettingsReturn {
  const [apiKey, setApiKey] = useState("");
  const [loading, setLoading] = useState(false);
  const [testStatus, setTestStatus] = useState<string | null>(null);

  useEffect(() => {
    loadKey();
  }, []);

  const loadKey = async () => {
    const saved = await TauriStoreService.get<string>("kaosApiKey");
    if (saved) setApiKey(saved);
  };

  const handleSave = useCallback(async () => {
    setLoading(true);
    await TauriStoreService.set("kaosApiKey", apiKey);
    onKeyChange(apiKey);
    setLoading(false);
    onClose();
  }, [apiKey, onClose, onKeyChange]);

  const testConnection = useCallback(
    async (serverUrl: string) => {
      setTestStatus("Testing...");
      try {
        const cleanUrl = serverUrl.replace(/\/+$/, "");
        const res = await kaosFetch(`${cleanUrl}/health`, apiKey);
        if (res.ok) {
          setTestStatus("Connected");
        } else if (res.status === 401 || res.status === 403) {
          setTestStatus("Invalid key");
        } else {
          setTestStatus(`Error: ${res.status}`);
        }
      } catch {
        setTestStatus("Connection failed");
      }
    },
    [apiKey],
  );

  return { apiKey, setApiKey, handleSave, loading, testStatus, testConnection };
}
