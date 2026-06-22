import { useEffect, useState } from "react";
import { useSystemStore, useAuthStore } from "@/shared/lib/stores";
import { useSystemMetrics } from "@/features/dashboard/hooks/useSystemMetrics";
import { kaosFetch } from "@/shared/api/kaos-client";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Badge } from "@/shared/ui/badge";
import { Sparkline } from "@/shared/ui/sparkline";
import { Cpu, MemoryStick, Gauge, Database, Bot, Activity } from "lucide-react";

interface DlqItem {
  id: string;
  workflow_name: string;
  status: string;
  error: string;
  created_at: string;
}

export default function DashboardPage() {
  const runtime = useSystemStore((s) => s.runtime);
  const metrics = useSystemStore((s) => s.metrics);
  const services = useSystemStore((s) => s.services);
  const status = useSystemStore((s) => s.status);
  const serverUrl = useAuthStore((s) => s.serverUrl);
  const history = useSystemMetrics();

  const [dlqItems, setDlqItems] = useState<DlqItem[]>([]);
  const [loading, setLoading] = useState(true);

  // Fetch workflows from DLQ endpoint
  useEffect(() => {
    const fetchDlq = async () => {
      try {
        const res = await kaosFetch(`${serverUrl}/api/orchestrator/dlq`, "");
        if (res.ok) {
          const data = await res.json();
          setDlqItems(data.failed || []);
        }
      } catch {
        // Backend offline — keep empty
      } finally {
        setLoading(false);
      }
    };
    fetchDlq();
    const interval = setInterval(fetchDlq, 10_000);
    return () => clearInterval(interval);
  }, [serverUrl]);

  const statusBadge = {
    online: "success" as const,
    degraded: "warning" as const,
    offline: "error" as const,
  };

  return (
    <div className="flex h-full flex-col gap-4 p-4">
      {/* Top Row: Quick Metrics */}
      <div className="grid grid-cols-4 gap-3">
        <MetricCard
          icon={<Cpu className="h-4 w-4 text-accent-primary" />}
          label="CPU"
          value={`${history.cpu[history.cpu.length - 1] || 0}%`}
          data={history.cpu}
          color="#3B82F6"
        />
        <MetricCard
          icon={<MemoryStick className="h-4 w-4 text-accent-neon" />}
          label="VRAM"
          value={`${runtime.vramUsed.toFixed(1)} / ${runtime.vramTotal}GB`}
          data={history.vram}
          color="#8B5CF6"
        />
        <MetricCard
          icon={<Gauge className="h-4 w-4 text-success" />}
          label="Latency"
          value={`${runtime.latency}ms`}
          data={history.latency}
          color="#10B981"
        />
        <MetricCard
          icon={<Database className="h-4 w-4 text-warning" />}
          label="Vectors Indexed"
          value={metrics.vectorCount.toLocaleString()}
          data={[]}
          color="#F59E0B"
        />
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
          <CardContent className="flex-1 min-h-0 p-0 px-4 pb-4">
            <div className="flex flex-col gap-1.5">
              {loading ? (
                <p className="text-xs text-text-dim py-4 text-center">Loading workflows...</p>
              ) : dlqItems.length === 0 ? (
                <p className="text-xs text-text-dim py-4 text-center">No failed workflows</p>
              ) : (
                dlqItems.map((item) => (
                  <div
                    key={item.id}
                    className="flex items-center justify-between rounded-lg border border-border-subtle bg-canvas/50 px-3 py-2 transition-colors hover:bg-bg-active"
                  >
                    <div className="flex items-center gap-2">
                      <span className="text-xs font-medium text-text-primary">{item.workflow_name}</span>
                    </div>
                    <div className="flex items-center gap-2">
                      <span className="text-[11px] text-text-dim font-mono">{item.error?.slice(0, 30)}</span>
                      <Badge variant="error">FAILED</Badge>
                    </div>
                  </div>
                ))
              )}
            </div>
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
          <CardContent className="flex-1 min-h-0 p-0 px-4 pb-4">
            <div className="flex flex-col gap-1.5">
              <div className="flex items-center justify-center h-full min-h-[100px]">
                <p className="text-xs text-text-dim text-center">
                  Agent telemetry coming soon in Fase 4<br />
                  <span className="text-[10px] text-text-muted">(Prometheus + Loki integration)</span>
                </p>
              </div>
          </CardContent>
        </Card>
      </div>

      {/* Bottom: Logs — placeholder until Prometheus/Loki */}
      <Card className="h-32 shrink-0">
        <CardHeader className="pb-1">
          <CardTitle className="text-xs font-semibold text-text-muted uppercase tracking-wider">
            System Log
          </CardTitle>
        </CardHeader>
        <CardContent className="p-0 px-4 pb-3">
          <div className="flex items-center justify-center h-20">
            <p className="text-xs text-text-dim text-center">
              No telemetry available<br />
              <span className="text-[10px] text-text-muted">Connect Prometheus + Loki for live logs (Fase 4)</span>
            </p>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}

function MetricCard({
  icon,
  label,
  value,
  data,
  color,
}: {
  icon: React.ReactNode;
  label: string;
  value: string;
  data: number[];
  color: string;
}) {
  return (
    <Card>
      <CardContent className="p-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-1.5 text-text-muted text-xs">
            {icon}
            <span>{label}</span>
          </div>
          {data.length > 1 && (
            <Sparkline data={data} width={64} height={20} color={color} />
          )}
        </div>
        <p className="mt-1 text-lg font-semibold text-text-primary font-mono">{value}</p>
      </CardContent>
    </Card>
  );
}
