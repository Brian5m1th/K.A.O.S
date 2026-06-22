import { GraphData } from "./graph-builder";
import { LayoutResult } from "./layout-engine";

export class GraphExport {
  static toJSON(graph: GraphData): string {
    return JSON.stringify(graph, null, 2);
  }

  static downloadJSON(graph: GraphData, filename?: string): void {
    const blob = new Blob([this.toJSON(graph)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = filename || `kaos-graph-${Date.now()}.json`;
    a.click();
    URL.revokeObjectURL(url);
  }

  static toGraphML(graph: GraphData): string {
    const lines: string[] = [];
    lines.push('<?xml version="1.0" encoding="UTF-8"?>');
    lines.push('<graphml xmlns="http://graphml.graphdrawing.org/xmlns">');
    lines.push("  <graph edgedefault=\"directed\">");

    for (const node of graph.nodes) {
      lines.push(`    <node id="${node.id}">`);
      lines.push("      <data key=\"label\">" + this._escapeXml(node.label) + "</data>");
      lines.push("      <data key=\"type\">" + this._escapeXml(node.type) + "</data>");
      if (node.phase) lines.push("      <data key=\"phase\">" + this._escapeXml(node.phase) + "</data>");
      if (node.status) lines.push("      <data key=\"status\">" + this._escapeXml(node.status) + "</data>");
      lines.push("    </node>");
    }

    for (const edge of graph.edges) {
      lines.push(`    <edge source="${edge.from}" target="${edge.to}"`);
      lines.push(`      <data key="relation">${this._escapeXml(edge.relation)}</data>`);
      lines.push("    </edge>");
    }

    lines.push("  </graph>");
    lines.push("</graphml>");
    return lines.join("\n");
  }

  static downloadGraphML(graph: GraphData, filename?: string): void {
    const blob = new Blob([this.toGraphML(graph)], { type: "application/xml" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = filename || `kaos-graph-${Date.now()}.graphml`;
    a.click();
    URL.revokeObjectURL(url);
  }

  static toSVG(layout: LayoutResult): string {
    const padding = 40;
    const w = layout.width + padding * 2;
    const h = layout.height + padding * 2;

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

    let svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}">\n`;
    svg += `  <rect width="${w}" height="${h}" fill="#f9fafb" rx="8"/>\n`;

    for (const edge of layout.edges) {
      const fromNode = layout.nodes.find((n) => n.id === edge.from);
      const toNode = layout.nodes.find((n) => n.id === edge.to);
      if (!fromNode || !toNode) continue;
      svg += `  <line x1="${fromNode.x + padding}" y1="${fromNode.y + padding}" x2="${toNode.x + padding}" y2="${toNode.y + padding}" stroke="#d1d5db" stroke-width="1.5" />\n`;
    }

    for (const node of layout.nodes) {
      const color = typeColors[node.type] || "#6b7280";
      const cx = node.x + padding;
      const cy = node.y + padding;
      svg += `  <circle cx="${cx}" cy="${cy}" r="6" fill="${color}" />\n`;
      svg += `  <text x="${cx + 10}" y="${cy + 4}" font-size="10" fill="#374151">${this._escapeXml(node.label.length > 20 ? node.label.substring(0, 20) + "..." : node.label)}</text>\n`;
    }

    svg += "</svg>";
    return svg;
  }

  static downloadSVG(layout: LayoutResult, filename?: string): void {
    const blob = new Blob([this.toSVG(layout)], { type: "image/svg+xml" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = filename || `kaos-graph-${Date.now()}.svg`;
    a.click();
    URL.revokeObjectURL(url);
  }

  private static _escapeXml(str: string): string {
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
}