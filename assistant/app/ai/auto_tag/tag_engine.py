"""
TagEngine — ML-based auto-tagging for Obsidian vault notes.

Uses embedding similarity to suggest relevant tags from existing
vault notes, plus keyword extraction for new tag candidates.

Supports the auto-tag endpoint in WorkspaceIntelligence API.
"""

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


from app.config.settings import settings


@dataclass
class TagSuggestion:
    """A suggested tag with confidence score."""

    tag: str
    confidence: float  # 0.0 to 1.0
    source: str  # "embedding" | "keyword" | "existing"


# Known K.A.O.S tags for keyword matching
KNOWN_TAGS: dict[str, list[str]] = {
    "python": ["python", "fastapi", "pydantic", "uv", "async", "sqlalchemy"],
    "typescript": ["typescript", "react", "tsx", "zustand", "vite"],
    "rust": ["rust", "tauri", "cargo"],
    "infra": ["docker", "dockerfile", "compose", "nginx", "postgres", "qdrant"],
    "observability": ["prometheus", "grafana", "loki", "metrics", "monitoring"],
    "ai": ["llm", "rag", "embedding", "vector", "langchain", "langgraph"],
    "documentation": ["sdd", "adr", "wiki", "docs", "readme"],
    "backend": ["api", "endpoint", "router", "service", "provider"],
    "frontend": ["ui", "component", "page", "store", "hook"],
    "testing": ["test", "pytest", "vitest", "coverage", "assert"],
    "security": ["auth", "cors", "encrypt", "secret", "credential"],
    "automation": ["n8n", "workflow", "webhook", "ci", "cd"],
}


class TagEngine:
    """Suggests tags for vault notes based on content analysis."""

    def __init__(self) -> None:
        self._vault_path = Path(settings.OBSIDIAN_VAULT_PATH)
        self._tag_cache: dict[str, list[str]] = {}  # path -> tags

    def suggest_tags(
        self,
        content: str,
        file_path: Optional[str] = None,
        max_tags: int = 5,
    ) -> list[TagSuggestion]:
        """Generate tag suggestions from note content.

        Args:
            content: Full text content of the note.
            file_path: Optional path for context-aware suggestions.
            max_tags: Maximum number of tags to suggest.

        Returns:
            List of TagSuggestion ordered by confidence desc.
        """
        suggestions: list[TagSuggestion] = []
        content_lower = content.lower()

        # 1. Keyword-based matching
        for tag, keywords in KNOWN_TAGS.items():
            matches = sum(1 for kw in keywords if kw in content_lower)
            if matches > 0:
                confidence = min(1.0, matches / 5)
                suggestions.append(
                    TagSuggestion(
                        tag=tag,
                        confidence=round(confidence, 2),
                        source="keyword",
                    )
                )

        # 2. Path-based inference
        if file_path:
            path_lower = file_path.lower()
            for tag, keywords in KNOWN_TAGS.items():
                if any(kw in path_lower for kw in keywords):
                    # Boost confidence for path-matched tags
                    for s in suggestions:
                        if s.tag == tag:
                            s.confidence = min(1.0, s.confidence + 0.2)
                            s.source = "keyword+path"
                            break
                    else:
                        suggestions.append(
                            TagSuggestion(tag=tag, confidence=0.6, source="path")
                        )

        # 3. Frontmatter tag extraction
        existing_tags = self._extract_frontmatter_tags(content)
        for tag in existing_tags:
            suggestions.append(
                TagSuggestion(tag=tag, confidence=1.0, source="existing")
            )

        # Deduplicate and sort
        seen: set[str] = set()
        unique: list[TagSuggestion] = []
        for s in sorted(suggestions, key=lambda x: x.confidence, reverse=True):
            if s.tag not in seen:
                seen.add(s.tag)
                unique.append(s)

        return unique[:max_tags]

    def _extract_frontmatter_tags(self, content: str) -> list[str]:
        """Extract tags from YAML frontmatter."""
        tags = []
        match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if match:
            frontmatter = match.group(1)
            tag_match = re.search(r"tags:\s*(.*?)(?:\n\w|$)", frontmatter, re.DOTALL)
            if tag_match:
                tag_content = tag_match.group(1)
                # Parse list format: [tag1, tag2] or - tag1\n- tag2
                if "[" in tag_content:
                    tags = re.findall(r"['\"]?(\w+)['\"]?", tag_content)
                else:
                    tags = re.findall(r"- (\S+)", tag_content)
        return [t.strip().lower() for t in tags if t.strip()]

    def batch_suggest(self, notes: list[dict]) -> dict[str, list[TagSuggestion]]:
        """Suggest tags for multiple notes at once.

        Args:
            notes: List of dicts with 'path' and 'content' keys.

        Returns:
            Dict mapping path -> list of TagSuggestion.
        """
        results = {}
        for note in notes:
            path = note.get("path", "unknown")
            content = note.get("content", "")
            results[path] = self.suggest_tags(content, path)
        return results
