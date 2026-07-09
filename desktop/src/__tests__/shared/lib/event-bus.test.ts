import { describe, it, expect, vi, beforeEach } from "vitest";
import { eventBus, type BusEvent } from "@/shared/lib/event-bus";

describe("EventBus", () => {
  beforeEach(() => {
    // @ts-expect-error - acesso ao array de listeners para limpeza
    eventBus._listeners?.forEach((_, key) => eventBus.off(key));
    vi.clearAllMocks();
  });

  describe("on / emit", () => {
    it("should register a listener and receive events", () => {
      const handler = vi.fn();
      eventBus.on("test:event", handler);

      eventBus.emit({ type: "test:event", payload: { data: 123 } });

      expect(handler).toHaveBeenCalledTimes(1);
      expect(handler).toHaveBeenCalledWith({
        type: "test:event",
        payload: { data: 123 },
      });
    });

    it("should not notify listeners of other event types", () => {
      const handler = vi.fn();
      eventBus.on("other:event", handler);

      eventBus.emit({ type: "test:event", payload: {} });

      expect(handler).not.toHaveBeenCalled();
    });

    it("should support multiple listeners for the same event", () => {
      const handler1 = vi.fn();
      const handler2 = vi.fn();
      eventBus.on("multi:event", handler1);
      eventBus.on("multi:event", handler2);

      eventBus.emit({ type: "multi:event", payload: { id: 1 } });

      expect(handler1).toHaveBeenCalledTimes(1);
      expect(handler2).toHaveBeenCalledTimes(1);
    });

    it("should handle events with no listeners gracefully", () => {
      expect(() => {
        eventBus.emit({ type: "unregistered:event", payload: {} });
      }).not.toThrow();
    });
  });

  describe("off", () => {
    it("should remove a specific listener", () => {
      const handler = vi.fn();
      eventBus.on("test:event", handler);

      eventBus.off("test:event", handler);
      eventBus.emit({ type: "test:event", payload: {} });

      expect(handler).not.toHaveBeenCalled();
    });

    it("should keep other listeners intact when removing one", () => {
      const handler1 = vi.fn();
      const handler2 = vi.fn();
      eventBus.on("test:event", handler1);
      eventBus.on("test:event", handler2);

      eventBus.off("test:event", handler1);
      eventBus.emit({ type: "test:event", payload: {} });

      expect(handler1).not.toHaveBeenCalled();
      expect(handler2).toHaveBeenCalledTimes(1);
    });
  });

  describe("once", () => {
    it("should fire only once and then auto-remove", () => {
      const handler = vi.fn();
      eventBus.once("one:time", handler);

      eventBus.emit({ type: "one:time", payload: { count: 1 } });
      eventBus.emit({ type: "one:time", payload: { count: 2 } });

      expect(handler).toHaveBeenCalledTimes(1);
    });
  });

  describe("stream events", () => {
    it("should handle chat:stream-start event", () => {
      const handler = vi.fn();
      eventBus.on("chat:stream-start", handler);

      eventBus.emit({
        type: "chat:stream-start",
        payload: { input: "Hello" },
      });

      expect(handler).toHaveBeenCalledWith({
        type: "chat:stream-start",
        payload: { input: "Hello" },
      });
    });

    it("should handle chat:stream-token event", () => {
      const handler = vi.fn();
      eventBus.on("chat:stream-token", handler);

      eventBus.emit({
        type: "chat:stream-token",
        payload: { token: "Hello" },
      });

      expect(handler).toHaveBeenCalledWith({
        type: "chat:stream-token",
        payload: { token: "Hello" },
      });
    });

    it("should handle chat:stream-end event", () => {
      const handler = vi.fn();
      eventBus.on("chat:stream-end", handler);

      eventBus.emit({
        type: "chat:stream-end",
        payload: { fullText: "Hello world", model: "kaos" },
      });

      expect(handler).toHaveBeenCalledWith({
        type: "chat:stream-end",
        payload: { fullText: "Hello world", model: "kaos" },
      });
    });

    it("should handle chat:error event", () => {
      const handler = vi.fn();
      eventBus.on("chat:error", handler);

      eventBus.emit({
        type: "chat:error",
        payload: { message: "Connection failed" },
      });

      expect(handler).toHaveBeenCalledWith({
        type: "chat:error",
        payload: { message: "Connection failed" },
      });
    });

    it("should handle tool:start event", () => {
      const handler = vi.fn();
      eventBus.on("tool:start", handler);

      const toolEvent = {
        type: "tool:start" as const,
        payload: { tool: "search", args: { query: "test" } },
      };
      eventBus.emit(toolEvent);

      expect(handler).toHaveBeenCalledWith(toolEvent);
    });

    it("should handle update:available event", () => {
      const handler = vi.fn();
      eventBus.on("update:available", handler);

      eventBus.emit({
        type: "update:available",
        payload: { version: "2.2.0" },
      });

      expect(handler).toHaveBeenCalledWith({
        type: "update:available",
        payload: { version: "2.2.0" },
      });
    });
  });
});