from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
import json
from typing import Optional
from pathlib import Path

from loguru import logger

from app.ai.vault_analyzer.vault_reader import VaultReader
from app.audit.feature_registry import FeatureRegistry
from app.audit.sdd_resolver import SDDResolver
from app.audit.runtime_resolver import RuntimePathResolver


@dataclass
class KnowledgeGraph:
    nodes: list[dict] = field(default_factory=list)
    edges: list[dict] = field(default_factory=list)
    features: list[dict] = field(default_factory=list)
    sdds: list[dict] = field(default_factory=list)
    workflows: list[dict] = field(default_factory=list)
    agents: list[dict] = field(default_factory=list)
    generated_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def to_dict(self) -> dict:
        return {
            "version": "1.0",
            "generated_at": self.generated_at,
            "total_nodes": len(self.nodes),
            "total_edges": len(self.edges),
            "nodes": self.nodes,
            "edges": self.edges,
            "features": self.features,
            "sdds": self.sdds,
            "workflows": self.workflows,
            "agents": self.agents,
        }


class KnowledgeGraphBuilder:
    """Builds knowledge graph from Graphify, Vault, and DRL sources.

    Deprecates the old CodeScanner regex-based scanner in favor of
    Graphify's AST-level graph.json (12k+ nodes, 22k+ edges).
    """

    GRAPHIFY_PATH = Path("graphify-out/graph.json")

    @classmethod
    def _load_graphify_graph(cls) -> Optional[dict]:
        """Load graphify-out/graph.json, return dict with 'files' and 'edges'."""
        gf_path = RuntimePathResolver.project_root() / cls.GRAPHIFY_PATH
        if not gf_path.exists():
            logger.warning(
                f"[knowledge_graph] Graphify graph not found at {gf_path}. "
                "Run `graphify update .` to generate it."
            )
            return None

        try:
            with open(gf_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            logger.error(f"[knowledge_graph] Failed to load Graphify graph: {e}")
            return None

        # Aggregate file-level nodes
        file_nodes: dict[str, dict] = {}
        for node in data.get("nodes", []):
            source_file = node.get("source_file", "")
            if not source_file:
                continue
            if source_file not in file_nodes:
                file_nodes[source_file] = {
                    "id": source_file,
                    "title": Path(source_file).name,
                    "type": KnowledgeGraphBuilder._infer_type(source_file),
                    "source": "code",
                    "path": source_file,
                }

        # Aggregate file-level edges
        file_edges = []
        seen_file_edges = set()
        for link in data.get("links", []):
            src = link.get("source", "")
            tgt = link.get("target", "")
            src_file = cls._resolve_source_file(data, src)
            tgt_file = cls._resolve_source_file(data, tgt)
            if src_file and tgt_file and src_file != tgt_file:
                edge_key = f"{src_file}|{tgt_file}"
                if edge_key not in seen_file_edges:
                    seen_file_edges.add(edge_key)
                    file_edges.append({
                        "source": src_file,
                        "target": tgt_file,
                        "relation": cls._map_relation(link.get("relation", "uses")),
                    })

        return {"files": file_nodes, "edges": file_edges}

    @staticmethod
    def _resolve_source_file(data: dict, symbol_id: str) -> Optional[str]:
        for node in data.get("nodes", []):
            if node.get("id") == symbol_id:
                return node.get("source_file") or None
        return None

    @staticmethod
    def _map_relation(relation: str) -> str:
        mapping = {
            "contains": "uses", "imports": "uses", "imports_from": "uses",
            "calls": "uses", "inherits": "uses", "implements": "implements",
            "documents": "documents", "depends_on": "depends_on",
            "emits": "emits", "owns": "owns", "re_exports": "uses",
        }
        return mapping.get(relation, "uses")

    @staticmethod
    def build() -> KnowledgeGraph:
        vault_nodes = VaultReader.scan_all()
        FeatureRegistry.load_from_json()
        SDDResolver.scan_all_sdds()

        # ── Load Graphify graph as the code relationship source ──
        graphify_data = KnowledgeGraphBuilder._load_graphify_graph()

        kg = KnowledgeGraph()
        seen_ids: set[str] = set()

        for vn in vault_nodes:
            entry = {
                "id": vn.id,
                "title": vn.title,
                "type": vn.type,
                "owner": vn.owner,
                "status": vn.status,
                "tags": vn.tags,
                "links": vn.links,
                "wikilinks": vn.wikilinks,
                "source": "vault",
                "path": vn.path,
            }
            kg.nodes.append(entry)
            seen_ids.add(vn.id)

            if vn.type == "feature":
                kg.features.append(entry)
            elif vn.type == "sdd":
                kg.sdds.append(entry)
            elif vn.type == "agent":
                kg.agents.append(entry)
            elif vn.type == "workflow":
                kg.workflows.append(entry)

            for link in vn.links:
                kg.edges.append(
                    {"source": vn.id, "target": link, "relation": "depends_on"}
                )
            for wl in vn.wikilinks:
                kg.edges.append(
                    {"source": vn.id, "target": wl, "relation": "documents"}
                )

        for feat in FeatureRegistry.list():
            fid = f"feature:{feat.id}"
            if fid not in seen_ids:
                entry = {
                    "id": fid,
                    "title": feat.name,
                    "type": "feature",
                    "status": feat.status,
                    "phase": feat.phase,
                    "source": "drl",
                    "docs": feat.docs,
                    "code_refs": feat.code_refs,
                }
                kg.nodes.append(entry)
                kg.features.append(entry)
                seen_ids.add(fid)

        # ── Graphify code nodes (aggregated at file level) ───────
        if graphify_data:
            for file_id, file_info in graphify_data.get("files", {}).items():
                if file_id not in seen_ids:
                    entry = {
                        "id": file_id,
                        "title": file_info["title"],
                        "type": file_info["type"],
                        "source": "code",
                    }
                    kg.nodes.append(entry)
                    seen_ids.add(file_id)

            for edge in graphify_data.get("edges", []):
                if edge["source"] in seen_ids and edge["target"] in seen_ids:
                    kg.edges.append({
                        "source": edge["source"],
                        "target": edge["target"],
                        "relation": edge["relation"],
                    })

        KnowledgeGraphBuilder._persist(kg)
        logger.info(
            f"[knowledge_graph] built: {len(kg.nodes)} nodes, {len(kg.edges)} edges, "
            f"{len(kg.features)} features, {len(kg.sdds)} sdds, "
            f"{len(kg.workflows)} workflows, {len(kg.agents)} agents"
        )
        return kg

    @staticmethod
    def load() -> KnowledgeGraph | None:
        path = RuntimePathResolver.knowledge_graph_path()
        if not path.exists():
            return None
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        kg = KnowledgeGraph(generated_at=data.get("generated_at", ""))
        kg.nodes = data.get("nodes", [])
        kg.edges = data.get("edges", [])
        kg.features = data.get("features", [])
        kg.sdds = data.get("sdds", [])
        kg.workflows = data.get("workflows", [])
        kg.agents = data.get("agents", [])
        return kg

    @staticmethod
    def _infer_type(ref: str) -> str:
        if "store" in ref:
            return "store"
        if "route" in ref or "page" in ref:
            return "page"
        if "tool" in ref:
            return "tool"
        if "event" in ref:
            return "event"
        if "agent" in ref or "workflow" in ref:
            return "agent"
        if "provider" in ref:
            return "provider"
        return "unknown"

    @staticmethod
    def _persist(kg: KnowledgeGraph):
        path = RuntimePathResolver.knowledge_graph_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(kg.to_dict(), f, indent=2, ensure_ascii=False)

    @staticmethod
    def update_file(file_path: str | Path) -> None:
        """Atualiza incrementalmente um unico arquivo no grafo de conhecimento."""
        path = Path(file_path).resolve()
        project_root = RuntimePathResolver.project_root().resolve()

        try:
            rel_path = path.relative_to(project_root).as_posix()
        except ValueError:
            logger.warning(
                f"[knowledge_graph] file {path} is not in project root {project_root}"
            )
            return

        kg = KnowledgeGraphBuilder.load()
        if not kg:
            logger.info(
                "[knowledge_graph] no existing graph found, performing full rebuild"
            )
            KnowledgeGraphBuilder.build()
            return

        node_id = None
        new_entry = None
        links = []
        wikilinks = []

        is_md = path.suffix.lower() == ".md"

        if is_md:
            vn = VaultReader.scan_single(path)
            if vn:
                node_id = vn.id
                new_entry = {
                    "id": vn.id,
                    "title": vn.title,
                    "type": vn.type,
                    "owner": vn.owner,
                    "status": vn.status,
                    "tags": vn.tags,
                    "links": vn.links,
                    "wikilinks": vn.wikilinks,
                    "source": "vault",
                    "path": rel_path,
                }
                links = vn.links
                wikilinks = vn.wikilinks
        else:
            # Check file existence in Graphify graph
            graphify_data = KnowledgeGraphBuilder._load_graphify_graph()
            if graphify_data and rel_path in graphify_data.get("files", {}):
                file_info = graphify_data["files"][rel_path]
                node_id = file_info["id"]
                ref_type = file_info["type"]
                new_entry = {
                    "id": node_id,
                    "title": file_info["title"],
                    "type": ref_type,
                    "source": "code",
                    "path": rel_path,
                }

        if node_id:
            # Remover old node
            kg.nodes = [n for n in kg.nodes if n["id"] != node_id]
            kg.features = [f for f in kg.features if f["id"] != node_id]
            kg.sdds = [s for s in kg.sdds if s["id"] != node_id]
            kg.workflows = [w for w in kg.workflows if w["id"] != node_id]
            kg.agents = [a for a in kg.agents if a["id"] != node_id]

            # Remover old outgoing edges
            kg.edges = [e for e in kg.edges if e["source"] != node_id]

            # Adicionar novo node
            kg.nodes.append(new_entry)
            if new_entry.get("type") == "feature":
                kg.features.append(new_entry)
            elif new_entry.get("type") == "sdd":
                kg.sdds.append(new_entry)
            elif new_entry.get("type") == "agent":
                kg.agents.append(new_entry)
            elif new_entry.get("type") == "workflow":
                kg.workflows.append(new_entry)

            # Adicionar edges
            for link in links:
                kg.edges.append(
                    {"source": node_id, "target": link, "relation": "depends_on"}
                )
            for wl in wikilinks:
                kg.edges.append(
                    {"source": node_id, "target": wl, "relation": "documents"}
                )

            kg.generated_at = datetime.now(timezone.utc).isoformat()
            KnowledgeGraphBuilder._persist(kg)
            logger.info(f"[knowledge_graph] incrementally updated node: {node_id}")
        else:
            # Se nao for detectado como node ativo (ex: deletado ou alterado de forma a nao dar match), remove
            KnowledgeGraphBuilder.delete_file(file_path, kg=kg)

    @staticmethod
    def delete_file(file_path: str | Path, kg: KnowledgeGraph | None = None) -> None:
        """Remove incrementalmente um arquivo do grafo de conhecimento."""
        path = Path(file_path).resolve()
        project_root = RuntimePathResolver.project_root().resolve()
        try:
            rel_path = path.relative_to(project_root).as_posix()
        except ValueError:
            return

        if not kg:
            kg = KnowledgeGraphBuilder.load()
        if not kg:
            return

        node_ids_to_remove = []
        for n in kg.nodes:
            if n.get("path") == rel_path or n.get("id") == rel_path:
                node_ids_to_remove.append(n.get("id"))

        if not node_ids_to_remove:
            stem = path.stem.lower()
            for n in kg.nodes:
                if n.get("id") == stem:
                    node_ids_to_remove.append(n.get("id"))

        if node_ids_to_remove:
            for node_id in node_ids_to_remove:
                kg.nodes = [n for n in kg.nodes if n["id"] != node_id]
                kg.features = [f for f in kg.features if f["id"] != node_id]
                kg.sdds = [s for s in kg.sdds if s["id"] != node_id]
                kg.workflows = [w for w in kg.workflows if w["id"] != node_id]
                kg.agents = [a for a in kg.agents if a["id"] != node_id]
                kg.edges = [
                    e
                    for e in kg.edges
                    if e["source"] != node_id and e["target"] != node_id
                ]
                logger.info(f"[knowledge_graph] incrementally removed node: {node_id}")

            kg.generated_at = datetime.now(timezone.utc).isoformat()
            KnowledgeGraphBuilder._persist(kg)
