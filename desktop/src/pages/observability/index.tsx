import { useState, useEffect } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Input } from "@/shared/ui/input";
import { Badge } from "@/shared/ui/badge";
import { ScrollArea } from "@/shared/ui/scroll-area";
import { useSystemStore } from "@/shared/lib/stores";
import { Sparkline } from "@/shared/ui/sparkline";
import { Search, Activity, AlertTriangle, Timeline } from "lucide-react";

interface LogEntry {
  level: "INFO" | "WARN" | "ERROR" | "DEBUG";
  message: string;
  timestamp: string;
}

interface Alert {
  id: string;
  severity: "critical" | "warning" | "info";
  message: string;
  time: string;
}

const MOCK_ALERTS: Alert[] = [
  { id: "1", severity: "critical", message: "Ollama service unresponsive >30s", time: "2m ago" },
  { id: "2", severity: "warning", message: "VRAM usage above 80% threshold", time: "10m ago" },
  { id: "3", severity: "info", message: "Model cache refreshed: 3 new models", time: "1h ago" },
];

export default function ObservabilityPage() {
  const runtime = useSystemStore((s) => s.runtime);
  const services = useSystemStore((s) => s.services);
  const [logFilter, setLogFilter] = useState("");
  const [logs, setLogs] = useState<LogEntry[]>([
    { level: "INFO", message: "KAOS Observability initialized", timestamp: new Date().toISOString() },
    { level: "INFO", message: "Connected to backend: localhost:8000", timestamp: new Date().toISOString() },
    { level: "DEBUG", message: "System metrics collection started", timestamp: new Date().toISOString() },
  ]);

  useEffect(() => {
    const interval = setInterval(() => {
      const levels: LogEntry["level"][] = ["INFO", "DEBUG", "WARN", "ERROR"];
      const level = levels[Math.floor(Math.random() * levels.length)];
      const messages = [
        "RAG query processed: 4 chunks retrieved",
        "LLM response: 342 tokens generated",
        "Qdrant health check passed",
        "VRAM buffer flushed: 1.2GB freed",
        "Tool call executed: search_web",
        "File watcher detected change in vault/",
      ];
      setLogs((prev) => [...prev.slice(-49), {
        level,
        message: messages[Math.floor(Math.random() * messages.length)],
        timestamp: new Date().toISOString(),
      }]);
    }, 3000);
    return () => clearInterval(interval);
  }, []);

  const filteredLogs = logFilter
    ? logs.filter((l) => l.message.toLowerCase().includes(logFilter.toLowerCase()))
    : logs;

  const serviceEntries = [
    { name: "Ollama", status: services.ollama },
    { name: "Backend", status: services.backend },
    { name: "Qdrant", status: services.qdrant },
  ];

  return (
    <div className="flex h-full flex-col gap-4 p-4">
      <div>
        <h1 className="text-base font-semibold text-text-primary">Observability</h1>
        <p className="text-xs text-text-muted mt-0.5">Monitoramento, métricas e logs do sistema</p>
      </div>

      {/* Top row: Metrics sparklines + services */}
      <div className="grid grid-cols-3 gap-3">
        <Card>
          <CardContent className="p-3">
            <div className="flex items-center justify-between">
              <span className="text-xs text-text-muted">Token Rate</span>
              <Badge variant="info">Active</Badge>
            </div>
            <p className="mt-1 text-lg font-semibold text-text-primary font-mono">342 t/s</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-3">
            <div className="flex items-center justify-between">
              <span className="text-xs text-text-muted">Avg Latency</span>
              <Badge variant={runtime.latency > 100 ? "warning" : "success"}>
                {runtime.latency > 100 ? "Slow" : "Fast"}
              </Badge>
            </div>
            <p className="mt-1 text-lg font-semibold text-text-primary font-mono">{runtime.latency}ms</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-3">
            <div className="flex items-center justify-between">
              <span className="text-xs text-text-muted">Services</span>
            </div>
            <div className="mt-1 flex gap-2">
              {serviceEntries.map((svc) => (
                <div key={svc.name} className="flex items-center gap-1.5">
                  <span className={`h-1.5 w-1.5 rounded-full ${svc.status ? "bg-success" : "bg-error"}`} />
                  <span className="text-xs text-text-muted">{svc.name}</span>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>

      <div className="grid grid-cols-2 gap-3 flex-1 min-h-0">
        {/* Logs */}
        <Card className="flex flex-col">
          <CardHeader className="pb-2">
            <div className="flex items-center justify-between">
              <CardTitle className="flex items-center gap-2 text-xs font-semibold text-text-muted uppercase tracking-wider">
                <Activity className="h-3.5 w-3.5" />
                Live Log Stream
              </CardTitle>
              <div className="w-48">
                <Input
                  value={logFilter}
                  onChange={(e) => setLogFilter(e.target.value)}
                  placeholder="Filter logs..."
                  className="h-7 text-[11px]"
                />
              </div>
            </div>
          </CardHeader>
          <CardContent className="flex-1 min-h-0 p-0 px-4 pb-4">
            <ScrollArea className="h-full">
              <div className="font-mono text-[11px] leading-5">
                {filteredLogs.map((log, i) => (
                  <div key={i} className={
                    log.level === "ERROR" ? "text-error" :
                    log.level === "WARN" ? "text-warning" :
                    log.level === "DEBUG" ? "text-text-dim" :
                    "text-text-muted"
                  }>
                    <span className="text-text-dim">[{log.timestamp.slice(11, 19)}]</span>{" "}
                    <span className="font-semibold">[{log.level}]</span>{" "}
                    {log.message}
                  </div>
                ))}
              </div>
            </ScrollArea>
          </CardContent>
        </Card>

        {/* Alerts */}
        <Card className="flex flex-col">
          <CardHeader className="pb-2">
            <CardTitle className="flex items-center gap-2 text-xs font-semibold text-text-muted uppercase tracking-wider">
              <AlertTriangle className="h-3.5 w-3.5" />
              Alerts
            </CardTitle>
          </CardHeader>
          <CardContent className="flex-1 min-h-0 p-0 px-4 pb-4">
            <div className="flex flex-col gap-1.5">
              {MOCK_ALERTS.map((alert) => (
                <div
                  key={alert.id}
                  className="flex items-center justify-between rounded-lg border border-border-subtle bg-canvas/50 px-3 py-2"
                >
                  <div className="flex items-center gap-2">
                    <span className={`h-1.5 w-1.5 rounded-full ${
                      alert.severity === "critical" ? "bg-error" :
                      alert.severity === "warning" ? "bg-warning" : "bg-accent-primary"
                    }`} />
                    <span className="text-xs text-text-primary">{alert.message}</span>
                  </div>
                  <span className="text-[10px] text-text-dim shrink-0">{alert.time}</span>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
