import { commandRegistry } from "./command-registry";
import {
  LayoutDashboard,
  MessageSquare,
  GitBranch,
  Bot,
  Container,
  BookOpen,
  Activity,
  Settings,
  Sun,
} from "lucide-react";

export function initializeCommands() {
  commandRegistry.registerMany([
    {
      id: "go-dashboard",
      label: "Go to Dashboard",
      keywords: ["home", "dashboard", "início"],
      icon: LayoutDashboard,
      category: "navigation",
      action: (ctx) => ctx.navigate("/"),
    },
    {
      id: "go-chat",
      label: "Open Chat",
      keywords: ["chat", "conversar", "IA", "messages"],
      icon: MessageSquare,
      category: "navigation",
      action: (ctx) => ctx.navigate("/chat"),
    },
    {
      id: "go-orchestration",
      label: "Open Orchestration",
      keywords: ["workflow", "orquestração", "fluxo", "n8n"],
      icon: GitBranch,
      category: "navigation",
      action: (ctx) => ctx.navigate("/orchestration"),
    },
    {
      id: "go-agents",
      label: "Open Agents",
      keywords: ["agent", "agente", "modelo", "IA"],
      icon: Bot,
      category: "navigation",
      action: (ctx) => ctx.navigate("/agents"),
    },
    {
      id: "go-pipelines",
      label: "Open Pipelines",
      keywords: ["pipeline", "deploy", "CI", "CD"],
      icon: Container,
      category: "navigation",
      action: (ctx) => ctx.navigate("/pipelines"),
    },
    {
      id: "go-vault",
      label: "Open Knowledge Vault",
      keywords: ["knowledge", "vault", "obsidian", "notes", "notas"],
      icon: BookOpen,
      category: "navigation",
      action: (ctx) => ctx.navigate("/vault"),
    },
    {
      id: "go-observability",
      label: "Open Observability",
      keywords: ["metrics", "monitoring", "logs", "grafana", "prometheus"],
      icon: Activity,
      category: "navigation",
      action: (ctx) => ctx.navigate("/observability"),
    },
    {
      id: "go-settings",
      label: "Open Settings",
      keywords: ["config", "settings", "preferences", "preferências"],
      icon: Settings,
      category: "navigation",
      action: (ctx) => ctx.navigate("/settings"),
    },
    {
      id: "toggle-theme",
      label: "Toggle Theme",
      keywords: ["theme", "tema", "dark", "light", "dark mode"],
      icon: Sun,
      category: "toggles",
      action: (ctx) => ctx.toggleTheme(),
    },
  ]);
}
