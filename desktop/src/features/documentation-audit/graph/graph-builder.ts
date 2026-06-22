import { FeatureEntry, DriftSnapshot } from "../store/drift-store";

export interface GraphNode {
  id: string;
  label: string;
  type: "feature" | "store" | "route" | "tool" | "agent" | "event" | "provider" | "sdd";
  phase?: string;
  status?: string;
  coverage?: number;
}

export interface GraphEdge {
  from: string;
  to: string;
  relation: "uses" | "emits" | "documents" | "depends_on" | "triggers" | "contains";
}

export interface GraphData {
  nodes: GraphNode[];
  edges: GraphEdge[];
  metadata: {
    totalNodes: number;
    totalEdges: number;
    nodeTypes: Record<string, number>;
    coverage: number;
    driftLevel: string;
  };
}

export class GraphBuilder {
  static buildFromSnapshot(snapshot: DriftSnapshot): GraphData {
    const nodes: GraphNode[] = [];
    const edges: GraphEdge[] = [];
    const nodeTypes: Record<string, number> = {};

    const addNode = (node: GraphNode) => {
      nodes.push(node);
      nodeTypes[node.type] = (nodeTypes[node.type] || 0) + 1;
    };

    for (const feature of snapshot.features) {
      addNode({
        id: feature.id,
        label: feature.name,
        type: "feature",
        phase: feature.phase,
        status: feature.status,
      });

      for (const doc of feature.docs) {
        const docId = `sdd:${doc}`;
        addNode({
          id: docId,
          label: doc,
          type: "sdd",
        });
        edges.push({
          from: feature.id,
          to: docId,
          relation: "documents",
        });
      }

      for (const codeRef of feature.codeRefs) {
        const codeType = this.inferCodeType(codeRef);
        addNode({
          id: codeRef,
          label: codeRef.split("/").pop() || codeRef,
          type: codeType,
        });
        edges.push({
          from: feature.id,
          to: codeRef,
          relation: "contains",
        });
      }
    }

    const inferredNodes = this.inferSystemNodes(snapshot);
    for (const node of inferredNodes) {
      if (!nodes.find(n => n.id === node.id)) {
        addNode(node);
      }
    }

    this.inferEdges(nodes, edges);

    return {
      nodes,
      edges,
      metadata: {
        totalNodes: nodes.length,
        totalEdges: edges.length,
        nodeTypes,
        coverage: snapshot.coverage,
        driftLevel: snapshot.driftLevel,
      },
    };
  }

  private static inferCodeType(path: string): GraphNode["type"] {
    if (path.includes("store")) return "store";
    if (path.includes("route") || path.includes("page")) return "route";
    if (path.includes("tool")) return "tool";
    if (path.includes("event")) return "event";
    if (path.includes("agent")) return "agent";
    if (path.includes("provider")) return "provider";
    if (path.includes("workflow")) return "agent";
    return "feature";
  }

  private static inferSystemNodes(snapshot: DriftSnapshot): GraphNode[] {
    const nodes: GraphNode[] = [];
    const knownSystems = [
      { id: "system.event-bus", label: "Event Bus", type: "event" as const },
      { id: "system.state-layer", label: "State Layer (Zustand)", type: "store" as const },
      { id: "system.command-layer", label: "Command Layer (CTRL+K)", type: "tool" as const },
      { id: "system.tool-layer", label: "Tool Layer (SSE)", type: "tool" as const },
      { id: "system.drl", label: "DRL Core", type: "feature" as const },
      { id: "system.audit", label: "Audit Engine", type: "feature" as const },
      { id: "system.graphify", label: "Graphify Engine", type: "feature" as const },
      { id: "system.auto-doc", label: "Auto-Doc Engine", type: "feature" as const },
    ];

    for (const sys of knownSystems) {
      nodes.push({ ...sys, phase: "KIRL", status: "active" });
    }

    return nodes;
  }

  private static inferEdges(nodes: GraphNode[], edges: GraphEdge[]) {
    const nodeMap = new Map(nodes.map(n => [n.id, n]));

    const systemEdges: GraphEdge[] = [
      { from: "system.drl", to: "system.audit", relation: "uses" },
      { from: "system.drl", to: "system.graphify", relation: "uses" },
      { from: "system.drl", to: "system.auto-doc", relation: "uses" },
      { from: "system.audit", to: "system.event-bus", relation: "emits" },
      { from: "system.graphify", to: "system.drl", relation: "documents" },
      { from: "system.auto-doc", to: "system.drl", relation: "documents" },
      { from: "system.state-layer", to: "system.command-layer", relation: "uses" },
      { from: "system.tool-layer", to: "system.event-bus", relation: "emits" },
    ];

    for (const edge of systemEdges) {
      if (nodeMap.has(edge.from) && nodeMap.has(edge.to)) {
        edges.push(edge);
      }
    }
  }
}