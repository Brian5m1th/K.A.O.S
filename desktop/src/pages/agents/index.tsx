import { useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Badge } from "@/shared/ui/badge";
import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";
import { Textarea } from "@/shared/ui/textarea";
import { Tabs } from "@/shared/ui/tabs";
import { Bot, Play, MessageSquare } from "lucide-react";

interface Agent {
  id: string;
  name: string;
  model: string;
  status: "active" | "inactive";
  temperature: number;
}

const MOCK_AGENTS: Agent[] = [
  { id: "1", name: "Memory Agent", model: "qwen2.5-7b", status: "active", temperature: 0.3 },
  { id: "2", name: "Code Reviewer", model: "llama3.3-70b", status: "active", temperature: 0.1 },
  { id: "3", name: "Research Bot", model: "mixtral-8x7b", status: "inactive", temperature: 0.7 },
];

const AGENT_TABS = [
  { id: "agents", label: "Agents" },
  { id: "playground", label: "Playground" },
];

export default function AgentsPage() {
  const [activeTab, setActiveTab] = useState("agents");
  const [selectedAgent, setSelectedAgent] = useState<Agent | null>(null);
  const [systemPrompt, setSystemPrompt] = useState("You are the operational core of KAOS. Respond in technical markdown format.");

  return (
    <div className="flex h-full flex-col gap-4 p-4">
      <div>
        <h1 className="text-base font-semibold text-text-primary">Agents</h1>
        <p className="text-xs text-text-muted mt-0.5">Gerenciamento de agentes e modelos de IA</p>
      </div>

      <Tabs tabs={AGENT_TABS} activeTab={activeTab} onTabChange={setActiveTab} />

      {activeTab === "agents" && (
        <div className="flex gap-4 flex-1 min-h-0">
          {/* Agent List */}
          <div className="w-72 shrink-0 flex flex-col gap-2">
            {MOCK_AGENTS.map((agent) => (
              <button
                key={agent.id}
                onClick={() => setSelectedAgent(agent)}
                className={`flex items-center gap-3 rounded-lg border p-3 text-left transition-colors ${
                  selectedAgent?.id === agent.id
                    ? "border-accent-primary bg-accent-primary/5"
                    : "border-border-subtle bg-surface hover:border-border-hover"
                }`}
              >
                <div className="rounded-lg bg-accent-neon/10 p-2">
                  <Bot className="h-4 w-4 text-accent-neon" />
                </div>
                <div className="flex-1 min-w-0">
                  <p className="text-sm font-medium text-text-primary truncate">{agent.name}</p>
                  <p className="text-[11px] text-text-dim font-mono truncate">{agent.model}</p>
                </div>
                <Badge variant={agent.status === "active" ? "success" : "neutral"}>
                  {agent.status}
                </Badge>
              </button>
            ))}
          </div>

          {/* Config Form */}
          <Card className="flex-1">
            <CardHeader>
              <CardTitle className="text-sm">
                {selectedAgent ? `Config: ${selectedAgent.name}` : "Select an agent"}
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div>
                <label className="mb-1.5 block text-xs font-medium text-text-muted">System Prompt</label>
                <Textarea
                  value={systemPrompt}
                  onChange={(e) => setSystemPrompt(e.target.value)}
                  className="min-h-[100px] text-xs font-mono"
                  placeholder="Define the agent's system prompt..."
                />
              </div>
              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="mb-1.5 block text-xs font-medium text-text-muted">Temperature</label>
                  <Input type="number" min="0" max="2" step="0.1" defaultValue="0.7" className="font-mono" />
                </div>
                <div>
                  <label className="mb-1.5 block text-xs font-medium text-text-muted">Top-P</label>
                  <Input type="number" min="0" max="1" step="0.05" defaultValue="0.9" className="font-mono" />
                </div>
              </div>
              <Button variant="primary" size="sm" disabled={!selectedAgent}>
                Save Configuration
              </Button>
            </CardContent>
          </Card>
        </div>
      )}

      {activeTab === "playground" && (
        <Card className="flex-1 flex flex-col">
          <CardContent className="flex-1 flex flex-col items-center justify-center text-text-muted p-8">
            <MessageSquare className="h-8 w-8 mb-2" />
            <p className="text-sm">Select an agent and type a message to test</p>
            <p className="text-xs mt-1">Chat interface will appear here</p>
            <Button variant="secondary" size="sm" className="mt-4" disabled={!selectedAgent}>
              <Play className="h-3.5 w-3.5 mr-1.5" />
              Start Test Chat
            </Button>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
