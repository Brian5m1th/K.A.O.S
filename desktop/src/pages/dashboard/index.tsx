import { useEffect, useState } from "react";
import { useSystemStore } from "@/shared/lib/stores";
import { useSystemMetrics } from "@/features/dashboard/hooks/useSystemMetrics";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Badge } from "@/shared/ui/badge";
import { Sparkline } from "@/shared/ui/sparkline";
import { ScrollArea } from "@/shared/ui/scroll-area";
import { Cpu, MemoryStick, Gauge, Database, Bot, Activity } from "lucide-react";

interface Workflow {
  id: string;
  name: string;
  status: "running" | "success" | "failed" | "idle";
  runtime: string;
}

interface AgentActivity {
  id: string;
  name: string;
  intention: string;
  status: "active" | "idle" | "thinking";
}

const MOCK_WORKFLOWS: Workflow[] = [
  { id: "1", name: "RAG Pipeline v2", status: "running", runtime: "1m 23s" },
  { id: "2", name: "Code Review Agent", status: "success", runtime: "4m 12s" },
  { id: "3", name: "Weekly Report Gen", status: "idle", runtime: "—" },
  { id: "4", name: "Knowledge Sync", status: "failed", runtime: "0m 45s" },
];

const MOCK_AGENTS: AgentActivity[] = [
  { id: "1", name: "Memory Agent", intention: "Consolidating notes from Obsidian vault...", status: "active" },
  { id: "2", name: "Code Reviewer", intention: "Awaiting PR submission", status: "idle" },
  { id: "3", name: "Research Bot", intention: "Summarizing latest papers on RAG", status: "thinking" },
];

export default function DashboardPage() {
  const runtime = useSystemStore((s) => s.runtime);
  const metrics = useSystemStore((s) => s.metrics);
  const services = useSystemStore((s) => s.services);
  const status = useSystemStore((s) => s.status);
  const history = useSystemMetrics();

  const [logs, setLogs] = useState<string[]>([
    "[INFO] KAOS Core initialized",
    "[INFO] Ollama service detected: Llama 3.3-70b",
    "[INFO] Qdrant vector store connected",
  ]);

  useEffect(() => {
    const interval = setInterval(() => {
      const entries = [
        `[INFO] RAG search injected: ${Math.floor(Math.random() * 6 + 1)} chunks from vault`,
        `[INFO] LLM response init: model=${runtime.activeModel || "default"}, latency=${runtime.latency}ms`,
        `[DEBUG] VRAM buffering: ${runtime.vramUsed.toFixed(1)}GB used`,
        `[INFO] Vector count: ${metrics.vectorCount} indexed`,
      ];
      setLogs((prev) => [...prev.slice(-19), entries[Math.floor(Math.random() * entries.length)]]);
    }, 4000);

    return () => clearInterval(interval);
  }, [runtime, metrics]);

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
              {MOCK_WORKFLOWS.map((wf) => (
                <div
                  key={wf.id}
                  className="flex items-center justify-between rounded-lg border border-border-subtle bg-canvas/50 px-3 py-2 transition-colors hover:bg-bg-active"
                >
                  <div className="flex items-center gap-2">
                    <span className="text-xs font-medium text-text-primary">{wf.name}</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <span className="text-[11px] text-text-dim font-mono">{wf.runtime}</span>
                    <Badge
                      variant={
                        wf.status === "running" ? "info" :
                        wf.status === "success" ? "success" :
                        wf.status === "failed" ? "error" : "neutral"
                      }
                    >
                      {wf.status === "running" ? "RUNNING" :
                       wf.status === "success" ? "SUCCESS" :
                       wf.status === "failed" ? "FAILED" : "IDLE"}
                    </Badge>
                  </div>
                </div>
              ))}
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
              {MOCK_AGENTS.map((agent) => (
                <div
                  key={agent.id}
                  className="rounded-lg border border-border-subtle bg-canvas/50 px-3 py-2.5 transition-colors hover:bg-bg-active"
                >
                  <div className="flex items-center justify-between mb-1">
                    <div className="flex items-center gap-2">
                      <span
                        className={`h-1.5 w-1.5 rounded-full ${
                          agent.status === "active" ? "bg-success animate-pulse" :
                          agent.status === "thinking" ? "bg-accent-neon animate-pulse" :
                          "bg-text-dim"
                        }`}
                      />
                      <span className="text-xs font-medium text-text-primary">{agent.name}</span>
                    </div>
                    <Badge
                      variant={
                        agent.status === "active" ? "success" :
                        agent.status === "thinking" ? "info" : "neutral"
                      }
                    >
                      {agent.status.toUpperCase()}
                    </Badge>
                  </div>
                  <p className="text-[11px] text-text-muted pl-3.5 truncate">{agent.intention}</p>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Bottom: Logs */}
      <Card className="h-40 shrink-0">
        <CardHeader className="pb-1">
          <CardTitle className="text-xs font-semibold text-text-muted uppercase tracking-wider">
            System Log
          </CardTitle>
        </CardHeader>
        <CardContent className="p-0 px-4 pb-3">
          <ScrollArea className="h-24">
            <div className="font-mono text-[11px] leading-5">
              {logs.map((log, i) => {
                const level = log.includes("[ERROR]") ? "text-error" :
                              log.includes("[WARN]") ? "text-warning" :
                              log.includes("[DEBUG]") ? "text-text-dim" :
                              "text-text-muted";
                return (
                  <div key={i} className={level}>
                    {log}
                  </div>
                );
              })}
            </div>
          </ScrollArea>
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
