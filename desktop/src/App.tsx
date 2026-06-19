import { useState } from "react";
import ProviderScreen from "./components/ProviderScreen";
import VaultScreen from "./components/VaultScreen";
import ChatScreen from "./components/ChatScreen";

type Screen = "provider" | "vault" | "chat";

const BACKEND_URL = "http://localhost:8000";

export default function App() {
  const [screen, setScreen] = useState<Screen>("provider");
  const [vaultPath, setVaultPath] = useState<string>("");
  const [connected, setConnected] = useState(false);

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
        <span style={{ color: connected ? "#4caf50" : "#f44336" }}>
          {connected ? "Connected" : "Disconnected"}
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
          />
        )}
        {screen === "chat" && (
          <ChatScreen
            serverUrl={BACKEND_URL}
            onDisconnect={handleDisconnect}
          />
        )}
      </main>
    </div>
  );
}
