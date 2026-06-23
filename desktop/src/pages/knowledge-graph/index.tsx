import { useEffect, useState, useCallback } from "react";
import ReactFlow, { MiniMap, Controls, Background, useNodesState, useEdgesState, MarkerType } from "reactflow";
import "reactflow/dist/style.css";
import { kaosFetch } from "@/shared/api/kaos-client";
import { Badge } from "@/shared/ui/badge";
import { Card, CardContent } from "@/shared/ui/card";
import { Loader2, RefreshCw, GitGraph } from "lucide-react";

const SERVER_URL = "http://localhost:8000";

export default function KnowledgeGraphPage() {
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [overview, setOverview] = useState<any>(null);

  const fetchKG = useCallback(async () => {
    setLoading(true);
    setError("");
    try {
      const res = await kaosFetch(`${SERVER_URL}/api/architecture/knowledge-graph`, "");
      if (!res.ok) throw new Error("API error");
      const data = await res.json();

      if (data.error) throw new Error(data.error);

      setOverview({ total_nodes: data.total_nodes, total_edges: data.total_edges, features: data.features?.length || 0, sdds: data.sdds?.length || 0 });

      const flowNodes: any[] = (data.nodes || []).map((n: any, i: number) => ({
        id: n.id,
        position: { x: 150 + (i % 4) * 220, y: 50 + Math.floor(i / 4) * 100 },
        data: { label: <span className="text-xs px-2">{n.title || n.id}</span> },
        style: { background: "#18181b", border: "1px solid #3B82F644", borderRadius: 6, padding: 4 },
      }));

      const flowEdges: any[] = (data.edges || []).map((e: any, i: number) => ({
        id: `e-${i}`,
        source: e.source,
        target: e.target,
        label: e.relation,
        type: "smoothstep",
        style: { stroke: "#52525b" },
        markerEnd: { type: MarkerType.ArrowClosed, color: "#52525b" },
        labelStyle: { fontSize: 9, fill: "#a1a1aa" },
      }));

      setNodes(flowNodes);
      setEdges(flowEdges);
    } catch (e: any) {
      setError(e.message || "Failed to load");
    } finally {
      setLoading(false);
    }
  }, [setNodes, setEdges]);

  useEffect(() => { fetchKG(); }, [fetchKG]);

  return (
    <div className="flex h-full flex-col">
      <div className="flex items-center justify-between border-b border-border-subtle px-4 py-2">
        <div className="flex items-center gap-2">
          <GitGraph className="h-4 w-4 text-accent-neon" />
          <span className="text-sm font-semibold text-text-primary">Knowledge Graph</span>
          {overview && (
            <div className="flex gap-2 ml-2">
              <Badge variant="info">{overview.total_nodes} entities</Badge>
              <Badge variant="success">{overview.features} features</Badge>
              <Badge variant="neutral">{overview.sdds} SDDs</Badge>
            </div>
          )}
        </div>
        <button onClick={fetchKG} disabled={loading} className="flex items-center gap-1 rounded-md bg-bg-active px-2 py-1 text-[11px] text-text-muted hover:text-text-primary">
          <RefreshCw className={`h-3 w-3 ${loading ? "animate-spin" : ""}`} />
          Refresh
        </button>
      </div>

      {loading ? (
        <div className="flex flex-1 items-center justify-center"><Loader2 className="h-6 w-6 animate-spin text-text-dim" /></div>
      ) : error ? (
        <div className="flex flex-1 items-center justify-center">
          <div className="text-center">
            <GitGraph className="h-10 w-10 text-text-dim mx-auto mb-3" />
            <p className="text-sm text-text-dim">{error}</p>
          </div>
        </div>
      ) : (
        <div className="flex-1">
          <ReactFlow nodes={nodes} edges={edges} onNodesChange={onNodesChange} onEdgesChange={onEdgesChange} fitView attributionPosition="bottom-left">
            <Controls /><MiniMap maskColor="rgba(9,9,11,0.8)" style={{ background: "#18181b" }} /><Background color="#27272a" gap={20} />
          </ReactFlow>
        </div>
      )}
    </div>
  );
}
