import { useEffect, useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";
import { Badge } from "@/shared/ui/badge";
import { Tabs } from "@/shared/ui/tabs";
import { kaosFetch } from "@/shared/api/kaos-client";
import { useAuthStore } from "@/shared/lib/stores";
import {
  Sun, Moon, Key, GitBranch, Workflow, Variable,
  RefreshCw, CheckCircle2, Loader2, ExternalLink,
  Globe, Shield, Cpu,
} from "lucide-react";

const SETTINGS_TABS = [
  { id: "theme", label: "Theme" },
  { id: "providers", label: "AI Providers" },
  { id: "catalog", label: "Catalog" },
  { id: "integrations", label: "Integrations" },
  { id: "env", label: "Environment" },
];

const SERVER_URL = "http://localhost:8000";

interface ProviderInfo {
  id: string; name: string; base_url: string;
  editable_url: boolean; configured: boolean;
  models: string[]; default_model?: string; fast_model?: string;
}

interface ProviderFormState {
  url: string; apiKey: string; model: string;
  testing: boolean; saving: boolean;
}

export default function SettingsPage() {
  const maskedKey = useAuthStore((s) => s.maskedKey);
  const [activeTab, setActiveTab] = useState("theme");

  // Providers
  const [providers, setProviders] = useState<ProviderInfo[]>([]);
  const [forms, setForms] = useState<Record<string, ProviderFormState>>({});
  const [loading, setLoading] = useState(true);

  // Catalog
  const [fallbackChain, setFallbackChain] = useState<string[]>([]);
  const [embeddingModel, setEmbeddingModel] = useState("");

  useEffect(() => {
    const fetchProviders = async () => {
      try {
        const res = await kaosFetch(`${SERVER_URL}/api/providers`, "");
        if (res.ok) {
          const data = await res.json();
          setProviders(data.providers || []);
          setFallbackChain(data.fallbackChain || []);
          setEmbeddingModel(data.embeddingModel || "");
          const initialForms: Record<string, ProviderFormState> = {};
          for (const p of data.providers || []) {
            initialForms[p.id] = {
              url: p.base_url || "", apiKey: "",
              model: p.default_model || p.models?.[0] || "",
              testing: false, saving: false,
            };
          }
          setForms(initialForms);
        }
      } catch {}
      finally { setLoading(false); }
    };
    fetchProviders();
  }, []);

  const handleTest = async (id: string) => {
    const f = forms[id]; if (!f) return;
    setForms((s) => ({ ...s, [id]: { ...s[id], testing: true } }));
    try {
      const res = await kaosFetch(`${SERVER_URL}/api/setup/provider/test`, "", {
        method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ provider: id, url: f.url, apiKey: f.apiKey }),
      });
      const d = await res.json();
      setProviders((prev) => prev.map((p) => p.id === id ? { ...p, configured: d.status === "connected" } : p));
    } catch {}
    finally { setForms((s) => ({ ...s, [id]: { ...s[id], testing: false } })); }
  };

  const handleSave = async (id: string) => {
    const f = forms[id]; if (!f) return;
    setForms((s) => ({ ...s, [id]: { ...s[id], saving: true } }));
    try {
      await kaosFetch(`${SERVER_URL}/api/setup/provider`, "", {
        method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ [id]: { url: f.url, apiKey: f.apiKey, model: f.model } }),
      });
      setProviders((prev) => prev.map((p) => p.id === id ? { ...p, configured: true } : p));
    } catch {}
    finally { setForms((s) => ({ ...s, [id]: { ...s[id], saving: false } })); }
  };

  const handleSaveGlobal = async () => {
    const payload: Record<string, any> = { _fallbackChain: fallbackChain, _embeddingModel: embeddingModel };
    for (const p of providers) {
      const f = forms[p.id];
      if (f) payload[p.id] = { url: f.url, apiKey: f.apiKey, model: f.model, fastModel: f.model };
    }
    await kaosFetch(`${SERVER_URL}/api/setup/provider`, "", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
  };

  const handleDiscoverModels = async (id: string) => {
    try {
      const res = await kaosFetch(`${SERVER_URL}/api/providers`, "");
      if (res.ok) {
        const data = await res.json();
        setProviders(data.providers || []);
      }
    } catch {}
  };

  const moveInChain = (index: number, direction: -1 | 1) => {
    const newChain = [...fallbackChain];
    const target = index + direction;
    if (target < 0 || target >= newChain.length) return;
    [newChain[index], newChain[target]] = [newChain[target], newChain[index]];
    setFallbackChain(newChain);
  };

  return (
    <div className="flex h-full flex-col gap-4 p-4 overflow-y-auto">
      <div>
        <h1 className="text-base font-semibold text-text-primary">Settings</h1>
        <p className="text-xs text-text-muted mt-0.5">Sistema de configurações do K.A.O.S</p>
      </div>

      <Tabs tabs={SETTINGS_TABS} activeTab={activeTab} onTabChange={setActiveTab} />

      {/* Theme Tab */}
      {activeTab === "theme" && (
        <Card>
          <CardContent className="p-4 space-y-4">
            <p className="text-sm font-medium text-text-primary">Appearance</p>
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
                {["#3B82F6", "#8B5CF6", "#10B981", "#F59E0B", "#EF4444"].map((c) => (
                  <button key={c} className="h-8 w-8 rounded-full border-2 border-border-subtle transition-transform hover:scale-110" style={{ backgroundColor: c }} />
                ))}
              </div>
            </div>
          </CardContent>
        </Card>
      )}

      {/* Providers Tab */}
      {activeTab === "providers" && (
        <div className="grid grid-cols-2 gap-3">
          {loading ? (
            <div className="col-span-2 flex justify-center py-8">
              <Loader2 className="h-5 w-5 animate-spin text-text-dim mr-2" />
              <span className="text-xs text-text-dim">Loading providers...</span>
            </div>
          ) : providers.map((p) => {
            const f = forms[p.id];
            return (
              <Card key={p.id}>
                <CardContent className="p-4 space-y-3">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                      {p.id === "openai" && <Globe className="h-4 w-4 text-green-400" />}
                      {p.id === "anthropic" && <Shield className="h-4 w-4 text-amber-400" />}
                      {p.id === "gemini" && <Cpu className="h-4 w-4 text-blue-400" />}
                      {p.id === "ollama" && <Variable className="h-4 w-4 text-purple-400" />}
                      {p.id === "openrouter" && <ExternalLink className="h-4 w-4 text-cyan-400" />}
                      {p.id === "openCode" && <Key className="h-4 w-4 text-zinc-400" />}
                      <h3 className="text-sm font-medium text-text-primary">{p.name}</h3>
                    </div>
                    <Badge variant={p.configured ? "success" : "neutral"}>
                      {p.configured ? "Connected" : "Disabled"}
                    </Badge>
                  </div>

                  {p.editable_url && (
                    <Input placeholder="API URL" value={f?.url || ""} onChange={(e) => setForms((s) => ({ ...s, [p.id]: { ...s[p.id], url: e.target.value } }))} className="text-xs" />
                  )}

                  {p.id !== "openCode" && (
                    <Input type="password" placeholder="API Key" value={f?.apiKey || ""} onChange={(e) => setForms((s) => ({ ...s, [p.id]: { ...s[p.id], apiKey: e.target.value } }))} className="text-xs" />
                  )}

                  <Input placeholder="Model" value={f?.model || ""} onChange={(e) => setForms((s) => ({ ...s, [p.id]: { ...s[p.id], model: e.target.value } }))} className="text-xs" />

                  <div className="flex gap-1">
                    {p.models.length > 0 && (
                      <Button variant="subtle" size="sm" onClick={() => handleDiscoverModels(p.id)} title="Discover models">
                        <RefreshCw className="h-3 w-3" />
                      </Button>
                    )}
                    <Button variant="secondary" size="sm" className="flex-1" onClick={() => handleTest(p.id)} disabled={f?.testing}>
                      {f?.testing ? <Loader2 className="h-3 w-3 mr-1 animate-spin" /> : <RefreshCw className="h-3 w-3 mr-1" />}
                      Test
                    </Button>
                    <Button variant="primary" size="sm" className="flex-1" onClick={() => handleSave(p.id)} disabled={f?.saving}>
                      {f?.saving ? <Loader2 className="h-3 w-3 mr-1 animate-spin" /> : <CheckCircle2 className="h-3 w-3 mr-1" />}
                      Save
                    </Button>
                  </div>

                  {p.models.length > 0 && (
                    <div className="text-[10px] text-text-dim">{p.models.length} models available</div>
                  )}
                </CardContent>
              </Card>
            );
          })}
        </div>
      )}

      {/* Catalog Tab (Fallback Chain + Embedding) */}
      {activeTab === "catalog" && (
        <div className="grid grid-cols-1 gap-3 max-w-lg">
          <Card>
            <CardHeader className="pb-2">
              <CardTitle className="text-xs font-semibold text-text-muted uppercase">Fallback Chain</CardTitle>
            </CardHeader>
            <CardContent className="p-4 space-y-2">
              <p className="text-[11px] text-text-dim">Order providers by fallback priority. Drag or use arrows.</p>
              {fallbackChain.map((pid, i) => {
                const p = providers.find((x) => x.id === pid);
                return (
                  <div key={pid} className="flex items-center justify-between rounded-lg border border-border-subtle bg-canvas/50 px-3 py-2">
                    <div className="flex items-center gap-2">
                      <span className="text-xs text-text-dim font-mono">{i + 1}.</span>
                      <span className="text-xs text-text-primary">{p?.name || pid}</span>
                    </div>
                    <div className="flex gap-1">
                      <button onClick={() => moveInChain(i, -1)} disabled={i === 0} className="text-text-dim hover:text-text-primary disabled:opacity-30 px-1">▲</button>
                      <button onClick={() => moveInChain(i, 1)} disabled={i === fallbackChain.length - 1} className="text-text-dim hover:text-text-primary disabled:opacity-30 px-1">▼</button>
                    </div>
                  </div>
                );
              })}
              <Button variant="primary" size="sm" onClick={handleSaveGlobal}>
                <CheckCircle2 className="h-3 w-3 mr-1" />
                Save Chain
              </Button>
            </CardContent>
          </Card>

          <Card>
            <CardHeader className="pb-2">
              <CardTitle className="text-xs font-semibold text-text-muted uppercase">Embedding Model</CardTitle>
            </CardHeader>
            <CardContent className="p-4 space-y-2">
              <Input value={embeddingModel} onChange={(e) => setEmbeddingModel(e.target.value)} placeholder="nomic-embed-text" className="text-xs" />
              <p className="text-[10px] text-text-dim">Model used for generating embeddings for vector search (RAG).</p>
              <Button variant="primary" size="sm" onClick={handleSaveGlobal}>
                <CheckCircle2 className="h-3 w-3 mr-1" />
                Save
              </Button>
            </CardContent>
          </Card>
        </div>
      )}

      {/* Integrations Tab */}
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
                    <div className="rounded-lg bg-bg-active p-2"><Icon className="h-4 w-4 text-text-primary" /></div>
                    <div>
                      <p className="text-sm font-medium text-text-primary">{integ.name}</p>
                      <p className="text-xs text-text-muted">{integ.desc}</p>
                    </div>
                  </div>
                  <div className="flex items-center gap-2">
                    <Badge variant={integ.status === "connected" ? "success" : "neutral"}>{integ.status}</Badge>
                    <Button variant="subtle" size="sm" disabled title="Coming Soon">Configure</Button>
                  </div>
                </div>
              );
            })}
          </CardContent>
        </Card>
      )}

      {/* Environment Tab */}
      {activeTab === "env" && (
        <Card>
          <CardContent className="p-4 space-y-3">
            <div className="flex items-center justify-between">
              <p className="text-sm font-medium text-text-primary">Environment Variables</p>
              <Button variant="primary" size="sm" disabled title="Coming Soon"><Key className="h-3.5 w-3.5 mr-1" />Add Variable</Button>
            </div>
            <div className="space-y-2">
              {[
                { key: "KAOS_API_KEY", value: maskedKey || "kaos-...key" },
                { key: "OLLAMA_HOST", value: "http://localhost:11434" },
                { key: "QDRANT_URL", value: "http://localhost:6333" },
                { key: "VAULT_PATH", value: "/workspace/kaos" },
              ].map((env) => (
                <div key={env.key} className="flex items-center justify-between rounded-lg border border-border-subtle bg-canvas/50 px-3 py-2">
                  <div className="flex items-center gap-3">
                    <Variable className="h-3.5 w-3.5 text-text-dim" />
                    <span className="text-xs font-mono text-text-primary">{env.key}</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <span className="text-xs font-mono text-text-dim">{env.value}</span>
                    <Button variant="subtle" size="sm" disabled title="Coming Soon">Edit</Button>
                    <Button variant="danger" size="sm" disabled title="Coming Soon">Remove</Button>
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
