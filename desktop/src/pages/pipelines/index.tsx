import { useState, useEffect } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Badge } from "@/shared/ui/badge";
import { Button } from "@/shared/ui/button";
import { kaosFetch } from "@/shared/api/kaos-client";
import { Container, Play, GitCommit, GitPullRequest, ExternalLink, Loader2, RefreshCw } from "lucide-react";

interface PipelineRun {
  id: string;
  name: string;
  branch: string;
  commit: string;
  status: "success" | "failed" | "running" | "pending";
  duration: string;
  timestamp: string;
}

export default function PipelinesPage() {
  const [runs, setRuns] = useState<PipelineRun[]>([]);
  const [loading, setLoading] = useState(true);
  const [triggering, setTriggering] = useState(false);

  const fetchPipelines = async () => {
    setLoading(true);
    try {
      const res = await kaosFetch("/api/integrations/github/runs");
      if (res.ok) {
        const data = await res.json();
        // Map ISO timestamp to relative time or clean date
        const formatted = (data.runs || []).map((r: any) => {
          let timeLabel = r.timestamp;
          if (r.timestamp) {
            try {
              const diffMs = Date.now() - new Date(r.timestamp).getTime();
              const mins = Math.floor(diffMs / 60000);
              if (mins < 1) timeLabel = "now";
              else if (mins < 60) timeLabel = `${mins}m ago`;
              else {
                const hrs = Math.floor(mins / 60);
                if (hrs < 24) timeLabel = `${hrs}h ago`;
                else timeLabel = new Date(r.timestamp).toLocaleDateString();
              }
            } catch {}
          }
          return {
            ...r,
            timestamp: timeLabel
          };
        });
        setRuns(formatted);
      }
    } catch (e) {
      console.error("Failed to load pipeline runs:", e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchPipelines();
    const interval = setInterval(fetchPipelines, 15000);
    return () => clearInterval(interval);
  }, []);

  const handleTriggerManual = async () => {
    setTriggering(true);
    try {
      const res = await kaosFetch("/api/integrations/github/trigger", "", {
        method: "POST"
      });
      if (res.ok) {
        // Wait briefly for GitHub API to process the run creation
        setTimeout(fetchPipelines, 2000);
      }
    } catch (e) {
      console.error(e);
    } finally {
      setTriggering(false);
    }
  };

  const handleOpenGithub = () => {
    window.open("https://github.com/Brian5m1th/K.A.O.S/actions", "_blank");
  };

  return (
    <div className="flex h-full flex-col gap-4 p-4">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-base font-semibold text-text-primary">Pipelines</h1>
          <p className="text-xs text-text-muted mt-0.5">CI/CD e automações de deploy</p>
        </div>
        <div className="flex items-center gap-2">
          <Button variant="subtle" size="sm" onClick={fetchPipelines} disabled={loading}>
            <RefreshCw className={`h-3.5 w-3.5 ${loading ? "animate-spin" : ""}`} />
          </Button>
          <Button variant="subtle" size="sm" onClick={handleOpenGithub}>
            <ExternalLink className="h-3.5 w-3.5 mr-1.5" />
            Open GitHub Actions
          </Button>
          <Button variant="primary" size="sm" onClick={handleTriggerManual} disabled={triggering}>
            {triggering ? (
              <Loader2 className="h-3.5 w-3.5 animate-spin mr-1.5" />
            ) : (
              <Play className="h-3.5 w-3.5 mr-1.5" />
            )}
            Trigger Manual
          </Button>
        </div>
      </div>

      <Card>
        <CardHeader className="pb-2">
          <CardTitle className="text-xs font-semibold text-text-muted uppercase tracking-wider">
            Recent Executions
          </CardTitle>
        </CardHeader>
        <CardContent className="p-0 px-4 pb-4">
          {loading && runs.length === 0 ? (
            <div className="flex flex-col items-center justify-center py-12 gap-2 text-text-muted">
              <Loader2 className="h-6 w-6 animate-spin" />
              <span className="text-xs">Carregando execuções do GitHub...</span>
            </div>
          ) : runs.length === 0 ? (
            <div className="text-center py-8 text-xs text-text-muted">
              Nenhuma execução encontrada. Conecte sua integração do GitHub nas configurações.
            </div>
          ) : (
            <div className="flex flex-col gap-1">
              {runs.map((pipe) => (
                <div
                  key={pipe.id}
                  className="flex items-center justify-between rounded-lg border border-border-subtle bg-canvas/50 px-3 py-2.5 transition-colors hover:bg-bg-active"
                >
                  <div className="flex items-center gap-3 min-w-0">
                    <div className={`rounded-full p-1 ${
                      pipe.status === "success" ? "bg-success/10" :
                      pipe.status === "failed" ? "bg-error/10" :
                      pipe.status === "running" ? "bg-accent-primary/10" :
                      "bg-text-dim/10"
                    }`}>
                      {pipe.status === "running" ? (
                        <Loader2 className="h-3.5 w-3.5 text-accent-primary animate-spin" />
                      ) : (
                        <Container className={`h-3.5 w-3.5 ${
                          pipe.status === "success" ? "text-success" :
                          pipe.status === "failed" ? "text-error" :
                          "text-text-dim"
                        }`} />
                      )}
                    </div>
                    <div className="min-w-0">
                      <p className="text-sm font-medium text-text-primary truncate">{pipe.name}</p>
                      <div className="flex items-center gap-2 text-[11px] text-text-dim">
                        <GitPullRequest className="h-3 w-3" />
                        <span>{pipe.branch}</span>
                        <GitCommit className="h-3 w-3 ml-1" />
                        <span className="font-mono">{pipe.commit}</span>
                      </div>
                    </div>
                  </div>
                  <div className="flex items-center gap-3 shrink-0">
                    <div className="text-right">
                      <p className="text-[11px] text-text-dim font-mono">{pipe.duration}</p>
                      <p className="text-[10px] text-text-dim">{pipe.timestamp}</p>
                    </div>
                    <Badge
                      variant={
                        pipe.status === "success" ? "success" :
                        pipe.status === "failed" ? "error" :
                        pipe.status === "running" ? "info" :
                        "neutral"
                      }
                    >
                      {pipe.status.toUpperCase()}
                    </Badge>
                  </div>
                </div>
              ))}
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
