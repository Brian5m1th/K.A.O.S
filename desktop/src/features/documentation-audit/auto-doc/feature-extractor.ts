export interface DetectedFeature {
  id: string;
  name: string;
  type: "store" | "route" | "tool" | "agent" | "provider";
  sourceFiles: string[];
  confidence: "high" | "medium" | "low";
}

export class FeatureExtractor {
  static extract(codeRefs: string[]): DetectedFeature[] {
    const features: DetectedFeature[] = [];
    const seen = new Set<string>();

    for (const ref of codeRefs) {
      const name = this._inferFeatureName(ref);
      if (name && !seen.has(name)) {
        seen.add(name);
        features.push({
          id: name.replace(/\s+/g, "-").toLowerCase(),
          name,
          type: this._inferType(ref),
          sourceFiles: [ref],
          confidence: "high",
        });
      }
    }

    return features;
  }

  static extractFromApiResponse(response: any): DetectedFeature[] {
    const allRefs: string[] = [];
    for (const key of ["stores", "routes", "tools", "events", "agents", "providers"]) {
      if (Array.isArray(response[key])) {
        allRefs.push(...response[key]);
      }
    }
    return this.extract(allRefs);
  }

  private static _inferFeatureName(ref: string): string {
    const base = ref.split("/").pop() || ref;
    const name = base.replace(/\.(ts|tsx|py)$/, "");
    const readable = name
      .replace(/[-_]/g, " ")
      .replace(/([a-z])([A-Z])/g, "$1 $2")
      .replace(/^use/, "")
      .trim();
    return readable || name;
  }

  private static _inferType(ref: string): DetectedFeature["type"] {
    if (ref.includes("store")) return "store";
    if (ref.includes("route") || ref.includes("page")) return "route";
    if (ref.includes("tool")) return "tool";
    if (ref.includes("agent") || ref.includes("workflow")) return "agent";
    if (ref.includes("provider")) return "provider";
    return "tool";
  }
}