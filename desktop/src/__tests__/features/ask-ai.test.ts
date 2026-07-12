import { describe, it, expect } from "vitest";

// ChatInput validation helpers
function validateMessage(message: string): { valid: boolean; error?: string } {
  if (!message || message.trim().length === 0) {
    return { valid: false, error: "Message cannot be empty" };
  }
  if (message.length > 10000) {
    return { valid: false, error: "Message exceeds 10000 character limit" };
  }
  return { valid: true };
}

// ModelSelector validation helpers
function isValidModel(model: string, availableModels: string[]): boolean {
  if (!model) return false;
  if (availableModels.includes(model)) return true;
  // Allow custom model names (not in the list but non-empty)
  return model.trim().length > 0;
}

describe("AskAI features", () => {
  describe("ChatInput validation", () => {
    it("should reject empty messages", () => {
      expect(validateMessage("").valid).toBe(false);
      expect(validateMessage("   ").valid).toBe(false);
    });

    it("should accept valid messages", () => {
      expect(validateMessage("Hello, how are you?").valid).toBe(true);
      expect(validateMessage("What is the capital of France?").valid).toBe(true);
    });

    it("should reject overly long messages", () => {
      const longMsg = "a".repeat(10001);
      expect(validateMessage(longMsg).valid).toBe(false);
    });

    it("should accept messages at the limit", () => {
      const limitMsg = "a".repeat(10000);
      expect(validateMessage(limitMsg).valid).toBe(true);
    });
  });

  describe("ModelSelector validation", () => {
    const availableModels = ["gpt-4", "gpt-3.5-turbo", "claude-3", "ollama/llama3"];

    it("should recognize known models", () => {
      expect(isValidModel("gpt-4", availableModels)).toBe(true);
      expect(isValidModel("claude-3", availableModels)).toBe(true);
    });

    it("should accept custom model names", () => {
      expect(isValidModel("my-custom-model", availableModels)).toBe(true);
    });

    it("should reject empty model names", () => {
      expect(isValidModel("", availableModels)).toBe(false);
    });
  });
});
