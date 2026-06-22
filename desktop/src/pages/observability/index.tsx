import { useEffect, useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Badge } from "@/shared/ui/badge";
import { useSystemStore } from "@/shared/lib/stores";
import { kaosFetch } from "@/shared/api/kaos-client";
import { Activity, AlertTriangle, Server, BarChart3, Database, Gauge } from "lucide-react";

export default function ObservabilityPage() {
  const runtime = useSystemStore((s) => s.runtime);
  const metrics = useSystemStore((s) => s.metrics);
  const services = useSystemStore((s) => s.services);

  const [obsServices, setObsServices] = useState<Record<string, boolean>>({});
  const [obsLoading, setObsLoading] = useState(true);

  useEffect(() => {
    const fetchObs = async () => {
      try {
        const res = await kaosFetch("http://localhost:8000/api/observability/health", "");
        if (res.ok) {
          const data = await res.json();
          setObsServices(data);
        }
      } catch {}
      finally { setObsLoading(false); }
    };
    fetchObs();
    const interval = setInterval(fetchObs, 15_000);
    return () => clearInterval(interval);
  }, []);

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

  return (
    <div className="flex h-full flex-col gap-4 p-4 overflow-y-auto">
      <div>
        <h1 className="text-base font-semibold text-text-primary">Observability</h1>
        <p className="text-xs text-text-muted mt-0.5">Monitoramento, métricas e logs do sistema</p>
      </div>

      <div className="grid grid-cols-4 gap-3">
        <Card>
          <CardContent className="p-3">
            <div className="flex items-center justify-between">
              <span className="text-xs text-text-muted flex items-center gap-1"><BarChart3 className="h-3 w-3" /> Token Rate</span>
              <Badge variant="info">Active</Badge>
            </div>
            <p className="mt-1 text-lg font-semibold text-text-primary font-mono">{metrics.tokenRate > 0 ? `${metrics.tokenRate} t/s` : "—"}</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-3">
            <div className="flex items-center justify-between">
              <span className="text-xs text-text-muted flex items-center gap-1"><Gauge className="h-3 w-3" /> Avg Latency</span>
              <Badge variant={runtime.latency > 100 ? "warning" : runtime.latency > 0 ? "success" : "neutral"}>
                {runtime.latency > 100 ? "Slow" : runtime.latency > 0 ? "Fast" : "N/A"}
              </Badge>
            </div>
            <p className="mt-1 text-lg font-semibold text-text-primary font-mono">{runtime.latency > 0 ? `${runtime.latency}ms` : "—"}</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-3">
            <div className="flex items-center justify-between">
              <span className="text-xs text-text-muted flex items-center gap-1"><Database className="h-3 w-3" /> Vectors</span>
            </div>
            <p className="mt-1 text-lg font-semibold text-text-primary font-mono">{metrics.vectorCount > 0 ? metrics.vectorCount.toLocaleString() : "—"}</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-3">
            <div className="flex items-center justify-between">
              <span className="text-xs text-text-muted flex items-center gap-1"><Activity className="h-3 w-3" /> Active Model</span>
            </div>
            <p className="mt-1 text-lg font-semibold text-text-primary font-mono text-sm">{runtime.activeModel || "—"}</p>
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader className="pb-2">
          <CardTitle className="flex items-center gap-2 text-xs font-semibold text-text-muted uppercase tracking-wider">
            <Server className="h-3.5 w-3.5" />
            Services
          </CardTitle>
        </CardHeader>
        <CardContent className="p-4">
          <div className="grid grid-cols-4 gap-3">
            {serviceEntries.map((svc) => (
              <div key={svc.name} className="flex items-center gap-2 rounded-lg border border-border-subtle bg-canvas/50 px-3 py-2">
                <span className={`h-2 w-2 rounded-full ${svc.status ? "bg-success" : "bg-error"}`} />
                <div>
                  <span className="text-xs text-text-primary">{svc.name}</span>
                  <span className="text-[10px] text-text-dim ml-2">{svc.status ? "UP" : "DOWN"}</span>
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>

      <div className="grid grid-cols-2 gap-3 flex-1 min-h-0">
        <Card className="flex flex-col">
          <CardHeader className="pb-2">
            <CardTitle className="flex items-center gap-2 text-xs font-semibold text-text-muted uppercase tracking-wider">
              <Activity className="h-3.5 w-3.5" />
              Live Log Stream
            </CardTitle>
          </CardHeader>
          <CardContent className="flex-1 flex items-center justify-center">
            <p className="text-xs text-text-dim text-center">
              {obsServices.loki ? (
                <>Connected to Loki. <a href="http://localhost:3001/explore" target="_blank" className="text-accent-primary underline">Open in Grafana</a></>
              ) : (
                <>No telemetry available<br /><span className="text-[10px] text-text-muted">Start Loki + Grafana for live logs</span></>
              )}
            </p>
          </CardContent>
        </Card>

        <Card className="flex flex-col">
          <CardHeader className="pb-2">
            <CardTitle className="flex items-center gap-2 text-xs font-semibold text-text-muted uppercase tracking-wider">
              <AlertTriangle className="h-3.5 w-3.5" />
              Alerts
            </CardTitle>
          </CardHeader>
          <CardContent className="flex-1 flex items-center justify-center">
            <p className="text-xs text-text-dim text-center">
              No alerts<br />
              <span className="text-[10px] text-text-muted">Alerts will appear here when thresholds are exceeded</span>
            </p>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
