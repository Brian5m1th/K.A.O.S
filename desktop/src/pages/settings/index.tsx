import { useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";
import { Badge } from "@/shared/ui/badge";
import { Tabs } from "@/shared/ui/tabs";
import {
  Sun,
  Moon,
  Key,
  GitBranch,
  Workflow,
  Variable,
  RefreshCw,
  CheckCircle2,
} from "lucide-react";

const SETTINGS_TABS = [
  { id: "theme", label: "Theme" },
  { id: "providers", label: "AI Providers" },
  { id: "integrations", label: "Integrations" },
  { id: "env", label: "Environment" },
];

export default function SettingsPage() {
  const [activeTab, setActiveTab] = useState("theme");

  return (
    <div className="flex h-full flex-col gap-4 p-4">
      <div>
        <h1 className="text-base font-semibold text-text-primary">Settings</h1>
        <p className="text-xs text-text-muted mt-0.5">Configurações gerais do sistema</p>
      </div>

      <Tabs tabs={SETTINGS_TABS} activeTab={activeTab} onTabChange={setActiveTab} />

      {activeTab === "theme" && (
        <Card>
          <CardContent className="p-4 space-y-4">
            <p className="text-sm text-text-primary font-medium">Appearance</p>
            <div className="flex gap-3">
              <button className="flex flex-col items-center gap-2 rounded-lg border-2 border-accent-primary bg-canvas p-4">
                <Moon className="h-6 w-6 text-accent-primary" />
                <span className="text-xs text-text-primary">Dark</span>
              </button>
              <button className="flex flex-col items-center gap-2 rounded-lg border-2 border-border-subtle bg-canvas p-4 opacity-50">
                <Sun className="h-6 w-6 text-text-muted" />
                <span className="text-xs text-text-muted">Light</span>
              </button>
            </div>
            <div>
              <label className="mb-1.5 block text-xs font-medium text-text-muted">Accent Color</label>
              <div className="flex gap-2">
                {["#3B82F6", "#8B5CF6", "#10B981", "#F59E0B", "#EF4444"].map((color) => (
                  <button
                    key={color}
                    className="h-8 w-8 rounded-full border-2 border-border-subtle transition-transform hover:scale-110"
                    style={{ backgroundColor: color }}
                  />
                ))}
              </div>
            </div>
          </CardContent>
        </Card>
      )}

      {activeTab === "providers" && (
        <div className="grid grid-cols-2 gap-3">
          {["Ollama", "OpenAI", "Anthropic", "Google"].map((provider) => (
            <Card key={provider}>
              <CardContent className="p-4 space-y-3">
                <div className="flex items-center justify-between">
                  <h3 className="text-sm font-medium text-text-primary">{provider}</h3>
                  <Badge variant={provider === "Ollama" ? "success" : "neutral"}>
                    {provider === "Ollama" ? "Connected" : "Disabled"}
                  </Badge>
                </div>
                <Input placeholder="API URL" defaultValue={provider === "Ollama" ? "http://localhost:11434" : ""} className="text-xs" />
                <Input type="password" placeholder="API Key" className="text-xs" />
                <Input placeholder="Model" defaultValue={provider === "Ollama" ? "llama3.3-70b" : ""} className="text-xs" />
                <div className="flex gap-2">
                  <Button variant="secondary" size="sm" className="flex-1">
                    <RefreshCw className="h-3 w-3 mr-1" />
                    Test
                  </Button>
                  <Button variant="primary" size="sm" className="flex-1">
                    Save
                  </Button>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      )}

      {activeTab === "integrations" && (
        <Card>
          <CardContent className="p-4 space-y-3">
            {[
              { name: "GitHub", icon: GitBranch, desc: "CI/CD workflows and code review", status: "connected" },
              { name: "N8N", icon: Workflow, desc: "Workflow automation engine", status: "disconnected" },
              { name: "Qdrant", icon: Variable, desc: "Vector database for RAG", status: "connected" },
            ].map((integ) => {
              const Icon = integ.icon;
              return (
                <div key={integ.name} className="flex items-center justify-between rounded-lg border border-border-subtle bg-canvas/50 px-4 py-3">
                  <div className="flex items-center gap-3">
                    <div className="rounded-lg bg-bg-active p-2">
                      <Icon className="h-4 w-4 text-text-primary" />
                    </div>
                    <div>
                      <p className="text-sm font-medium text-text-primary">{integ.name}</p>
                      <p className="text-xs text-text-muted">{integ.desc}</p>
                    </div>
                  </div>
                  <div className="flex items-center gap-2">
                    <Badge variant={integ.status === "connected" ? "success" : "neutral"}>
                      {integ.status}
                    </Badge>
                    <Button variant="subtle" size="sm">Configure</Button>
                  </div>
                </div>
              );
            })}
          </CardContent>
        </Card>
      )}

      {activeTab === "env" && (
        <Card>
          <CardContent className="p-4 space-y-3">
            <div className="flex items-center justify-between">
              <p className="text-sm text-text-primary font-medium">Environment Variables</p>
              <Button variant="primary" size="sm">
                <Key className="h-3.5 w-3.5 mr-1" />
                Add Variable
              </Button>
            </div>
            <div className="space-y-2">
              {[
                { key: "KAOS_API_KEY", value: "sk-...****" },
                { key: "OLLAMA_HOST", value: "http://localhost:11434" },
                { key: "QDRANT_URL", value: "http://localhost:6333" },
                { key: "DOCS_PATH", value: "docs/" },
              ].map((env) => (
                <div key={env.key} className="flex items-center justify-between rounded-lg border border-border-subtle bg-canvas/50 px-3 py-2">
                  <div className="flex items-center gap-3">
                    <Variable className="h-3.5 w-3.5 text-text-dim" />
                    <span className="text-xs font-mono text-text-primary">{env.key}</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <span className="text-xs font-mono text-text-dim">{env.value}</span>
                    <Button variant="subtle" size="sm">Edit</Button>
                    <Button variant="danger" size="sm">Remove</Button>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
