import { useEffect, useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Badge } from "@/shared/ui/badge";
import { Button } from "@/shared/ui/button";
import { kaosFetch } from "@/shared/api/kaos-client";
import { useAuthStore } from "@/shared/lib/stores";
import { GitBranch, Plus, Play, RotateCw, Loader2 } from "lucide-react";

interface DlqItem {
  id: string;
  workflow_name: string;
  status: string;
  error: string;
  created_at: string;
}

export default function OrchestrationPage() {
  const serverUrl = useAuthStore((s) => s.serverUrl);
  const [workflows, setWorkflows] = useState<DlqItem[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchWorkflows = async () => {
    try {
      const res = await kaosFetch(`${serverUrl}/api/orchestrator/dlq`, "");
      if (res.ok) {
        const data = await res.json();
        setWorkflows(data.failed || []);
      }
    } catch {
      // Backend offline
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchWorkflows();
    const interval = setInterval(fetchWorkflows, 15_000);
    return () => clearInterval(interval);
  }, [serverUrl]);

  return (
    <div className="flex h-full flex-col gap-4 p-4">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-base font-semibold text-text-primary">Orquestração</h1>
          <p className="text-xs text-text-muted mt-0.5">Workflows ativos e pipelines de agentes</p>
        </div>
        <div className="flex items-center gap-2">
          <Button variant="secondary" size="sm" onClick={fetchWorkflows} disabled={loading}>
            <RotateCw className={`h-3.5 w-3.5 mr-1.5 ${loading ? "animate-spin" : ""}`} />
            Refresh
          </Button>
          <Button variant="primary" size="sm" disabled title="Coming Soon">
            <Plus className="h-3.5 w-3.5 mr-1.5" />
            Create Workflow
          </Button>
        </div>
      </div>

      {loading ? (
        <div className="flex items-center justify-center flex-1">
          <Loader2 className="h-5 w-5 animate-spin text-text-dim" />
          <span className="ml-2 text-xs text-text-dim">Loading workflows...</span>
        </div>
      ) : workflows.length === 0 ? (
        <div className="flex items-center justify-center flex-1">
          <p className="text-xs text-text-dim">No failed workflows</p>
        </div>
      ) : (
        <div className="grid grid-cols-2 gap-3">
          {workflows.map((wf) => (
            <Card key={wf.id} className="group">
              <CardContent className="p-4">
                <div className="flex items-start justify-between">
                  <div className="flex items-start gap-3">
                    <div className="mt-0.5 rounded-lg bg-accent-neon/10 p-2">
                      <GitBranch className="h-4 w-4 text-accent-neon" />
                    </div>
                    <div>
                      <h3 className="text-sm font-medium text-text-primary">{wf.workflow_name}</h3>
                      <p className="text-xs text-text-muted mt-0.5">{wf.error?.slice(0, 60)}</p>
                    </div>
                  </div>
                  <Badge variant="error">FAILED</Badge>
                </div>
                <div className="mt-3 flex items-center justify-between text-[11px] text-text-dim">
                  <span>{wf.created_at ? new Date(wf.created_at).toLocaleString() : "—"}</span>
                </div>
                <div className="mt-3">
                  <Button
                    variant="secondary"
                    size="sm"
                    className="w-full"
                    disabled
                    title="Coming Soon"
                  >
                    <Play className="h-3 w-3 mr-1.5" />
                    Retry
                  </Button>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      )}
    </div>
  );
}
