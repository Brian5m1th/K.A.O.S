import { create } from "zustand";
import { persist } from "zustand/middleware";

type UpdatePhase = "idle" | "checking" | "available" | "not-available" | "downloading" | "ready" | "error";

type UpdateChannel = "stable" | "beta" | "nightly";

interface UpdateInfo {
  version: string;
  date: string;
  body: string;
}

interface UpdateState {
  phase: UpdatePhase;
  channel: UpdateChannel;
  currentVersion: string;
  update: UpdateInfo | null;
  progress: number;
  lastCheckAt: string | null;
  error: string | null;

  setPhase: (phase: UpdatePhase) => void;
  setUpdate: (update: UpdateInfo | null) => void;
  setProgress: (progress: number) => void;
  setLastCheckAt: (date: string) => void;
  setError: (error: string | null) => void;
  setChannel: (channel: UpdateChannel) => void;
  setCurrentVersion: (version: string) => void;
}

/**
 * Store de atualizacao do K.A.O.S Desktop.
 *
 * Segue o padrao de system-store.ts: armazena apenas o necessario para sobreviver
 * - create()(...persist(...)) com partialize para persistir so o necessario
 * - Mutacoes atomicas chamadas APENAS pelo useUpdaterService
 * - currentVersion vem de __APP_VERSION__ (injetado pelo Vite) como fallback, mas atualizada dinamicamente
 */
export const useUpdateStore = create<UpdateState>()(
  persist(
    (set) => ({
      phase: "idle",
      channel: "stable",
      currentVersion: __APP_VERSION__,
      update: null,
      progress: 0,
      lastCheckAt: null,
      error: null,

      setPhase: (phase) => set({ phase }),
      setUpdate: (update) => set({ update }),
      setProgress: (progress) => set({ progress }),
      setLastCheckAt: (lastCheckAt) => set({ lastCheckAt }),
      setError: (error) => set({ error }),
      setChannel: (channel) => set({ channel }),
      setCurrentVersion: (currentVersion) => set({ currentVersion }),
    }),
    {
      name: "kaos-update-store",
      // Persistir apenas o necessario para sobreviver a reinicializacao
      partialize: (state) => ({
        lastCheckAt: state.lastCheckAt,
        channel: state.channel,
      }),
    },
  ),
);
