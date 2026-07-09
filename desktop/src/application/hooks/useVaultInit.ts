import { useState, useCallback } from "react";
import { kaosFetch } from "@/infrastructure";

interface UseVaultInitReturn {
  path: string;
  status: string;
  setPath: (path: string) => void;
  handleInit: () => Promise<void>;
  loading: boolean;
}

export function useVaultInit(
  initialPath: string,
  serverUrl: string,
  apiKey: string,
  onDone: (path: string) => void,
): UseVaultInitReturn {
  const [path, setPath] = useState(initialPath || "");
  const [status, setStatus] = useState("");
  const [loading, setLoading] = useState(false);

  const handleInit = useCallback(async () => {
    if (!path) return;
    setLoading(true);
    setStatus("Initializing vault...");

    try {
      const resp = await kaosFetch(
        `${serverUrl.replace(/\/+$/, "")}/indexing/init-folders`,
        apiKey,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ vault_path: path }),
        },
      );

      if (resp.ok) {
        setStatus("Vault initialized");
        onDone(path);
      } else {
        const err = await resp.text();
        setStatus(`Error: ${err}`);
      }
    } catch (e) {
      setStatus(`Connection failed: ${e}`);
    } finally {
      setLoading(false);
    }
  }, [path, serverUrl, apiKey, onDone]);

  return { path, status, setPath, handleInit, loading };
}
