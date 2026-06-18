import { useState } from "react";
import ProviderScreen from "./components/ProviderScreen";
import VaultScreen from "./components/VaultScreen";
import ChatScreen from "./components/ChatScreen";

type Screen = "provider" | "vault" | "chat";

export default function App() {
  const [screen, setScreen] = useState<Screen>("provider");
  const [provider, setProvider] = useState<string>("");
  const [vaultPath, setVaultPath] = useState<string>("");
  const [serverUrl, setServerUrl] = useState<string>("http://localhost:8000");
  const [connected, setConnected] = useState(false);

  const handleProviderDone = (p: string, url: string) => {
    setProvider(p);
    setServerUrl(url);
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
            initialProvider={provider}
            initialUrl={serverUrl}
          />
        )}
        {screen === "vault" && (
          <VaultScreen
            onDone={handleVaultDone}
            initialPath={vaultPath}
            serverUrl={serverUrl}
          />
        )}
        {screen === "chat" && (
          <ChatScreen
            serverUrl={serverUrl}
            onDisconnect={handleDisconnect}
          />
        )}
      </main>
    </div>
  );
}
