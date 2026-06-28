import { useEffect, useState, useCallback } from "react";
import ReactFlow, {
  MiniMap,
  Controls,
  Background,
  useNodesState,
  useEdgesState,
  MarkerType,
  useReactFlow,
  ReactFlowProvider,
} from "reactflow";
import "reactflow/dist/style.css";
import { kaosFetch } from "@/shared/api/kaos-client";
import { Badge } from "@/shared/ui/badge";
import { Loader2, RefreshCw, GitGraph, Hammer, Search, X, Link, Compass } from "lucide-react";

const SERVER_URL = "http://localhost:8000";

function KnowledgeGraphInner() {
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);
  const [loading, setLoading] = useState(true);
  const [rebuilding, setRebuilding] = useState(false);
  const [error, setError] = useState("");
  const [overview, setOverview] = useState<any>(null);
  const [selectedNode, setSelectedNode] = useState<any>(null);
  const [searchQuery, setSearchQuery] = useState("");

  const { setCenter } = useReactFlow();

  const fetchKG = useCallback(async () => {
    setLoading(true);
    setError("");
    try {
      const res = await kaosFetch(`${SERVER_URL}/api/architecture/knowledge-graph`, "");
      if (!res.ok) throw new Error("Erro na API do grafo");
      const data = await res.json();

      if (data.error) throw new Error(data.error);

      setOverview({
        total_nodes: data.total_nodes,
        total_edges: data.total_edges,
        features: data.features?.length || 0,
        sdds: data.sdds?.length || 0,
        workflows: data.workflows?.length || 0,
        agents: data.agents?.length || 0,
      });

      const flowNodes: any[] = (data.nodes || []).map((n: any, i: number) => {
        let borderColor = "rgba(161, 161, 170, 0.2)"; // Padrão cinza
        if (n.type === "feature") borderColor = "rgba(16, 185, 129, 0.4)"; // Verde
        else if (n.type === "sdd") borderColor = "rgba(245, 158, 11, 0.4)"; // Amarelo
        else if (n.type === "agent" || n.type === "workflow") borderColor = "rgba(139, 92, 246, 0.4)"; // Roxo
        else if (n.type === "store") borderColor = "rgba(59, 130, 246, 0.4)"; // Azul
        else if (n.type === "event") borderColor = "rgba(236, 72, 153, 0.4)"; // Rosa

        return {
          id: n.id,
          position: { x: 150 + (i % 4) * 240, y: 50 + Math.floor(i / 4) * 120 },
          data: {
            label: (
              <div className="flex flex-col items-center select-none text-left">
                <span className="text-[9px] opacity-60 uppercase font-mono tracking-wider block mb-0.5">{n.type}</span>
                <span className="font-bold text-text-primary text-[11px] truncate max-w-[155px] block">{n.title || n.id}</span>
              </div>
            ),
            fullData: n,
          },
          style: {
            background: "var(--surface-raised, #18181b)",
            border: `1px solid ${borderColor}`,
            borderRadius: 8,
            padding: 8,
            width: 180,
            boxShadow: "0 4px 6px -1px rgba(0, 0, 0, 0.1)",
            cursor: "pointer",
          },
        };
      });

      const flowEdges: any[] = (data.edges || []).map((e: any, i: number) => ({
        id: `e-${i}`,
        source: e.source,
        target: e.target,
        label: e.relation,
        type: "smoothstep",
        style: { stroke: "var(--border-subtle, #52525b)" },
        markerEnd: { type: MarkerType.ArrowClosed, color: "var(--border-subtle, #52525b)" },
        labelStyle: { fontSize: 8, fill: "var(--text-dim, #a1a1aa)" },
      }));

      setNodes(flowNodes);
      setEdges(flowEdges);
    } catch (e: any) {
      setError(e.message || "Falha ao carregar o grafo");
    } finally {
      setLoading(false);
    }
  }, [setNodes, setEdges]);

  const rebuildGraph = async () => {
    setRebuilding(true);
    try {
      const res = await kaosFetch(`${SERVER_URL}/api/architecture/knowledge-graph`, "POST");
      if (!res.ok) throw new Error("Erro ao reconstruir o grafo no backend");
      await fetchKG();
    } catch (e: any) {
      alert(e.message || "Erro durante a reconstrução");
    } finally {
      setRebuilding(false);
    }
  };

  useEffect(() => {
    fetchKG();
  }, [fetchKG]);

  const handleNodeClick = (_event: any, node: any) => {
    setSelectedNode(node.data.fullData);
  };

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (!searchQuery.trim()) return;

    const foundNode = nodes.find(
      (n: any) =>
        n.id.toLowerCase().includes(searchQuery.toLowerCase()) ||
        (n.data.fullData?.title && n.data.fullData.title.toLowerCase().includes(searchQuery.toLowerCase()))
    );

    if (foundNode) {
      setCenter(foundNode.position.x + 90, foundNode.position.y + 30, { zoom: 1.4, duration: 800 });
      setSelectedNode(foundNode.data.fullData);
    }
  };

  const dependencies = selectedNode
    ? edges.filter((e: any) => e.source === selectedNode.id).map((e: any) => e.target)
    : [];

  const dependents = selectedNode
    ? edges.filter((e: any) => e.target === selectedNode.id).map((e: any) => e.source)
    : [];

  const focusOnNodeById = (id: string) => {
    const foundNode = nodes.find((n: any) => n.id === id);
    if (foundNode) {
      setCenter(foundNode.position.x + 90, foundNode.position.y + 30, { zoom: 1.4, duration: 800 });
      setSelectedNode(foundNode.data.fullData);
    }
  };

  return (
    <div className="flex h-full w-full flex-row overflow-hidden bg-bg-primary text-text-primary">
      {/* Area Central: Grafo e Controles */}
      <div className="flex flex-1 flex-col h-full overflow-hidden">
        {/* Header */}
        <div className="flex items-center justify-between border-b border-border-subtle bg-surface-raised px-4 py-2">
          <div className="flex items-center gap-2">
            <GitGraph className="h-4 w-4 text-accent-neon" />
            <span className="text-sm font-semibold text-text-primary">Knowledge Graph</span>
            {overview && (
              <div className="flex gap-2 ml-2 hidden lg:flex">
                <Badge variant="info">{overview.total_nodes} entidades</Badge>
                <Badge variant="success">{overview.features} features</Badge>
                <Badge variant="neutral">{overview.sdds} SDDs</Badge>
                {overview.workflows > 0 && <Badge variant="warning">{overview.workflows} workflows</Badge>}
                {overview.agents > 0 && <Badge variant="neutral">{overview.agents} agents</Badge>}
              </div>
            )}
          </div>

          <div className="flex items-center gap-2">
            {/* Search Bar */}
            <form onSubmit={handleSearch} className="relative flex items-center">
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Buscar nó..."
                className="w-40 rounded-md border border-border-subtle bg-bg-primary px-2 py-1 pl-7 text-[11px] text-text-primary focus:border-accent-primary focus:outline-none"
              />
              <Search className="absolute left-2.5 h-3 w-3 text-text-dim" />
            </form>

            {/* Rebuild Graph */}
            <button
              onClick={rebuildGraph}
              disabled={rebuilding || loading}
              className="flex items-center gap-1 rounded-md bg-accent-primary hover:bg-accent-secondary px-2.5 py-1 text-[11px] font-medium text-white disabled:opacity-50 transition-colors"
            >
              {rebuilding ? (
                <Loader2 className="h-3 w-3 animate-spin" />
              ) : (
                <Hammer className="h-3 w-3" />
              )}
              Rebuild Graph
            </button>

            {/* Refresh */}
            <button
              onClick={fetchKG}
              disabled={loading || rebuilding}
              className="flex items-center gap-1 rounded-md bg-bg-active px-2.5 py-1 text-[11px] text-text-muted hover:text-text-primary disabled:opacity-50 transition-colors"
            >
              <RefreshCw className={`h-3 w-3 ${loading && !rebuilding ? "animate-spin" : ""}`} />
              Refresh
            </button>
          </div>
        </div>

        {/* Graph Body */}
        {loading && !rebuilding ? (
          <div className="flex flex-1 items-center justify-center bg-bg-primary">
            <Loader2 className="h-6 w-6 animate-spin text-text-dim" />
          </div>
        ) : error ? (
          <div className="flex flex-1 items-center justify-center bg-bg-primary p-4">
            <div className="text-center max-w-sm">
              <GitGraph className="h-10 w-10 text-text-dim mx-auto mb-3" />
              <p className="text-sm text-text-dim mb-3">{error}</p>
              <button
                onClick={rebuildGraph}
                className="rounded-md bg-accent-primary px-3 py-1.5 text-xs text-white hover:bg-accent-secondary transition-colors"
              >
                Reconstruir Grafo
              </button>
            </div>
          </div>
        ) : (
          <div className="flex-1 w-full bg-bg-primary relative">
            <ReactFlow
              nodes={nodes}
              edges={edges}
              onNodesChange={onNodesChange}
              onEdgesChange={onEdgesChange}
              onNodeClick={handleNodeClick}
              fitView
              attributionPosition="bottom-left"
            >
              <Controls />
              <MiniMap maskColor="rgba(9, 9, 11, 0.85)" style={{ background: "#18181b" }} />
              <Background color="#27272a" gap={20} />
            </ReactFlow>
          </div>
        )}
      </div>

      {/* Sidebar de Detalhes Lateral Direita */}
      {selectedNode && (
        <div className="w-80 border-l border-border-subtle bg-surface-raised flex flex-col h-full animate-in slide-in-from-right duration-200">
          {/* Sidebar Header */}
          <div className="flex items-center justify-between border-b border-border-subtle p-3 bg-surface-elevated">
            <div className="flex items-center gap-2">
              <Compass className="h-4 w-4 text-accent-primary" />
              <span className="text-[10px] font-bold uppercase tracking-wider text-text-muted">Detalhes do Nó</span>
            </div>
            <button
              onClick={() => setSelectedNode(null)}
              className="rounded-md p-1 hover:bg-bg-active text-text-dim hover:text-text-primary"
            >
              <X className="h-4 w-4" />
            </button>
          </div>

          {/* Sidebar Content */}
          <div className="flex-1 overflow-y-auto p-4 space-y-4">
            {/* Title / Header */}
            <div>
              <span className="text-[9px] text-text-dim uppercase font-mono tracking-wide block">{selectedNode.type}</span>
              <h3 className="text-sm font-bold text-text-primary break-all mt-0.5">{selectedNode.title || selectedNode.id}</h3>
              <Badge
                variant={
                  selectedNode.source === "code"
                    ? "info"
                    : selectedNode.source === "vault"
                    ? "success"
                    : "neutral"
                }
                className="mt-1.5"
              >
                {selectedNode.source}
              </Badge>
            </div>

            {/* Path */}
            {selectedNode.path && (
              <div className="space-y-1">
                <span className="text-[10px] text-text-dim font-semibold uppercase tracking-wide block">Caminho</span>
                <div className="rounded border border-border-subtle bg-bg-primary p-2">
                  <span className="text-[11px] font-mono break-all select-all text-text-muted block">{selectedNode.path}</span>
                </div>
              </div>
            )}

            {/* Meta */}
            {(selectedNode.status || selectedNode.owner) && (
              <div className="grid grid-cols-2 gap-2 py-2 border-y border-border-subtle">
                {selectedNode.status && (
                  <div>
                    <span className="text-[9px] text-text-dim uppercase tracking-wide block">Status</span>
                    <span className="text-xs font-semibold text-text-primary capitalize">{selectedNode.status}</span>
                  </div>
                )}
                {selectedNode.owner && (
                  <div>
                    <span className="text-[9px] text-text-dim uppercase tracking-wide block">Dono</span>
                    <span className="text-xs text-text-primary font-medium">{selectedNode.owner}</span>
                  </div>
                )}
              </div>
            )}

            {/* Tags */}
            {selectedNode.tags && selectedNode.tags.length > 0 && (
              <div className="space-y-1">
                <span className="text-[10px] text-text-dim font-semibold uppercase tracking-wide block">Tags</span>
                <div className="flex flex-wrap gap-1">
                  {selectedNode.tags.map((t: string) => (
                    <Badge key={t} variant="neutral">
                      {t}
                    </Badge>
                  ))}
                </div>
              </div>
            )}

            {/* Connections (Dependencies) */}
            <div className="space-y-3 pt-2">
              <div>
                <span className="text-[10px] text-text-dim font-semibold uppercase tracking-wide block mb-1">
                  Dependências de Saída ({dependencies.length})
                </span>
                {dependencies.length > 0 ? (
                  <div className="space-y-1">
                    {dependencies.map((dep) => (
                      <button
                        key={dep}
                        onClick={() => focusOnNodeById(dep)}
                        className="w-full flex items-center justify-between p-1.5 rounded border border-border-subtle hover:border-accent-primary bg-bg-primary text-left transition-colors"
                      >
                        <span className="text-[10px] font-mono truncate w-[85%] text-text-muted">{dep}</span>
                        <Link className="h-3 w-3 text-text-dim" />
                      </button>
                    ))}
                  </div>
                ) : (
                  <span className="text-[11px] text-text-dim block italic">Nenhuma dependência de saída</span>
                )}
              </div>

              <div>
                <span className="text-[10px] text-text-dim font-semibold uppercase tracking-wide block mb-1">
                  Dependentes de Entrada ({dependents.length})
                </span>
                {dependents.length > 0 ? (
                  <div className="space-y-1">
                    {dependents.map((dep) => (
                      <button
                        key={dep}
                        onClick={() => focusOnNodeById(dep)}
                        className="w-full flex items-center justify-between p-1.5 rounded border border-border-subtle hover:border-accent-primary bg-bg-primary text-left transition-colors"
                      >
                        <span className="text-[10px] font-mono truncate w-[85%] text-text-muted">{dep}</span>
                        <Link className="h-3 w-3 text-text-dim" />
                      </button>
                    ))}
                  </div>
                ) : (
                  <span className="text-[11px] text-text-dim block italic">Nenhum dependente de entrada</span>
                )}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default function KnowledgeGraphPage() {
  return (
    <ReactFlowProvider>
      <KnowledgeGraphInner />
    </ReactFlowProvider>
  );
}
