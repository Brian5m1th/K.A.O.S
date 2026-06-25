import React from "react";
import ReactDOM from "react-dom/client";
import { AppProviders } from "./app/providers";
import "./shared/styles/globals.css";
import { setAccessTokenProvider, setServerUrlProvider } from "./shared/api/kaos-client";
import { useAuthStore } from "./shared/lib/stores/auth-store";

// Registra o provedor de tokens para o kaosFetch de forma a quebrar dependência circular
setAccessTokenProvider(() => useAuthStore.getState().accessToken);
setServerUrlProvider(() => useAuthStore.getState().serverUrl || "http://localhost:8000");

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <AppProviders />
  </React.StrictMode>,
);
