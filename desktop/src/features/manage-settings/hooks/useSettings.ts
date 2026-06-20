import { useState, useEffect, useCallback } from "react";
import { TauriStoreService } from "@/shared/api/tauri-store-service";

interface UseSettingsReturn {
  apiKey: string;
  setApiKey: (key: string) => void;
  handleSave: () => Promise<void>;
  loading: boolean;
}

export function useSettings(
  onClose: () => void,
  onKeyChange: (key: string) => void,
): UseSettingsReturn {
  const [apiKey, setApiKey] = useState("");
  const [loading, setLoading] = useState(false);

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

  return { apiKey, setApiKey, handleSave, loading };
}
