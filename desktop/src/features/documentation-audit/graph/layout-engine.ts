import { GraphNode, GraphEdge } from "./graph-builder";

export interface LayoutResult {
  nodes: (GraphNode & { x: number; y: number })[];
  edges: GraphEdge[];
  width: number;
  height: number;
}

export class LayoutEngine {
  static forceDirected(
    nodes: GraphNode[],
    edges: GraphEdge[],
    width: number = 800,
    height: number = 600,
    iterations: number = 100
  ): LayoutResult {
    const positions: Map<string, { x: number; y: number; vx: number; vy: number }> = new Map();

    const centerX = width / 2;
    const centerY = height / 2;
    const radius = Math.min(width, height) * 0.4;

    nodes.forEach((node, i) => {
      const angle = (2 * Math.PI * i) / nodes.length;
      positions.set(node.id, {
        x: centerX + radius * Math.cos(angle) + (Math.random() - 0.5) * 50,
        y: centerY + radius * Math.sin(angle) + (Math.random() - 0.5) * 50,
        vx: 0,
        vy: 0,
      });
    });

    const repulsionStrength = 5000;
    const attractionStrength = 0.01;
    const damping = 0.9;

    for (let iter = 0; iter < iterations; iter++) {
      const posArray = Array.from(positions.entries());

      for (let i = 0; i < posArray.length; i++) {
        for (let j = i + 1; j < posArray.length; j++) {
          const [idA, posA] = posArray[i];
          const [idB, posB] = posArray[j];
          const dx = posA.x - posB.x;
          const dy = posA.y - posB.y;
          const dist = Math.sqrt(dx * dx + dy * dy) || 1;
          const force = repulsionStrength / (dist * dist);
          posA.vx += (dx / dist) * force;
          posA.vy += (dy / dist) * force;
          posB.vx -= (dx / dist) * force;
          posB.vy -= (dy / dist) * force;
        }
      }

      for (const edge of edges) {
        const from = positions.get(edge.from);
        const to = positions.get(edge.to);
        if (!from || !to) continue;
        const dx = to.x - from.x;
        const dy = to.y - from.y;
        const dist = Math.sqrt(dx * dx + dy * dy) || 1;
        const force = attractionStrength * dist;
        from.vx += (dx / dist) * force;
        from.vy += (dy / dist) * force;
        to.vx -= (dx / dist) * force;
        to.vy -= (dy / dist) * force;
      }

      for (const [, pos] of positions) {
        pos.x += pos.vx;
        pos.y += pos.vy;
        pos.vx *= damping;
        pos.vy *= damping;
      }
    }

    const layoutedNodes = nodes.map((node) => {
      const pos = positions.get(node.id);
      return {
        ...node,
        x: pos ? Math.max(10, Math.min(width - 10, pos.x)) : centerX,
        y: pos ? Math.max(10, Math.min(height - 10, pos.y)) : centerY,
      };
    });

    return { nodes: layoutedNodes, edges, width, height };
  }

  static hierarchical(
    nodes: GraphNode[],
    edges: GraphEdge[],
    width: number = 800,
    height: number = 600
  ): LayoutResult {
    const levels = new Map<string, number>();
    const edgeMap = new Map<string, string[]>();

    for (const edge of edges) {
      if (!edgeMap.has(edge.to)) edgeMap.set(edge.to, []);
      edgeMap.get(edge.to)!.push(edge.from);
    }

    const computeLevel = (nodeId: string, visited: Set<string> = new Set()): number => {
      if (levels.has(nodeId)) return levels.get(nodeId)!;
      if (visited.has(nodeId)) return 0;
      visited.add(nodeId);

      const parents = edgeMap.get(nodeId) || [];
      if (parents.length === 0) {
        levels.set(nodeId, 0);
        return 0;
      }
      const maxParentLevel = Math.max(...parents.map((p) => computeLevel(p, visited)));
      levels.set(nodeId, maxParentLevel + 1);
      return levels.get(nodeId)!;
    };

    for (const node of nodes) {
      computeLevel(node.id);
    }

    const maxLevel = Math.max(...Array.from(levels.values()), 0);
    const levelNodes = new Map<number, GraphNode[]>();
    for (const node of nodes) {
      const level = levels.get(node.id) || 0;
      if (!levelNodes.has(level)) levelNodes.set(level, []);
      levelNodes.get(level)!.push(node);
    }

    const layoutedNodes = nodes.map((node) => {
      const level = levels.get(node.id) || 0;
      const siblings = levelNodes.get(level) || [];
      const idx = siblings.indexOf(node);
      const totalInLevel = siblings.length;
      const levelHeight = height / (maxLevel + 1);
      return {
        ...node,
        x: width * ((idx + 0.5) / totalInLevel),
        y: level * levelHeight + levelHeight / 2,
      };
    });

    return { nodes: layoutedNodes, edges, width, height };
  }

  static radial(
    nodes: GraphNode[],
    edges: GraphEdge[],
    width: number = 800,
    height: number = 600
  ): LayoutResult {
    const centerX = width / 2;
    const centerY = height / 2;
    const maxRadius = Math.min(width, height) * 0.4;
    const angleStep = (2 * Math.PI) / nodes.length;

    const layoutedNodes = nodes.map((node, i) => ({
      ...node,
      x: centerX + maxRadius * Math.cos(i * angleStep),
      y: centerY + maxRadius * Math.sin(i * angleStep),
    }));

    return { nodes: layoutedNodes, edges, width, height };
  }
}