import { useEffect, useState, useRef } from "react";
import { useNavigate } from "react-router-dom";
import { useSystemStore, useAuthStore } from "@/application";
import { useSystemMetrics } from "@/features/dashboard/hooks/useSystemMetrics";
import { kaosFetch } from "@/infrastructure";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Badge } from "@/shared/ui/badge";
import { Sparkline } from "@/shared/ui/sparkline";
import {
  Cpu,
  MemoryStick,
  Gauge,
  Database,
  Bot,
  Activity,
  Loader2,
  Terminal,
  MessageSquare,
  BookOpen,
  FileText,
  Play,
  ExternalLink,
  AlertTriangle,
  AlertCircle,
  Info,
} from "lucide-react";

type PanelState = "loading" | "offline" | "empty" | "online";

interface DlqItem {
  id: string;
  workflow_name: string;
  status: string;
  error: string;
  created_at: string;
}

interface AgentItem {
  name: string;
  role: string;
  status: "active" | "idle";
  activity: string;
}

interface CostBreakdownItem {
  total_tokens?: number;
}

interface AgentInstanceItem {
  name: string;
}

interface NotificationItem {
  id: string;
  level: "info" | "warning" | "error" | "critical";
  title: string;
  message: string;
  source: string;
  created_at: string;
  read: boolean;
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
      <Card className="border border-border-subtle bg-surface/50">
        <CardContent className="p-3">
          <div className="flex items-center gap-1.5 text-text-muted text-xs mb-2">
            {icon}
            <span>{label}</span>
          </div>
          <Loader2 className="h-4 w-4 animate-spin text-text-dim" />
        </CardContent>
      </Card>
    );
  }
  if (state === "offline") {
    return (
      <Card className="border border-border-subtle bg-surface/50">
        <CardContent className="p-3">
          <div className="flex items-center gap-1.5 text-text-muted text-xs mb-2">
            {icon}
            <span>{label}</span>
          </div>
          <p className="text-xs text-text-dim">—</p>
        </CardContent>
      </Card>
    );
  }
  if (state === "empty") {
    return (
      <Card className="border border-border-subtle bg-surface/50">
        <CardContent className="p-3">
          <div className="flex items-center gap-1.5 text-text-muted text-xs mb-2">
            {icon}
            <span>{label}</span>
          </div>
          <p className="text-lg font-semibold text-text-primary font-mono">—</p>
        </CardContent>
      </Card>
    );
  }
  return (
    <Card className="border border-border-subtle bg-surface/50 hover:bg-surface transition-colors shadow-md backdrop-blur-sm">
      <CardContent className="p-3">
        <div className="flex items-center justify-between mb-1">
          <div className="flex items-center gap-1.5 text-text-muted text-xs">
            {icon}
            <span>{label}</span>
          </div>
          {data.length > 1 && <Sparkline data={data} width={64} height={20} color={color} />}
        </div>
        <p className="text-lg font-semibold text-text-primary font-mono">{value}</p>
      </CardContent>
    </Card>
  );
}

export default function DashboardPage() {
  const navigate = useNavigate();
  const runtime = useSystemStore((s) => s.runtime);
  const metrics = useSystemStore((s) => s.metrics);
  const status = useSystemStore((s) => s.status);
  const serverUrl = useAuthStore((s) => s.serverUrl);
  const user = useAuthStore((s) => s.user);
  const history = useSystemMetrics();

  const [dlqItems, setDlqItems] = useState<DlqItem[]>([]);
  const [wfLoading, setWfLoading] = useState(true);
  const isOnline = status === "online";
  const logsEndRef = useRef<HTMLDivElement>(null);

  // Notifications/Alerts States
  const [notifications, setNotifications] = useState<NotificationItem[]>([]);
  const [alertsLoading, setAlertsLoading] = useState(true);

  // Observability & Costs States
  const [obsHealth, setObsHealth] = useState<{ prometheus: boolean; loki: boolean; grafana: boolean }>({
    prometheus: false,
    loki: false,
    grafana: false,
  });
  const [costs, setCosts] = useState<{ total_usd: number; total_tokens: number }>({
    total_usd: 0.0,
    total_tokens: 0,
  });

  // Active agents — populated from backend
  const [agents, setAgents] = useState<AgentItem[]>([]);

  // System logs — populated via SSE from backend
  const [sysLogs, setSysLogs] = useState<string[]>([]);

  // Active alerts — populated from backend notifications
  const activeAlerts = notifications;

  // Fetch workflows from DLQ
  useEffect(() => {
    if (!isOnline) {
      setWfLoading(false);
      return;
    }
    const fetchDlq = async () => {
      try {
        const res = await kaosFetch(`${serverUrl}/api/orchestrator/dlq`, "");
        if (res.ok) {
          const data = await res.json();
          setDlqItems(data.failed || []);
        }
      } catch (e) {
        console.error("[dashboard] Failed to fetch DLQ:", e);
      } finally {
        setWfLoading(false);
      }
    };
    fetchDlq();
    const interval = setInterval(fetchDlq, 15_000);
    return () => clearInterval(interval);
  }, [serverUrl, isOnline]);

  // Fetch real observability health & costs
  useEffect(() => {
    if (!isOnline) return;
    const fetchObservabilityData = async () => {
      try {
        const [healthRes, costsRes] = await Promise.all([
          kaosFetch(`${serverUrl}/api/observability/health`, ""),
          kaosFetch(`${serverUrl}/api/observability/costs`, ""),
        ]);
        if (healthRes.ok) {
          const healthData = await healthRes.json();
          setObsHealth({
            prometheus: !!healthData.prometheus,
            loki: !!healthData.loki,
            grafana: !!healthData.grafana,
          });
        }
        if (costsRes.ok) {
          const costsData = await costsRes.json();
          const totalTokens = (costsData.breakdown || []).reduce(
            (acc: number, item: CostBreakdownItem) => acc + (item.total_tokens || 0),
            0
          );
          setCosts({
            total_usd: costsData.total_usd || 0,
            total_tokens: totalTokens,
          });
        }
      } catch (err) {
        console.error("Failed to fetch observability data", err);
      }
    };

    fetchObservabilityData();
    const interval = setInterval(fetchObservabilityData, 10_000);
    return () => clearInterval(interval);
  }, [serverUrl, isOnline]);

  // Fetch real notifications from backend
  const fetchNotifications = async () => {
    if (!isOnline) {
      setAlertsLoading(false);
      return;
    }
    try {
      const res = await kaosFetch(`${serverUrl}/api/notifications`, "");
      if (res.ok) {
        const data = await res.json();
        setNotifications(data.notifications || []);
      }
    } catch (e) {
      console.error("[dashboard] Failed to fetch notifications:", e);
    } finally {
      setAlertsLoading(false);
    }
  };

  useEffect(() => {
    fetchNotifications();
    const interval = setInterval(fetchNotifications, 10_000);
    return () => clearInterval(interval);
  }, [serverUrl, isOnline]);

  // Real SSE system logs stream
  useEffect(() => {
    if (!isOnline) return;

    const url = `${serverUrl}/api/observability/logs/stream`;
    console.log("[DashboardPage] Conectando ao Live System Logs:", url);

    const eventSource = new EventSource(url);

    eventSource.onmessage = (event) => {
      if (event.data) {
        setSysLogs((prev) => [...prev.slice(-49), event.data]);
      }
    };

    eventSource.onerror = (err) => {
      console.error("[DashboardPage] Erro no EventSource de logs:", err);
      eventSource.close();
    };

    return () => {
      eventSource.close();
    };
  }, [serverUrl, isOnline]);

  // Fetch real agent status from backend
  const fetchAgentStatus = async () => {
    if (!isOnline) return;
    try {
      const res = await kaosFetch(`${serverUrl}/api/agents/status`, "");
      if (res.ok) {
        const data = await res.json();
        const runningNames = Object.values(data.instances || {}).map((inst: AgentInstanceItem) => inst.name);
        setAgents((prev) =>
          prev.map((agent) => {
            const isRunning = runningNames.includes(agent.name);
            return {
              ...agent,
              status: isRunning ? "active" : "idle",
              activity: isRunning ? "Processando tarefas..." : "Aguardando gatilho",
            };
          })
        );
      }
    } catch (e) {
      console.error("Erro ao carregar status dos agentes:", e);
    }
  };

  useEffect(() => {
    fetchAgentStatus();
    const interval = setInterval(fetchAgentStatus, 10000);
    return () => clearInterval(interval);
  }, [serverUrl, isOnline]);

  // Auto scroll logs
  useEffect(() => {
    logsEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [sysLogs]);

  const sysState: PanelState =
    history.cpu.length === 0 && !isOnline ? "loading" : isOnline ? "online" : "offline";

  const welcomeName = user?.name || user?.email || "Developer";

  // Quick Actions configuration
  const quickActions = [
    {
      label: "New Chat",
      icon: MessageSquare,
      onClick: () => navigate("/chat"),
      desc: "Talk to IA assistant",
    },
    {
      label: "Run Agent",
      icon: Bot,
      onClick: () => navigate("/agents"),
      desc: "Manage active agents",
    },
    {
      label: "Open Vault",
      icon: BookOpen,
      onClick: () => navigate("/vault"),
      desc: "Access knowledge base",
    },
    {
      label: "View Docs",
      icon: FileText,
      onClick: () => navigate("/documentation"),
      desc: "Check document syncs",
    },
  ];

  return (
    <div className="flex h-full flex-col gap-4 p-4 overflow-y-auto bg-canvas text-text-primary">
      {/* Header section with personalized name and status */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-border-subtle pb-4">
        <div>
          <h1 className="text-lg font-black tracking-tight text-text-primary">
            Welcome back, {welcomeName}
          </h1>
          <p className="text-xs text-text-muted mt-0.5">
            Monitor and control the K.A.O.S operations workspace in real time.
          </p>
        </div>
        <div className="flex items-center gap-2">
          <Badge
            variant={
              status === "online" ? "success" : status === "degraded" ? "warning" : "error"
            }
            className="animate-pulse"
          >
            {status === "online" ? "ONLINE" : status === "degraded" ? "DEGRADED" : "OFFLINE"}
          </Badge>
          <span className="text-[11px] text-text-dim font-medium">
            {status === "online"
              ? "All K.A.O.S orchestrator systems are operational"
              : status === "degraded"
                ? "Partial degrade detected"
                : "Failed backend connection"}
          </span>
        </div>
      </div>

      {/* Quick Actions strip */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
        {quickActions.map((action, idx) => {
          const Icon = action.icon;
          return (
            <button
              key={idx}
              onClick={action.onClick}
              className="flex items-center gap-3 rounded-xl border border-border-subtle bg-surface-raised/40 p-3 text-left hover:bg-surface-hover hover:border-accent-primary/30 transition-all outline-none group"
            >
              <div className="rounded-lg bg-bg-active p-2 text-text-muted group-hover:text-accent-primary group-hover:bg-accent-primary/5 transition-colors">
                <Icon className="h-4 w-4" />
              </div>
              <div className="min-w-0">
                <p className="text-xs font-bold text-text-primary group-hover:text-accent-primary transition-colors">
                  {action.label}
                </p>
                <p className="text-[10px] text-text-dim truncate">{action.desc}</p>
              </div>
            </button>
          );
        })}
      </div>

      {/* Metric Cards Row */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
        <MetricCard
          icon={<Cpu className="h-4 w-4 text-accent-primary" />}
          label="CPU Util"
          value={`${history.cpu[history.cpu.length - 1] || 0}%`}
          data={history.cpu}
          color="var(--accent-primary)"
          state={sysState}
        />
        <MetricCard
          icon={<MemoryStick className="h-4 w-4 text-accent-neon" />}
          label="VRAM Alloc"
          value={runtime.vramTotal > 0 ? `${runtime.vramUsed.toFixed(1)} / ${runtime.vramTotal}GB` : "CPU Mode"}
          data={history.vram}
          color="var(--accent-neon)"
          state={sysState}
        />
        <MetricCard
          icon={<Gauge className="h-4 w-4 text-success" />}
          label="LLM Latency"
          value={`${runtime.latency}ms`}
          data={history.latency}
          color="#10B981"
          state={sysState}
        />
        <MetricCard
          icon={<Database className="h-4 w-4 text-warning" />}
          label="Vectors Indexed"
          value={metrics.vectorCount.toLocaleString()}
          data={[]}
          color="#F59E0B"
          state={sysState}
        />
      </div>

      {/* 3-Column Middle Layout: Workflows / Agents / Alerts */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-4 flex-1 min-h-0">
        {/* Active/Failed Workflows */}
        <Card className="flex flex-col border border-border-subtle bg-surface/30 min-h-[220px]">
          <CardHeader className="pb-2 border-b border-border-subtle flex flex-row items-center justify-between">
            <CardTitle className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-text-primary">
              <Activity className="h-4 w-4 text-accent-primary" />
              Workflows (DLQ)
            </CardTitle>
          </CardHeader>
          <CardContent className="flex-1 min-h-0 px-4 py-3 overflow-y-auto">
            {!isOnline ? (
              <div className="h-full flex items-center justify-center">
                <p className="text-xs text-text-dim text-center">System offline — connect to backend to view workflows</p>
              </div>
            ) : wfLoading ? (
              <div className="flex items-center justify-center h-full">
                <Loader2 className="h-4 w-4 animate-spin text-text-dim" />
              </div>
            ) : dlqItems.length === 0 ? (
              <div className="flex flex-col items-center justify-center h-full text-text-dim text-xs py-8">
                No failed workflows in Dead-Letter Queue
              </div>
            ) : (
              <div className="flex flex-col gap-2">
                {dlqItems.map((item) => (
                  <div
                    key={item.id}
                    className="flex items-center justify-between rounded-lg border border-border-subtle bg-canvas/50 px-3 py-2"
                  >
                    <span className="text-xs font-medium text-text-primary">
                      {item.workflow_name}
                    </span>
                    <div className="flex items-center gap-2">
                      <span className="text-[10px] text-text-dim font-mono">
                        {item.error?.slice(0, 30)}...
                      </span>
                      <Badge variant="error">FAILED</Badge>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </CardContent>
        </Card>

        {/* Observability & Cost Monitor */}
        <Card className="flex flex-col border border-border-subtle bg-surface/30 min-h-[220px]">
          <CardHeader className="pb-2 border-b border-border-subtle flex flex-row items-center justify-between">
            <CardTitle className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-text-primary">
              <Activity className="h-4 w-4 text-accent-neon" />
              Observability & Costs
            </CardTitle>
          </CardHeader>
          <CardContent className="flex-1 min-h-0 p-3 space-y-3 overflow-y-auto text-xs">
            <div className="space-y-1.5">
              <div className="flex justify-between border-b border-border-subtle pb-1">
                <span className="text-text-muted">Total Cost (USD)</span>
                <span className="font-mono font-bold text-accent-neon">${costs.total_usd.toFixed(6)}</span>
              </div>
              <div className="flex justify-between border-b border-border-subtle pb-1">
                <span className="text-text-muted">Tokens Consumed</span>
                <span className="font-mono font-bold">{costs.total_tokens.toLocaleString()}</span>
              </div>
            </div>

            <div className="space-y-2 mt-2">
              <p className="text-[10px] font-bold text-text-muted uppercase tracking-wider">Metrics Infrastructure</p>
              <div className="flex items-center justify-between">
                <span className="text-text-muted">Prometheus</span>
                <Badge variant={obsHealth.prometheus ? "success" : "error"} className="text-[9px]">
                  {obsHealth.prometheus ? "ONLINE" : "OFFLINE"}
                </Badge>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-text-muted">Loki</span>
                <Badge variant={obsHealth.loki ? "success" : "error"} className="text-[9px]">
                  {obsHealth.loki ? "ONLINE" : "OFFLINE"}
                </Badge>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-text-muted">Grafana</span>
                <Badge variant={obsHealth.grafana ? "success" : "error"} className="text-[9px]">
                  {obsHealth.grafana ? "ONLINE" : "OFFLINE"}
                </Badge>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Active System Alerts */}
        <Card className="flex flex-col border border-border-subtle bg-surface/30 min-h-[220px]">
          <CardHeader className="pb-2 border-b border-border-subtle flex flex-row items-center justify-between">
            <CardTitle className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-text-primary">
              <AlertCircle className="h-4 w-4 text-accent-neon" />
              Active System Alerts
            </CardTitle>
          </CardHeader>
          <CardContent className="flex-1 min-h-0 p-3 space-y-2 overflow-y-auto">
            {alertsLoading ? (
              <div className="flex items-center justify-center h-full">
                <Loader2 className="h-4 w-4 animate-spin text-text-dim" />
              </div>
            ) : activeAlerts.length === 0 ? (
              <div className="flex flex-col items-center justify-center h-full text-text-dim text-xs py-8">
                No active alerts
              </div>
            ) : (
              activeAlerts.map((alert) => {
                const isCrit = alert.level === "critical" || alert.level === "error";
                return (
                  <div
                    key={alert.id}
                    className={`flex items-start gap-2.5 p-2 rounded-lg border bg-canvas/30 text-xs transition-colors ${
                      isCrit
                        ? "border-red-500/20 hover:bg-red-500/5 text-red-200"
                        : "border-border-subtle hover:bg-surface-hover text-text-primary"
                    }`}
                  >
                    {isCrit ? (
                      <AlertTriangle className="h-4 w-4 text-error shrink-0 mt-0.5" />
                    ) : alert.level === "warning" ? (
                      <AlertCircle className="h-4 w-4 text-warning shrink-0 mt-0.5" />
                    ) : (
                      <Info className="h-4 w-4 text-accent-primary shrink-0 mt-0.5" />
                    )}
                    <div className="min-w-0 flex-1">
                      <p className="font-bold leading-tight truncate">{alert.title}</p>
                      <p className="text-[10px] text-text-muted mt-0.5 leading-snug">
                        {alert.message}
                      </p>
                    </div>
                  </div>
                );
              })
            )}
          </CardContent>
        </Card>
      </div>

      {/* Terminal System Log */}
      <Card className="h-40 shrink-0 border border-border-subtle bg-surface/30 flex flex-col">
        <CardHeader className="pb-1 pt-2 border-b border-border-subtle flex flex-row items-center justify-between">
          <CardTitle className="flex items-center gap-2 text-xs font-semibold text-text-muted uppercase tracking-wider">
            <Terminal className="w-3.5 h-3.5 text-accent-primary" />
            Live System Log
          </CardTitle>
          <Badge
            variant="success"
            className="text-[9px] bg-green-500/10 text-green-500 border border-green-500/20 font-mono tracking-wider animate-pulse"
          >
            LIVE
          </Badge>
        </CardHeader>
        <CardContent className="p-2 bg-canvas/60 overflow-y-auto flex-1 font-mono text-[10px] text-text-muted space-y-1 select-text scrollbar-thin">
          {sysLogs.map((log, idx) => (
            <div
              key={idx}
              className="hover:bg-surface/20 px-1 rounded transition-colors text-accent-primary"
            >
              {log}
            </div>
          ))}
          <div ref={logsEndRef} />
        </CardContent>
      </Card>
    </div>
  );
}
