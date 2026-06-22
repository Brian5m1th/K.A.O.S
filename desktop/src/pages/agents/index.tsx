import { useState, useEffect } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Badge } from "@/shared/ui/badge";
import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";
import { Textarea } from "@/shared/ui/textarea";
import { Tabs } from "@/shared/ui/tabs";
import { motion, AnimatePresence } from "framer-motion";
import { useAgentStore, type AgentConfig, type AgentStatus } from "@/shared/lib/stores";
import { Bot, MessageSquare, Play, Square, RotateCcw, Plus } from "lucide-react";

const AGENT_STATUS_MAP: Record<AgentStatus, { variant: "success" | "info" | "warning" | "error" | "neutral"; label: string }> = {
  idle: { variant: "neutral", label: "IDLE" },
  starting: { variant: "info", label: "STARTING" },
  running: { variant: "success", label: "RUNNING" },
  paused: { variant: "warning", label: "PAUSED" },
  error: { variant: "error", label: "ERROR" },
  stopped: { variant: "neutral", label: "STOPPED" },
};

const DEFAULT_AGENTS: AgentConfig[] = [
  { id: "memory", name: "Memory Agent", model: "qwen2.5-7b", systemPrompt: "Consolidate and retrieve information from the knowledge vault.", temperature: 0.3, topP: 0.9 },
  { id: "code-reviewer", name: "Code Reviewer", model: "llama3.3-70b", systemPrompt: "Review code changes for bugs, style, and security issues.", temperature: 0.1, topP: 0.9 },
  { id: "research", name: "Research Bot", model: "mixtral-8x7b", systemPrompt: "Search and summarize information from the web and local documents.", temperature: 0.7, topP: 0.95 },
];

const AGENT_TABS = [
  { id: "agents", label: "Agents" },
  { id: "playground", label: "Playground" },
];

export default function AgentsPage() {
  const [activeTab, setActiveTab] = useState("agents");
  const [selectedId, setSelectedId] = useState<string | null>(null);

  const agents = useAgentStore((s) => s.agents);
  const register = useAgentStore((s) => s.register);
  const start = useAgentStore((s) => s.start);
  const stop = useAgentStore((s) => s.stop);
  const pause = useAgentStore((s) => s.pause);
  const resume = useAgentStore((s) => s.resume);
  const updateConfig = useAgentStore((s) => s.updateConfig);

  const [systemPrompt, setSystemPrompt] = useState("");

  // Register default agents on mount
  useEffect(() => {
    DEFAULT_AGENTS.forEach((cfg) => {
      if (!agents[cfg.id]) register(cfg);
    });
  }, []);

  const selectedAgent = selectedId ? agents[selectedId] : null;

  useEffect(() => {
    if (selectedAgent) setSystemPrompt(selectedAgent.config.systemPrompt);
  }, [selectedAgent]);

  const handleSavePrompt = () => {
    if (selectedId) updateConfig(selectedId, { systemPrompt });
  };

  const statusBadge = (status: AgentStatus) => {
    const s = AGENT_STATUS_MAP[status];
    return <Badge variant={s.variant}>{s.label}</Badge>;
  };

  return (
    <div className="flex h-full flex-col gap-4 p-4">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-base font-semibold text-text-primary">Agents</h1>
          <p className="text-xs text-text-muted mt-0.5">Runtime de agentes de IA — {Object.keys(agents).length} ativos</p>
        </div>
        <Button variant="primary" size="sm">
          <Plus className="h-3.5 w-3.5 mr-1.5" />
          New Agent
        </Button>
      </div>

      <Tabs tabs={AGENT_TABS} activeTab={activeTab} onTabChange={setActiveTab} />

      {activeTab === "agents" && (
        <div className="flex gap-4 flex-1 min-h-0">
          {/* Agent List */}
          <div className="w-72 shrink-0 flex flex-col gap-2 overflow-y-auto">
            {Object.values(agents).map((agent) => {
              const isRunning = agent.status === "running" || agent.status === "starting";
              return (
                <motion.button
                  key={agent.config.id}
                  layout
                  onClick={() => setSelectedId(agent.config.id)}
                  className={`flex items-center gap-3 rounded-lg border p-3 text-left transition-all ${
                    selectedId === agent.config.id
                      ? "border-accent-primary bg-accent-primary/5"
                      : "border-border-subtle bg-surface hover:border-border-hover hover:scale-[1.02]"
                  }`}
                >
                  <div className={`rounded-lg p-2 ${
                    isRunning ? "bg-accent-neon/10" : "bg-bg-active"
                  }`}>
                    <Bot className={`h-4 w-4 ${isRunning ? "text-accent-neon" : "text-text-muted"}`} />
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="text-sm font-medium text-text-primary truncate">{agent.config.name}</p>
                    <p className="text-[11px] text-text-dim font-mono truncate">{agent.config.model}</p>
                  </div>
                  {statusBadge(agent.status)}
                </motion.button>
              );
            })}
          </div>

          {/* Config Panel */}
          <AnimatePresence mode="wait">
            {selectedAgent ? (
              <motion.div
                key={selectedAgent.config.id}
                initial={{ opacity: 0, x: 10 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: -10 }}
                className="flex-1 flex flex-col gap-3"
              >
                <Card>
                  <CardHeader className="pb-2">
                    <div className="flex items-center justify-between">
                      <CardTitle className="text-sm">{selectedAgent.config.name}</CardTitle>
                      {statusBadge(selectedAgent.status)}
                    </div>
                  </CardHeader>
                  <CardContent className="space-y-4">
                    <div>
                      <label className="mb-1.5 block text-xs font-medium text-text-muted">System Prompt</label>
                      <Textarea
                        value={systemPrompt}
                        onChange={(e) => setSystemPrompt(e.target.value)}
                        className="min-h-[100px] text-xs font-mono"
                      />
                    </div>
                    <div className="grid grid-cols-2 gap-3">
                      <div>
                        <label className="mb-1.5 block text-xs font-medium text-text-muted">Temperature</label>
                        <Input
                          type="number" min="0" max="2" step="0.1"
                          value={selectedAgent.config.temperature}
                          onChange={(e) => updateConfig(selectedAgent.config.id, { temperature: parseFloat(e.target.value) })}
                          className="font-mono"
                        />
                      </div>
                      <div>
                        <label className="mb-1.5 block text-xs font-medium text-text-muted">Top-P</label>
                        <Input
                          type="number" min="0" max="1" step="0.05"
                          value={selectedAgent.config.topP}
                          onChange={(e) => updateConfig(selectedAgent.config.id, { topP: parseFloat(e.target.value) })}
                          className="font-mono"
                        />
                      </div>
                    </div>
                    <div className="flex gap-2">
                      <Button variant="primary" size="sm" onClick={handleSavePrompt}>Save</Button>
                      {selectedAgent.status === "idle" || selectedAgent.status === "stopped" ? (
                        <Button variant="secondary" size="sm" onClick={() => start(selectedAgent.config.id)}>
                          <Play className="h-3 w-3 mr-1.5" />
                          Start
                        </Button>
                      ) : selectedAgent.status === "running" || selectedAgent.status === "starting" ? (
                        <>
                          <Button variant="secondary" size="sm" onClick={() => pause(selectedAgent.config.id)}>
                            <Square className="h-3 w-3 mr-1.5" />
                            Pause
                          </Button>
                          <Button variant="danger" size="sm" onClick={() => stop(selectedAgent.config.id)}>
                            <Square className="h-3 w-3 mr-1.5" />
                            Stop
                          </Button>
                        </>
                      ) : selectedAgent.status === "paused" ? (
                        <Button variant="secondary" size="sm" onClick={() => resume(selectedAgent.config.id)}>
                          <RotateCcw className="h-3 w-3 mr-1.5" />
                          Resume
                        </Button>
                      ) : null}
                      {selectedAgent.status === "error" && (
                        <Button variant="secondary" size="sm" onClick={() => start(selectedAgent.config.id)}>
                          <RotateCcw className="h-3 w-3 mr-1.5" />
                          Restart
                        </Button>
                      )}
                    </div>
                  </CardContent>
                </Card>
                {selectedAgent.error && (
                  <Card className="border-error/30">
                    <CardContent className="p-3">
                      <p className="text-xs text-error font-mono">{selectedAgent.error}</p>
                    </CardContent>
                  </Card>
                )}
              </motion.div>
            ) : (
              <Card className="flex-1 flex items-center justify-center">
                <CardContent className="text-center text-text-muted p-8">
                  <Bot className="h-8 w-8 mx-auto mb-2 opacity-50" />
                  <p className="text-sm">Select an agent to configure</p>
                </CardContent>
              </Card>
            )}
          </AnimatePresence>
        </div>
      )}

      {activeTab === "playground" && (
        <Card className="flex-1 flex flex-col items-center justify-center text-text-muted p-8">
          <MessageSquare className="h-8 w-8 mb-2 opacity-50" />
          <p className="text-sm">Test your agents in real-time</p>
          <p className="text-xs mt-1">Select an agent and start a conversation</p>
          {selectedId && agents[selectedId] && (
            <Button variant="secondary" size="sm" className="mt-4" disabled={agents[selectedId].status !== "running"}>
              <MessageSquare className="h-3.5 w-3.5 mr-1.5" />
              Open Chat with {agents[selectedId].config.name}
            </Button>
          )}
        </Card>
      )}
    </div>
  );
}
