import { useEffect, useState } from "react";

interface Props {
  onDone: () => void;
  serverUrl?: string;
}

interface ProviderFields {
  url: string;
  apiKey: string;
  model: string;
}

type ProviderConfig = Record<string, ProviderFields>;

const DEFAULT_CONFIG: ProviderConfig = {
  ollama: { url: "http://localhost:11434", apiKey: "", model: "qwen3:14b" },
  openai: { url: "https://api.openai.com/v1", apiKey: "", model: "gpt-4o" },
  anthropic: { url: "https://api.anthropic.com", apiKey: "", model: "claude-sonnet-4-20250514" },
  google: { url: "https://generativelanguage.googleapis.com", apiKey: "", model: "gemini-2.0-flash" },
};

const PROVIDER_LABELS: Record<string, string> = {
  ollama: "Ollama (Local)",
  openai: "OpenAI",
  anthropic: "Anthropic Claude",
  google: "Google Gemini",
};

const PROVIDER_ORDER = ["ollama", "openai", "anthropic", "google"];

type StatusMap = Record<string, string>;

export default function ProviderScreen({ onDone, serverUrl = "http://localhost:8000" }: Props) {
  const [config, setConfig] = useState<ProviderConfig>(DEFAULT_CONFIG);
  const [statuses, setStatuses] = useState<StatusMap>({});
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    loadFromStore();
  }, []);

  const loadFromStore = async () => {
    try {
      const { Store } = await import("@tauri-apps/plugin-store");
      const store = await Store.load("settings.json");
      const saved = await store.get<ProviderConfig>("providerConfig");
      if (saved && typeof saved === "object") {
        setConfig((prev) => {
          const merged: ProviderConfig = {};
          for (const key of PROVIDER_ORDER) {
            merged[key] = { ...prev[key], ...saved[key] };
          }
          return merged;
        });
        return;
      }
    } catch {}
    try {
      const resp = await fetch(`${serverUrl.replace(/\/+$/, "")}/api/setup/provider`);
      if (resp.ok) {
        const data = await resp.json();
        if (data && typeof data === "object") {
          setConfig((prev) => {
            const merged: ProviderConfig = {};
            for (const key of PROVIDER_ORDER) {
              merged[key] = { ...prev[key], ...data[key] };
            }
            return merged;
          });
        }
      }
    } catch {}
  };

  const updateField = (provider: string, field: keyof ProviderFields, value: string) => {
    setConfig((prev) => ({
      ...prev,
      [provider]: { ...prev[provider], [field]: value },
    }));
  };

  const handleTest = async (provider: string) => {
    setStatuses((s) => ({ ...s, [provider]: "Testing..." }));
    const fields = config[provider];
    const base = fields.url.replace(/\/+$/, "");
    const endpoints: Record<string, string> = {
      ollama: `${base}/api/tags`,
      openai: `${base}/models`,
      anthropic: base,
      google: `${base}/models`,
    };
    const endpoint = endpoints[provider] || base;
    try {
      const headers: Record<string, string> = {};
      if (fields.apiKey) {
        if (provider === "openai") headers["Authorization"] = `Bearer ${fields.apiKey}`;
        else if (provider === "anthropic") {
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
  };

  const handleSave = async () => {
    setSaving(true);
    try {
      const { Store } = await import("@tauri-apps/plugin-store");
      const store = await Store.load("settings.json");
      await store.set("providerConfig", config);
      await store.save();
    } catch {}
    try {
      await fetch(`${serverUrl.replace(/\/+$/, "")}/api/setup/provider`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(config),
      });
    } catch {}
    setSaving(false);
    onDone();
  };

  return (
    <div style={{ padding: "32px", maxWidth: "640px", margin: "0 auto" }}>
      <h2>Provider Configuration</h2>
      <p style={{ color: "#aaa", marginBottom: "20px", fontSize: "14px" }}>
        Configure all LLM providers. API keys are stored locally and sent to the KAOS backend.
      </p>

      {PROVIDER_ORDER.map((provider) => {
        const fields = config[provider];
        const status = statuses[provider] || "";
        return (
          <div key={provider} style={{
            border: "1px solid #444",
            borderRadius: "8px",
            padding: "16px",
            marginBottom: "12px",
            background: "#1e1e1e",
          }}>
            <h3 style={{ margin: "0 0 12px 0", color: "#e0e0e0" }}>
              {PROVIDER_LABELS[provider]}
            </h3>

            <div style={{ display: "flex", flexDirection: "column", gap: "8px" }}>
              <input
                value={fields.url}
                onChange={(e) => updateField(provider, "url", e.target.value)}
                placeholder="Server URL"
                style={{
                  padding: "10px",
                  borderRadius: "6px",
                  border: "1px solid #555",
                  background: "#2a2a2a",
                  color: "#e0e0e0",
                  fontSize: "13px",
                }}
              />

              {provider !== "ollama" && (
                <div style={{ position: "relative" }}>
                  <input
                    type="password"
                    value={fields.apiKey}
                    onChange={(e) => updateField(provider, "apiKey", e.target.value)}
                    placeholder="API Key"
                    style={{
                      padding: "10px",
                      borderRadius: "6px",
                      border: "1px solid #555",
                      background: "#2a2a2a",
                      color: "#e0e0e0",
                      fontSize: "13px",
                      width: "100%",
                      boxSizing: "border-box",
                    }}
                  />
                </div>
              )}

              <input
                value={fields.model}
                onChange={(e) => updateField(provider, "model", e.target.value)}
                placeholder="Model name"
                style={{
                  padding: "10px",
                  borderRadius: "6px",
                  border: "1px solid #555",
                  background: "#2a2a2a",
                  color: "#e0e0e0",
                  fontSize: "13px",
                }}
              />

              <div style={{ display: "flex", alignItems: "center", gap: "8px" }}>
                <button
                  onClick={() => handleTest(provider)}
                  style={{
                    padding: "8px 16px",
                    borderRadius: "6px",
                    border: "none",
                    background: "#2196f3",
                    color: "white",
                    cursor: "pointer",
                    fontSize: "13px",
                  }}
                >
                  Test Connection
                </button>
                {status && (
                  <span style={{
                    fontSize: "13px",
                    color: status === "Connected" ? "#4caf50" : "#f44336",
                  }}>
                    {status}
                  </span>
                )}
              </div>
            </div>
          </div>
        );
      })}

      <button
        onClick={handleSave}
        disabled={saving}
        style={{
          padding: "12px 24px",
          borderRadius: "6px",
          border: "none",
          background: saving ? "#555" : "#4caf50",
          color: "white",
          cursor: saving ? "not-allowed" : "pointer",
          width: "100%",
          fontSize: "16px",
          fontWeight: "bold",
          marginTop: "8px",
        }}
      >
        {saving ? "Saving..." : "Continue"}
      </button>
    </div>
  );
}
