import { useState, useEffect, useCallback } from "react";
import type {
  ProviderConfig,
  ProviderName,
  StatusMap,
} from "@/entities/provider";
import {
  DEFAULT_CONFIG,
  PROVIDER_ORDER,
  TEST_ENDPOINTS,
} from "@/entities/provider";
import { TauriStoreService } from "@/shared/api/tauri-store-service";
import { kaosFetch } from "@/shared/api/kaos-client";

interface UseProviderConfigReturn {
  config: ProviderConfig;
  statuses: StatusMap;
  saving: boolean;
  updateField: (provider: ProviderName, field: string, value: string) => void;
  handleTest: (provider: ProviderName) => Promise<void>;
  handleSave: (serverUrl: string, apiKey: string) => Promise<void>;
}

export function useProviderConfig(
  onDone: () => void,
): UseProviderConfigReturn {
  const [config, setConfig] = useState<ProviderConfig>(DEFAULT_CONFIG);
  const [statuses, setStatuses] = useState<StatusMap>({});
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    loadFromStore();
  }, []);

  const loadFromStore = async () => {
    const saved = await TauriStoreService.get<Partial<ProviderConfig>>(
      "providerConfig",
    );
    if (saved && typeof saved === "object") {
      setConfig((prev) => {
        const merged = { ...prev };
        for (const key of PROVIDER_ORDER) {
          if (saved[key]) {
            merged[key] = { ...prev[key], ...saved[key] };
          }
        }
        return merged;
      });
    }
  };

  const updateField = useCallback(
    (provider: ProviderName, field: string, value: string) => {
      setConfig((prev) => ({
        ...prev,
        [provider]: { ...prev[provider], [field]: value },
      }));
    },
    [],
  );

  const handleTest = useCallback(
    async (provider: ProviderName) => {
      setStatuses((s) => ({ ...s, [provider]: "Testing..." }));
      const fields = config[provider];
      const base = fields.url.replace(/\/+$/, "");
      const endpoint = TEST_ENDPOINTS[provider](base);

      try {
        const headers: Record<string, string> = {};
        if (fields.apiKey) {
          if (provider === "openai") {
            headers["Authorization"] = `Bearer ${fields.apiKey}`;
          } else if (provider === "anthropic") {
            headers["x-api-key"] = fields.apiKey;
            headers["anthropic-version"] = "2023-06-01";
          }
        }

        let url = endpoint;
        if (provider === "google" && fields.apiKey) {
          const sep = url.includes("?") ? "&" : "?";
          url = `${url}${sep}key=${fields.apiKey}`;
        }

        const resp = await fetch(url, { method: "GET", headers });
        if (resp.ok || resp.status === 401 || resp.status === 403) {
          setStatuses((s) => ({ ...s, [provider]: "Connected" }));
        } else {
          setStatuses((s) => ({ ...s, [provider]: `Error: ${resp.status}` }));
        }
      } catch {
        setStatuses((s) => ({ ...s, [provider]: "Connection failed" }));
      }
    },
    [config],
  );

  const handleSave = useCallback(
    async (serverUrl: string, apiKey: string) => {
      setSaving(true);
      try {
        await TauriStoreService.set("providerConfig", config);

        await kaosFetch(
          `${serverUrl.replace(/\/+$/, "")}/api/setup/provider`,
          apiKey,
          {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(config),
          },
        );
      } catch {
        // Silently fail — store already saved locally
      }
      setSaving(false);
      onDone();
    },
    [config, onDone],
  );

  return { config, statuses, saving, updateField, handleTest, handleSave };
}
