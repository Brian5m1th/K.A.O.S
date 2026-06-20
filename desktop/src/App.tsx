import { useEffect, useState } from "react";
import ProviderScreen from "./components/ProviderScreen";
import VaultScreen from "./components/VaultScreen";
import ChatScreen from "./components/ChatScreen";
import SettingsScreen from "./components/SettingsScreen";

type Screen = "provider" | "vault" | "chat" | "settings";

const BACKEND_URL = "http://localhost:8000";

export default function App() {
  const [screen, setScreen] = useState<Screen>("provider");
  const [vaultPath, setVaultPath] = useState<string>("");
  const [connected, setConnected] = useState(false);
  const [apiKey, setApiKey] = useState("");

  useEffect(() => {
    loadApiKey();
  }, []);

  const loadApiKey = async () => {
    try {
      const { Store } = await import("@tauri-apps/plugin-store");
      const store = await Store.load("settings.json");
      const saved = await store.get<string>("kaosApiKey");
      if (saved) setApiKey(saved);
    } catch {}
  };

  const handleProviderDone = () => {
    setScreen("vault");
  };

  const handleVaultDone = (vp: string) => {
    setVaultPath(vp);
    setConnected(true);
    setScreen("chat");
  };

  const handleDisconnect = () => {
    setConnected(false);
  };

  return (
    <div style={{ height: "100%", display: "flex", flexDirection: "column" }}>
      <header style={{
        padding: "8px 16px",
        background: "#1a1a2e",
        color: "#e0e0e0",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        fontSize: "14px",
      }}>
        <span style={{ fontWeight: "bold" }}>KAOS v0.5.0</span>
        <span style={{ display: "flex", gap: "8px", alignItems: "center" }}>
          <span
            onClick={() => setScreen("settings")}
            style={{ cursor: "pointer", color: "#888", fontSize: "18px", lineHeight: 1 }}
            title="Settings"
          >
            ⚙
          </span>
          <span style={{ color: connected ? "#4caf50" : "#f44336" }}>
            {connected ? "Connected" : "Disconnected"}
          </span>
        </span>
      </header>

      <main style={{ flex: 1, overflow: "auto" }}>
        {screen === "provider" && (
          <ProviderScreen
            onDone={handleProviderDone}
            serverUrl={BACKEND_URL}
          />
        )}
        {screen === "vault" && (
          <VaultScreen
            onDone={handleVaultDone}
            initialPath={vaultPath}
            serverUrl={BACKEND_URL}
            apiKey={apiKey}
          />
        )}
        {screen === "chat" && (
          <ChatScreen
            serverUrl={BACKEND_URL}
            onDisconnect={handleDisconnect}
            apiKey={apiKey}
          />
        )}
        {screen === "settings" && (
          <SettingsScreen
            onClose={() => setScreen("provider")}
            onKeyChange={setApiKey}
          />
        )}
      </main>
    </div>
  );
}
