from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
import json
from pathlib import Path

from loguru import logger

from app.ai.vault_analyzer.vault_reader import VaultReader
from app.audit.feature_registry import FeatureRegistry
from app.audit.sdd_resolver import SDDResolver
from app.audit.code_scanner import CodeScanner
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
    @staticmethod
    def build() -> KnowledgeGraph:
        vault_nodes = VaultReader.scan_all()
        FeatureRegistry.load_from_json()
        code = CodeScanner.scan_all()
        SDDResolver.scan_all_sdds()

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

        all_code_refs = (
            code.stores
            + code.routes
            + code.tools
            + code.events
            + code.agents
            + code.workflows
            + code.providers
        )
        for ref in all_code_refs:
            if ref not in seen_ids:
                ref_type = KnowledgeGraphBuilder._infer_type(ref)
                entry = {
                    "id": ref,
                    "title": ref.split("/")[-1],
                    "type": ref_type,
                    "source": "code",
                }
                kg.nodes.append(entry)
                seen_ids.add(ref)

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
            logger.warning(f"[knowledge_graph] file {path} is not in project root {project_root}")
            return

        kg = KnowledgeGraphBuilder.load()
        if not kg:
            logger.info("[knowledge_graph] no existing graph found, performing full rebuild")
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
            code = CodeScanner.scan_all()
            all_code_refs = (
                code.stores
                + code.routes
                + code.tools
                + code.events
                + code.agents
                + code.workflows
                + code.providers
            )
            if rel_path in all_code_refs:
                node_id = rel_path
                ref_type = KnowledgeGraphBuilder._infer_type(rel_path)
                new_entry = {
                    "id": rel_path,
                    "title": rel_path.split("/")[-1],
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
                kg.edges.append({"source": node_id, "target": link, "relation": "depends_on"})
            for wl in wikilinks:
                kg.edges.append({"source": node_id, "target": wl, "relation": "documents"})

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
                kg.edges = [e for e in kg.edges if e["source"] != node_id and e["target"] != node_id]
                logger.info(f"[knowledge_graph] incrementally removed node: {node_id}")

            kg.generated_at = datetime.now(timezone.utc).isoformat()
            KnowledgeGraphBuilder._persist(kg)
