import { useState, useEffect, useRef } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Badge } from "@/shared/ui/badge";
import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";
import { Textarea } from "@/shared/ui/textarea";
import { Tabs } from "@/shared/ui/tabs";
import { EmptyState } from "@/shared/ui/empty-state";
import { Dialog } from "@/shared/ui/dialog";
import { MessageBubble } from "@/entities/message/ui/MessageBubble";
import { ScrollArea } from "@/shared/ui/scroll-area";
import { motion, AnimatePresence } from "framer-motion";
import { useAgentStore, type AgentConfig, type AgentStatus } from "@/shared/lib/stores";
import { Bot, MessageSquare, Play, Square, RotateCcw, Plus, Send, Loader2 } from "lucide-react";
import { kaosFetch } from "@/shared/api/kaos-client";

const AGENT_STATUS_MAP: Record<
  AgentStatus,
  { variant: "success" | "info" | "warning" | "error" | "neutral"; label: string }
> = {
  idle: { variant: "neutral", label: "IDLE" },
  starting: { variant: "info", label: "STARTING" },
  running: { variant: "success", label: "RUNNING" },
  paused: { variant: "warning", label: "PAUSED" },
  error: { variant: "error", label: "ERROR" },
  stopped: { variant: "neutral", label: "STOPPED" },
};

const DEFAULT_AGENTS: AgentConfig[] = [
  {
    id: "memory",
    name: "Memory Agent",
    model: "qwen2.5-7b",
    systemPrompt: "Consolidate and retrieve information from the knowledge vault.",
    temperature: 0.3,
    topP: 0.9,
  },
  {
    id: "code-reviewer",
    name: "Code Reviewer",
    model: "llama3.3-70b",
    systemPrompt: "Review code changes for bugs, style, and security issues.",
    temperature: 0.1,
    topP: 0.9,
  },
  {
    id: "research",
    name: "Research Bot",
    model: "mixtral-8x7b",
    systemPrompt: "Search and summarize information from the web and local documents.",
    temperature: 0.7,
    topP: 0.95,
  },
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

  // New Agent Form States
  const [newAgentOpen, setNewAgentOpen] = useState(false);
  const [newAgentName, setNewAgentName] = useState("");
  const [newAgentModel, setNewAgentModel] = useState("qwen3:14b");
  const [newAgentPrompt, setNewAgentPrompt] = useState("");
  const [newAgentTemp, setNewAgentTemp] = useState(0.7);
  const [newAgentTopP, setNewAgentTopP] = useState(0.9);

  // Playground Chat States
  const [chatInput, setChatInput] = useState("");
  const [chatMessages, setChatMessages] = useState<
    Array<{ role: "user" | "assistant" | "system"; content: string }>
  >([]);
  const [chatLoading, setChatLoading] = useState(false);
  const chatEndRef = useRef<HTMLDivElement>(null);

  // Register real agents from backend on mount
  useEffect(() => {
    const fetchOpenCodeAgents = async () => {
      try {
        const res = await kaosFetch("/api/opencode/agents", "");
        if (res.ok) {
          const data = await res.json();
          const list = data.agents || [];

          if (list.length === 0) {
            // Fallback to default mock agents if no agents are found on backend
            DEFAULT_AGENTS.forEach((cfg) => {
              if (!agents[cfg.id]) register(cfg);
            });
            return;
          }

          for (const a of list) {
            try {
              const detailRes = await kaosFetch(`/api/opencode/agent/${a.id}`, "");
              if (detailRes.ok) {
                const detail = await detailRes.json();
                const content = detail.content || "";

                // Parse name from heading or fallback to file name
                const nameLine = content
                  .split("\n")
                  .find((line: string) => line.trim().startsWith("# "));
                const name = nameLine ? nameLine.replace(/^#\s+/, "").trim() : a.name;

                const agentCfg: AgentConfig = {
                  id: a.id,
                  name: name,
                  model: "qwen3:14b",
                  systemPrompt: content,
                  temperature: 0.1,
                  topP: 0.9,
                };
                register(agentCfg);
              }
            } catch (err) {
              console.error("Failed to load agent detail:", a.id, err);
            }
          }
        } else {
          // Fallback on HTTP error
          DEFAULT_AGENTS.forEach((cfg) => {
            if (!agents[cfg.id]) register(cfg);
          });
        }
      } catch (err) {
        console.error("Failed to fetch opencode agents:", err);
        // Fallback on connect error
        DEFAULT_AGENTS.forEach((cfg) => {
          if (!agents[cfg.id]) register(cfg);
        });
      }
    };
    fetchOpenCodeAgents();
  }, [register]);

  const selectedAgent = selectedId ? agents[selectedId] : null;

  useEffect(() => {
    if (selectedAgent) setSystemPrompt(selectedAgent.config.systemPrompt);
  }, [selectedAgent]);

  // Reset/Initialize Playground messages when active agent changes
  useEffect(() => {
    if (selectedAgent) {
      setChatMessages([
        {
          role: "system",
          content: selectedAgent.config.systemPrompt,
        },
        {
          role: "assistant",
          content: `Olá! Eu sou o ${selectedAgent.config.name}. Como posso ajudar você hoje no Playground?`,
        },
      ]);
    } else {
      setChatMessages([]);
    }
  }, [selectedId, activeTab]);

  // Scroll to bottom of chat
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chatMessages]);

  const handleSavePrompt = () => {
    if (selectedId) updateConfig(selectedId, { systemPrompt });
  };

  const handleCreateAgent = () => {
    if (!newAgentName.trim()) return;
    const id = newAgentName.toLowerCase().replace(/\s+/g, "-");
    const agentCfg: AgentConfig = {
      id,
      name: newAgentName,
      model: newAgentModel,
      systemPrompt: newAgentPrompt,
      temperature: newAgentTemp,
      topP: newAgentTopP,
    };
    register(agentCfg);
    setNewAgentOpen(false);
    setSelectedId(id);

    // Reset Form
    setNewAgentName("");
    setNewAgentModel("qwen3:14b");
    setNewAgentPrompt("");
    setNewAgentTemp(0.7);
    setNewAgentTopP(0.9);
  };

  const handleSendPlayground = async () => {
    if (!chatInput.trim() || chatLoading || !selectedId || !selectedAgent) return;

    const userMessageText = chatInput.trim();
    const newUserMsg = { role: "user" as const, content: userMessageText };
    const updatedMessages = [...chatMessages, newUserMsg];

    setChatMessages(updatedMessages);
    setChatInput("");
    setChatLoading(true);

    try {
      const payload = {
        session_id: `playground-${selectedId}`,
        message: userMessageText,
        history: updatedMessages.slice(0, -1).map((m) => ({
          role: m.role,
          content: m.content,
        })),
        user_id: "playground-user",
        role: "user",
      };

      const res = await kaosFetch("/api/chat/message", "", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      if (res.ok) {
        const reader = res.body?.getReader();
        if (reader) {
          const decoder = new TextDecoder();
          let assistantText = "";

          setChatMessages((prev) => [...prev, { role: "assistant", content: "" }]);

          while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            const chunk = decoder.decode(value, { stream: true });
            assistantText += chunk;
            setChatMessages((prev) => {
              const next = [...prev];
              if (next.length > 0) {
                next[next.length - 1] = { role: "assistant", content: assistantText };
              }
              return next;
            });
          }
        } else {
          const text = await res.text();
          setChatMessages((prev) => [...prev, { role: "assistant", content: text }]);
        }
      } else {
        setChatMessages((prev) => [
          ...prev,
          { role: "assistant", content: `Erro na comunicação com o backend (HTTP ${res.status}).` },
        ]);
      }
    } catch (err) {
      console.error(err);
      setChatMessages((prev) => [
        ...prev,
        { role: "assistant", content: "Falha de conexão. O servidor backend está rodando?" },
      ]);
    } finally {
      setChatLoading(false);
    }
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
          <p className="text-xs text-text-muted mt-0.5">
            Runtime de agentes de IA — {Object.keys(agents).length} ativos
          </p>
        </div>
        <Button variant="primary" size="sm" onClick={() => setNewAgentOpen(true)}>
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
                <button
                  key={agent.config.id}
                  onClick={() => setSelectedId(agent.config.id)}
                  className={`flex items-center gap-3 rounded-lg border p-3 text-left transition-all outline-none ${
                    selectedId === agent.config.id
                      ? "border-accent-primary bg-accent-primary/5"
                      : "border-border-subtle bg-surface hover:border-border-hover"
                  }`}
                >
                  <div
                    className={`rounded-lg p-2 ${
                      isRunning ? "bg-accent-neon/10" : "bg-bg-active"
                    }`}
                  >
                    <Bot
                      className={`h-4 w-4 ${isRunning ? "text-accent-neon animate-pulse" : "text-text-muted"}`}
                    />
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="text-sm font-medium text-text-primary truncate">
                      {agent.config.name}
                    </p>
                    <p className="text-[11px] text-text-dim font-mono truncate">
                      {agent.config.model}
                    </p>
                  </div>
                  {statusBadge(agent.status)}
                </button>
              );
            })}
          </div>

          {/* Config Panel */}
          <AnimatePresence mode="wait">
            {selectedAgent ? (
              <motion.div
                key={selectedAgent.config.id}
                initial={{ opacity: 0, y: 5 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -5 }}
                className="flex-1 flex flex-col gap-3 min-h-0 overflow-y-auto"
              >
                <Card>
                  <CardHeader className="pb-2 border-b border-border-subtle/50">
                    <div className="flex items-center justify-between">
                      <CardTitle className="text-sm">{selectedAgent.config.name}</CardTitle>
                      {statusBadge(selectedAgent.status)}
                    </div>
                  </CardHeader>
                  <CardContent className="space-y-4 pt-4">
                    <div>
                      <label className="mb-1.5 block text-xs font-semibold text-text-muted">
                        System Prompt
                      </label>
                      <Textarea
                        value={systemPrompt}
                        onChange={(e) => setSystemPrompt(e.target.value)}
                        className="min-h-[140px] text-xs font-mono"
                      />
                    </div>
                    <div className="grid grid-cols-2 gap-3">
                      <div>
                        <label className="mb-1.5 block text-xs font-semibold text-text-muted">
                          Temperature
                        </label>
                        <Input
                          type="number"
                          min="0"
                          max="2"
                          step="0.1"
                          value={selectedAgent.config.temperature}
                          onChange={(e) =>
                            updateConfig(selectedAgent.config.id, {
                              temperature: parseFloat(e.target.value),
                            })
                          }
                          className="font-mono"
                        />
                      </div>
                      <div>
                        <label className="mb-1.5 block text-xs font-semibold text-text-muted">
                          Top-P
                        </label>
                        <Input
                          type="number"
                          min="0"
                          max="1"
                          step="0.05"
                          value={selectedAgent.config.topP}
                          onChange={(e) =>
                            updateConfig(selectedAgent.config.id, {
                              topP: parseFloat(e.target.value),
                            })
                          }
                          className="font-mono"
                        />
                      </div>
                    </div>
                    <div className="flex gap-2 pt-2">
                      <Button variant="primary" size="sm" onClick={handleSavePrompt}>
                        Save Configuration
                      </Button>
                      {selectedAgent.status === "idle" || selectedAgent.status === "stopped" ? (
                        <Button
                          variant="subtle"
                          size="sm"
                          onClick={() => start(selectedAgent.config.id)}
                        >
                          <Play className="h-3 w-3 mr-1.5" />
                          Start Agent
                        </Button>
                      ) : selectedAgent.status === "running" ||
                        selectedAgent.status === "starting" ? (
                        <>
                          <Button
                            variant="subtle"
                            size="sm"
                            onClick={() => pause(selectedAgent.config.id)}
                          >
                            <Square className="h-3 w-3 mr-1.5" />
                            Pause
                          </Button>
                          <Button
                            variant="danger"
                            size="sm"
                            onClick={() => stop(selectedAgent.config.id)}
                          >
                            <Square className="h-3 w-3 mr-1.5" />
                            Stop
                          </Button>
                        </>
                      ) : selectedAgent.status === "paused" ? (
                        <Button
                          variant="subtle"
                          size="sm"
                          onClick={() => resume(selectedAgent.config.id)}
                        >
                          <RotateCcw className="h-3 w-3 mr-1.5" />
                          Resume
                        </Button>
                      ) : null}
                      {selectedAgent.status === "error" && (
                        <Button
                          variant="subtle"
                          size="sm"
                          onClick={() => start(selectedAgent.config.id)}
                        >
                          <RotateCcw className="h-3 w-3 mr-1.5" />
                          Restart
                        </Button>
                      )}
                    </div>
                  </CardContent>
                </Card>
                {selectedAgent.error && (
                  <Card className="border-error/30 bg-error/5">
                    <CardContent className="p-3">
                      <p className="text-xs text-error font-mono">{selectedAgent.error}</p>
                    </CardContent>
                  </Card>
                )}
              </motion.div>
            ) : (
              <div className="flex-1 flex items-center justify-center">
                <EmptyState
                  icon={<Bot className="h-6 w-6" />}
                  title="Select an agent to configure"
                  description="Choose one of the active agent models on the sidebar list to modify details or initiate its runtime."
                />
              </div>
            )}
          </AnimatePresence>
        </div>
      )}

      {activeTab === "playground" && (
        <div className="flex-1 flex flex-col min-h-0 border border-border-subtle bg-surface-raised/40 rounded-xl overflow-hidden shadow-sm">
          {!selectedAgent ? (
            <div className="flex-1 flex items-center justify-center p-8">
              <EmptyState
                icon={<MessageSquare className="h-6 w-6" />}
                title="Playground Inativo"
                description="Selecione um agente na aba 'Agents' primeiro e certifique-se de que ele está em execução."
              />
            </div>
          ) : selectedAgent.status !== "running" ? (
            <div className="flex-1 flex items-center justify-center p-8">
              <EmptyState
                icon={<Play className="h-6 w-6" />}
                title="Agente inativo"
                description={`O agente ${selectedAgent.config.name} está no estado: ${selectedAgent.status.toUpperCase()}. Inicie o agente para testá-lo no playground.`}
                action={
                  <Button variant="primary" size="sm" onClick={() => start(selectedAgent.config.id)}>
                    <Play className="h-3.5 w-3.5 mr-1.5" />
                    Iniciar {selectedAgent.config.name}
                  </Button>
                }
              />
            </div>
          ) : (
            /* Active Chat Interface */
            <div className="flex-1 flex flex-col min-h-0 bg-surface">
              {/* Chat Header */}
              <div className="flex items-center justify-between border-b border-border-subtle px-4 py-2.5 bg-surface-raised/50">
                <div className="flex items-center gap-2">
                  <Bot className="h-4 w-4 text-accent-neon animate-pulse" />
                  <span className="text-xs font-semibold text-text-primary">
                    Playground: {selectedAgent.config.name}
                  </span>
                </div>
                <div className="flex items-center gap-1.5">
                  <span className="h-1.5 w-1.5 rounded-full bg-accent-primary animate-ping" />
                  <span className="text-[10px] text-accent-primary font-semibold font-mono">
                    CONNECTED
                  </span>
                </div>
              </div>

              {/* Chat Message Window */}
              <ScrollArea className="flex-1 p-4">
                <div className="space-y-4 max-w-3xl mx-auto">
                  {chatMessages
                    .filter((msg) => msg.role !== "system")
                    .map((msg, index) => (
                      <MessageBubble
                        key={index}
                        message={{
                          role: msg.role === "user" ? "user" : "assistant",
                          text: msg.content,
                        }}
                        isLast={index === chatMessages.length - 2} // -2 because of system role filtered out
                      />
                    ))}
                  {chatLoading && (
                    <div className="flex items-center gap-2 text-xs text-text-dim font-mono mt-2 pl-2">
                      <Loader2 className="h-3 w-3 animate-spin text-accent-neon" />
                      <span>{selectedAgent.config.name} is streaming...</span>
                    </div>
                  )}
                  <div ref={chatEndRef} />
                </div>
              </ScrollArea>

              {/* Chat Input Area */}
              <div className="p-3 border-t border-border-subtle bg-surface-raised/30">
                <div className="max-w-3xl mx-auto flex gap-2">
                  <Input
                    value={chatInput}
                    onChange={(e) => setChatInput(e.target.value)}
                    placeholder={`Conversar com ${selectedAgent.config.name}...`}
                    className="flex-1 bg-surface-elevated text-xs border-border-subtle"
                    onKeyDown={(e) => {
                      if (e.key === "Enter" && !e.shiftKey) {
                        e.preventDefault();
                        handleSendPlayground();
                      }
                    }}
                    disabled={chatLoading}
                  />
                  <Button
                    variant="primary"
                    size="sm"
                    className="shrink-0"
                    onClick={handleSendPlayground}
                    disabled={chatLoading || !chatInput.trim()}
                  >
                    {chatLoading ? (
                      <Loader2 className="h-3.5 w-3.5 animate-spin" />
                    ) : (
                      <Send className="h-3.5 w-3.5" />
                    )}
                  </Button>
                </div>
              </div>
            </div>
          )}
        </div>
      )}

      {/* New Agent Modal */}
      <Dialog
        open={newAgentOpen}
        onClose={() => setNewAgentOpen(false)}
        title="Create New AI Agent"
        className="max-w-md"
      >
        <div className="space-y-4 pt-2">
          <div>
            <label className="mb-1.5 block text-xs font-semibold text-text-muted">
              Agent Name
            </label>
            <Input
              value={newAgentName}
              onChange={(e) => setNewAgentName(e.target.value)}
              placeholder="e.g. Architect Bot, Analyst, QA Helper"
              className="text-xs"
            />
          </div>

          <div>
            <label className="mb-1.5 block text-xs font-semibold text-text-muted">
              AI Model Select
            </label>
            <select
              value={newAgentModel}
              onChange={(e) => setNewAgentModel(e.target.value)}
              className="w-full rounded-lg border border-border-subtle bg-surface-elevated px-3 py-2 text-xs text-text-primary focus:border-accent-primary focus:outline-none focus:ring-1 focus:ring-accent-primary/20 transition-all font-mono"
            >
              <option value="qwen3:14b">qwen3:14b (Default)</option>
              <option value="llama3.3-70b">llama3.3-70b (High Reasoning)</option>
              <option value="qwen2.5-7b">qwen2.5-7b (Fast Chat)</option>
              <option value="mixtral-8x7b">mixtral-8x7b (Deep Context)</option>
              <option value="deepseek-r1:14b">deepseek-r1:14b (Advanced Thinker)</option>
            </select>
          </div>

          <div>
            <label className="mb-1.5 block text-xs font-semibold text-text-muted">
              System Instruction / Prompt
            </label>
            <Textarea
              value={newAgentPrompt}
              onChange={(e) => setNewAgentPrompt(e.target.value)}
              placeholder="You are an expert assistant designed to..."
              className="min-h-[100px] text-xs font-mono"
            />
          </div>

          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="mb-1.5 block text-xs font-semibold text-text-muted">
                Temperature
              </label>
              <Input
                type="number"
                min="0"
                max="2"
                step="0.1"
                value={newAgentTemp}
                onChange={(e) => setNewAgentTemp(parseFloat(e.target.value))}
                className="font-mono text-xs"
              />
            </div>
            <div>
              <label className="mb-1.5 block text-xs font-semibold text-text-muted">
                Top-P
              </label>
              <Input
                type="number"
                min="0"
                max="1"
                step="0.05"
                value={newAgentTopP}
                onChange={(e) => setNewAgentTopP(parseFloat(e.target.value))}
                className="font-mono text-xs"
              />
            </div>
          </div>

          <div className="flex justify-end gap-2 pt-2 border-t border-border-subtle/50 mt-6">
            <Button variant="subtle" size="sm" onClick={() => setNewAgentOpen(false)}>
              Cancel
            </Button>
            <Button
              variant="primary"
              size="sm"
              onClick={handleCreateAgent}
              disabled={!newAgentName.trim()}
            >
              Register Agent
            </Button>
          </div>
        </div>
      </Dialog>
    </div>
  );
}
