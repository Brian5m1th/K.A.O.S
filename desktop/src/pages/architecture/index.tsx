import React, { useEffect, useRef, useCallback } from "react";
import { useGraphStore, useGraphData, useGraphSelection, useGraphView, useGraphFilters } from "@/features/documentation-audit/graph/graph-store";
import { useGraphUpdater } from "@/features/documentation-audit/graph/graph-updater";
import { useDriftActions } from "@/features/documentation-audit/store/drift-store";
import { LayoutEngine, LayoutResult } from "@/features/documentation-audit/graph/layout-engine";
import { GraphExport } from "@/features/documentation-audit/graph/graph-export";
import { GraphNode } from "@/features/documentation-audit/graph/graph-builder";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Download, ZoomIn, ZoomOut, Maximize2, RefreshCw } from "lucide-react";

const typeColors: Record<string, string> = {
  feature: "#3b82f6",
  store: "#10b981",
  route: "#f59e0b",
  tool: "#8b5cf6",
  agent: "#ef4444",
  event: "#06b6d4",
  provider: "#f97316",
  sdd: "#6b7280",
};

export function ArchitecturePage() {
  const svgRef = useRef<SVGSVGElement>(null);
  const graph = useGraphData();
  const { selectedNode, hoveredNode } = useGraphSelection();
  const { zoom, pan } = useGraphView();
  const { selectNode, setHoveredNode, setZoom, setPan, resetView, setLayout, setFilterType, setGraph } = useGraphStore();
  const { filterType, layout: layoutType } = useGraphFilters();
  const { loadSnapshot } = useDriftActions();
  const [layoutResult, setLayoutResult] = React.useState<LayoutResult | null>(null);

  const updatedGraph = useGraphUpdater();

  useEffect(() => {
    if (updatedGraph) {
      setGraph(updatedGraph);
    }
  }, [updatedGraph, setGraph]);

  useEffect(() => {
    loadSnapshot();
  }, [loadSnapshot]);

  useEffect(() => {
    if (!graph || !graph.nodes.length) return;

    const filtered = filterType ? graph.nodes.filter((n) => n.type === filterType) : graph.nodes;
    const filteredEdges = graph.edges.filter(
      (e) => filtered.some((n) => n.id === e.from) && filtered.some((n) => n.id === e.to)
    );

    let result: LayoutResult;
    switch (layoutType) {
      case "hierarchical":
        result = LayoutEngine.hierarchical(filtered, filteredEdges);
        break;
      case "radial":
        result = LayoutEngine.radial(filtered, filteredEdges);
        break;
      default:
        result = LayoutEngine.forceDirected(filtered, filteredEdges);
    }
    setLayoutResult(result);
  }, [graph, filterType, layoutType]);

  const handleSvgClick = useCallback(
    (e: React.MouseEvent) => {
      if ((e.target as SVGElement).tagName === "svg") {
        selectNode(null);
      }
    },
    [selectNode]
  );

  const handleNodeClick = useCallback(
    (node: GraphNode) => {
      selectNode(selectedNode?.id === node.id ? null : node);
    },
    [selectNode, selectedNode]
  );

  const handleWheel = useCallback(
    (e: React.WheelEvent) => {
      e.preventDefault();
      setZoom(zoom - e.deltaY * 0.001);
    },
    [zoom, setZoom]
  );

  const handleMouseDown = useCallback(
    (e: React.MouseEvent) => {
      if ((e.target as SVGElement).tagName === "svg") {
        const startX = e.clientX - pan.x;
        const startY = e.clientY - pan.y;
        const handleMouseMove = (me: MouseEvent) => {
          setPan({ x: me.clientX - startX, y: me.clientY - startY });
        };
        const handleMouseUp = () => {
          document.removeEventListener("mousemove", handleMouseMove);
          document.removeEventListener("mouseup", handleMouseUp);
        };
        document.addEventListener("mousemove", handleMouseMove);
        document.addEventListener("mouseup", handleMouseUp);
      }
    },
    [pan, setPan]
  );

  const nodeTypes = graph ? Array.from(new Set(graph.nodes.map((n) => n.type))) : [];

  return (
    <div className="p-6 space-y-4 bg-canvas text-text-primary">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-bold text-text-primary">Architecture Graph</h1>
        <div className="flex items-center gap-2">
          <div className="flex items-center gap-1 bg-surface-raised rounded-lg p-1 border border-border-subtle">
            {(["force", "hierarchical", "radial"] as const).map((l) => (
              <button
                key={l}
                onClick={() => setLayout(l)}
                className={`px-3 py-1 text-xs rounded-md transition-colors ${layoutType === l ? "bg-surface border border-border-subtle text-text-primary shadow" : "text-text-dim hover:text-text-primary"}`}
              >
                {l === "force" ? "Force" : l === "hierarchical" ? "Hierarchical" : "Radial"}
              </button>
            ))}
          </div>
          <button onClick={() => setZoom(zoom + 0.2)} className="p-2 bg-surface-raised border border-border-subtle rounded-lg hover:bg-surface-hover text-text-primary">
            <ZoomIn className="w-4 h-4" />
          </button>
          <button onClick={() => setZoom(zoom - 0.2)} className="p-2 bg-surface-raised border border-border-subtle rounded-lg hover:bg-surface-hover text-text-primary">
            <ZoomOut className="w-4 h-4" />
          </button>
          <button onClick={resetView} className="p-2 bg-surface-raised border border-border-subtle rounded-lg hover:bg-surface-hover text-text-primary">
            <Maximize2 className="w-4 h-4" />
          </button>
          {graph && (
            <button onClick={() => GraphExport.downloadJSON(graph)} className="p-2 bg-surface-raised border border-border-subtle rounded-lg hover:bg-surface-hover text-text-primary">
              <Download className="w-4 h-4" />
            </button>
          )}
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-4 gap-4">
        <div className="lg:col-span-3">
          <Card>
            <CardContent className="p-0">
              {layoutResult ? (
                <svg
                  ref={svgRef}
                  className="w-full h-[600px] cursor-grab active:cursor-grabbing"
                  onClick={handleSvgClick}
                  onWheel={handleWheel}
                  onMouseDown={handleMouseDown}
                >
                  <g transform={`translate(${pan.x}, ${pan.y}) scale(${zoom})`}>
                    <rect x={-5000} y={-5000} width={10000} height={10000} fill="transparent" />
                    {layoutResult.edges.map((edge, i) => {
                      const from = layoutResult.nodes.find((n) => n.id === edge.from);
                      const to = layoutResult.nodes.find((n) => n.id === edge.to);
                      if (!from || !to) return null;
                      return (
                        <line
                          key={`edge-${i}`}
                          x1={from.x}
                          y1={from.y}
                          x2={to.x}
                          y2={to.y}
                          stroke={selectedNode && (selectedNode.id === edge.from || selectedNode.id === edge.to) ? "#6366f1" : "#d1d5db"}
                          strokeWidth={selectedNode && (selectedNode.id === edge.from || selectedNode.id === edge.to) ? 2 : 1}
                          opacity={selectedNode && (selectedNode.id === edge.from || selectedNode.id === edge.to) ? 1 : 0.4}
                        />
                      );
                    })}
                    {layoutResult.nodes.map((node) => {
                      const color = typeColors[node.type] || "#6b7280";
                      const isSelected = selectedNode?.id === node.id;
                      const isHovered = hoveredNode?.id === node.id;
                      return (
                        <g
                          key={node.id}
                          onClick={(e) => {
                            e.stopPropagation();
                            handleNodeClick(node);
                          }}
                          onMouseEnter={() => setHoveredNode(node)}
                          onMouseLeave={() => setHoveredNode(null)}
                          style={{ cursor: "pointer" }}
                        >
                          <circle
                            cx={node.x}
                            cy={node.y}
                            r={isSelected ? 10 : isHovered ? 8 : 6}
                            fill={color}
                            stroke={isSelected ? "#fff" : "none"}
                            strokeWidth={isSelected ? 2 : 0}
                          />
                          {(isSelected || isHovered) && (
                            <text
                              x={node.x + 12}
                              y={node.y + 4}
                              fontSize="11"
                              fill="var(--text-primary, #ffffff)"
                              fontWeight={isSelected ? "bold" : "normal"}
                            >
                              {node.label}
                            </text>
                          )}
                        </g>
                      );
                    })}
                  </g>
                </svg>
              ) : (
                <div className="h-[600px] flex items-center justify-center text-text-muted">
                  No graph data available. Run audit first.
                </div>
              )}
            </CardContent>
          </Card>
        </div>

        <div className="space-y-4">
          <Card className="border border-border-subtle bg-surface-raised/40">
            <CardHeader className="pb-2">
              <CardTitle className="text-sm text-text-primary">Node Types</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-1">
                <button
                  onClick={() => setFilterType(null)}
                  className={`w-full text-left px-2 py-1 text-xs rounded transition-colors ${!filterType ? "bg-primary/20 text-text-primary border border-primary/30" : "text-text-muted hover:bg-surface-hover hover:text-text-primary"}`}
                >
                  All ({graph?.nodes.length || 0})
                </button>
                {nodeTypes.map((type) => {
                  const count = graph?.nodes.filter((n) => n.type === type).length || 0;
                  return (
                    <button
                      key={type}
                      onClick={() => setFilterType(type)}
                      className={`w-full text-left px-2 py-1 text-xs rounded transition-colors ${filterType === type ? "bg-primary/20 text-text-primary border border-primary/30" : "text-text-muted hover:bg-surface-hover hover:text-text-primary"}`}
                    >
                      {type} ({count})
                    </button>
                  );
                })}
              </div>
            </CardContent>
          </Card>

          {selectedNode && (
            <Card className="border border-border-subtle bg-surface-raised/40 text-text-primary">
              <CardHeader className="pb-2">
                <CardTitle className="text-sm">Node Details</CardTitle>
              </CardHeader>
              <CardContent className="text-xs space-y-1 text-text-muted">
                <p><span className="font-medium text-text-primary">ID:</span> {selectedNode.id}</p>
                <p><span className="font-medium text-text-primary">Label:</span> {selectedNode.label}</p>
                <p><span className="font-medium text-text-primary">Type:</span> {selectedNode.type}</p>
                {selectedNode.phase && <p><span className="font-medium text-text-primary">Phase:</span> {selectedNode.phase}</p>}
                {selectedNode.status && <p><span className="font-medium text-text-primary">Status:</span> {selectedNode.status}</p>}
              </CardContent>
            </Card>
          )}

          {graph && (
            <Card className="border border-border-subtle bg-surface-raised/40">
              <CardHeader className="pb-2">
                <CardTitle className="text-sm text-text-primary">Export</CardTitle>
              </CardHeader>
              <CardContent className="space-y-1">
                <button onClick={() => GraphExport.downloadJSON(graph)} className="w-full px-3 py-2 bg-surface hover:bg-surface-hover rounded text-xs flex items-center gap-2 text-text-primary border border-border-subtle transition-colors">
                  <Download className="w-3 h-3 text-text-muted" /> Export JSON
                </button>
                <button onClick={() => GraphExport.downloadGraphML(graph)} className="w-full px-3 py-2 bg-surface hover:bg-surface-hover rounded text-xs flex items-center gap-2 text-text-primary border border-border-subtle transition-colors">
                  <Download className="w-3 h-3 text-text-muted" /> Export GraphML
                </button>
                {layoutResult && (
                  <button onClick={() => GraphExport.downloadSVG(layoutResult)} className="w-full px-3 py-2 bg-surface hover:bg-surface-hover rounded text-xs flex items-center gap-2 text-text-primary border border-border-subtle transition-colors">
                    <Download className="w-3 h-3 text-text-muted" /> Export SVG
                  </button>
                )}
              </CardContent>
            </Card>
          )}
        </div>
      </div>
    </div>
  );
}