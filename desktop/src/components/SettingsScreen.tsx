import { useEffect, useState } from "react";

interface Props {
  onClose: () => void;
  onKeyChange: (key: string) => void;
}

export default function SettingsScreen({ onClose, onKeyChange }: Props) {
  const [apiKey, setApiKey] = useState("");

  useEffect(() => {
    loadKey();
  }, []);

  const loadKey = async () => {
    try {
      const { Store } = await import("@tauri-apps/plugin-store");
      const store = await Store.load("settings.json");
      const saved = await store.get<string>("kaosApiKey");
      if (saved) setApiKey(saved);
    } catch {}
  };

  const handleSave = async () => {
    try {
      const { Store } = await import("@tauri-apps/plugin-store");
      const store = await Store.load("settings.json");
      await store.set("kaosApiKey", apiKey);
      await store.save();
    } catch {}
    onKeyChange(apiKey);
    onClose();
  };

  return (
    <div style={{ padding: "32px", maxWidth: "480px", margin: "0 auto" }}>
      <h2>Settings</h2>
      <p style={{ color: "#aaa", marginBottom: "20px", fontSize: "14px" }}>
        Configure the API key used to authenticate with the KAOS backend.
      </p>

      <label style={{ color: "#ccc", fontSize: "13px", display: "block", marginBottom: "6px" }}>
        API Key
      </label>
      <input
        type="password"
        value={apiKey}
        onChange={(e) => setApiKey(e.target.value)}
        placeholder="Enter KAOS API key"
        style={{
          padding: "10px",
          borderRadius: "6px",
          border: "1px solid #555",
          background: "#2a2a2a",
          color: "#e0e0e0",
          width: "100%",
          boxSizing: "border-box",
          fontSize: "13px",
        }}
      />

      <div style={{ display: "flex", gap: "8px", marginTop: "16px" }}>
        <button
          onClick={onClose}
          style={{
            padding: "10px 20px",
            borderRadius: "6px",
            border: "none",
            background: "#555",
            color: "white",
            cursor: "pointer",
            flex: 1,
          }}
        >
          Cancel
        </button>
        <button
          onClick={handleSave}
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
          Save
        </button>
      </div>
    </div>
  );
}
