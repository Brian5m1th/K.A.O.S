import { useEffect } from "react";
import { useUpdateScheduler } from "./useUpdateScheduler";

/**
 * Hook bridge que dispara a verificacao de atualizacao no startup.
 * Consumido por use-init.ts.
 *
 * G-10: schedule e estavel (usa getState() internamente + useCallback),
 *       entao eslint-disable e intencional para evitar re-execucao.
 */
export function useUpdateCheck() {
  const { schedule } = useUpdateScheduler();

  useEffect(() => {
    schedule(); // silencioso, respeita cooldown
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
}
