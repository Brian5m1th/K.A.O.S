import { useEffect, useState } from "react";
import { useSystemStore, useAuthStore } from "@/shared/lib/stores";
import { useSystemMetrics } from "@/features/dashboard/hooks/useSystemMetrics";
import { kaosFetch } from "@/shared/api/kaos-client";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Badge } from "@/shared/ui/badge";
import { Sparkline } from "@/shared/ui/sparkline";
import { Cpu, MemoryStick, Gauge, Database, Bot, Activity, Loader2 } from "lucide-react";

type PanelState = "loading" | "offline" | "empty" | "online";

interface DlqItem {
  id: string;
  workflow_name: string;
  status: string;
  error: string;
  created_at: string;
}

function MetricCard({
  icon,
  label,
  value,
  data,
  color,
  state = "online",
}: {
  icon: React.ReactNode;
  label: string;
  value: string;
  data: number[];
  color: string;
  state?: PanelState;
}) {
  if (state === "loading") {
    return (
      <Card>
        <CardContent className="p-3">
          <div className="flex items-center gap-1.5 text-text-muted text-xs mb-2">{icon}<span>{label}</span></div>
          <Loader2 className="h-4 w-4 animate-spin text-text-dim" />
        </CardContent>
      </Card>
    );
  }
  if (state === "offline") {
    return (
      <Card>
        <CardContent className="p-3">
          <div className="flex items-center gap-1.5 text-text-muted text-xs mb-2">{icon}<span>{label}</span></div>
          <p className="text-xs text-text-dim">—</p>
        </CardContent>
      </Card>
    );
  }
  if (state === "empty") {
    return (
      <Card>
        <CardContent className="p-3">
          <div className="flex items-center gap-1.5 text-text-muted text-xs mb-2">{icon}<span>{label}</span></div>
          <p className="text-lg font-semibold text-text-primary font-mono">—</p>
        </CardContent>
      </Card>
    );
  }
  return (
    <Card>
      <CardContent className="p-3">
        <div className="flex items-center justify-between mb-1">
          <div className="flex items-center gap-1.5 text-text-muted text-xs">{icon}<span>{label}</span></div>
          {data.length > 1 && <Sparkline data={data} width={64} height={20} color={color} />}
        </div>
        <p className="text-lg font-semibold text-text-primary font-mono">{value}</p>
      </CardContent>
    </Card>
  );
}

function EmptyState({ icon, title, description }: { icon: React.ReactNode; title: string; description?: string }) {
  return (
    <div className="flex flex-col items-center justify-center h-full py-8">
      <div className="text-text-dim mb-2">{icon}</div>
      <p className="text-xs text-text-dim">{title}</p>
      {description && <p className="text-[10px] text-text-muted mt-1">{description}</p>}
    </div>
  );
}

export default function DashboardPage() {
  const runtime = useSystemStore((s) => s.runtime);
  const metrics = useSystemStore((s) => s.metrics);
  const services = useSystemStore((s) => s.services);
  const status = useSystemStore((s) => s.status);
  const serverUrl = useAuthStore((s) => s.serverUrl);
  const history = useSystemMetrics();

  const [dlqItems, setDlqItems] = useState<DlqItem[]>([]);
  const [wfLoading, setWfLoading] = useState(true);
  const isOnline = status === "online";

  // Fetch workflows from DLQ
  useEffect(() => {
    if (!isOnline) { setWfLoading(false); return; }
    const fetchDlq = async () => {
      try {
        const res = await kaosFetch(`${serverUrl}/api/orchestrator/dlq`, "");
        if (res.ok) {
          const data = await res.json();
          setDlqItems(data.failed || []);
        }
      } catch {} finally { setWfLoading(false); }
    };
    fetchDlq();
    const interval = setInterval(fetchDlq, 15_000);
    return () => clearInterval(interval);
  }, [serverUrl, isOnline]);

  const sysState: PanelState = history.cpu.length === 0 && !isOnline ? "loading" : isOnline ? "online" : "offline";

  return (
    <div className="flex h-full flex-col gap-4 p-4 overflow-y-auto">
      {/* Status bar */}
      <div className="flex items-center gap-2">
        <Badge variant={status === "online" ? "success" : status === "degraded" ? "warning" : "error"}>
          {status === "online" ? "ONLINE" : status === "degraded" ? "DEGRADED" : "OFFLINE"}
        </Badge>
        <span className="text-[11px] text-text-dim">
          {status === "online" ? "System operational" : status === "degraded" ? "Partial outage" : "No backend connection"}
        </span>
      </div>

      {/* Top Row: Quick Metrics */}
      <div className="grid grid-cols-4 gap-3">
        <MetricCard icon={<Cpu className="h-4 w-4 text-accent-primary" />} label="CPU"
          value={`${history.cpu[history.cpu.length - 1] || 0}%`} data={history.cpu} color="#3B82F6" state={sysState} />
        <MetricCard icon={<MemoryStick className="h-4 w-4 text-accent-neon" />} label="VRAM"
          value={`${runtime.vramUsed.toFixed(1)} / ${runtime.vramTotal}GB`} data={history.vram} color="#8B5CF6" state={sysState} />
        <MetricCard icon={<Gauge className="h-4 w-4 text-success" />} label="Latency"
          value={`${runtime.latency}ms`} data={history.latency} color="#10B981" state={sysState} />
        <MetricCard icon={<Database className="h-4 w-4 text-warning" />} label="Vectors Indexed"
          value={metrics.vectorCount.toLocaleString()} data={[]} color="#F59E0B" state={sysState} />
      </div>

      {/* Middle Row: Workflows + Agents */}
      <div className="grid grid-cols-2 gap-3 flex-1 min-h-0">
        {/* Active Workflows */}
        <Card className="flex flex-col">
          <CardHeader className="pb-2">
            <CardTitle className="flex items-center gap-2 text-sm font-semibold">
              <Activity className="h-4 w-4 text-accent-primary" />
              Active Workflows
            </CardTitle>
          </CardHeader>
          <CardContent className="flex-1 min-h-0 px-4 pb-4">
            {!isOnline ? (
              <p className="text-xs text-text-dim py-4">System offline — connect to backend to view workflows</p>
            ) : wfLoading ? (
              <div className="flex items-center justify-center py-4"><Loader2 className="h-4 w-4 animate-spin text-text-dim" /></div>
            ) : dlqItems.length === 0 ? (
              <p className="text-xs text-text-dim py-4">No failed workflows</p>
            ) : (
              <div className="flex flex-col gap-1.5">
                {dlqItems.map((item) => (
                  <div key={item.id} className="flex items-center justify-between rounded-lg border border-border-subtle bg-canvas/50 px-3 py-2">
                    <span className="text-xs font-medium text-text-primary">{item.workflow_name}</span>
                    <div className="flex items-center gap-2">
                      <span className="text-[11px] text-text-dim font-mono">{item.error?.slice(0, 30)}</span>
                      <Badge variant="error">FAILED</Badge>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </CardContent>
        </Card>

        {/* Agent Monitor */}
        <Card className="flex flex-col">
          <CardHeader className="pb-2">
            <CardTitle className="flex items-center gap-2 text-sm font-semibold">
              <Bot className="h-4 w-4 text-accent-neon" />
              Agent Monitor
            </CardTitle>
          </CardHeader>
          <CardContent className="flex-1 min-h-0 px-4 pb-4 flex items-center justify-center">
            {!isOnline ? (
              <p className="text-xs text-text-dim text-center">System offline</p>
            ) : (
              <EmptyState icon={<Bot className="h-8 w-8" />} title="No agents running"
                description="Agent telemetry available in a future phase" />
            )}
          </CardContent>
        </Card>
      </div>

      {/* Bottom: Logs */}
      <Card className="h-32 shrink-0">
        <CardHeader className="pb-1">
          <CardTitle className="text-xs font-semibold text-text-muted uppercase tracking-wider">System Log</CardTitle>
        </CardHeader>
        <CardContent className="p-0 px-4 pb-3 flex items-center justify-center h-20">
          {!isOnline ? (
            <p className="text-xs text-text-dim text-center">No telemetry available<br /><span className="text-[10px] text-text-muted">Backend offline</span></p>
          ) : (
            <p className="text-xs text-text-dim text-center">No telemetry available<br /><span className="text-[10px] text-text-muted">Connect Prometheus + Loki for live logs</span></p>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
