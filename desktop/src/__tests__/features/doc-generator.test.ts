import { describe, it, expect } from "vitest";

// Document generator validation helpers (mirrors backend logic)
interface DocSection {
  title: string;
  content: string;
  type: "sdd" | "adr" | "guide" | "api";
}

function validateDocStructure(sections: DocSection[]): {
  valid: boolean;
  errors: string[];
} {
  const errors: string[] = [];

  if (!sections || sections.length === 0) {
    return { valid: false, errors: ["Document must have at least one section"] };
  }

  for (const [i, section] of sections.entries()) {
    if (!section.title || section.title.trim().length === 0) {
      errors.push(`Section ${i + 1}: title is required`);
    }
    if (!section.content || section.content.trim().length === 0) {
      errors.push(`Section ${i + 1} ("${section.title || "untitled"}"): content is required`);
    }
    if (!["sdd", "adr", "guide", "api"].includes(section.type)) {
      errors.push(`Section ${i + 1} ("${section.title}"): invalid type "${section.type}"`);
    }
  }

  return { valid: errors.length === 0, errors };
}

function generateFrontmatter(title: string, type: string, tags: string[]): string {
  const escaped = tags.map((t) => `  - ${t}`).join("\n");
  return [
    "---",
    `title: "${title}"`,
    `type: ${type}`,
    "tags:",
    escaped,
    "---",
  ].join("\n");
}

describe("DocGeneratorModal", () => {
  describe("Document structure validation", () => {
    it("should reject empty documents", () => {
      const result = validateDocStructure([]);
      expect(result.valid).toBe(false);
      expect(result.errors).toContain("Document must have at least one section");
    });

    it("should reject sections without title", () => {
      const sections: DocSection[] = [
        { title: "", content: "Some content", type: "sdd" },
      ];
      const result = validateDocStructure(sections);
      expect(result.valid).toBe(false);
      expect(result.errors[0]).toContain("title is required");
    });

    it("should reject sections without content", () => {
      const sections: DocSection[] = [
        { title: "My Section", content: "", type: "sdd" },
      ];
      const result = validateDocStructure(sections);
      expect(result.valid).toBe(false);
    });

    it("should reject invalid document types", () => {
      const sections: DocSection[] = [
        { title: "Bad Type", content: "Content", type: "invalid" as any },
      ];
      const result = validateDocStructure(sections);
      expect(result.valid).toBe(false);
      expect(result.errors[0]).toContain('invalid type "invalid"');
    });

    it("should accept valid documents", () => {
      const sections: DocSection[] = [
        { title: "Overview", content: "System overview", type: "sdd" },
        { title: "API Spec", content: "API endpoints", type: "api" },
      ];
      const result = validateDocStructure(sections);
      expect(result.valid).toBe(true);
      expect(result.errors).toHaveLength(0);
    });
  });

  describe("Frontmatter generation", () => {
    it("should generate valid YAML frontmatter", () => {
      const result = generateFrontmatter("Test Doc", "sdd", ["kaos", "backend"]);
      expect(result).toContain('title: "Test Doc"');
      expect(result).toContain("type: sdd");
      expect(result).toContain("- kaos");
      expect(result).toContain("- backend");
    });

    it("should handle empty tags list", () => {
      const result = generateFrontmatter("No Tags", "guide", []);
      expect(result).toContain("tags:");
      expect(result).not.toContain("-");
    });
  });
});
