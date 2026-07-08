import type { ReactNode } from "react";
import { BrowserRouter } from "react-router-dom";
import { AppRoutes } from "@/app/routes";
import { CommandPalette } from "@/widgets/command-palette";
import { initializeCommands } from "@/shared/lib/commands-init";
initializeCommands();

interface Props {
  children?: ReactNode;
}

export function AppProviders({ children }: Props) {
  return (
    <BrowserRouter>
      {children || <AppRoutes />}
      <CommandPalette />
    </BrowserRouter>
  );
}
