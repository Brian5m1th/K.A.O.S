import { create } from "zustand";
import { GraphData, GraphNode, GraphEdge } from "./graph-builder";

interface GraphState {
  graph: GraphData | null;
  selectedNode: GraphNode | null;
  hoveredNode: GraphNode | null;
  zoom: number;
  pan: { x: number; y: number };
  filterType: string | null;
  layout: "force" | "hierarchical" | "radial";
  setGraph: (graph: GraphData) => void;
  selectNode: (node: GraphNode | null) => void;
  setHoveredNode: (node: GraphNode | null) => void;
  setZoom: (zoom: number) => void;
  setPan: (pan: { x: number; y: number }) => void;
  setFilterType: (type: string | null) => void;
  setLayout: (layout: "force" | "hierarchical" | "radial") => void;
  resetView: () => void;
}

export const useGraphStore = create<GraphState>((set) => ({
  graph: null,
  selectedNode: null,
  hoveredNode: null,
  zoom: 1,
  pan: { x: 0, y: 0 },
  filterType: null,
  layout: "force",

  setGraph: (graph) => set({ graph }),
  selectNode: (node) => set({ selectedNode: node }),
  setHoveredNode: (node) => set({ hoveredNode: node }),
  setZoom: (zoom) => set({ zoom: Math.max(0.1, Math.min(5, zoom)) }),
  setPan: (pan) => set({ pan }),
  setFilterType: (type) => set({ filterType: type }),
  setLayout: (layout) => set({ layout }),

  resetView: () => set({ zoom: 1, pan: { x: 0, y: 0 }, selectedNode: null, filterType: null }),
}));

export function useGraphData() {
  return useGraphStore((s) => s.graph);
}

export function useGraphSelection() {
  return useGraphStore((s) => ({ selectedNode: s.selectedNode, hoveredNode: s.hoveredNode }));
}

export function useGraphView() {
  return useGraphStore((s) => ({ zoom: s.zoom, pan: s.pan }));
}

export function useGraphFilters() {
  return useGraphStore((s) => ({ filterType: s.filterType, layout: s.layout }));
}