import { useEffect } from "react";
import { useAuthStore } from "@/shared/lib/stores";
import { useUpdateCheck } from "@/features/auto-update/hooks/useUpdateCheck";

export function useAppInit() {
  const checkSetupStatus = useAuthStore((s) => s.checkSetupStatus);
  useUpdateCheck();

  useEffect(() => {
    checkSetupStatus();
  }, [checkSetupStatus]);
}
