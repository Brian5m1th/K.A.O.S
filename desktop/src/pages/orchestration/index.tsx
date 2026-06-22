import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Badge } from "@/shared/ui/badge";
import { Button } from "@/shared/ui/button";
import { GitBranch, Plus, Play, RotateCw } from "lucide-react";

interface Workflow {
  id: string;
  name: string;
  description: string;
  status: "running" | "success" | "failed" | "idle";
  nodes: number;
  lastRun: string;
}

const WORKFLOWS: Workflow[] = [
  { id: "1", name: "RAG Pipeline", description: "Document ingestion + vector search", status: "running", nodes: 4, lastRun: "now" },
  { id: "2", name: "Code Review Agent", description: "Automated PR review with LLM", status: "success", nodes: 3, lastRun: "2m ago" },
  { id: "3", name: "Weekly Report", description: "Aggregate metrics + generate report", status: "idle", nodes: 5, lastRun: "1h ago" },
  { id: "4", name: "Knowledge Sync", description: "Sync Obsidian vault to Qdrant", status: "failed", nodes: 2, lastRun: "15m ago" },
  { id: "5", name: "Research Monitor", description: "Track arxiv papers by topic", status: "idle", nodes: 6, lastRun: "3h ago" },
];

export default function OrchestrationPage() {
  return (
    <div className="flex h-full flex-col gap-4 p-4">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-base font-semibold text-text-primary">Orquestração</h1>
          <p className="text-xs text-text-muted mt-0.5">Workflows ativos e pipelines de agentes</p>
        </div>
        <div className="flex items-center gap-2">
          <Button variant="secondary" size="sm">
            <RotateCw className="h-3.5 w-3.5 mr-1.5" />
            Refresh
          </Button>
          <Button variant="primary" size="sm">
            <Plus className="h-3.5 w-3.5 mr-1.5" />
            Create Workflow
          </Button>
        </div>
      </div>

      <div className="grid grid-cols-2 gap-3">
        {WORKFLOWS.map((wf) => (
          <Card key={wf.id} className="group">
            <CardContent className="p-4">
              <div className="flex items-start justify-between">
                <div className="flex items-start gap-3">
                  <div className="mt-0.5 rounded-lg bg-accent-neon/10 p-2">
                    <GitBranch className="h-4 w-4 text-accent-neon" />
                  </div>
                  <div>
                    <h3 className="text-sm font-medium text-text-primary">{wf.name}</h3>
                    <p className="text-xs text-text-muted mt-0.5">{wf.description}</p>
                  </div>
                </div>
                <Badge
                  variant={
                    wf.status === "running" ? "info" :
                    wf.status === "success" ? "success" :
                    wf.status === "failed" ? "error" : "neutral"
                  }
                >
                  {wf.status.toUpperCase()}
                </Badge>
              </div>
              <div className="mt-3 flex items-center justify-between text-[11px] text-text-dim">
                <span>{wf.nodes} nodes</span>
                <span>{wf.lastRun}</span>
              </div>
              {wf.status === "idle" && (
                <div className="mt-3 opacity-0 group-hover:opacity-100 transition-opacity">
                  <Button variant="secondary" size="sm" className="w-full">
                    <Play className="h-3 w-3 mr-1.5" />
                    Trigger Manual
                  </Button>
                </div>
              )}
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
