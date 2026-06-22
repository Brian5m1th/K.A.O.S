import { create } from "zustand";

interface AppState {
  theme: "dark" | "light";
  setTheme: (theme: "dark" | "light") => void;
}

export const useAppStore = create<AppState>((set) => ({
  theme: "dark",
  setTheme: (theme) => set({ theme }),
}));
