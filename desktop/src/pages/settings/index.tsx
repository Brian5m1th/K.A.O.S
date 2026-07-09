import { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";
import { Badge } from "@/shared/ui/badge";
import { Tabs } from "@/shared/ui/tabs";
import { kaosFetch } from "@/infrastructure";
import { useAuthStore, useThemeStore, useSystemStore } from "@/application";
import { UpdateCard } from "@/features/auto-update/ui/UpdateCard";
import {
  Sun, Moon, Key, GitBranch, Workflow, Variable,
  RefreshCw, CheckCircle2, Loader2, Globe, Shield, Cpu, ExternalLink,
} from "lucide-react";

const SETTINGS_TABS = [
  { id: "theme", label: "Theme" },
  { id: "providers", label: "AI Providers" },
  { id: "catalog", label: "Catalog" },
  { id: "integrations", label: "Integrations" },
  { id: "env", label: "Environment" },
  { id: "updates", label: "Atualizações" },
];

interface ProviderInfo {
  id: string; name: string; base_url: string;
  editable_url: boolean; configured: boolean;
  models: string[]; default_model?: string; fast_model?: string;
  status?: "healthy" | "unhealthy" | "unknown";
  latency?: number;
}

interface IntegrationInfo {
  type: string;
  status: string;
  metadata: Record<string, unknown>;
}

interface ProviderFormState {
  url: string; apiKey: string; model: string;
  testing: boolean; saving: boolean;
}

const THEMES = ["dark", "light", "kaos-blue", "purple", "terminal", "cyberpunk", "nordic", "forest"] as const;
const ACCENT_COLORS = ["#3B82F6", "#8B5CF6", "#10B981", "#F59E0B", "#EF4444", "#06B6D4"];

export default function SettingsPage() {
  const maskedKey = useAuthStore((s) => s.maskedKey);
  const mode = useThemeStore((s) => s.mode);
  const accentColor = useThemeStore((s) => s.accentColor);
  const setMode = useThemeStore((s) => s.setMode);
  const setAccentColor = useThemeStore((s) => s.setAccentColor);
  const saveToBackend = useThemeStore((s) => s.saveToBackend);
  const [searchParams] = useSearchParams();
  const [activeTab, setActiveTab] = useState(searchParams.get("tab") ?? "theme");

  const [providers, setProviders] = useState<ProviderInfo[]>([]);
  const [forms, setForms] = useState<Record<string, ProviderFormState>>({});
  const [loading, setLoading] = useState(true);
  const [fallbackChain, setFallbackChain] = useState<string[]>([]);
  const [embeddingModel, setEmbeddingModel] = useState("");
  const [integrations, setIntegrations] = useState<IntegrationInfo[]>([]);
  const [envVars, setEnvVars] = useState<{ key: string; value: string }[]>([]);
  const [activeProvider, setActiveProvider] = useState("ollama");

  useEffect(() => {
    const fetchAll = async () => {
      try {
        // Fetch providers
        const provRes = await kaosFetch("/api/providers", "");
        if (provRes.ok) {
          const data = await provRes.json();
          setProviders(data.providers || []);
          setFallbackChain(data.fallbackChain || []);
          setEmbeddingModel(data.embeddingModel || "");
          setActiveProvider(data.activeProvider || "ollama");
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

        // Fetch integrations
        const intRes = await kaosFetch("/api/integrations", "");
        if (intRes.ok) {
          const intData = await intRes.json();
          setIntegrations(intData.integrations || []);
        }

        // Fetch settings (for env vars display)
        const setRes = await kaosFetch("/api/settings", "");
        if (setRes.ok) {
          const setData = await setRes.json();
          const envList: { key: string; value: string }[] = [];
          for (const [key, val] of Object.entries(setData)) {
            if (typeof val === "string" && !key.startsWith("_")) {
              envList.push({ key, value: val });
            }
          }
          setEnvVars(envList);
        }
      } catch {} finally { setLoading(false); }
    };
    fetchAll();
  }, []);

  const handleTest = async (id: string) => {
    const f = forms[id]; if (!f) return;
    setForms((s) => ({ ...s, [id]: { ...s[id], testing: true } }));
    try {
      const res = await kaosFetch("/api/setup/provider/test", "", {
        method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ provider: id, url: f.url, apiKey: f.apiKey }),
      });
      const d = await res.json();
      setProviders((prev) => prev.map((p) => p.id === id ? { ...p, configured: d.status === "connected" } : p));
    } catch {} finally { setForms((s) => ({ ...s, [id]: { ...s[id], testing: false } })); }
  };

  const handleSave = async (id: string) => {
    const f = forms[id]; if (!f) return;
    setForms((s) => ({ ...s, [id]: { ...s[id], saving: true } }));
    try {
      await kaosFetch("/api/setup/provider", "", {
        method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ [id]: { url: f.url, apiKey: f.apiKey, model: f.model } }),
      });
      setProviders((prev) => prev.map((p) => p.id === id ? { ...p, configured: true } : p));
    } catch {} finally { setForms((s) => ({ ...s, [id]: { ...s[id], saving: false } })); }
  };

  const handleActivate = async (id: string) => {
    try {
      const res = await kaosFetch("/api/setup/provider/active", "", {
        method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ provider: id }),
      });
      if (res.ok) {
        setActiveProvider(id);
      }
    } catch {}
  };

  const handleSaveGlobal = async () => {
    const payload: Record<string, any> = { _fallbackChain: fallbackChain, _embeddingModel: embeddingModel };
    for (const p of providers) {
      const f = forms[p.id];
      if (f) payload[p.id] = { url: f.url, apiKey: f.apiKey, model: f.model, fastModel: f.model };
    }
    await kaosFetch("/api/setup/provider", "", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
  };

  const moveInChain = (index: number, direction: -1 | 1) => {
    const newChain = [...fallbackChain];
    const target = index + direction;
    if (target < 0 || target >= newChain.length) return;
    [newChain[index], newChain[target]] = [newChain[target], newChain[index]];
    setFallbackChain(newChain);
  };

  const providerIcons: Record<string, React.ReactNode> = {
    openai: <Globe className="h-4 w-4 text-green-400" />,
    anthropic: <Shield className="h-4 w-4 text-amber-400" />,
    gemini: <Cpu className="h-4 w-4 text-blue-400" />,
    ollama: <Variable className="h-4 w-4 text-purple-400" />,
    openrouter: <ExternalLink className="h-4 w-4 text-cyan-400" />,
    openCode: <Key className="h-4 w-4 text-zinc-400" />,
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
            <div className="flex flex-wrap gap-3">
              {THEMES.map((t) => (
                <button
                  key={t}
                  onClick={() => { setMode(t); saveToBackend(); }}
                  className={`flex flex-col items-center gap-2 rounded-lg border-2 p-4 transition-all ${
                    mode === t
                      ? "border-accent-primary bg-canvas"
                      : "border-border-subtle bg-canvas/50 opacity-60 hover:opacity-100"
                  }`}
                >
                  {t !== "light"
                    ? <Moon className="h-6 w-6 text-accent-primary" />
                    : <Sun className="h-6 w-6 text-text-muted" />
                  }
                  <span className="text-xs text-text-primary capitalize">{t.replace("-", " ")}</span>
                </button>
              ))}
            </div>
            <div>
              <label className="mb-1.5 block text-xs font-medium text-text-muted">Accent Color</label>
              <div className="flex flex-wrap gap-2">
                {ACCENT_COLORS.map((c) => (
                  <button
                    key={c}
                    onClick={() => { setAccentColor(c); saveToBackend(); }}
                    className={`h-8 w-8 rounded-full border-2 transition-transform hover:scale-110 ${
                      accentColor === c ? "border-white scale-110" : "border-border-subtle"
                    }`}
                    style={{ backgroundColor: c }}
                  />
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
            <div className="col-span-2 flex justify-center py-8"><Loader2 className="h-5 w-5 animate-spin text-text-dim mr-2" /><span className="text-xs text-text-dim">Loading providers...</span></div>
          ) : providers.filter((p) => p.id !== "openCode").map((p) => {
            const f = forms[p.id];
            return (
              <Card key={p.id}>
                <CardContent className="p-4 space-y-3">
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2">
                        {providerIcons[p.id] || <Variable className="h-4 w-4 text-zinc-400" />}
                        <h3 className="text-sm font-medium text-text-primary">{p.name}</h3>
                      </div>
                      <div className="flex items-center gap-2">
                        {p.latency !== undefined && p.latency > 0 && (
                          <span className="text-[11px] text-text-muted font-mono">
                            {p.latency}ms
                          </span>
                        )}
                        {activeProvider === p.id && (
                          <Badge variant="info">Active</Badge>
                        )}
                        <Badge variant={
                          p.status === "healthy" ? "success" :
                          p.status === "unhealthy" ? "error" :
                          "neutral"
                        }>
                          {p.status === "healthy" ? "Healthy" :
                           p.status === "unhealthy" ? "Unhealthy" :
                           p.configured ? "Configured" : "Disabled"}
                        </Badge>
                      </div>
                    </div>
                  {p.editable_url && (
                    <Input placeholder="API URL" value={f?.url || ""} onChange={(e) => setForms((s) => ({ ...s, [p.id]: { ...s[p.id], url: e.target.value } }))} className="text-xs" />
                  )}
                  <Input type="password" placeholder="API Key" value={f?.apiKey || ""} onChange={(e) => setForms((s) => ({ ...s, [p.id]: { ...s[p.id], apiKey: e.target.value } }))} className="text-xs" />
                  <Input placeholder="Model" value={f?.model || ""} onChange={(e) => setForms((s) => ({ ...s, [p.id]: { ...s[p.id], model: e.target.value } }))} className="text-xs" />
                  <div className="flex gap-2">
                    <Button variant="secondary" size="sm" className="flex-1" onClick={() => handleTest(p.id)} disabled={f?.testing}>
                      {f?.testing ? <Loader2 className="h-3 w-3 mr-1 animate-spin" /> : <RefreshCw className="h-3 w-3 mr-1" />} Test
                    </Button>
                    <Button variant="primary" size="sm" className="flex-1" onClick={() => handleSave(p.id)} disabled={f?.saving}>
                      {f?.saving ? <Loader2 className="h-3 w-3 mr-1 animate-spin" /> : <CheckCircle2 className="h-3 w-3 mr-1" />} Save
                    </Button>
                    {activeProvider !== p.id && (
                      <Button variant="secondary" size="sm" className="flex-1" onClick={() => handleActivate(p.id)} disabled={!p.configured && p.id !== "ollama"}>
                        Activate
                      </Button>
                    )}
                  </div>
                </CardContent>
              </Card>
            );
          })}
        </div>
      )}

      {/* Catalog Tab */}
      {activeTab === "catalog" && (
        <div className="grid grid-cols-1 gap-3 max-w-lg">
          <Card>
            <CardHeader className="pb-2"><CardTitle className="text-xs font-semibold text-text-muted uppercase">Fallback Chain</CardTitle></CardHeader>
            <CardContent className="p-4 space-y-2">
              <p className="text-[11px] text-text-dim">Provider fallback priority order.</p>
              {fallbackChain.map((pid, i) => {
                const p = providers.find((x) => x.id === pid);
                return (
                  <div key={pid} className="flex items-center justify-between rounded-lg border border-border-subtle bg-canvas/50 px-3 py-2">
                    <span className="text-xs text-text-primary">{i + 1}. {p?.name || pid}</span>
                    <div className="flex gap-1">
                      <button onClick={() => moveInChain(i, -1)} disabled={i === 0} className="text-text-dim hover:text-text-primary disabled:opacity-30 px-1">▲</button>
                      <button onClick={() => moveInChain(i, 1)} disabled={i === fallbackChain.length - 1} className="text-text-dim hover:text-text-primary disabled:opacity-30 px-1">▼</button>
                    </div>
                  </div>
                );
              })}
              <Button variant="primary" size="sm" onClick={handleSaveGlobal}><CheckCircle2 className="h-3 w-3 mr-1" />Save Chain</Button>
            </CardContent>
          </Card>
          <Card>
            <CardHeader className="pb-2"><CardTitle className="text-xs font-semibold text-text-muted uppercase">Embedding Model</CardTitle></CardHeader>
            <CardContent className="p-4 space-y-2">
              <Input value={embeddingModel} onChange={(e) => setEmbeddingModel(e.target.value)} className="text-xs" />
              <Button variant="primary" size="sm" onClick={handleSaveGlobal}><CheckCircle2 className="h-3 w-3 mr-1" />Save</Button>
            </CardContent>
          </Card>
        </div>
      )}

      {/* Integrations Tab */}
      {activeTab === "integrations" && (
        <Card>
          <CardContent className="p-4 space-y-3">
            {loading ? (
              <div className="flex justify-center py-4"><Loader2 className="h-4 w-4 animate-spin text-text-dim" /></div>
            ) : integrations.length === 0 ? (
              <p className="text-xs text-text-muted text-center py-4">No integrations configured. Use the API to add one.</p>
            ) : integrations.map((integ) => {
              const Icon = integ.type === "github" ? GitBranch :
                           integ.type === "n8n" ? Workflow :
                           Variable;
              return (
                <div key={integ.type} className="flex items-center justify-between rounded-lg border border-border-subtle bg-canvas/50 px-4 py-3">
                  <div className="flex items-center gap-3">
                    <div className="rounded-lg bg-bg-active p-2"><Icon className="h-4 w-4 text-text-primary" /></div>
                    <div>
                      <p className="text-sm font-medium text-text-primary capitalize">{integ.type}</p>
                      {integ.metadata && Object.keys(integ.metadata).length > 0 && (
                        <p className="text-xs text-text-muted">{JSON.stringify(integ.metadata)}</p>
                      )}
                    </div>
                  </div>
                  <Badge variant={integ.status === "connected" ? "success" : "neutral"}>
                    {integ.status}
                  </Badge>
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
              <p className="text-sm font-medium text-text-primary">Config Values (from /api/settings)</p>
            </div>
            <div className="space-y-2">
              {loading ? (
                <div className="flex justify-center py-4"><Loader2 className="h-4 w-4 animate-spin text-text-dim" /></div>
              ) : envVars.length === 0 ? (
                <p className="text-xs text-text-muted text-center py-4">No settings loaded.</p>
              ) : envVars.map((env) => (
                <div key={env.key} className="flex items-center justify-between rounded-lg border border-border-subtle bg-canvas/50 px-3 py-2">
                  <div className="flex items-center gap-3">
                    <Variable className="h-3.5 w-3.5 text-text-dim" />
                    <span className="text-xs font-mono text-text-primary">{env.key}</span>
                  </div>
                  <span className="text-xs font-mono text-text-dim">{env.value}</span>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      )}

      {/* Updates Tab */}
      {activeTab === "updates" && <UpdateCard />}
    </div>
  );
}
