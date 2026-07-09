import type { LucideIcon } from "lucide-react";
import type { useSystemStore } from "@/application/stores/system-store";

type SystemState = ReturnType<typeof useSystemStore.getState>;

export interface CommandContext {
  navigate: (path: string) => void;
  toggleTheme: () => void;
  system: SystemState;
}

export interface Command {
  id: string;
  label: string;
  keywords: string[];
  icon: LucideIcon;
  action: (ctx: CommandContext) => void;
  category: "navigation" | "actions" | "toggles";
}

class CommandRegistry {
  private commands: Map<string, Command> = new Map();

  register(command: Command) {
    this.commands.set(command.id, command);
  }

  registerMany(commands: Command[]) {
    commands.forEach((cmd) => this.commands.set(cmd.id, cmd));
  }

  getAll(): Command[] {
    return Array.from(this.commands.values());
  }

  search(query: string): Command[] {
    const q = query.toLowerCase();
    return this.getAll().filter(
      (cmd) =>
        cmd.label.toLowerCase().includes(q) ||
        cmd.keywords.some((k) => k.toLowerCase().includes(q)),
    );
  }

  execute(id: string, ctx: CommandContext) {
    const cmd = this.commands.get(id);
    if (!cmd) {
      throw new Error(`Command '${id}' not found`);
    }
    cmd.action(ctx);
  }
}

export const commandRegistry = new CommandRegistry();
