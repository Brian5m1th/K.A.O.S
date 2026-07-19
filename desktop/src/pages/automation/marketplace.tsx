import { useEffect, useState } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/shared/ui/card";
import { Button } from "@/shared/ui/button";
import { Badge } from "@/shared/ui/badge";
import { kaosFetch } from "@/infrastructure";
import {
  Download, CheckCircle, RefreshCw, AlertCircle, FileJson,
  GitBranch, GitPullRequest, MessageSquare, ShieldCheck, Database, RefreshCcw, type LucideIcon
} from "lucide-react";

interface WorkflowTemplate {
  id: string;
  name: string;
  description: string;
  category: "IA" | "GitHub" | "Messaging" | "DevOps" | "MCP";
  icon: LucideIcon;
  json_name: string;
  installed: boolean;
}

interface TemplateApiItem {
  name: string;
  description: string;
  category: string;
  json_name: string;
  nodes?: unknown[];
  connections?: unknown;
}

interface WorkflowApiItem {
  name: string;
  id: string;
  is_active: boolean;
}

const CATEGORY_ICONS: Record<string, LucideIcon> = {
  IA: Database,
  GitHub: GitPullRequest,
  Messaging: MessageSquare,
  DevOps: ShieldCheck,
  MCP: GitBranch,
};

export default function AutomationMarketplace() {
  const [templates, setTemplates] = useState<WorkflowTemplate[]>([]);
  const [loading, setLoading] = useState(true);
  const [installingId, setInstallingId] = useState<string | null>(null);
  const [message, setMessage] = useState<{ text: string; type: "success" | "error" } | null>(null);

  useEffect(() => {
    Promise.all([fetchTemplates(), fetchInstalledWorkflows()]);
  }, []);

  const fetchTemplates = async () => {
    try {
      const res = await kaosFetch("/api/automation/templates");
      if (res.ok) {
        const data = await res.json();
        const tpls: WorkflowTemplate[] = (data.templates || []).map((t: TemplateApiItem, i: number) => ({
          id: `tpl_${i + 1}`,
          name: t.name,
          description: t.description,
          category: (t.category as WorkflowTemplate["category"]) || "IA",
          icon: CATEGORY_ICONS[t.category] || Database,
          json_name: t.json_name,
          installed: false,
        }));
        setTemplates(tpls);
      }
    } catch (e) {
      console.error("Failed to fetch templates", e);
    }
  };

  const fetchInstalledWorkflows = async () => {
    setLoading(true);
    try {
      const res = await kaosFetch("/api/automation/workflows");
      if (res.ok) {
        const data = await res.json();
        const activeNames = new Set(data.workflows.map((w: WorkflowApiItem) => w.name));
        
        setTemplates((prev) =>
          prev.map((t) => ({
            ...t,
            installed: activeNames.has(t.name),
          }))
        );
      }
    } catch (e) {
      console.error("Failed to fetch installed workflows", e);
    } finally {
      setLoading(false);
    }
  };

  const handleInstall = async (tpl: WorkflowTemplate) => {
    setInstallingId(tpl.id);
    setMessage(null);
    try {
      // 1. Fetch template JSON schema from backend static assets
      let jsonData: Record<string, unknown> | null = null;
      const jsonRes = await fetch(`/workflows/${tpl.json_name}`).catch(() => null);
      if (jsonRes && jsonRes.ok) {
        jsonData = await jsonRes.json();
        console.debug(`[marketplace] Template JSON loaded: ${tpl.json_name}`);
      } else {
        console.warn(`[marketplace] Template JSON not found at /workflows/${tpl.json_name}, using fallback`);
      }

      const payload = {
        name: tpl.name,
        description: tpl.description,
        json_data: jsonData || {
          name: tpl.name,
          nodes: [
            {
              id: "node_1",
              name: "Webhook Trigger",
              type: "n8n-nodes-base.webhook",
              position: [100, 300]
            }
          ],
          connections: {}
        }
      };

      const res = await kaosFetch("/api/automation/workflows/import", "", {
        method: "POST",
        body: JSON.stringify(payload),
      });

      if (res.ok) {
        setMessage({ text: `Workflow "${tpl.name}" instalado com sucesso no n8n!`, type: "success" });
        setTemplates((prev) =>
          prev.map((t) => (t.id === tpl.id ? { ...t, installed: true } : t))
        );
      } else {
        const err = await res.json();
        setMessage({ text: `Falha na instalação: ${err.detail || "Erro interno"}`, type: "error" });
      }
    } catch (e) {
      setMessage({ text: `Erro de rede ao conectar com o backend.`, type: "error" });
    } finally {
      setInstallingId(null);
    }
  };

  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = async (e) => {
      try {
        const json = JSON.parse(e.target?.result as string);
        const name = json.name || file.name.replace(".json", "");
        
        const payload = {
          name,
          description: "Workflow customizado importado por arquivo JSON.",
          json_data: json
        };

        const res = await kaosFetch("/api/automation/workflows/import", "", {
          method: "POST",
          body: JSON.stringify(payload)
        });

        if (res.ok) {
          setMessage({ text: `Workflow "${name}" importado com sucesso por arquivo!`, type: "success" });
          fetchInstalledWorkflows();
        } else {
          const err = await res.json();
          setMessage({ text: `Erro ao importar arquivo: ${err.detail}`, type: "error" });
        }
      } catch (err) {
        setMessage({ text: "Arquivo JSON inválido ou mal formatado.", type: "error" });
      }
    };
    reader.readAsText(file);
  };

  return (
    <div className="flex flex-col gap-6 p-6 h-full overflow-y-auto">
      <div className="flex items-center justify-between border-b border-border-subtle pb-4">
        <div>
          <h1 className="text-xl font-bold text-text-primary tracking-tight">Automation Marketplace</h1>
          <p className="text-sm text-text-muted mt-1">
            Instale e ative integrações oficiais homologadas para o ecossistema K.A.O.S.
          </p>
        </div>
        <div className="flex items-center gap-3">
          <label className="flex items-center gap-2 px-3 py-1.5 rounded-md border border-border-subtle bg-surface-raised/40 hover:bg-surface-raised cursor-pointer text-xs font-medium text-text-secondary transition-all">
            <FileJson className="h-4 w-4 text-accent-neon" />
            <span>Upload JSON</span>
            <input type="file" accept=".json" onChange={handleFileUpload} className="hidden" />
          </label>
          <Button variant="subtle" size="sm" onClick={fetchInstalledWorkflows} disabled={loading}>
            <RefreshCw className={`h-3.5 w-3.5 ${loading ? "animate-spin" : ""}`} />
          </Button>
        </div>
      </div>

      {message && (
        <div className={`flex items-center gap-3 px-4 py-3 rounded-md border text-sm transition-all ${
          message.type === "success" 
            ? "bg-success/10 border-success/30 text-success" 
            : "bg-danger/10 border-danger/30 text-danger"
        }`}>
          {message.type === "success" ? <CheckCircle className="h-4 w-4" /> : <AlertCircle className="h-4 w-4" />}
          <span>{message.text}</span>
        </div>
      )}

      {loading ? (
        <div className="flex flex-col items-center justify-center flex-1 py-12 gap-2 text-text-muted">
          <RefreshCw className="h-8 w-8 animate-spin text-accent-primary" />
          <span className="text-xs">Carregando catálogo de integrações...</span>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {templates.map((tpl) => {
            const IconComponent = tpl.icon;
            return (
              <Card key={tpl.id} className="border border-border-subtle bg-surface-raised/20 hover:border-border-muted transition-all duration-300 flex flex-col justify-between hover:shadow-lg hover:shadow-accent-primary/5">
                <CardHeader className="pb-3">
                  <div className="flex items-start justify-between">
                    <div className="p-2.5 rounded-lg bg-surface-overlay/80 border border-border-subtle text-accent-neon">
                      <IconComponent className="h-5 w-5" />
                    </div>
                    <Badge variant={tpl.category === "IA" ? "success" : "neutral"}>
                      {tpl.category}
                    </Badge>
                  </div>
                  <CardTitle className="text-sm font-semibold text-text-primary mt-3">
                    {tpl.name}
                  </CardTitle>
                  <CardDescription className="text-xs text-text-muted mt-1 leading-relaxed">
                    {tpl.description}
                  </CardDescription>
                </CardHeader>
                <CardContent className="pt-0 pb-4 flex justify-end">
                  {tpl.installed ? (
                    <Button variant="subtle" size="sm" className="w-full flex items-center justify-center gap-1.5 text-success border-success/20 bg-success/5 hover:bg-success/10" disabled>
                      <CheckCircle className="h-3.5 w-3.5" />
                      <span>Instalado</span>
                    </Button>
                  ) : (
                    <Button
                      variant="primary"
                      size="sm"
                      className="w-full flex items-center justify-center gap-1.5 shadow-sm shadow-accent-primary/20"
                      onClick={() => handleInstall(tpl)}
                      disabled={installingId === tpl.id}
                    >
                      {installingId === tpl.id ? (
                        <>
                          <RefreshCw className="h-3.5 w-3.5 animate-spin" />
                          <span>Instalando...</span>
                        </>
                      ) : (
                        <>
                          <Download className="h-3.5 w-3.5" />
                          <span>Instalação 1-Clique</span>
                        </>
                      )}
                    </Button>
                  )}
                </CardContent>
              </Card>
            );
          })}
        </div>
      )}
    </div>
  );
}
