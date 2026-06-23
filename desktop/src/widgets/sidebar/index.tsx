import { useNavigate, useLocation } from "react-router-dom";
import { cn } from "@/shared/lib/utils";
import {
  LayoutDashboard,
  MessageSquare,
  GitBranch,
  Bot,
  Container,
  BookOpen,
  Activity,
  Settings,
  FileText,
  Users,
} from "lucide-react";
import { useSystemStore } from "@/shared/lib/stores";

interface NavItem {
  id: string;
  label: string;
  path: string;
  icon: typeof LayoutDashboard;
}

const NAV_ITEMS: NavItem[] = [
  { id: "dashboard", label: "Dashboard", path: "/", icon: LayoutDashboard },
  { id: "chat", label: "Chat", path: "/chat", icon: MessageSquare },
  { id: "orchestration", label: "Orquestração", path: "/orchestration", icon: GitBranch },
  { id: "agents", label: "Agents", path: "/agents", icon: Bot },
  { id: "pipelines", label: "Pipelines", path: "/pipelines", icon: Container },
  { id: "vault", label: "Knowledge", path: "/vault", icon: BookOpen },
  { id: "observability", label: "Observability", path: "/observability", icon: Activity },
  { id: "users", label: "Users", path: "/users", icon: Users },
  { id: "documentation", label: "Doc Health", path: "/documentation", icon: FileText },
  { id: "settings", label: "Settings", path: "/settings", icon: Settings },
];

export function Sidebar() {
  const navigate = useNavigate();
  const location = useLocation();
  const systemStatus = useSystemStore((s) => s.status);

  return (
    <aside className="flex h-full w-56 flex-col border-r border-border-subtle bg-surface">
      <div className="flex items-center gap-2 border-b border-border-subtle px-4 py-3">
        <span className="text-sm font-bold text-text-primary">KAOS</span>
        <span className="text-[10px] text-text-dim">v0.5.0</span>
      </div>

      <nav className="flex-1 space-y-1 p-2">
        {NAV_ITEMS.map((item) => {
          const Icon = item.icon;
          const isActive = location.pathname === item.path;

          return (
            <button
              key={item.id}
              onClick={() => navigate(item.path)}
              className={cn(
                "flex w-full items-center gap-2 rounded-md px-3 py-2 text-sm transition-all duration-150",
                "hover:scale-[1.02] active:scale-[0.98]",
                isActive
                  ? "bg-bg-active text-text-primary"
                  : "text-text-muted hover:bg-bg-active/50 hover:text-text-primary",
              )}
            >
              <Icon className="h-4 w-4" />
              <span>{item.label}</span>
            </button>
          );
        })}
      </nav>

      <div className="border-t border-border-subtle p-3">
        <div className="flex items-center gap-2">
          <div
            className={cn(
              "h-2 w-2 rounded-full",
              systemStatus === "online" && "bg-success",
              systemStatus === "degraded" && "bg-warning",
              systemStatus === "offline" && "bg-error",
            )}
          />
          <span className="text-xs text-text-muted capitalize">
            {systemStatus}
          </span>
        </div>
      </div>
    </aside>
  );
}
