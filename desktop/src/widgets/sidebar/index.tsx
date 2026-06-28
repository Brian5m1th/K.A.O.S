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
  Wrench,
  Network,
  Share2,
  ChevronLeft,
  ChevronRight,
  Terminal,
  Coins,
} from "lucide-react";
import { useSystemStore, useUpdateStore, useUIStore, useAuthStore } from "@/shared/lib/stores";
import { Tooltip } from "@/shared/ui/tooltip";

interface NavItem {
  id: string;
  label: string;
  path: string;
  icon: typeof LayoutDashboard;
  allowedRoles?: string[];
}

interface NavGroup {
  name: string;
  items: NavItem[];
}

const NAV_GROUPS: NavGroup[] = [
  {
    name: "Core",
    items: [
      { id: "dashboard", label: "Dashboard", path: "/", icon: LayoutDashboard },
      { id: "chat", label: "Chat", path: "/chat", icon: MessageSquare },
    ],
  },
  {
    name: "Intelligence",
    items: [
      { id: "agents", label: "Agents", path: "/agents", icon: Bot },
      { id: "orchestration", label: "Automation Studio", path: "/automation/studio", icon: GitBranch, allowedRoles: ["admin", "editor"] },
      { id: "prompts", label: "Prompt Library", path: "/prompts", icon: FileText, allowedRoles: ["admin", "editor"] },
    ],
  },
  {
    name: "Knowledge",
    items: [
      { id: "vault", label: "Knowledge Vault", path: "/vault", icon: BookOpen, allowedRoles: ["admin", "editor"] },
      { id: "knowledge-graph", label: "Knowledge Graph", path: "/knowledge-graph", icon: Network, allowedRoles: ["admin", "editor"] },
      { id: "graphify", label: "Graphify Docs", path: "/graphify", icon: Share2, allowedRoles: ["admin", "editor"] },
    ],
  },
  {
    name: "DevOps",
    items: [
      { id: "pipelines", label: "Pipelines", path: "/pipelines", icon: Container, allowedRoles: ["admin", "editor"] },
      { id: "observability", label: "Observability", path: "/observability", icon: Activity, allowedRoles: ["admin", "editor"] },
      { id: "events", label: "Event Explorer", path: "/events", icon: Terminal, allowedRoles: ["admin", "editor"] },
      { id: "tools", label: "Tools & Registry", path: "/tools", icon: Wrench, allowedRoles: ["admin"] },
    ],
  },
  {
    name: "System",
    items: [
      { id: "users", label: "Users", path: "/users", icon: Users, allowedRoles: ["admin"] },
      { id: "documentation", label: "Doc Health", path: "/documentation", icon: FileText, allowedRoles: ["admin", "editor"] },
      { id: "costs", label: "Cost Center", path: "/costs", icon: Coins, allowedRoles: ["admin"] },
      { id: "settings", label: "Settings", path: "/settings", icon: Settings, allowedRoles: ["admin", "editor"] },
    ],
  },
];

export function Sidebar() {
  const navigate = useNavigate();
  const location = useLocation();
  const systemStatus = useSystemStore((s) => s.status);
  const currentVersion = useUpdateStore((s) => s.currentVersion);
  const sidebarCollapsed = useUIStore((s) => s.sidebarCollapsed);
  const toggleSidebar = useUIStore((s) => s.toggleSidebar);
  const setCommandPaletteOpen = useUIStore((s) => s.setCommandPaletteOpen);
  const user = useAuthStore((s) => s.user);

  const role = user?.role || "viewer";

  const visibleGroups = NAV_GROUPS.map((group) => {
    const items = group.items.filter(
      (item) => !item.allowedRoles || item.allowedRoles.includes(role)
    );
    return { ...group, items };
  }).filter((group) => group.items.length > 0);

  return (
    <aside
      className={cn(
        "flex h-full flex-col border-r border-border-subtle bg-surface transition-all duration-300 ease-in-out select-none",
        sidebarCollapsed ? "w-14" : "w-60"
      )}
    >
      {/* Brand Header */}
      <div className="flex h-12 items-center justify-between border-b border-border-subtle px-3 py-2">
        <div className="flex items-center gap-2 overflow-hidden">
          <svg
            className="h-6 w-6 text-accent-primary shrink-0"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2.5"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <path d="M4 4v16h4v-8l6 8h5l-7-9 7-7h-5l-6 8V4H4z" />
          </svg>
          {!sidebarCollapsed && (
            <div className="flex flex-col">
              <span className="text-sm font-black tracking-wider text-text-primary">K.A.O.S</span>
              <span className="text-[9px] font-medium text-text-dim leading-none">v{currentVersion}</span>
            </div>
          )}
        </div>
      </div>

      {/* Nav Menu */}
      <nav className="flex-1 space-y-4 overflow-y-auto p-2 scrollbar-thin">
        {visibleGroups.map((group, groupIdx) => (
          <div key={group.name} className="space-y-1">
            {!sidebarCollapsed ? (
              <h3 className="px-3 text-[10px] font-semibold uppercase tracking-wider text-text-dim/80">
                {group.name}
              </h3>
            ) : (
              groupIdx > 0 && <div className="my-2 border-t border-border-subtle/50 mx-1" />
            )}

            <div className="space-y-[2px]">
              {group.items.map((item) => {
                const Icon = item.icon;
                const isActive =
                  item.path === "/"
                    ? location.pathname === "/"
                    : location.pathname.startsWith(item.path);

                const buttonEl = (
                  <button
                    onClick={() => navigate(item.path)}
                    aria-label={item.label}
                    aria-current={isActive ? "page" : undefined}
                    className={cn(
                      "flex w-full items-center gap-3 rounded-md p-2 text-sm transition-all duration-150 relative",
                      "active:scale-[0.98] outline-none group",
                      isActive
                        ? "bg-bg-active text-text-primary font-medium"
                        : "text-text-muted hover:bg-surface-hover hover:text-text-primary",
                      sidebarCollapsed ? "justify-center" : "justify-start px-3"
                    )}
                  >
                    {/* Active Accent Indicator Line */}
                    {isActive && (
                      <div className="absolute left-0 top-1.5 bottom-1.5 w-[3px] rounded-r bg-accent-primary" />
                    )}

                    <Icon className={cn("h-4 w-4 shrink-0 transition-transform duration-fast", !isActive && "group-hover:scale-105")} />
                    {!sidebarCollapsed && (
                      <span className="truncate">{item.label}</span>
                    )}
                  </button>
                );

                return sidebarCollapsed ? (
                  <Tooltip key={item.id} content={item.label} side="right">
                    {buttonEl}
                  </Tooltip>
                ) : (
                  <div key={item.id}>{buttonEl}</div>
                );
              })}
            </div>
          </div>
        ))}
      </nav>

      {/* Footer Area */}
      <div className="border-t border-border-subtle bg-bg-canvas/20 p-2 space-y-2">
        {/* Ctrl+K Command Palette Trigger Prompt */}
        {!sidebarCollapsed && (
          <button
            onClick={() => setCommandPaletteOpen(true)}
            className="flex w-full items-center justify-between rounded-md border border-border-subtle bg-surface-raised px-2 py-1.5 text-left text-[11px] text-text-muted hover:text-text-primary transition-colors duration-fast"
          >
            <span className="flex items-center gap-1.5">
              <Terminal className="h-3.5 w-3.5" />
              <span>Search actions...</span>
            </span>
            <kbd className="pointer-events-none inline-flex h-4 select-none items-center gap-0.5 rounded border border-border-subtle bg-bg-active px-1 text-[9px] font-mono text-text-dim">
              <span>Ctrl</span><span>K</span>
            </kbd>
          </button>
        )}

        {/* System Status / Toggle Collapse */}
        <div className="flex items-center justify-between px-1">
          <div className="flex items-center gap-2 overflow-hidden">
            <div
              className={cn(
                "h-2.5 w-2.5 rounded-full ring-2 ring-transparent transition-all",
                systemStatus === "online" && "bg-accent-primary ring-accent-primary/20",
                systemStatus === "degraded" && "bg-warning ring-warning/20",
                systemStatus === "offline" && "bg-error ring-error/20",
              )}
            />
            {!sidebarCollapsed && (
              <span className="text-xs text-text-muted capitalize truncate">
                {systemStatus}
              </span>
            )}
          </div>

          <button
            onClick={toggleSidebar}
            aria-label={sidebarCollapsed ? "Expand sidebar" : "Collapse sidebar"}
            className="rounded p-1 text-text-dim hover:bg-bg-active hover:text-text-primary transition-colors duration-fast"
          >
            {sidebarCollapsed ? (
              <ChevronRight className="h-4 w-4" />
            ) : (
              <ChevronLeft className="h-4 w-4" />
            )}
          </button>
        </div>
      </div>
    </aside>
  );
}
