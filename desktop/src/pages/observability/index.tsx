import { useEffect, useState, useRef } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Badge } from "@/shared/ui/badge";
import { useSystemStore, useAuthStore } from "@/application";
import { kaosFetch } from "@/infrastructure";
import { Activity, AlertTriangle, Server, Loader2, Play, Terminal } from "lucide-react";

interface AlertItem {
  id: number;
  type: string;
  message: string;
  time: string;
}

export default function ObservabilityPage() {
  const runtime = useSystemStore((s) => s.runtime);
  const metrics = useSystemStore((s) => s.metrics);
  const services = useSystemStore((s) => s.services);
  const serverUrl = useAuthStore((s) => s.serverUrl);

  const [obsServices, setObsServices] = useState<Record<string, boolean>>({});
  const logsEndRef = useRef<HTMLDivElement>(null);

  // Live logs — populated via SSE from backend
  const [liveLogs, setLiveLogs] = useState<string[]>([]);

  // System alerts — fetched from backend notifications
  const [alerts, setAlerts] = useState<AlertItem[]>([]);
  const [alertsLoading, setAlertsLoading] = useState(true);

  interface NotificationItem {
    id: number;
    level: string;
    title: string;
    message: string;
    created_at: string;
  }

  // Fetch real notifications from backend
  useEffect(() => {
    const fetchNotifications = async () => {
      try {
        const res = await kaosFetch(`${serverUrl}/api/notifications?unread_only=true&limit=10`, "");
        if (res.ok) {
          const data: { notifications: NotificationItem[] } = await res.json();
          const items = (data.notifications || []).map((n: NotificationItem) => ({
            id: n.id,
            type: n.level === "critical" || n.level === "error" ? "error" : n.level === "warning" ? "warn" : "info",
            message: `${n.title}: ${n.message}`,
            time: n.created_at ? new Date(n.created_at).toLocaleString() : "—",
          }));
          setAlerts(items);
        }
      } catch (e) {
        console.error("[observability] Failed to fetch notifications:", e);
      } finally {
        setAlertsLoading(false);
      }
    };
    fetchNotifications();
    const interval = setInterval(fetchNotifications, 10_000);
    return () => clearInterval(interval);
  }, [serverUrl]);
  useEffect(() => {
    const fetchObs = async () => {
      try {
        const res = await kaosFetch(`${serverUrl}/api/observability/health`, "");
        if (res.ok) {
          const data = await res.json();
          setObsServices(data);
        }
      } catch (e) {
        console.error("[observability] Failed to fetch observability health:", e);
      }
    };
    fetchObs();
    const interval = setInterval(fetchObs, 15_000);
    return () => clearInterval(interval);
  }, [serverUrl]);

  // Stream real-time logs from backend using SSE
  useEffect(() => {
    const cleanUrl = serverUrl.replace(/\/+$/, "");
    const eventSource = new EventSource(`${cleanUrl}/api/observability/logs/stream`);

    eventSource.onmessage = (event) => {
      if (event.data) {
        setLiveLogs((prev) => [...prev.slice(-199), event.data]);
      }
    };

    eventSource.onerror = (err) => {
      console.error("EventSource failed:", err);
    };

    return () => {
      eventSource.close();
    };
  }, [serverUrl]);

  // Auto scroll logs
  useEffect(() => {
    logsEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [liveLogs]);

  const serviceEntries = [
    { name: "Ollama", status: services.ollama },
    { name: "Backend", status: services.backend },
    { name: "Qdrant", status: services.qdrant },
    { name: "Postgres", status: services.postgres },
    { name: "N8N", status: services.n8n },
    { name: "Grafana", status: obsServices.grafana ?? services.grafana },
    { name: "Prometheus", status: obsServices.prometheus ?? services.prometheus },
    { name: "Loki", status: obsServices.loki ?? false },
  ];

  const allUp = serviceEntries.some((s) => s.status);
  const tokenRate = metrics.tokenRate > 0 ? `${metrics.tokenRate} t/s` : "—";
  const avgLatency = runtime.latency > 0 ? `${runtime.latency}ms` : "—";

  return (
    <div className="flex h-full flex-col gap-4 p-4 overflow-y-auto bg-canvas text-text-primary">
      <div>
        <h1 className="text-base font-semibold text-text-primary">Observability</h1>
        <p className="text-xs text-text-muted mt-0.5">Monitoramento, métricas e logs do sistema em tempo real</p>
      </div>

      {/* Quick Metrics */}
      <div className="grid grid-cols-3 gap-3">
        <Card className="border border-border-subtle bg-surface/50 shadow-md backdrop-blur-sm">
          <CardContent className="p-3">
            <div className="flex items-center justify-between mb-1">
              <span className="text-xs text-text-muted">Token Rate</span>
              <Badge variant={metrics.tokenRate > 0 ? "success" : "neutral"} className="animate-pulse">
                {metrics.tokenRate > 0 ? "Active" : "Idle"}
              </Badge>
            </div>
            <p className="text-xl font-bold text-accent-neon font-mono">{tokenRate}</p>
          </CardContent>
        </Card>
        <Card className="border border-border-subtle bg-surface/50 shadow-md backdrop-blur-sm">
          <CardContent className="p-3">
            <div className="flex items-center justify-between mb-1">
              <span className="text-xs text-text-muted">Avg Latency</span>
              <Badge variant={runtime.latency > 150 ? "warning" : runtime.latency > 0 ? "success" : "neutral"}>
                {runtime.latency > 150 ? "Slow" : runtime.latency > 0 ? "Optimal" : "—"}
              </Badge>
            </div>
            <p className="text-xl font-bold text-accent-primary font-mono">{avgLatency}</p>
          </CardContent>
        </Card>
        <Card className="border border-border-subtle bg-surface/50 shadow-md backdrop-blur-sm">
          <CardContent className="p-3">
            <div className="flex items-center justify-between mb-1">
              <span className="text-xs text-text-muted">Infrastructure</span>
              <Badge variant={allUp ? "success" : "warning"}>
                {serviceEntries.filter((s) => s.status).length}/{serviceEntries.length} UP
              </Badge>
            </div>
            <div className="mt-1.5 flex flex-wrap gap-x-3 gap-y-1">
              {serviceEntries.map((svc) => (
                <div key={svc.name} className="flex items-center gap-1.5">
                  <span className={`h-1.5 w-1.5 rounded-full ${svc.status ? "bg-success animate-pulse" : "bg-error"}`} />
                  <span className="text-[10px] text-text-muted">{svc.name}</span>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Logs and Alerts */}
      <div className="grid grid-cols-2 gap-3 flex-1 min-h-0">
        {/* Terminal Log Stream */}
        <Card className="flex flex-col border border-border-subtle bg-surface/30 shadow-inner">
          <CardHeader className="pb-2 border-b border-border-subtle">
            <CardTitle className="flex items-center justify-between text-xs font-semibold text-text-muted uppercase tracking-wider">
              <div className="flex items-center gap-2">
                <Terminal className="h-3.5 w-3.5 text-accent-primary animate-pulse" />
                Live Log Stream
              </div>
              <Badge variant="info" className="text-[9px] px-1 font-mono uppercase bg-accent-primary/20 text-accent-primary border-none">
                Streaming
              </Badge>
            </CardTitle>
          </CardHeader>
          <CardContent className="flex-1 min-h-0 p-3 bg-canvas/40 overflow-y-auto font-mono text-[10px] space-y-1 select-text scrollbar-thin">
            {liveLogs.map((log, idx) => {
              const isError = log.includes("ERROR");
              const isWarn = log.includes("WARN");
              const isDebug = log.includes("DEBUG");
              let colorClass = "text-text-muted";
              if (isError) colorClass = "text-error font-semibold";
              else if (isWarn) colorClass = "text-warning";
              else if (isDebug) colorClass = "text-text-dim";
              else colorClass = "text-accent-primary";

              return (
                <div key={idx} className={`leading-relaxed hover:bg-surface/20 px-1 rounded transition-colors ${colorClass}`}>
                  {log}
                </div>
              );
            })}
            <div ref={logsEndRef} />
          </CardContent>
        </Card>

        {/* Live Alerts list */}
        <Card className="flex flex-col border border-border-subtle bg-surface/30 shadow-inner">
          <CardHeader className="pb-2 border-b border-border-subtle">
            <CardTitle className="flex items-center gap-2 text-xs font-semibold text-text-muted uppercase tracking-wider">
              <AlertTriangle className="h-3.5 w-3.5 text-warning" />
              Active System Alerts
            </CardTitle>
          </CardHeader>
          <CardContent className="flex-1 min-h-0 p-3 space-y-2 overflow-y-auto">
            {alerts.length === 0 ? (
              <div className="flex flex-col items-center justify-center h-full text-text-dim text-xs">
                No active alerts
              </div>
            ) : (
              alerts.map((alert) => {
                const indicatorColor = alert.type === "error" ? "bg-error" : alert.type === "warn" ? "bg-warning" : "bg-accent-primary";
                const cardBorder = alert.type === "error" ? "border-error/20 bg-error/5" : alert.type === "warn" ? "border-warning/20 bg-warning/5" : "border-border-subtle bg-surface/10";
                
                return (
                  <div key={alert.id} className={`flex items-start justify-between p-3 border rounded-lg transition-all hover:scale-[1.01] ${cardBorder}`}>
                    <div className="flex items-start gap-2.5 min-w-0">
                      <span className={`h-2.5 w-2.5 rounded-full mt-1 shrink-0 ${indicatorColor} animate-ping`} />
                      <div className="min-w-0">
                        <p className="text-xs font-medium text-text-primary leading-tight">{alert.message}</p>
                        <span className="text-[10px] text-text-dim block mt-1">{alert.time}</span>
                      </div>
                    </div>
                    <Badge variant={alert.type as "success" | "warning" | "error" | "info"} className="capitalize text-[9px] py-0 px-1 font-mono select-none">
                      {alert.type}
                    </Badge>
                  </div>
                );
              })
            )}
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
