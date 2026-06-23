import { kaosFetch } from "@/shared/api/kaos-client";

export interface IntrospectionResult {
  stores: string[];
  routes: string[];
  tools: string[];
  events: string[];
  agents: string[];
  providers: string[];
}

export class CodeIntrospector {
  static scan(): IntrospectionResult {
    const allModules = this._findAllModules();
    return {
      stores: allModules.filter(m => m.includes("store") || m.includes("Store")),
      routes: allModules.filter(m => m.includes("page") || m.includes("route") || m.includes("Route")),
      tools: allModules.filter(m => m.includes("tool") || m.includes("Tool") || m.includes("schema")),
      events: allModules.filter(m => m.includes("event") || m.includes("Event") || m.includes("bus")),
      agents: allModules.filter(m => m.includes("agent") || m.includes("Agent") || m.includes("workflow")),
      providers: allModules.filter(m => m.includes("provider") || m.includes("Provider")),
    };
  }

  static async scanFromApi(): Promise<IntrospectionResult> {
    try {
      const response = await kaosFetch("/api/audit/scan-code", "", { method: "POST" });
      if (response.ok) {
        const data = await response.json();
        return {
          stores: data.stores || [],
          routes: data.routes || [],
          tools: data.tools || [],
          events: data.events || [],
          agents: data.agents || [],
          providers: data.providers || [],
        };
      }
    } catch {
    }
    return this.scan();
  }

  private static _findAllModules(): string[] {
    const knownModules = [
      "agent-store", "app-store", "auth-store", "chat-store", "system-store", "ui-store",
      "documentation", "observability", "orchestration", "pipelines", "settings", "vault",
      "command-palette", "sidebar", "topbar",
      "event-bus", "command-registry", "tool-schema",
      "useChatStream", "useProviderConfig", "useSystemMetrics", "useVaultInit", "useSettings",
      "kaos-client", "tauri-store-service",
    ];
    return knownModules;
  }
}