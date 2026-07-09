import { describe, it, expect, vi, beforeEach } from "vitest";
import { commandRegistry, type Command, type CommandContext } from "@/infrastructure/commands";

const mockCtx: CommandContext = {
  navigate: vi.fn(),
  toggleTheme: vi.fn(),
  system: {} as any,
};

describe("CommandRegistry", () => {
  // Nota: Nao ha metodo clear/unregister no CommandRegistry
  // Os testes acumulam comandos, mas sao independentes

  it("should register and find commands via getAll", () => {
    const cmd: Command = {
      id: "test", label: "Test", keywords: ["t"],
      icon: vi.fn() as any, action: vi.fn(), category: "actions",
    };
    commandRegistry.register(cmd);
    expect(commandRegistry.getAll()).toHaveLength(1);
    expect(commandRegistry.getAll()[0].id).toBe("test");
  });

  it("should register many commands", () => {
    const before = commandRegistry.getAll().length;
    const c1: Command = { id: "a", label: "A", keywords: [], icon: vi.fn() as any, action: vi.fn(), category: "navigation" };
    const c2: Command = { id: "b", label: "B", keywords: [], icon: vi.fn() as any, action: vi.fn(), category: "actions" };
    commandRegistry.registerMany([c1, c2]);
    expect(commandRegistry.getAll()).toHaveLength(before + 2);
  });

  it("should search by label", () => {
    commandRegistry.register({ id: "x", label: "MyCommand", keywords: [], icon: vi.fn() as any, action: vi.fn(), category: "actions" });
    expect(commandRegistry.search("My")).toHaveLength(1);
    expect(commandRegistry.search("zzz")).toHaveLength(0);
  });

  it("should execute a command and throw for unknown", () => {
    const action = vi.fn();
    commandRegistry.register({ id: "exec", label: "Exec", keywords: [], icon: vi.fn() as any, action, category: "actions" });
    commandRegistry.execute("exec", mockCtx);
    expect(action).toHaveBeenCalledWith(mockCtx);
    expect(() => commandRegistry.execute("unknown", mockCtx)).toThrow();
  });
});