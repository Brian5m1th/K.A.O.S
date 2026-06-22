import { eventBus } from "@/shared/lib/event-bus";
import { CodeIntrospector, IntrospectionResult } from "./code-introspector";
import { FeatureExtractor, DetectedFeature } from "./feature-extractor";

export type SyncEvent = "docs:auto-updated" | "docs:sync-complete" | "docs:sync-error";

export interface SyncResult {
  timestamp: string;
  featuresDetected: number;
  sddsGenerated: number;
  errors: string[];
}

export class DocSyncEngine {
  private static _interval: number | null = null;
  private static _intervalId: ReturnType<typeof setInterval> | null = null;
  private static _running = false;

  static start(intervalMs: number = 60000): void {
    if (this._running) return;
    this._running = true;
    this._intervalId = setInterval(() => this._sync(), intervalMs);
    this._sync();
  }

  static stop(): void {
    if (this._intervalId) {
      clearInterval(this._intervalId);
      this._intervalId = null;
    }
    this._running = false;
  }

  static isRunning(): boolean {
    return this._running;
  }

  static async runOnce(): Promise<SyncResult> {
    return this._sync();
  }

  private static async _sync(): Promise<SyncResult> {
    const result: SyncResult = {
      timestamp: new Date().toISOString(),
      featuresDetected: 0,
      sddsGenerated: 0,
      errors: [],
    };

    try {
      const introspection = await CodeIntrospector.scanFromApi();
      const features = FeatureExtractor.extractFromApiResponse(introspection);
      result.featuresDetected = features.length;

      for (const feature of features) {
        try {
          const response = await fetch("/api/audit/generate-feature-node", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              featureId: feature.id,
              featureName: feature.name,
              featureType: feature.type,
              phase: "auto-detected",
              tags: [feature.type],
              links: [],
              description: `Auto-detected ${feature.type}: ${feature.name}`,
              responsibilities: [`Manage ${feature.name}`],
              emits: [],
              usedBy: [],
            }),
          });
          if (response.ok) {
            result.sddsGenerated++;
          }
        } catch {
          result.errors.push(`Failed to generate SDD for ${feature.id}`);
        }
      }

      eventBus.emit({
        type: "docs:auto-updated",
        payload: {
          timestamp: result.timestamp,
          featuresDetected: result.featuresDetected,
          sddsGenerated: result.sddsGenerated,
        },
      });
    } catch (err) {
      const msg = err instanceof Error ? err.message : String(err);
      result.errors.push(msg);
      eventBus.emit({
        type: "docs:sync-error",
        payload: { timestamp: result.timestamp, error: msg },
      });
    }

    return result;
  }
}