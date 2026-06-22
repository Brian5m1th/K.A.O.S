import { create } from "zustand";

interface AuthState {
  apiKey: string;
  serverUrl: string;
  connected: boolean;
  setApiKey: (key: string) => void;
  setServerUrl: (url: string) => void;
  setConnected: (connected: boolean) => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  apiKey: "",
  serverUrl: "http://localhost:8000",
  connected: false,
  setApiKey: (apiKey) => set({ apiKey }),
  setServerUrl: (serverUrl) => set({ serverUrl }),
  setConnected: (connected) => set({ connected }),
}));
