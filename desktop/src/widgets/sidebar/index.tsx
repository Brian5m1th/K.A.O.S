import { cn } from "@/shared/lib/utils";

type Screen = "provider" | "vault" | "chat" | "settings";

interface NavItem {
  id: Screen;
  label: string;
  icon: string;
}

const NAV_ITEMS: NavItem[] = [
  { id: "provider", label: "Providers", icon: "⚙" },
  { id: "vault", label: "Vault", icon: "📁" },
  { id: "chat", label: "Chat", icon: "💬" },
  { id: "settings", label: "Settings", icon: "🔧" },
];

interface Props {
  currentScreen: Screen;
  onNavigate: (screen: Screen) => void;
  connected: boolean;
}

export function Sidebar({ currentScreen, onNavigate, connected }: Props) {
  return (
    <aside className="flex h-full w-56 flex-col border-r border-zinc-800 bg-zinc-900/50">
      <div className="flex items-center gap-2 border-b border-zinc-800 px-4 py-3">
        <span className="text-sm font-bold text-zinc-100">KAOS</span>
        <span className="text-[10px] text-zinc-500">v0.5.0</span>
      </div>

      <nav className="flex-1 space-y-1 p-2">
        {NAV_ITEMS.map((item) => (
          <button
            key={item.id}
            onClick={() => onNavigate(item.id)}
            className={cn(
              "flex w-full items-center gap-2 rounded-md px-3 py-2 text-sm transition-colors",
              currentScreen === item.id
                ? "bg-zinc-800 text-zinc-100"
                : "text-zinc-400 hover:bg-zinc-800/50 hover:text-zinc-200",
            )}
          >
            <span className="text-base">{item.icon}</span>
            <span>{item.label}</span>
          </button>
        ))}
      </nav>

      <div className="border-t border-zinc-800 p-3">
        <div className="flex items-center gap-2">
          <div
            className={cn(
              "h-2 w-2 rounded-full",
              connected ? "bg-success" : "bg-error",
            )}
          />
          <span className="text-xs text-zinc-500">
            {connected ? "Connected" : "Disconnected"}
          </span>
        </div>
      </div>
    </aside>
  );
}
