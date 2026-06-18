import { useState } from "react";

interface Props {
  onDone: (provider: string, url: string) => void;
  initialProvider: string;
  initialUrl: string;
}

const PROVIDERS = [
  { id: "ollama", label: "Ollama (Local)", defaultUrl: "http://localhost:11434" },
  { id: "openai", label: "OpenAI", defaultUrl: "https://api.openai.com/v1" },
  { id: "anthropic", label: "Anthropic Claude", defaultUrl: "https://api.anthropic.com/v1" },
  { id: "google", label: "Google Gemini", defaultUrl: "https://generativelanguage.googleapis.com/v1" },
];

export default function ProviderScreen({ onDone, initialProvider, initialUrl }: Props) {
  const [provider, setProvider] = useState(initialProvider || "ollama");
  const [url, setUrl] = useState(initialUrl || "http://localhost:11434");
  const [status, setStatus] = useState("");

  const handleTest = async () => {
    setStatus("Testing...");
    try {
      const resp = await fetch(`${url.replace(/\/+$/, "")}/api/tags`);
      if (resp.ok) {
        setStatus("Connected");
      } else {
        setStatus(`Error: ${resp.status}`);
      }
    } catch {
      setStatus("Connection failed");
    }
  };

  return (
    <div style={{ padding: "32px", maxWidth: "480px", margin: "0 auto" }}>
      <h2>Select LLM Provider</h2>
      <div style={{ display: "flex", flexDirection: "column", gap: "12px", marginTop: "16px" }}>
        {PROVIDERS.map((p) => (
          <label key={p.id} style={{
            padding: "12px",
            border: `2px solid ${provider === p.id ? "#4caf50" : "#444"}`,
            borderRadius: "8px",
            cursor: "pointer",
            background: provider === p.id ? "#1a3a1a" : "#1e1e1e",
            color: "#e0e0e0",
          }}>
            <input
              type="radio"
              name="provider"
              value={p.id}
              checked={provider === p.id}
              onChange={() => { setProvider(p.id); setUrl(p.defaultUrl); }}
              style={{ marginRight: "8px" }}
            />
            {p.label}
          </label>
        ))}

        <input
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Server URL"
          style={{
            padding: "10px",
            borderRadius: "6px",
            border: "1px solid #555",
            background: "#2a2a2a",
            color: "#e0e0e0",
            marginTop: "8px",
          }}
        />

        <div style={{ display: "flex", gap: "8px", marginTop: "8px" }}>
          <button
            onClick={handleTest}
            style={{
              padding: "10px 20px",
              borderRadius: "6px",
              border: "none",
              background: "#2196f3",
              color: "white",
              cursor: "pointer",
              flex: 1,
            }}
          >
            Test Connection
          </button>
          <button
            onClick={() => onDone(provider, url)}
            style={{
              padding: "10px 20px",
              borderRadius: "6px",
              border: "none",
              background: "#4caf50",
              color: "white",
              cursor: "pointer",
              flex: 1,
            }}
          >
            Continue
          </button>
        </div>

        {status && (
          <p style={{
            textAlign: "center",
            color: status === "Connected" ? "#4caf50" : "#f44336",
            marginTop: "8px",
          }}>
            {status}
          </p>
        )}
      </div>
    </div>
  );
}
