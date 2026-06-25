import { useEffect } from "react";
import { Outlet } from "react-router-dom";
import { Sidebar } from "@/widgets/sidebar";
import { TopBar } from "@/widgets/topbar";
import { useThemeStore } from "@/shared/lib/stores";

export function AppLayout() {
  const loadFromBackend = useThemeStore((s) => s.loadFromBackend);

  useEffect(() => {
    loadFromBackend();
  }, [loadFromBackend]);

  return (
    <div className="flex h-full">
      <Sidebar />
      <div className="flex flex-1 flex-col overflow-hidden">
        <TopBar />
        <main className="flex-1 overflow-auto bg-canvas">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
