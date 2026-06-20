import { useEffect, useState } from "react";
import { TauriStoreService } from "@/shared/api/tauri-store-service";
import { Sidebar } from "@/widgets/sidebar";
import ChatPage from "@/pages/chat";
import ProvidersPage from "@/pages/providers";
import VaultPage from "@/pages/vault";
import SettingsPage from "@/pages/settings";
import "@/shared/styles/globals.css";

type Screen = "provider" | "vault" | "chat" | "settings";

const BACKEND_URL = "http://localhost:8000";

export default function App() {
  const [screen, setScreen] = useState<Screen>("provider");
  const [vaultPath, setVaultPath] = useState("");
  const [connected, setConnected] = useState(false);
  const [apiKey, setApiKey] = useState("");

  useEffect(() => {
    TauriStoreService.get<string>("kaosApiKey").then((key) => {
      if (key) setApiKey(key);
    });
  }, []);

  const handleProviderDone = () => setScreen("vault");
  const handleVaultDone = (vp: string) => {
    setVaultPath(vp);
    setConnected(true);
    setScreen("chat");
  };
  const handleDisconnect = () => setConnected(false);

  return (
    <div className="flex h-full">
      <Sidebar
        currentScreen={screen}
        onNavigate={setScreen}
        connected={connected}
      />
      <main className="flex-1 overflow-auto bg-canvas">
        {screen === "provider" && (
          <ProvidersPage
            onDone={handleProviderDone}
            serverUrl={BACKEND_URL}
            apiKey={apiKey}
          />
        )}
        {screen === "vault" && (
          <VaultPage
            onDone={handleVaultDone}
            initialPath={vaultPath}
            serverUrl={BACKEND_URL}
            apiKey={apiKey}
          />
        )}
        {screen === "chat" && (
          <ChatPage
            serverUrl={BACKEND_URL}
            apiKey={apiKey}
            onDisconnect={handleDisconnect}
          />
        )}
        {screen === "settings" && (
          <SettingsPage
            onClose={() => setScreen("provider")}
            onKeyChange={setApiKey}
          />
        )}
      </main>
    </div>
  );
}
