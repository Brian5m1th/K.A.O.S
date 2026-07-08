import { useEffect, useState, useRef } from "react";
import { useNavigate } from "react-router-dom";
import { useSystemStore, useAuthStore } from "@/shared/lib/stores";
import { useSystemMetrics } from "@/features/dashboard/hooks/useSystemMetrics";
import { kaosFetch } from "@/shared/api/kaos-client";
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

  // Active agents simulated state list
  const [agents, setAgents] = useState<AgentItem[]>([
    {
      name: "kaos-architect",
      role: "Arquitetura & SDD",
      status: "active",
      activity: "Analisando dependências...",
    },
    {
      name: "kaos-auditor",
      role: "Drift & KIRL Verification",
      status: "idle",
      activity: "Aguardando novos commits",
    },
    {
      name: "kaos-coder",
      role: "Code Generation",
      status: "idle",
      activity: "Aguardando tarefas",
    },
  ]);

  // System logs rolling simulated state
  const [sysLogs, setSysLogs] = useState<string[]>([
    "INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)",
    "INFO: Connecting to Qdrant vector database at localhost:6333",
    "INFO: Qdrant client connected successfully. Collection 'kaos' ready.",
    "INFO: PostgreSQL asyncpg pool initialized, size=20",
    "INFO: LangGraph compilation completed successfully. 12 nodes, 8 edges registered.",
  ]);

  // Combined real + fallback simulated notifications
  const fallbackAlerts: NotificationItem[] = [
    {
      id: "drift",
      level: "warning",
      title: "Drift de documentação",
      message: "Drift médio detectado em SDD-KIRL.md",
      source: "audit",
      created_at: new Date(Date.now() - 14 * 60000).toISOString(),
      read: false,
    },
    {
      id: "latency",
      level: "critical",
      title: "Ollama VRAM Degradado",
      message: "Latência ultrapassou 120ms (VRAM cheia)",
      source: "system",
      created_at: new Date(Date.now() - 5 * 60000).toISOString(),
      read: false,
    },
    {
      id: "n8n",
      level: "error",
      title: "Conexão com Webhook Falhou",
      message: "Webhook N8N 'backup-vault' timed out",
      source: "integrations",
      created_at: new Date().toISOString(),
      read: false,
    },
  ];

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
      } catch {} finally {
        setWfLoading(false);
      }
    };
    fetchDlq();
    const interval = setInterval(fetchDlq, 15_000);
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
    } catch {} finally {
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
        const runningNames = Object.values(data.instances || {}).map((inst: any) => inst.name);
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

  const activeAlerts = notifications.length > 0 ? notifications : fallbackAlerts;
  const isSimulatedAlerts = notifications.length === 0;

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
          value={`${runtime.vramUsed.toFixed(1)} / ${runtime.vramTotal}GB`}
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

        {/* Agent Monitor */}
        <Card className="flex flex-col border border-border-subtle bg-surface/30 min-h-[220px]">
          <CardHeader className="pb-2 border-b border-border-subtle flex flex-row items-center justify-between">
            <CardTitle className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-text-primary">
              <Bot className="h-4 w-4 text-accent-neon" />
              Agent core Status
            </CardTitle>
            <Badge
              variant="neutral"
              className="text-[9px] bg-amber-500/10 text-amber-500 border border-amber-500/20 font-mono tracking-wider"
            >
              SIMULATED
            </Badge>
          </CardHeader>
          <CardContent className="flex-1 min-h-0 p-3 space-y-2 overflow-y-auto">
            {agents.map((agent) => {
              const isActive = agent.status === "active";
              const indicatorColor = isActive ? "bg-success" : "bg-text-dim";

              return (
                <div
                  key={agent.name}
                  className={`flex items-center justify-between p-3 border border-border-subtle rounded-lg bg-canvas/30 transition-all ${
                    isActive ? "border-accent-neon/30 bg-accent-neon/5" : ""
                  }`}
                >
                  <div className="flex items-start gap-3 min-w-0">
                    <div className="relative mt-1">
                      <span
                        className={`h-2.5 w-2.5 rounded-full block ${indicatorColor} ${isActive ? "animate-pulse" : ""}`}
                      />
                      {isActive && (
                        <span className="absolute inset-0 rounded-full bg-success animate-ping opacity-75" />
                      )}
                    </div>
                    <div className="min-w-0">
                      <p className="text-xs font-bold text-text-primary">{agent.name}</p>
                      <p className="text-[10px] text-text-muted mt-0.5">{agent.role}</p>
                      <span className="text-[10px] text-accent-neon block mt-1 truncate">
                        {agent.activity}
                      </span>
                    </div>
                  </div>
                  <Badge
                    variant={isActive ? "success" : "neutral"}
                    className="text-[9px] py-0 px-1 font-mono uppercase tracking-wider"
                  >
                    {agent.status}
                  </Badge>
                </div>
              );
            })}
          </CardContent>
        </Card>

        {/* Active System Alerts */}
        <Card className="flex flex-col border border-border-subtle bg-surface/30 min-h-[220px]">
          <CardHeader className="pb-2 border-b border-border-subtle flex flex-row items-center justify-between">
            <CardTitle className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-text-primary">
              <AlertCircle className="h-4 w-4 text-accent-neon" />
              Active System Alerts
            </CardTitle>
            {isSimulatedAlerts && (
              <Badge
                variant="neutral"
                className="text-[9px] bg-amber-500/10 text-amber-500 border border-amber-500/20 font-mono tracking-wider"
              >
                SIMULATED
              </Badge>
            )}
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
