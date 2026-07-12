from __future__ import annotations
import hashlib
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Optional
import json
from pathlib import Path

from loguru import logger

from app.ai.vault_analyzer.vault_reader import VaultReader
from app.audit.drl_snapshot import DRLSnapshotManager
from app.audit.feature_registry import FeatureRegistry
from app.audit.runtime_resolver import RuntimePathResolver


@dataclass
class ArchNode:
    id: str
    label: str
    type: str
    owner: str = "shared"
    status: str = "unknown"
    source: str = ""  # vault | code | drl
    phase: str = ""


@dataclass
class ArchEdge:
    source: str
    target: str
    relation: str  # depends_on | uses | emits | owns | documents | implements


@dataclass
class ArchGraphSnapshot:
    nodes: list[ArchNode] = field(default_factory=list)
    edges: list[ArchEdge] = field(default_factory=list)
    generated_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def to_dict(self) -> dict:
        return {
            "version": "1.0",
            "generated_at": self.generated_at,
            "nodes": [
                {
                    "id": n.id,
                    "label": n.label,
                    "type": n.type,
                    "owner": n.owner,
                    "status": n.status,
                    "source": n.source,
                    "phase": n.phase,
                }
                for n in self.nodes
            ],
            "edges": [
                {"source": e.source, "target": e.target, "relation": e.relation}
                for e in self.edges
            ],
        }


class GraphBuilder:
    """Builds architecture graph from Graphify, Vault, and DRL sources.

    Deprecates the old CodeScanner regex-based scanner in favor of
    Graphify's AST-level graph.json (12k+ nodes, 22k+ edges).
    """

    GRAPHIFY_PATH = Path("graphify-out/graph.json")

    @staticmethod
    def build() -> ArchGraphSnapshot:
        vault_nodes = VaultReader.scan_all()
        drl = DRLSnapshotManager.load()

        # ── Load Graphify graph as the code relationship source ──
        graphify_data = GraphBuilder._load_graphify_graph()

        snapshot = ArchGraphSnapshot()
        seen_ids: set[str] = set()

        # ── Vault nodes ──────────────────────────────────────────
        for vn in vault_nodes:
            node = ArchNode(
                id=vn.id,
                label=vn.title,
                type=vn.type,
                owner=vn.owner,
                status=vn.status,
                source="vault",
            )
            snapshot.nodes.append(node)
            seen_ids.add(vn.id)

            for link in vn.links:
                snapshot.edges.append(
                    ArchEdge(source=vn.id, target=link, relation="depends_on")
                )
            for wl in vn.wikilinks:
                snapshot.edges.append(
                    ArchEdge(source=vn.id, target=wl, relation="documents")
                )

        # ── DRL / Feature nodes ──────────────────────────────────
        if drl:
            features = drl.features
        else:
            FeatureRegistry.load_from_json()
            features = FeatureRegistry.list()

        for feat in features:
            fid = f"feature:{feat.id}"
            if fid not in seen_ids:
                snapshot.nodes.append(
                    ArchNode(
                        id=fid,
                        label=feat.name,
                        type="feature",
                        status=feat.status,
                        source="drl",
                        phase=feat.phase,
                    )
                )
                seen_ids.add(fid)
            for doc_ref in feat.docs:
                snapshot.edges.append(
                    ArchEdge(source=fid, target=doc_ref, relation="documents")
                )
            for code_ref in feat.code_refs:
                snapshot.edges.append(
                    ArchEdge(source=fid, target=code_ref, relation="implements")
                )

        # ── Graphify code nodes (aggregated at file level) ───────
        if graphify_data:
            GraphBuilder._add_graphify_nodes(snapshot, seen_ids, graphify_data)

        # ── System edges & persist ───────────────────────────────
        GraphBuilder._infer_system_edges(snapshot)
        GraphBuilder._persist(snapshot)

        # Sync graph summary to DRL snapshot
        node_types: dict[str, int] = {}
        edge_types: dict[str, int] = {}
        for n in snapshot.nodes:
            node_types[n.type] = node_types.get(n.type, 0) + 1
        for e in snapshot.edges:
            edge_types[e.relation] = edge_types.get(e.relation, 0) + 1

        # Compute fingerprint
        nodes_json = json.dumps(
            [asdict(n) for n in snapshot.nodes], sort_keys=True, default=str
        )
        edges_json = json.dumps(
            [asdict(e) for e in snapshot.edges], sort_keys=True, default=str
        )
        graph_fingerprint = hashlib.sha256(
            f"{nodes_json}|{edges_json}".encode()
        ).hexdigest()

        DRLSnapshotManager.update_graph_summary(
            total_nodes=len(snapshot.nodes),
            total_edges=len(snapshot.edges),
            node_types=node_types,
            edge_types=edge_types,
            source_hash=graph_fingerprint,
            graph_version="1.0",
        )

        logger.info(
            f"[graph_builder] built graph: {len(snapshot.nodes)} nodes, {len(snapshot.edges)} edges"
        )
        return snapshot

    @staticmethod
    def _load_graphify_graph() -> Optional[dict]:
        """Loads graphify-out/graph.json and returns aggregated file-level data.

        Returns:
            dict with 'files' (set of source_file paths) and
            'edges' (list of {source, target, relation}).
            Returns None if graph.json is unavailable.
        """
        gf_path = RuntimePathResolver.project_root() / GraphBuilder.GRAPHIFY_PATH
        if not gf_path.exists():
            logger.warning(
                f"[graph_builder] Graphify graph not found at {gf_path}. "
                "Run `graphify update .` to generate it."
            )
            return None

        try:
            with open(gf_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            logger.error(f"[graph_builder] Failed to load Graphify graph: {e}")
            return None

        # Aggregate file-level nodes
        file_nodes: dict[str, dict] = {}
        for node in data.get("nodes", []):
            source_file = node.get("source_file", "")
            if not source_file:
                continue
            file_label = source_file.split("/")[-1]
            if source_file not in file_nodes:
                file_nodes[source_file] = {
                    "id": source_file,
                    "label": file_label,
                    "type": GraphBuilder._infer_type(source_file),
                    "source": "code",
                }

        # Aggregate file-level edges from links
        file_edges = []
        seen_file_edges = set()
        for link in data.get("links", []):
            src = link.get("source", "")
            tgt = link.get("target", "")
            # Map symbol-level links to file-level
            src_file = GraphBuilder._resolve_source_file(data, src)
            tgt_file = GraphBuilder._resolve_source_file(data, tgt)
            if src_file and tgt_file and src_file != tgt_file:
                edge_key = f"{src_file}->{tgt_file}"
                if edge_key not in seen_file_edges:
                    seen_file_edges.add(edge_key)
                    file_edges.append(
                        {
                            "source": src_file,
                            "target": tgt_file,
                            "relation": GraphBuilder._infer_relation(
                                link.get("relation", "uses")
                            ),
                        }
                    )

        # Add community cluster info from GRAPH_REPORT.md
        for node in data.get("nodes", []):
            sf = node.get("source_file", "")
            if sf:
                pass

        return {
            "files": file_nodes,
            "edges": file_edges,
        }

    @staticmethod
    def _resolve_source_file(data: dict, symbol_id: str) -> Optional[str]:
        """Resolve a symbol ID back to its source file."""
        for node in data.get("nodes", []):
            if node.get("id") == symbol_id:
                return node.get("source_file") or None
        return None

    @staticmethod
    def _add_graphify_nodes(
        snapshot: ArchGraphSnapshot,
        seen_ids: set[str],
        graphify_data: dict,
    ):
        """Add Graphify-derived nodes and edges to the snapshot."""
        for file_id, file_info in graphify_data.get("files", {}).items():
            if file_id not in seen_ids:
                snapshot.nodes.append(
                    ArchNode(
                        id=file_id,
                        label=file_info["label"],
                        type=file_info["type"],
                        source="code",
                    )
                )
                seen_ids.add(file_id)

        for edge in graphify_data.get("edges", []):
            if edge["source"] in seen_ids and edge["target"] in seen_ids:
                snapshot.edges.append(
                    ArchEdge(
                        source=edge["source"],
                        target=edge["target"],
                        relation=edge["relation"],
                    )
                )

    @staticmethod
    def _infer_type(ref: str) -> str:
        """Infer the type of a code reference from its path."""
        ref_lower = ref.lower()
        if "store" in ref_lower or "/stores/" in ref:
            return "store"
        if "route" in ref_lower or "/pages/" in ref or "/routes/" in ref:
            return "page"
        if "tool" in ref_lower:
            return "tool"
        if "event" in ref_lower or "eventbus" in ref_lower:
            return "event"
        if "agent" in ref_lower or "workflow" in ref_lower:
            return "agent"
        if "provider" in ref_lower:
            return "provider"
        if ref_lower.endswith(".py"):
            return "backend_module"
        if ref_lower.endswith(".ts") or ref_lower.endswith(".tsx"):
            return "frontend_module"
        if ref_lower.endswith(".rs"):
            return "rust_module"
        return "unknown"

    @staticmethod
    def _infer_relation(relation: str) -> str:
        """Map Graphify relation names to ArchEdge relation types."""
        mapping = {
            "contains": "uses",
            "imports": "uses",
            "imports_from": "uses",
            "calls": "uses",
            "uses": "uses",
            "inherits": "uses",
            "implements": "implements",
            "documents": "documents",
            "depends_on": "depends_on",
            "emits": "emits",
            "owns": "owns",
            "re_exports": "uses",
        }
        return mapping.get(relation, "uses")

    @staticmethod
    def _infer_system_edges(snapshot: ArchGraphSnapshot):
        node_ids = {n.id for n in snapshot.nodes}
        system_edges = [
            ("drl.core", "audit.engine", "uses"),
            ("drl.core", "graphify.engine", "uses"),
            ("audit.engine", "system.event-bus", "emits"),
            ("system.event-bus", "drl.core", "depends_on"),
        ]
        for src, tgt, rel in system_edges:
            if src in node_ids and tgt in node_ids:
                snapshot.edges.append(ArchEdge(source=src, target=tgt, relation=rel))

    @staticmethod
    def _persist(snapshot: ArchGraphSnapshot):
        path = RuntimePathResolver.graph_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(snapshot.to_dict(), f, indent=2, ensure_ascii=False)

    @staticmethod
    def load() -> Optional[ArchGraphSnapshot]:
        path = RuntimePathResolver.graph_path()
        if not path.exists():
            return None
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        snapshot = ArchGraphSnapshot(generated_at=data.get("generated_at", ""))
        snapshot.nodes = [ArchNode(**n) for n in data.get("nodes", [])]
        snapshot.edges = [ArchEdge(**e) for e in data.get("edges", [])]
        return snapshot
