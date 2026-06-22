from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
import json

from loguru import logger

from app.ai.vault_analyzer.vault_reader import VaultReader
from app.audit.drl_snapshot import DRLSnapshotManager
from app.audit.code_scanner import CodeScanner


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
    @staticmethod
    def build() -> ArchGraphSnapshot:
        vault_nodes = VaultReader.scan_all()
        drl = DRLSnapshotManager.load()
        code = CodeScanner.scan_all()

        snapshot = ArchGraphSnapshot()
        seen_ids: set[str] = set()

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

        if drl:
            for feature in drl.features:
                fid = f"feature:{feature.id}"
                if fid not in seen_ids:
                    snapshot.nodes.append(
                        ArchNode(
                            id=fid,
                            label=feature.name,
                            type="feature",
                            status=feature.status,
                            source="drl",
                            phase=feature.phase,
                        )
                    )
                    seen_ids.add(fid)
                for doc_ref in feature.docs:
                    snapshot.edges.append(
                        ArchEdge(
                            source=fid,
                            target=doc_ref,
                            relation="documents",
                        )
                    )
                for code_ref in feature.code_refs:
                    snapshot.edges.append(
                        ArchEdge(
                            source=fid,
                            target=code_ref,
                            relation="implements",
                        )
                    )

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
                ref_type = GraphBuilder._infer_type(ref)
                snapshot.nodes.append(
                    ArchNode(
                        id=ref,
                        label=ref.split("/")[-1],
                        type=ref_type,
                        source="code",
                    )
                )
                seen_ids.add(ref)

        GraphBuilder._infer_system_edges(snapshot)
        GraphBuilder._persist(snapshot)

        logger.info(
            f"[graph_builder] built graph: {len(snapshot.nodes)} nodes, {len(snapshot.edges)} edges"
        )
        return snapshot

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
        path = Path("docs/runtime/architecture/graph.json")
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(snapshot.to_dict(), f, indent=2, ensure_ascii=False)

    @staticmethod
    def load() -> Optional[ArchGraphSnapshot]:
        path = Path("docs/runtime/architecture/graph.json")
        if not path.exists():
            return None
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        snapshot = ArchGraphSnapshot(generated_at=data.get("generated_at", ""))
        snapshot.nodes = [ArchNode(**n) for n in data.get("nodes", [])]
        snapshot.edges = [ArchEdge(**e) for e in data.get("edges", [])]
        return snapshot
