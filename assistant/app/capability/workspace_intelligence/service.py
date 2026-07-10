"""Workspace Intelligence Service.

SDD-KAOS-EVOLUTION-001: Central service to manage Vault/Workspace sanity, tags,
                       and semantic links.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any
import yaml
from loguru import logger

from app.config.settings import settings
from app.rag.embeddings.embedder import get_embedder
from app.providers.vector.qdrant import QdrantVectorStore


class WorkspaceIntelligenceService:
    """Service providing workspace analysis, duplicate detection, and tag/link suggestions."""

    def __init__(self, vault_path: str | None = None) -> None:
        self.vault_path = Path(vault_path or settings.OBSIDIAN_VAULT_PATH or "./vault")
        self.vector_store = QdrantVectorStore()

    def _read_note(self, note_path: Path) -> tuple[dict[str, Any], str]:
        """Parses frontmatter and content of a Markdown file."""
        if not note_path.exists():
            return {}, ""
        content = note_path.read_text(encoding="utf-8")
        
        frontmatter = {}
        body = content
        
        # Regex to parse frontmatter YAML
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if match:
            try:
                frontmatter = yaml.safe_load(match.group(1)) or {}
                body = content[match.end():]
            except Exception as e:
                logger.warning(f"[WorkspaceIntelligence] YAML parse fail for {note_path.name}: {e}")
                
        return frontmatter, body

    def _write_note(self, note_path: Path, frontmatter: dict[str, Any], body: str) -> None:
        """Saves frontmatter and content back to a Markdown file."""
        fm_yaml = yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False).strip()
        new_content = f"---\n{fm_yaml}\n---\n{body}"
        note_path.write_text(new_content, encoding="utf-8")

    async def auto_tag(self, relative_path: str) -> list[str]:
        """Auto tag note using semantic neighbors or content fallback."""
        abs_path = self.vault_path / relative_path.lstrip("/")
        if not abs_path.exists():
            logger.warning(f"File not found: {abs_path}")
            return []

        frontmatter, body = self._read_note(abs_path)
        
        # 1. Look for semantic tags in Qdrant (similar notes)
        suggested_tags = set()
        try:
            embedder = get_embedder()
            query_vector = embedder.embed_query(body[:1000])
            hits = await self.vector_store.search(settings.QDRANT_COLLECTION, query_vector, limit=5)
            
            for hit in hits:
                hit_abs_path = self.vault_path / hit.path.lstrip("/")
                if hit_abs_path.exists() and hit_abs_path != abs_path:
                    hit_fm, _ = self._read_note(hit_abs_path)
                    hit_tags = hit_fm.get("tags", [])
                    if isinstance(hit_tags, list):
                        suggested_tags.update(hit_tags)
                    elif isinstance(hit_tags, str):
                        suggested_tags.add(hit_tags)
        except Exception as e:
            logger.debug(f"[WorkspaceIntelligence] Qdrant search skipped/failed: {e}")

        # Heuristic fallback if no semantic tags found
        if not suggested_tags:
            # Match words longer than 5 chars that appear multiple times as placeholder tags
            words = re.findall(r"\b[a-zA-ZáéíóúâêîôûãõçÁÉÍÓÚÂÊÎÔÛÃÕÇ]{5,}\b", body.lower())
            freq = {}
            for w in words:
                freq[w] = freq.get(w, 0) + 1
            sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
            suggested_tags.update([word for word, count in sorted_words[:4]])

        # Update note frontmatter
        current_tags = frontmatter.get("tags", [])
        if isinstance(current_tags, str):
            current_tags = [current_tags]
        elif not isinstance(current_tags, list):
            current_tags = []
            
        tags_list = list(set(current_tags) | suggested_tags)
        frontmatter["tags"] = tags_list
        self._write_note(abs_path, frontmatter, body)
        
        logger.info(f"[WorkspaceIntelligence] Tagged '{relative_path}' with {tags_list}")
        return tags_list

    async def suggest_links(self, relative_path: str) -> list[dict[str, Any]]:
        """Recommends connections wikilink [[Other Note]] using cosine similarity."""
        abs_path = self.vault_path / relative_path.lstrip("/")
        if not abs_path.exists():
            return []

        _, body = self._read_note(abs_path)
        
        # Find existing links in note body
        existing_links = set(re.findall(r"\[\[(.*?)\]\]", body))
        
        recommendations = []
        try:
            embedder = get_embedder()
            query_vector = embedder.embed_query(body[:1000])
            hits = await self.vector_store.search(settings.QDRANT_COLLECTION, query_vector, limit=10)
            
            for hit in hits:
                hit_name = Path(hit.path).stem
                # Don't suggest if same file, already linked, or duplicate suggestion
                if (
                    hit.path != relative_path 
                    and hit_name not in existing_links 
                    and hit.score > 0.4
                ):
                    recommendations.append({
                        "path": hit.path,
                        "title": hit_name,
                        "score": round(hit.score, 4)
                    })
        except Exception as e:
            logger.debug(f"[WorkspaceIntelligence] Link suggestion skipped/failed: {e}")
            
        return recommendations

    def check_vault_health(self) -> dict[str, Any]:
        """Returns sanity metrics of the vault."""
        total_notes = 0
        missing_frontmatter = 0
        all_note_names = set()
        links_found = []

        if not self.vault_path.exists():
            return {"total_notes": 0, "healthy": False}

        for path in self.vault_path.glob("**/*.md"):
            total_notes += 1
            all_note_names.add(path.stem)
            
            content = path.read_text(encoding="utf-8")
            if not content.startswith("---"):
                missing_frontmatter += 1
                
            # Extract links
            links = re.findall(r"\[\[(.*?)\]\]", content)
            links_found.extend(links)

        # Basic health metric
        broken_links_count = sum(1 for link in links_found if link.split("|")[0] not in all_note_names)
        
        return {
            "total_notes": total_notes,
            "missing_frontmatter": missing_frontmatter,
            "broken_links": broken_links_count,
            "healthy": broken_links_count == 0 and missing_frontmatter == 0,
        }
