import { useCallback } from "react";
import { useUpdateStore } from "@/shared/lib/stores";
import { eventBus } from "@/shared/lib/event-bus";
import { useUpdaterService } from "./useUpdaterService";

/** Cooldown entre verificacoes: 6 horas */
const COOLDOWN_MS = 6 * 60 * 60 * 1000;

/**
 * Agendador de verificacao de atualizacoes.
 *
 * G-04: usa useUpdateStore.getState() no momento da chamada, nao no mount.
 * G-05: schedule(force=true) para bypassar cooldown quando usuario clica manualmente.
 */
export function useUpdateScheduler() {
  const { checkForUpdates } = useUpdaterService();

  const schedule = useCallback(
    (force = false) => {
      const { lastCheckAt } = useUpdateStore.getState();

      if (!force && lastCheckAt) {
        const elapsed = Date.now() - new Date(lastCheckAt).getTime();
        if (elapsed < COOLDOWN_MS) {
          console.debug(
            "[updater] cooldown ativo, próxima verificação em",
            Math.round((COOLDOWN_MS - elapsed) / 60000),
            "min",
          );
          eventBus.emit({
            type: "update:skipped",
            payload: { lastCheckAt },
          });
          return;
        }
      }

      void checkForUpdates();
    },
    [checkForUpdates],
  );

  return { schedule };
}
