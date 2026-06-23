import { useEffect } from "react";
import { useAuthStore } from "@/shared/lib/stores";

export function useAppInit() {
  const checkSetupStatus = useAuthStore((s) => s.checkSetupStatus);

  useEffect(() => {
    checkSetupStatus();
  }, [checkSetupStatus]);
}
