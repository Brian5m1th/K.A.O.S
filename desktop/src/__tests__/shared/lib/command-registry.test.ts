import { describe, it, expect, vi, beforeEach } from "vitest";
import {
  commandRegistry,
  Command,
} from "@/shared/lib/command-registry";

describe("CommandRegistry", () => {
  beforeEach(() => {
    commandRegistry.clear();
  });

  describe("register", () => {
    it("should register a new command", () => {
      const command: Command = {
        id: "test-command",
        name: "Test Command",
        handler: vi.fn(),
      };

      commandRegistry.register(command);
      const retrieved = commandRegistry.get("test-command");
      expect(retrieved).toEqual(command);
    });

    it("should overwrite existing command with same id", () => {
      const cmd1: Command = { id: "same-id", name: "First", handler: vi.fn() };
      const cmd2: Command = {
        id: "same-id",
        name: "Second",
        handler: vi.fn(),
      };

      commandRegistry.register(cmd1);
      commandRegistry.register(cmd2);

      expect(commandRegistry.get("same-id")?.name).toBe("Second");
    });
  });

  describe("get", () => {
    it("should return undefined for non-registered command", () => {
      expect(commandRegistry.get("non-existent")).toBeUndefined();
    });
  });

  describe("execute", () => {
    it("should execute a registered command", () => {
      const handler = vi.fn(() => "executed");
      commandRegistry.register({
        id: "my-cmd",
        name: "My Command",
        handler,
      });

      const result = commandRegistry.execute("my-cmd", { arg: 1 });

      expect(handler).toHaveBeenCalledWith({ arg: 1 });
      expect(result).toBe("executed");
    });

    it("should throw for non-registered command", () => {
      expect(() =>
        commandRegistry.execute("unknown-cmd", {})
      ).toThrowError(
        expect.objectContaining({
          message: expect.stringContaining("unknown-cmd"),
        })
      );
    });
  });

  describe("list", () => {
    it("should return all registered command ids", () => {
      commandRegistry.register({
        id: "cmd-a",
        name: "Command A",
        handler: vi.fn(),
      });
      commandRegistry.register({
        id: "cmd-b",
        name: "Command B",
        handler: vi.fn(),
      });

      const ids = commandRegistry.list();
      expect(ids).toContain("cmd-a");
      expect(ids).toContain("cmd-b");
      expect(ids).toHaveLength(2);
    });

    it("should return empty array when no commands are registered", () => {
      expect(commandRegistry.list()).toEqual([]);
    });
  });

  describe("clear", () => {
    it("should remove all commands", () => {
      commandRegistry.register({
        id: "cmd",
        name: "Cmd",
        handler: vi.fn(),
      });

      commandRegistry.clear();
      expect(commandRegistry.list()).toEqual([]);
    });
  });
});