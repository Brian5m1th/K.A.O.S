import type { ToolEvent, ToolEventType } from "./tool-schema";
import type { AgentStatus } from "./stores/agent-store";

export interface SystemMetrics {
  cpu: number;
  vramUsed: number;
  latency: number;
  vectorCount: number;
  tokenRate: number;
}

export type AppEvent =
  | { type: ToolEventType; payload: ToolEvent }
  | { type: "agent:status"; payload: { id: string; status: AgentStatus } }
  | { type: "agent:message"; payload: { id: string; text: string } }
  | { type: "system:metrics"; payload: SystemMetrics }
  | { type: "system:status"; payload: "online" | "degraded" | "offline" }
  | { type: "chat:stream-start"; payload: { model: string } }
  | { type: "chat:stream-token"; payload: { token: string } }
  | { type: "chat:stream-end"; payload: { fullText: string } }
  | { type: "chat:error"; payload: { message: string } };

type Listener = (event: AppEvent) => void;

class EventBus {
  private listeners = new Map<string, Set<Listener>>();
  private wildcardListeners = new Set<Listener>();

  on(type: AppEvent["type"], listener: Listener) {
    if (!this.listeners.has(type)) {
      this.listeners.set(type, new Set());
    }
    this.listeners.get(type)!.add(listener);
    return () => this.off(type, listener);
  }

  onAny(listener: Listener) {
    this.wildcardListeners.add(listener);
    return () => this.wildcardListeners.delete(listener);
  }

  off(type: AppEvent["type"], listener: Listener) {
    this.listeners.get(type)?.delete(listener);
  }

  emit(event: AppEvent) {
    const typeListeners = this.listeners.get(event.type);
    if (typeListeners) {
      typeListeners.forEach((fn) => {
        try {
          fn(event);
        } catch {
          // Silently handle listener errors
        }
      });
    }
    this.wildcardListeners.forEach((fn) => {
      try {
        fn(event);
      } catch {
        // Silently handle listener errors
      }
    });
  }

  clear() {
    this.listeners.clear();
    this.wildcardListeners.clear();
  }
}

export const eventBus = new EventBus();
