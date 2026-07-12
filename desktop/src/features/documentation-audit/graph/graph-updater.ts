import { useEffect, useRef, useState } from "react";
import { useDriftStore } from "../store/drift-store";
import { GraphBuilder, GraphData } from "./graph-builder";
import { eventBus } from "@/infrastructure";

interface GraphUpdaterProps {
  onGraphUpdate: (graph: GraphData) => void;
}

export function GraphUpdater({ onGraphUpdate }: GraphUpdaterProps) {
  const { driftReport, lastScan } = useDriftStore();
  const lastScanRef = useRef(lastScan);

  useEffect(() => {
    if (!driftReport) return;

    if (lastScanRef.current === lastScan) return;
    lastScanRef.current = lastScan;

    const graph = GraphBuilder.buildFromSnapshot({
      features: driftReport.features || [],
      coverage: driftReport.coverage,
      driftLevel: driftReport.driftLevel,
      lastCommit: "",
      graphSummary: { totalNodes: 0, totalEdges: 0, featureCount: 0, sddCount: 0, lastUpdated: new Date().toISOString() },
      missingCount: driftReport.missing_features.length,
      outdatedCount: driftReport.outdated_docs.length,
      generatedAt: driftReport.driftHistory[0]?.date || new Date().toISOString(),
    });

    onGraphUpdate(graph);
    eventBus.emit({ type: "graph:updated", payload: graph });
  }, [driftReport, lastScan, onGraphUpdate]);

  return null;
}

export function useGraphUpdater() {
  const [graph, setGraph] = useState<GraphData | null>(null);
  const { driftReport, lastScan } = useDriftStore();

  useEffect(() => {
    if (!driftReport) return;

    const g = GraphBuilder.buildFromSnapshot({
      features: driftReport.features || [],
      coverage: driftReport.coverage,
      driftLevel: driftReport.driftLevel,
      lastCommit: "",
      graphSummary: { totalNodes: 0, totalEdges: 0, featureCount: 0, sddCount: 0, lastUpdated: new Date().toISOString() },
      missingCount: driftReport.missing_features.length,
      outdatedCount: driftReport.outdated_docs.length,
      generatedAt: new Date().toISOString(),
    });

    setGraph(g);
  }, [driftReport, lastScan]);

  return graph;
}
