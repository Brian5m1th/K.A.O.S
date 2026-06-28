import { useState, useEffect, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import ReactFlow, {
  MiniMap,
  Controls,
  Background,
  useNodesState,
  useEdgesState,
  Node,
  Edge,
  MarkerType
} from "reactflow";
import "reactflow/dist/style.css";

import { Card, CardContent } from "@/shared/ui/card";
import { Badge } from "@/shared/ui/badge";
import { Button } from "@/shared/ui/button";
import { kaosFetch } from "@/shared/api/kaos-client";
import {
  Play, ToggleLeft, ToggleRight, Activity, AlertTriangle, CheckCircle, Info, RefreshCw
} from "lucide-react";

interface WorkflowItem {
  id: string;
  n8n_workflow_id: string;
  name: string;
  description: string;
  is_active: boolean;
  version: number;
}

interface ExecutionLog {
  id: string;
  workflow_id: string;
  status: string;
  trigger_event: string;
  duration_ms: number;
  created_at: string;
}

const INITIAL_NODES: Node[] = [
  {
    id: "n8n_webhook",
    type: "input",
    data: { label: "🌐 Webhook Trigger" },
    position: { x: 50, y: 150 },
    style: { background: "#0c0f1d", color: "#60a5fa", border: "1px solid #1d4ed8", borderRadius: "8px", boxShadow: "0 0 10px rgba(59, 130, 246, 0.2)" }
  },
  {
    id: "kaos_depth_check",
    data: { label: "🛡️ Depth Guard" },
    position: { x: 250, y: 150 },
    style: { background: "#0c0f1d", color: "#10b981", border: "1px solid #047857", borderRadius: "8px", boxShadow: "0 0 10px rgba(16, 185, 129, 0.2)" }
  },
  {
    id: "kaos_llm_routing",
    data: { label: "🧠 Intent Router" },
    position: { x: 450, y: 80 },
    style: { background: "#0c0f1d", color: "#c084fc", border: "1px solid #6b21a8", borderRadius: "8px", boxShadow: "0 0 10px rgba(168, 85, 247, 0.2)" }
  },
  {
    id: "local_ollama_fallback",
    type: "output",
    data: { label: "💻 Local Ollama" },
    position: { x: 650, y: 50 },
    style: { background: "#0c0f1d", color: "#f59e0b", border: "1px solid #b45309", borderRadius: "8px" }
  },
  {
    id: "discord_alert",
    type: "output",
    data: { label: "🚨 Discord Webhook" },
    position: { x: 650, y: 220 },
    style: { background: "#0c0f1d", color: "#ef4444", border: "1px solid #b91c1c", borderRadius: "8px" }
  }
];

const INITIAL_EDGES: Edge[] = [
  { id: "e_web_depth", source: "n8n_webhook", target: "kaos_depth_check", animated: true, markerEnd: { type: MarkerType.ArrowClosed } },
  { id: "e_depth_router", source: "kaos_depth_check", target: "kaos_llm_routing", animated: true },
  { id: "e_router_ollama", source: "kaos_llm_routing", target: "local_ollama_fallback", label: "fallback" },
  { id: "e_depth_discord", source: "kaos_depth_check", target: "discord_alert", label: "budget-limit", style: { stroke: "#ef4444" } }
];

export default function AutomationStudio() {
  const navigate = useNavigate();
  const [workflows, setWorkflows] = useState<WorkflowItem[]>([]);
  const [selectedWorkflow, setSelectedWorkflow] = useState<WorkflowItem | null>(null);
  const [history, setHistory] = useState<ExecutionLog[]>([]);
  
  const [nodes, setNodes, onNodesChange] = useNodesState(INITIAL_NODES);
  const [edges, setEdges, onEdgesChange] = useEdgesState(INITIAL_EDGES);

  const [loading, setLoading] = useState(false);
  const [triggeringId, setTriggeringId] = useState<string | null>(null);

  useEffect(() => {
    fetchWorkflows();
    fetchHistory();
  }, []);

  useEffect(() => {
    if (!selectedWorkflow) return;
    
    const jsonData = (selectedWorkflow as any).json_data || {};
    const n8nNodes = jsonData.nodes || [];
    const n8nConnections = jsonData.connections || {};

    // 1. Map nodes
    const mappedNodes: Node[] = n8nNodes.map((n: any) => {
      const isInput = n.type?.includes("webhook") || n.type?.includes("trigger");
      const isOutput = n.type?.includes("httpRequest") || n.type?.includes("respond");
      
      let style: React.CSSProperties = { background: "#0c0f1d", color: "#c084fc", border: "1px solid #6b21a8", borderRadius: "8px" };
      if (isInput) {
        style = { background: "#0c0f1d", color: "#60a5fa", border: "1px solid #1d4ed8", borderRadius: "8px", boxShadow: "0 0 10px rgba(59, 130, 246, 0.2)" };
      } else if (isOutput) {
        style = { background: "#0c0f1d", color: "#10b981", border: "1px solid #047857", borderRadius: "8px", boxShadow: "0 0 10px rgba(16, 185, 129, 0.2)" };
      }

      return {
        id: n.name,
        type: isInput ? "input" : isOutput ? "output" : undefined,
        data: { label: n.name },
        position: { x: n.position?.[0] ?? 100, y: n.position?.[1] ?? 150 },
        style
      };
    });

    // 2. Map edges
    const mappedEdges: Edge[] = [];
    Object.entries(n8nConnections).forEach(([sourceName, connectionData]: [string, any]) => {
      const mainConnections = connectionData.main || [];
      mainConnections.forEach((targetsList: any[]) => {
        targetsList.forEach((target: any) => {
          if (target && target.node) {
            mappedEdges.push({
              id: `e_${sourceName}_${target.node}`,
              source: sourceName,
              target: target.node,
              animated: true,
              markerEnd: { type: MarkerType.ArrowClosed }
            });
          }
        });
      });
    });

    setNodes(mappedNodes.length > 0 ? mappedNodes : INITIAL_NODES);
    setEdges(mappedEdges.length > 0 ? mappedEdges : INITIAL_EDGES);
  }, [selectedWorkflow, setNodes, setEdges]);

  const fetchWorkflows = async () => {
    try {
      const res = await kaosFetch("/api/automation/workflows");
      if (res.ok) {
        const data = await res.json();
        setWorkflows(data.workflows || []);
        if (data.workflows?.length > 0 && !selectedWorkflow) {
          setSelectedWorkflow(data.workflows[0]);
        }
      }
    } catch (e) {
      console.error(e);
    }
  };

  const fetchHistory = async () => {
    try {
      const res = await kaosFetch("/api/automation/history");
      if (res.ok) {
        const data = await res.json();
        setHistory(data.history || []);
      }
    } catch (e) {
      console.error(e);
    }
  };

  const handleToggle = async (wf: WorkflowItem) => {
    try {
      const res = await kaosFetch(`/api/automation/workflows/${wf.id}/toggle`, "", {
        method: "POST",
        body: JSON.stringify({ is_active: !wf.is_active })
      });
      if (res.ok) {
        setWorkflows((prev) =>
          prev.map((w) => (w.id === wf.id ? { ...w, is_active: !w.is_active } : w))
        );
        if (selectedWorkflow && selectedWorkflow.id === wf.id) {
          setSelectedWorkflow({ ...selectedWorkflow, is_active: !selectedWorkflow.is_active });
        }
      }
    } catch (e) {
      console.error(e);
    }
  };

  const handleTrigger = async (wf: WorkflowItem) => {
    setTriggeringId(wf.id);
    try {
      // Direct post trigger using SDK hooks exposed via API
      const res = await kaosFetch("/api/webhooks/n8n/chat", "", {
        method: "POST",
        body: JSON.stringify({ message: "Test execution manually triggered.", event: "manual.trigger" })
      });
      if (res.ok) {
        fetchHistory();
      }
    } catch (e) {
      console.error(e);
    } finally {
      setTriggeringId(null);
    }
  };

  return (
    <div className="flex h-full w-full bg-[#030712] overflow-hidden">
      {/* Sidebar - Workflows list */}
      <div className="w-80 border-r border-border-subtle bg-surface-raised/10 flex flex-col justify-between">
        <div className="flex flex-col flex-1 overflow-hidden">
          <div className="p-4 border-b border-border-subtle flex items-center justify-between">
            <div className="flex items-center gap-2">
              <Activity className="h-4 w-4 text-accent-neon animate-pulse" />
              <h2 className="text-sm font-semibold text-text-primary">Automation Studio</h2>
            </div>
            <div className="flex items-center gap-1">
              <Button variant="subtle" size="sm" onClick={() => navigate("/automation/marketplace")} className="text-[11px] px-2 py-1">
                Marketplace
              </Button>
              <Button variant="subtle" size="sm" onClick={fetchWorkflows}>
                <RefreshCw className="h-3 w-3" />
              </Button>
            </div>
          </div>
          
          <div className="flex-1 overflow-y-auto p-3 flex flex-col gap-2">
            {workflows.map((wf) => (
              <div
                key={wf.id}
                onClick={() => setSelectedWorkflow(wf)}
                className={`p-3 rounded-lg border transition-all cursor-pointer ${
                  selectedWorkflow?.id === wf.id
                    ? "border-accent-primary bg-accent-primary/5"
                    : "border-border-subtle bg-surface-raised/20 hover:bg-surface-raised/40"
                }`}
              >
                <div className="flex items-center justify-between">
                  <span className="text-xs font-medium text-text-primary truncate pr-2">{wf.name}</span>
                  <Badge variant={wf.is_active ? "success" : "neutral"}>
                    {wf.is_active ? "Active" : "Inactive"}
                  </Badge>
                </div>
                <p className="text-[10px] text-text-muted mt-1.5 truncate">{wf.description}</p>
              </div>
            ))}
          </div>
        </div>

        {/* Short Execution History widget */}
        <div className="border-t border-border-subtle p-3 h-52 flex flex-col overflow-hidden">
          <span className="text-[10px] font-semibold text-text-secondary uppercase tracking-wider mb-2">Logs Recentes</span>
          <div className="flex-1 overflow-y-auto flex flex-col gap-1.5">
            {history.slice(0, 5).map((h) => (
              <div key={h.id} className="p-2 rounded bg-surface-overlay/40 border border-border-subtle flex items-center justify-between text-[10px]">
                <div className="flex items-center gap-1.5">
                  {h.status === "success" ? (
                    <CheckCircle className="h-3 w-3 text-success" />
                  ) : h.status === "failed" ? (
                    <AlertTriangle className="h-3 w-3 text-danger" />
                  ) : (
                    <RefreshCw className="h-3 w-3 text-warning animate-spin" />
                  )}
                  <span className="text-text-primary truncate w-24">{h.trigger_event || "Event"}</span>
                </div>
                <span className="text-text-muted">{h.duration_ms ? `${h.duration_ms}ms` : "-"}</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Editor Canvas Area */}
      <div className="flex-1 flex flex-col bg-[#070b19] relative">
        {selectedWorkflow && (
          <div className="absolute top-4 left-4 z-10 flex items-center gap-3 bg-surface-raised/80 backdrop-blur-md border border-border-subtle p-3 rounded-lg shadow-xl">
            <div>
              <h3 className="text-xs font-bold text-text-primary">{selectedWorkflow.name}</h3>
              <p className="text-[9px] text-text-muted mt-0.5">n8n ID: {selectedWorkflow.n8n_workflow_id}</p>
            </div>
            <div className="flex items-center gap-2 border-l border-border-subtle pl-3">
              <Button
                variant="subtle"
                size="sm"
                className="p-1.5"
                onClick={() => handleToggle(selectedWorkflow)}
              >
                {selectedWorkflow.is_active ? (
                  <ToggleRight className="h-5 w-5 text-accent-neon" />
                ) : (
                  <ToggleLeft className="h-5 w-5 text-text-muted" />
                )}
              </Button>
              <Button
                variant="primary"
                size="sm"
                className="h-7 text-[10px] px-2.5 flex items-center gap-1 shadow-sm shadow-accent-primary/20"
                onClick={() => handleTrigger(selectedWorkflow)}
                disabled={triggeringId === selectedWorkflow.id}
              >
                <Play className="h-3 w-3" />
                <span>Test Run</span>
              </Button>
            </div>
          </div>
        )}

        <div className="flex-1 w-full h-full">
          <ReactFlow
            nodes={nodes}
            edges={edges}
            onNodesChange={onNodesChange}
            onEdgesChange={onEdgesChange}
            fitView
          >
            <Controls style={{ background: "#0c0f1d", border: "1px solid #1f2937", color: "#9ca3af" }} />
            <MiniMap style={{ background: "#0c0f1d", border: "1px solid #1f2937" }} maskColor="rgba(3, 7, 18, 0.6)" />
            <Background color="#1e293b" gap={16} size={1} />
          </ReactFlow>
        </div>
      </div>
    </div>
  );
}
