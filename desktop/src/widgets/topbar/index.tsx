import { useSystemStore } from "@/shared/lib/stores";
import { cn } from "@/shared/lib/utils";
import { useEffect, useState } from "react";

export function TopBar() {
  const status = useSystemStore((s) => s.status);
  const runtime = useSystemStore((s) => s.runtime);
  const [time, setTime] = useState(new Date());

  useEffect(() => {
    const interval = setInterval(() => setTime(new Date()), 1000);
    return () => clearInterval(interval);
  }, []);

  const statusColor =
    status === "online"
      ? "bg-success"
      : status === "degraded"
        ? "bg-warning"
        : "bg-error";

  const statusLabel =
    status === "online"
      ? "NOMINAL"
      : status === "degraded"
        ? "DEGRADED"
        : "OFFLINE";

  const timeStr = time.toLocaleTimeString("pt-BR", { hour: "2-digit", minute: "2-digit" });

  return (
    <header className="flex h-9 items-center justify-between border-b border-border-subtle bg-surface/80 px-4 text-xs text-text-muted backdrop-blur-md">
      <div className="flex items-center gap-3">
        <div className="flex items-center gap-1.5">
          <div className={cn("h-1.5 w-1.5 rounded-full", statusColor)} />
          <span className="font-mono text-[11px] uppercase tracking-wider">
            System: {statusLabel}
          </span>
        </div>
      </div>

      <div className="flex items-center gap-4">
        {runtime.activeModel && (
          <span className="font-mono text-[11px]">
            Ollama: {runtime.activeModel} (Local)
          </span>
        )}
        {runtime.vramTotal > 0 && (
          <span className="font-mono text-[11px]">
            VRAM: {runtime.vramUsed.toFixed(1)}/{runtime.vramTotal}GB
          </span>
        )}
        <span className="font-mono text-[11px]">{timeStr}</span>
      </div>
    </header>
  );
}
