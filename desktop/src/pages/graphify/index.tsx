import { useEffect, useState, useCallback, useRef } from "react";
import ReactFlow, {
  MiniMap,
  Controls,
  Background,
  useNodesState,
  useEdgesState,
  MarkerType,
  type Node,
  type Edge,
} from "reactflow";
import "reactflow/dist/style.css";
import { kaosFetch } from "@/shared/api/kaos-client";
import { useAuthStore } from "@/shared/lib/stores";
import { Card, CardContent } from "@/shared/ui/card";
import { Badge } from "@/shared/ui/badge";
import { Loader2, RefreshCw, Network } from "lucide-react";

const NODE_COLORS: Record<string, string> = {
  feature: "#3B82F6",
  store: "#10B981",
  route: "#F59E0B",
  tool: "#8B5CF6",
  agent: "#EF4444",
  event: "#06B6D4",
  provider: "#F97316",
  sdd: "#6B7280",
  page: "#EC4899",
};

export default function GraphifyPage() {
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [stats, setStats] = useState({ nodes: 0, edges: 0 });

  const fetchGraph = useCallback(async () => {
    setLoading(true);
    setError("");
    try {
      const res = await kaosFetch("/api/architecture/graph", "");
      if (!res.ok) throw new Error("API error");
      const data = await res.json();

      if (data.error || !data.nodes) {
        throw new Error(data.error || "No graph data");
      }

      const flowNodes: Node[] = data.nodes.map((n: any, i: number) => ({
        id: n.id,
        type: "default",
        position: { x: 150 + (i % 4) * 200, y: 50 + Math.floor(i / 4) * 120 },
        data: {
          label: (
            <div className="flex items-center gap-2 px-2 py-1">
              <span
                className="h-2.5 w-2.5 rounded-full"
                style={{ backgroundColor: NODE_COLORS[n.type] || "#6B7280" }}
              />
              <span className="text-xs font-medium">{n.label}</span>
              <span className="text-[9px] text-gray-400 uppercase">{n.type}</span>
            </div>
          ),
        },
        style: {
          background: "rgba(24, 24, 27, 0.9)",
          border: `1px solid ${NODE_COLORS[n.type] || "#6B7280"}44`,
          borderRadius: 8,
          padding: 4,
        },
      }));

      const flowEdges: Edge[] = data.edges.map((e: any, i: number) => ({
        id: `e-${i}`,
        source: e.source,
        target: e.target,
        label: e.relation,
        type: "smoothstep",
        animated: e.relation === "emits",
        style: { stroke: "#52525b", strokeWidth: 1.5 },
        markerEnd: { type: MarkerType.ArrowClosed, color: "#52525b" },
        labelStyle: { fontSize: 9, fill: "#a1a1aa" },
      }));

      setNodes(flowNodes);
      setEdges(flowEdges);
      setStats({ nodes: data.nodes.length, edges: data.edges.length });
    } catch (e: any) {
      setError(e.message || "Failed to load graph");
    } finally {
      setLoading(false);
    }
  }, [setNodes, setEdges]);

  useEffect(() => {
    fetchGraph();
  }, [fetchGraph]);

  return (
    <div className="flex h-full flex-col">
      <div className="flex items-center justify-between border-b border-border-subtle px-4 py-2">
        <div className="flex items-center gap-2">
          <Network className="h-4 w-4 text-accent-primary" />
          <span className="text-sm font-semibold text-text-primary">Graphify Explorer</span>
          {!loading && (
            <Badge variant="info">{stats.nodes} nodes / {stats.edges} edges</Badge>
          )}
        </div>
        <button
          onClick={fetchGraph}
          disabled={loading}
          className="flex items-center gap-1 rounded-md bg-bg-active px-2 py-1 text-[11px] text-text-muted hover:text-text-primary transition-colors"
        >
          <RefreshCw className={`h-3 w-3 ${loading ? "animate-spin" : ""}`} />
          Refresh
        </button>
      </div>

      {loading ? (
        <div className="flex flex-1 items-center justify-center">
          <Loader2 className="h-6 w-6 animate-spin text-text-dim" />
        </div>
      ) : error ? (
        <div className="flex flex-1 items-center justify-center">
          <div className="text-center">
            <Network className="h-10 w-10 text-text-dim mx-auto mb-3" />
            <p className="text-sm text-text-dim">{error}</p>
            <button
              onClick={fetchGraph}
              className="mt-3 text-xs text-accent-primary hover:underline"
            >
              Build graph first via POST /api/architecture/graph
            </button>
          </div>
        </div>
      ) : (
        <div className="flex-1">
          <ReactFlow
            nodes={nodes}
            edges={edges}
            onNodesChange={onNodesChange}
            onEdgesChange={onEdgesChange}
            fitView
            attributionPosition="bottom-left"
          >
            <Controls />
            <MiniMap
              nodeColor={(n) => NODE_COLORS[(n.data?.label?.props?.children?.[2]?.props?.children as string)?.toLowerCase()] || "#6B7280"}
              maskColor="rgba(9, 9, 11, 0.8)"
              style={{ background: "#18181b" }}
            />
            <Background color="#27272a" gap={20} />
          </ReactFlow>
        </div>
      )}
    </div>
  );
}
