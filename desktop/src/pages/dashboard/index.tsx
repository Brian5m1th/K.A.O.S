import { useEffect, useState, useRef } from "react";
import { useSystemStore, useAuthStore } from "@/shared/lib/stores";
import { useSystemMetrics } from "@/features/dashboard/hooks/useSystemMetrics";
import { kaosFetch } from "@/shared/api/kaos-client";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Badge } from "@/shared/ui/badge";
import { Sparkline } from "@/shared/ui/sparkline";
import { Cpu, MemoryStick, Gauge, Database, Bot, Activity, Loader2, Terminal } from "lucide-react";

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
          <div className="flex items-center gap-1.5 text-text-muted text-xs mb-2">{icon}<span>{label}</span></div>
          <Loader2 className="h-4 w-4 animate-spin text-text-dim" />
        </CardContent>
      </Card>
    );
  }
  if (state === "offline") {
    return (
      <Card className="border border-border-subtle bg-surface/50">
        <CardContent className="p-3">
          <div className="flex items-center gap-1.5 text-text-muted text-xs mb-2">{icon}<span>{label}</span></div>
          <p className="text-xs text-text-dim">—</p>
        </CardContent>
      </Card>
    );
  }
  if (state === "empty") {
    return (
      <Card className="border border-border-subtle bg-surface/50">
        <CardContent className="p-3">
          <div className="flex items-center gap-1.5 text-text-muted text-xs mb-2">{icon}<span>{label}</span></div>
          <p className="text-lg font-semibold text-text-primary font-mono">—</p>
        </CardContent>
      </Card>
    );
  }
  return (
    <Card className="border border-border-subtle bg-surface/50 hover:bg-surface transition-colors shadow-md backdrop-blur-sm">
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
  const logsEndRef = useRef<HTMLDivElement>(null);

  // Active agents state list
  const [agents, setAgents] = useState<AgentItem[]>([
    { name: "kaos-architect", role: "Arquitetura & SDD", status: "active", activity: "Analisando dependências..." },
    { name: "kaos-auditor", role: "Drift & KIRL Verification", status: "idle", activity: "Aguardando novos commits" },
    { name: "kaos-coder", role: "Code Generation", status: "idle", activity: "Aguardando tarefas" }
  ]);

  // System logs rolling state
  const [sysLogs, setSysLogs] = useState<string[]>([
    "INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)",
    "INFO: Connecting to Qdrant vector database at localhost:6333",
    "INFO: Qdrant client connected successfully. Collection 'kaos' ready.",
    "INFO: PostgreSQL asyncpg pool initialized, size=20",
    "INFO: LangGraph compilation completed successfully. 12 nodes, 8 edges registered."
  ]);

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

  // Simulate sys logs
  useEffect(() => {
    const templates = [
      "INFO: [smart_router] Classified query intent as RAG workflow",
      "INFO: [qdrant] Similarity query executed in 14ms",
      "DEBUG: [cost_tracker] Accumulated session cost updated, total=0.0034 USD",
      "INFO: [kirl] Drift scan completed, no significant drifts found",
      "INFO: [ollama] Local model tags fetched, active: qwen2.5:latest",
      "INFO: [mcp_manager] Tool execution request: filesystem_read_file",
      "INFO: [memory] smart context window injected in system prompt"
    ];

    const sysLogInterval = setInterval(() => {
      const randomTpl = templates[Math.floor(Math.random() * templates.length)];
      setSysLogs((prev) => [...prev.slice(-8), randomTpl]);
    }, 5000);

    return () => clearInterval(sysLogInterval);
  }, []);

  // Simulate agent active toggling
  useEffect(() => {
    const agentInterval = setInterval(() => {
      setAgents((prev) =>
        prev.map((agent) => {
          if (agent.name === "kaos-coder") {
            const isNowActive = Math.random() > 0.5;
            return {
              ...agent,
              status: isNowActive ? "active" : "idle",
              activity: isNowActive ? "Gerando testes unitários..." : "Aguardando tarefas"
            };
          }
          if (agent.name === "kaos-architect") {
            const isNowIdle = Math.random() > 0.7;
            return {
              ...agent,
              status: isNowIdle ? "idle" : "active",
              activity: isNowIdle ? "Aguardando trigger" : "Analisando estrutura do código..."
            };
          }
          return agent;
        })
      );
    }, 6000);

    return () => clearInterval(agentInterval);
  }, []);

  // Auto scroll logs
  useEffect(() => {
    logsEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [sysLogs]);

  const sysState: PanelState = history.cpu.length === 0 && !isOnline ? "loading" : isOnline ? "online" : "offline";

  return (
    <div className="flex h-full flex-col gap-4 p-4 overflow-y-auto bg-canvas text-text-primary">
      {/* Status bar */}
      <div className="flex items-center gap-2">
        <Badge variant={status === "online" ? "success" : status === "degraded" ? "warning" : "error"} className="animate-pulse">
          {status === "online" ? "ONLINE" : status === "degraded" ? "DEGRADED" : "OFFLINE"}
        </Badge>
        <span className="text-[11px] text-text-dim font-medium">
          {status === "online" ? "Todos os serviços do K.A.O.S estão rodando" : status === "degraded" ? "Serviço parcial degradado" : "Conexão com o backend falhou"}
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
        {/* Active/Failed Workflows */}
        <Card className="flex flex-col border border-border-subtle bg-surface/30">
          <CardHeader className="pb-2 border-b border-border-subtle">
            <CardTitle className="flex items-center gap-2 text-sm font-semibold">
              <Activity className="h-4 w-4 text-accent-primary" />
              Active / Dead-Letter Workflows
            </CardTitle>
          </CardHeader>
          <CardContent className="flex-1 min-h-0 px-4 py-3 overflow-y-auto">
            {!isOnline ? (
              <p className="text-xs text-text-dim py-4 text-center">System offline — connect to backend to view workflows</p>
            ) : wfLoading ? (
              <div className="flex items-center justify-center py-8"><Loader2 className="h-4 w-4 animate-spin text-text-dim" /></div>
            ) : dlqItems.length === 0 ? (
              <div className="flex flex-col items-center justify-center h-full text-text-dim text-xs py-8">
                No failed workflows in Dead-Letter Queue
              </div>
            ) : (
              <div className="flex flex-col gap-2">
                {dlqItems.map((item) => (
                  <div key={item.id} className="flex items-center justify-between rounded-lg border border-border-subtle bg-canvas/50 px-3 py-2">
                    <span className="text-xs font-medium text-text-primary">{item.workflow_name}</span>
                    <div className="flex items-center gap-2">
                      <span className="text-[10px] text-text-dim font-mono">{item.error?.slice(0, 30)}...</span>
                      <Badge variant="error">FAILED</Badge>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </CardContent>
        </Card>

        {/* Agent Monitor (Dynamic) */}
        <Card className="flex flex-col border border-border-subtle bg-surface/30">
          <CardHeader className="pb-2 border-b border-border-subtle">
            <CardTitle className="flex items-center gap-2 text-sm font-semibold">
              <Bot className="h-4 w-4 text-accent-neon" />
              Agent Core Status
            </CardTitle>
          </CardHeader>
          <CardContent className="flex-1 min-h-0 p-3 space-y-2 overflow-y-auto">
            {agents.map((agent) => {
              const isActive = agent.status === "active";
              const indicatorColor = isActive ? "bg-success" : "bg-text-dim";
              
              return (
                <div key={agent.name} className={`flex items-center justify-between p-3 border border-border-subtle rounded-lg bg-canvas/30 transition-all ${isActive ? "border-accent-neon/30 bg-accent-neon/5" : ""}`}>
                  <div className="flex items-start gap-3 min-w-0">
                    <div className="relative mt-1">
                      <span className={`h-2.5 w-2.5 rounded-full block ${indicatorColor} ${isActive ? "animate-pulse" : ""}`} />
                      {isActive && <span className="absolute inset-0 rounded-full bg-success animate-ping opacity-75" />}
                    </div>
                    <div className="min-w-0">
                      <p className="text-xs font-bold text-text-primary">{agent.name}</p>
                      <p className="text-[10px] text-text-muted mt-0.5">{agent.role}</p>
                      <span className="text-[10px] text-accent-neon block mt-1 truncate">{agent.activity}</span>
                    </div>
                  </div>
                  <Badge variant={isActive ? "success" : "neutral"} className="text-[9px] py-0 px-1 font-mono uppercase tracking-wider">
                    {agent.status}
                  </Badge>
                </div>
              );
            })}
          </CardContent>
        </Card>
      </div>

      {/* Bottom: Terminal System Log */}
      <Card className="h-40 shrink-0 border border-border-subtle bg-surface/30 flex flex-col">
        <CardHeader className="pb-1 pt-2 border-b border-border-subtle">
          <CardTitle className="flex items-center gap-2 text-xs font-semibold text-text-muted uppercase tracking-wider">
            <Terminal className="w-3.5 h-3.5 text-accent-primary" />
            Live System Log
          </CardTitle>
        </CardHeader>
        <CardContent className="p-2 bg-canvas/60 overflow-y-auto flex-1 font-mono text-[10px] text-text-muted space-y-1 select-text scrollbar-thin">
          {sysLogs.map((log, idx) => (
            <div key={idx} className="hover:bg-surface/20 px-1 rounded transition-colors text-accent-primary">
              {log}
            </div>
          ))}
          <div ref={logsEndRef} />
        </CardContent>
      </Card>
    </div>
  );
}
