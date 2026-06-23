from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional
import re
import yaml

from loguru import logger
from app.audit.runtime_resolver import RuntimePathResolver


@dataclass
class VaultNode:
    id: str
    title: str
    type: str
    owner: str = "shared"
    status: str = "unknown"
    tags: list[str] = field(default_factory=list)
    links: list[str] = field(default_factory=list)
    path: str = ""
    content: str = ""
    wikilinks: list[str] = field(default_factory=list)
    drift_score: float = 0.0
    created: str = ""
    updated: str = ""


class VaultReader:
    @classmethod
    def get_scan_dirs(cls) -> list[Path]:
        root = RuntimePathResolver.project_root()
        return [
            root / "docs" / "sdd",
            root / "docs" / "architecture",
            root / "docs" / "guides",
            root / "docs" / "api",
            root / "docs" / "features",
            root / "docs" / "wiki",
            root / ".opencode" / "plans",
        ]

    @classmethod
    def scan_all(cls) -> list[VaultNode]:
        nodes: list[VaultNode] = []
        seen_ids: set[str] = set()

        scan_dirs = cls.get_scan_dirs()
        for scan_dir in scan_dirs:
            if not scan_dir.exists():
                continue
            for md_file in scan_dir.rglob("*.md"):
                try:
                    node = cls._parse_file(md_file)
                    if node and node.id not in seen_ids:
                        seen_ids.add(node.id)
                        nodes.append(node)
                except Exception as e:
                    logger.warning(f"[vault_reader] error parsing {md_file}: {e}")

        logger.info(
            f"[vault_reader] scanned {len(nodes)} nodes from {len(scan_dirs)} dirs"
        )
        return nodes

    @classmethod
    def scan_dir(cls, directory: Path) -> list[VaultNode]:
        nodes: list[VaultNode] = []
        if not directory.exists():
            return nodes
        for md_file in directory.rglob("*.md"):
            try:
                node = cls._parse_file(md_file)
                if node:
                    nodes.append(node)
            except Exception:
                pass
        return nodes

    @classmethod
    def scan_single(cls, file_path: Path) -> Optional[VaultNode]:
        if not file_path.exists():
            return None
        return cls._parse_file(file_path)

    @classmethod
    def _parse_file(cls, path: Path) -> Optional[VaultNode]:
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            return None

        meta, body = cls._parse_frontmatter(content)
        if not meta:
            return None

        node_id = meta.get("id", path.stem.lower().replace(" ", "-"))
        wikilinks = cls._extract_wikilinks(content)

        return VaultNode(
            id=node_id,
            title=meta.get("title", path.stem),
            type=meta.get("type", "unknown"),
            owner=meta.get("owner", "shared"),
            status=meta.get("status", "unknown"),
            tags=meta.get("tags", []),
            links=meta.get("links", []),
            path=path.resolve()
            .relative_to(RuntimePathResolver.project_root())
            .as_posix(),
            content=body.strip(),
            wikilinks=wikilinks,
            drift_score=0.0,
            created=meta.get("created", ""),
            updated=meta.get("updated", ""),
        )

    @classmethod
    def _parse_frontmatter(cls, content: str) -> tuple[dict | None, str]:
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)", content, re.DOTALL)
        if not match:
            return None, content
        try:
            meta = yaml.safe_load(match.group(1))
            body = match.group(2)
            return meta if isinstance(meta, dict) else None, body
        except Exception:
            return None, content

    @classmethod
    def _extract_wikilinks(cls, content: str) -> list[str]:
        links = re.findall(r"\[\[([^\]]+?)(?:\|[^\]]+)?\]\]", content)
        return list(set(links))

    @classmethod
    def get_node_by_id(cls, node_id: str) -> Optional[VaultNode]:
        for node in cls.scan_all():
            if node.id == node_id:
                return node
        return None

    @classmethod
    def get_nodes_by_type(cls, node_type: str) -> list[VaultNode]:
        return [n for n in cls.scan_all() if n.type == node_type]

    @classmethod
    def get_orphan_nodes(cls) -> list[VaultNode]:
        nodes = cls.scan_all()
        linked_ids = set()
        for node in nodes:
            for link in node.links + node.wikilinks:
                linked_ids.add(link)
        return [n for n in nodes if n.id not in linked_ids and n.links and n.wikilinks]

    @classmethod
    def get_node_count_by_type(cls) -> dict[str, int]:
        counts: dict[str, int] = {}
        for node in cls.scan_all():
            counts[node.type] = counts.get(node.type, 0) + 1
        return counts

    @classmethod
    def get_total_links(cls) -> int:
        nodes = cls.scan_all()
        return sum(len(n.links) + len(n.wikilinks) for n in nodes)
