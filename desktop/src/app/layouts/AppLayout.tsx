import { Outlet } from "react-router-dom";
import { Sidebar } from "@/widgets/sidebar";
import { TopBar } from "@/widgets/topbar";
import { useAppInit } from "@/shared/lib/use-init";

export function AppLayout() {
  useAppInit();

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
