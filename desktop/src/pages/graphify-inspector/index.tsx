/**
 * Graphify Path Inspector — Desktop UI for code intelligence queries.
 *
 * Uses GraphStore (REST API) — never imports Graphify directly.
 * Allows searching for symbols, explaining them, and tracing dependency paths.
 */

import { useState } from "react";
import { useGraphStore } from "@/application/stores/graph-store";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Badge } from "@/shared/ui/badge";
import { Loader2, Search, GitBranch, Code } from "lucide-react";

export default function GraphifyInspectorPage() {
  const explainConcept = useGraphStore((s) => s.explainConcept);
  const findPath = useGraphStore((s) => s.findPath);
  const queryGraph = useGraphStore((s) => s.queryGraph);
  const loading = useGraphStore((s) => s.loading);
  const currentNode = useGraphStore((s) => s.currentNode);
  const currentPath = useGraphStore((s) => s.currentPath);
  const queryResults = useGraphStore((s) => s.queryResults);

  const [concept, setConcept] = useState("");
  const [sourceSymbol, setSourceSymbol] = useState("");
  const [targetSymbol, setTargetSymbol] = useState("");
  const [searchQuery, setSearchQuery] = useState("");

  return (
    <div className="flex h-full flex-col gap-4 p-4 overflow-y-auto bg-canvas text-text-primary">
      <div>
        <h1 className="text-base font-semibold">Graphify Inspector</h1>
        <p className="text-xs text-text-muted mt-0.5">
          Explore code structure, trace dependency paths, and search the AST graph
        </p>
      </div>

      {/* Explain Symbol */}
      <Card className="border border-border-subtle bg-surface/50">
        <CardHeader className="pb-2">
          <CardTitle className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider">
            <Code className="h-4 w-4 text-accent-primary" />
            Explain Symbol
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-3">
          <div className="flex gap-2">
            <input
              className="flex-1 rounded-lg border border-border-subtle bg-canvas px-3 py-1.5 text-xs text-text-primary"
              placeholder="e.g. CodeScanner, OllamaProvider, GraphBuilder"
              value={concept}
              onChange={(e) => setConcept(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && explainConcept(concept)}
            />
            <button
              onClick={() => explainConcept(concept)}
              disabled={loading || !concept}
              className="rounded-lg bg-accent-primary/20 px-3 py-1.5 text-xs font-medium text-accent-primary hover:bg-accent-primary/30 disabled:opacity-50"
            >
              {loading ? <Loader2 className="h-3.5 w-3.5 animate-spin" /> : "Explain"}
            </button>
          </div>
          {currentNode && (
            <div className="rounded-lg border border-border-subtle bg-canvas p-3 space-y-1 text-xs">
              <p><span className="text-text-muted">ID:</span> <code className="text-accent-primary">{currentNode.id}</code></p>
              <p><span className="text-text-muted">Label:</span> <span className="text-text-primary font-medium">{currentNode.label}</span></p>
              <p><span className="text-text-muted">Source:</span> <code className="text-accent-neon">{currentNode.source_file}</code></p>
              <p><span className="text-text-muted">Type:</span> <Badge variant="info">{currentNode.type}</Badge></p>
              <p><span className="text-text-muted">Connections:</span> <span className="font-mono">{currentNode.degree}</span></p>
              <p><span className="text-text-muted">Community:</span> <span>{currentNode.community}</span></p>
            </div>
          )}
        </CardContent>
      </Card>

      {/* Find Path */}
      <Card className="border border-border-subtle bg-surface/50">
        <CardHeader className="pb-2">
          <CardTitle className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider">
            <GitBranch className="h-4 w-4 text-accent-neon" />
            Trace Dependency Path
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-3">
          <div className="flex gap-2">
            <input
              className="flex-1 rounded-lg border border-border-subtle bg-canvas px-3 py-1.5 text-xs text-text-primary"
              placeholder="Source symbol"
              value={sourceSymbol}
              onChange={(e) => setSourceSymbol(e.target.value)}
            />
            <span className="text-text-dim self-center">→</span>
            <input
              className="flex-1 rounded-lg border border-border-subtle bg-canvas px-3 py-1.5 text-xs text-text-primary"
              placeholder="Target symbol"
              value={targetSymbol}
              onChange={(e) => setTargetSymbol(e.target.value)}
            />
            <button
              onClick={() => findPath(sourceSymbol, targetSymbol)}
              disabled={loading || !sourceSymbol || !targetSymbol}
              className="rounded-lg bg-accent-neon/20 px-3 py-1.5 text-xs font-medium text-accent-neon hover:bg-accent-neon/30 disabled:opacity-50"
            >
              Trace
            </button>
          </div>
          {currentPath && (
            <div className="rounded-lg border border-border-subtle bg-canvas p-3 text-xs font-mono">
              <p className="text-text-dim">{currentPath.description}</p>
              <p className="text-accent-neon mt-1">Hops: {currentPath.hops}</p>
            </div>
          )}
        </CardContent>
      </Card>

      {/* Search Graph */}
      <Card className="border border-border-subtle bg-surface/50">
        <CardHeader className="pb-2">
          <CardTitle className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider">
            <Search className="h-4 w-4 text-warning" />
            Search Code Graph
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-3">
          <div className="flex gap-2">
            <input
              className="flex-1 rounded-lg border border-border-subtle bg-canvas px-3 py-1.5 text-xs text-text-primary"
              placeholder="Search symbols, files, or communities..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && queryGraph(searchQuery)}
            />
            <button
              onClick={() => queryGraph(searchQuery)}
              disabled={loading || !searchQuery}
              className="rounded-lg bg-warning/20 px-3 py-1.5 text-xs font-medium text-warning hover:bg-warning/30 disabled:opacity-50"
            >
              Search
            </button>
          </div>
          {queryResults && (
            <div className="space-y-1 max-h-64 overflow-y-auto">
              <p className="text-[10px] text-text-dim">{queryResults.total_found} results</p>
              {queryResults.nodes.map((n, i) => (
                <div key={i} className="rounded border border-border-subtle bg-canvas px-2 py-1 text-xs flex justify-between">
                  <span className="text-accent-primary">{n.label}</span>
                  <span className="text-text-dim">{n.source_file}</span>
                </div>
              ))}
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
