import { describe, it, expect, vi } from "vitest";

// Settings validation helpers (mirrors backend behavior)
interface SettingEntry {
  key: string;
  value: string;
  category: string;
}

function validateSettings(settings: SettingEntry[]): {
  valid: boolean;
  errors: string[];
} {
  const errors: string[] = [];
  const keys = new Set<string>();

  for (const [i, entry] of settings.entries()) {
    if (!entry.key || entry.key.trim().length === 0) {
      errors.push(`Entry ${i + 1}: key is required`);
      continue;
    }

    if (keys.has(entry.key)) {
      errors.push(`Duplicate key: "${entry.key}"`);
    }
    keys.add(entry.key);

    if (!entry.category || entry.category.trim().length === 0) {
      errors.push(`Entry "${entry.key}": category is required`);
    }

    if (entry.value === undefined || entry.value === null) {
      errors.push(`Entry "${entry.key}": value is required`);
    }
  }

  return { valid: errors.length === 0, errors };
}

function sanitizeSettingValue(value: string): string {
  return value
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .trim();
}

describe("useSettings", () => {
  describe("Settings validation", () => {
    it("should accept valid settings", () => {
      const settings: SettingEntry[] = [
        { key: "model", value: "gpt-4", category: "inference" },
        { key: "temperature", value: "0.7", category: "inference" },
      ];
      const result = validateSettings(settings);
      expect(result.valid).toBe(true);
    });

    it("should reject entries without key", () => {
      const settings: SettingEntry[] = [
        { key: "", value: "test", category: "test" },
      ];
      const result = validateSettings(settings);
      expect(result.valid).toBe(false);
    });

    it("should reject duplicate keys", () => {
      const settings: SettingEntry[] = [
        { key: "model", value: "gpt-4", category: "inference" },
        { key: "model", value: "claude-3", category: "inference" },
      ];
      const result = validateSettings(settings);
      expect(result.valid).toBe(false);
      expect(result.errors[0]).toContain("Duplicate key");
    });

    it("should reject entries without category", () => {
      const settings: SettingEntry[] = [
        { key: "test", value: "value", category: "" },
      ];
      const result = validateSettings(settings);
      expect(result.valid).toBe(false);
    });
  });

  describe("Value sanitization", () => {
    it("should trim whitespace", () => {
      expect(sanitizeSettingValue("  hello  ")).toBe("hello");
    });

    it("should escape HTML characters", () => {
      expect(sanitizeSettingValue('<script>alert("xss")</script>')).toBe(
        "&lt;script&gt;alert(&quot;xss&quot;)&lt;/script&gt;"
      );
    });

    it("should handle empty strings", () => {
      expect(sanitizeSettingValue("")).toBe("");
    });
  });
});
