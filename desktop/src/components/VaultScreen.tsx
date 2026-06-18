import { useState } from "react";

interface Props {
  onDone: (path: string) => void;
  initialPath: string;
  serverUrl: string;
}

export default function VaultScreen({ onDone, initialPath, serverUrl }: Props) {
  const [path, setPath] = useState(initialPath || "");
  const [status, setStatus] = useState("");

  const handleInit = async () => {
    if (!path) return;
    setStatus("Initializing vault...");
    try {
      const resp = await fetch(`${serverUrl.replace(/\/+$/, "")}/indexing/init-folders`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ vault_path: path }),
      });
      if (resp.ok) {
        setStatus("Vault initialized");
        onDone(path);
      } else {
        const err = await resp.text();
        setStatus(`Error: ${err}`);
      }
    } catch (e) {
      setStatus(`Connection failed: ${e}`);
    }
  };

  return (
    <div style={{ padding: "32px", maxWidth: "480px", margin: "0 auto" }}>
      <h2>Obsidian Vault</h2>
      <p style={{ color: "#aaa", marginBottom: "16px" }}>
        Point to your Obsidian vault folder. KAOS will create its folder structure there.
      </p>

      <input
        value={path}
        onChange={(e) => setPath(e.target.value)}
        placeholder="C:\Users\...\Obsidian\Vault"
        style={{
          padding: "10px",
          borderRadius: "6px",
          border: "1px solid #555",
          background: "#2a2a2a",
          color: "#e0e0e0",
          width: "100%",
          boxSizing: "border-box",
        }}
      />

      <div style={{ display: "flex", gap: "8px", marginTop: "12px" }}>
        <button
          onClick={handleInit}
          disabled={!path}
          style={{
            padding: "10px 20px",
            borderRadius: "6px",
            border: "none",
            background: path ? "#4caf50" : "#555",
            color: "white",
            cursor: path ? "pointer" : "not-allowed",
            flex: 1,
          }}
        >
          Initialize & Enter
        </button>
      </div>

      {status && (
        <p style={{
          textAlign: "center",
          color: status.startsWith("Error") ? "#f44336" : "#4caf50",
          marginTop: "8px",
        }}>
          {status}
        </p>
      )}
    </div>
  );
}
