import { useState, useEffect } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Badge } from "@/shared/ui/badge";
import { Button } from "@/shared/ui/button";
import { Container, Play, GitCommit, GitPullRequest, ExternalLink, Loader2 } from "lucide-react";

interface PipelineRun {
  id: string;
  name: string;
  branch: string;
  commit: string;
  status: "success" | "failed" | "running" | "pending";
  duration: string;
  timestamp: string;
}

const INITIAL_PIPELINES: PipelineRun[] = [
  { id: "1", name: "CI: Build & Test", branch: "main", commit: "a1b2c3d", status: "success", duration: "2m 34s", timestamp: "2m ago" },
  { id: "2", name: "Docker: Deploy API", branch: "main", commit: "e4f5g6h", status: "running", duration: "1m 12s", timestamp: "now" },
  { id: "3", name: "Lint & Format", branch: "feature/ui", commit: "i7j8k9l", status: "failed", duration: "0m 45s", timestamp: "15m ago" },
  { id: "4", name: "Release: v0.6.0", branch: "release", commit: "m0n1o2p", status: "pending", duration: "—", timestamp: "queued" },
  { id: "5", name: "Sync: Docs Deploy", branch: "main", commit: "q3r4s5t", status: "success", duration: "1m 05s", timestamp: "1h ago" },
  { id: "6", name: "Test: E2E Suite", branch: "feature/agents", commit: "u6v7w8x", status: "pending", duration: "—", timestamp: "queued" },
];

export default function PipelinesPage() {
  const [runs, setRuns] = useState<PipelineRun[]>(INITIAL_PIPELINES);
  const [triggering, setTriggering] = useState(false);

  // Simulate pipeline transitions
  useEffect(() => {
    const timer = setInterval(() => {
      setRuns((currentRuns) =>
        currentRuns.map((run) => {
          if (run.status === "pending") {
            return { ...run, status: "running", timestamp: "now" };
          }
          if (run.status === "running") {
            // Keep running for a bit, or transition
            const shouldTransition = Math.random() > 0.5;
            if (shouldTransition) {
              const status = Math.random() > 0.15 ? "success" : "failed";
              return {
                ...run,
                status,
                duration: `${Math.floor(Math.random() * 3)}m ${Math.floor(Math.random() * 60)}s`,
                timestamp: "just now",
              };
            }
          }
          return run;
        })
      );
    }, 4000);

    return () => clearInterval(timer);
  }, []);

  const handleTriggerManual = () => {
    setTriggering(true);
    setTimeout(() => {
      const newId = String(runs.length + 1);
      const newRun: PipelineRun = {
        id: newId,
        name: "Manual Trigger: CI Build",
        branch: "dev",
        commit: Math.random().toString(36).substring(2, 9),
        status: "pending",
        duration: "—",
        timestamp: "queued",
      };
      setRuns((prev) => [newRun, ...prev]);
      setTriggering(false);
    }, 1000);
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
        </CardContent>
      </Card>
    </div>
  );
}
