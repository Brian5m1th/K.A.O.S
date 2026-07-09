import { describe, it, expect, vi, beforeEach } from "vitest";
import { eventBus } from "@/infrastructure/event-bus";

describe("EventBus", () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe("on / emit", () => {
    it("should register a listener and receive events", () => {
      const handler = vi.fn();
      eventBus.on("chat:stream-start", handler);

      eventBus.emit({ type: "chat:stream-start", payload: { model: "kaos" } });

      expect(handler).toHaveBeenCalledTimes(1);
      expect(handler).toHaveBeenCalledWith({
        type: "chat:stream-start",
        payload: { model: "kaos" },
      });
    });

    it("should handle events with no listeners gracefully", () => {
      expect(() => {
        eventBus.emit({ type: "chat:stream-start", payload: { model: "kaos" } });
      }).not.toThrow();
    });
  });

  describe("off", () => {
    it("should remove a specific listener", () => {
      const handler = vi.fn();
      eventBus.on("chat:stream-start", handler);

      eventBus.off("chat:stream-start", handler);
      eventBus.emit({ type: "chat:stream-start", payload: { model: "kaos" } });

      expect(handler).not.toHaveBeenCalled();
    });
  });

  describe("stream events", () => {
    it("should handle chat:stream-start event", () => {
      const handler = vi.fn();
      eventBus.on("chat:stream-start", handler);

      eventBus.emit({ type: "chat:stream-start", payload: { model: "kaos" } });

      expect(handler).toHaveBeenCalledWith({
        type: "chat:stream-start",
        payload: { model: "kaos" },
      });
    });

    it("should handle chat:stream-end event", () => {
      const handler = vi.fn();
      eventBus.on("chat:stream-end", handler);

      eventBus.emit({ type: "chat:stream-end", payload: { fullText: "Hello world" } });

      expect(handler).toHaveBeenCalledWith({
        type: "chat:stream-end",
        payload: { fullText: "Hello world" },
      });
    });

    it("should handle update:available event", () => {
      const handler = vi.fn();
      eventBus.on("update:available", handler);

      eventBus.emit({
        type: "update:available",
        payload: { version: "2.2.0", date: "2025-06-01" },
      });

      expect(handler).toHaveBeenCalledWith({
        type: "update:available",
        payload: { version: "2.2.0", date: "2025-06-01" },
      });
    });
  });
});