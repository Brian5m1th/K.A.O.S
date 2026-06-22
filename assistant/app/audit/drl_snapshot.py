from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from loguru import logger

from app.audit.feature_registry import FeatureRegistry, FeatureEntry
from app.audit.audit_engine import AuditEngine, DriftReport


@dataclass
class GraphSummary:
    total_nodes: int = 0
    total_edges: int = 0
    node_types: dict[str, int] = field(default_factory=dict)
    generated_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


@dataclass
class DRLSnapshot:
    features: list[FeatureEntry] = field(default_factory=list)
    coverage: float = 0.0
    drift_level: str = "low"
    last_commit: str = ""
    graph_summary: GraphSummary = field(default_factory=GraphSummary)
    missing_count: int = 0
    outdated_count: int = 0
    generated_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def to_dict(self) -> dict:
        return {
            "version": "1.0",
            "generated_at": self.generated_at,
            "features": [f.to_dict() for f in self.features],
            "coverage": round(self.coverage, 1),
            "driftLevel": self.drift_level,
            "lastCommit": self.last_commit,
            "missingCount": self.missing_count,
            "outdatedCount": self.outdated_count,
            "graphSummary": {
                "totalNodes": self.graph_summary.total_nodes,
                "totalEdges": self.graph_summary.total_edges,
                "nodeTypes": self.graph_summary.node_types,
                "generatedAt": self.graph_summary.generated_at,
            },
        }


class DRLSnapshotManager:
    _snapshot_path = Path("docs/runtime/snapshot.json")

    @classmethod
    def build_snapshot(cls, drift_report: DriftReport | None = None) -> DRLSnapshot:
        FeatureRegistry.load_from_json()

        if drift_report is None:
            drift_report = AuditEngine.load_latest_report()

        features = FeatureRegistry.list()
        commits = []
        try:
            from app.audit.commit_mapper import CommitMapper

            commits = CommitMapper.load()
        except Exception:
            pass

        last_commit = commits[0].hash if commits else ""

        snapshot = DRLSnapshot(
            features=features,
            coverage=drift_report.coverage if drift_report else 0.0,
            drift_level=drift_report.drift_level if drift_report else "low",
            last_commit=last_commit,
            missing_count=len(drift_report.missing_features) if drift_report else 0,
            outdated_count=len(drift_report.outdated_docs) if drift_report else 0,
            graph_summary=GraphSummary(),
        )

        cls._persist(snapshot)
        logger.info(
            f"[drl_snapshot] snapshot built: coverage={snapshot.coverage:.1f}%, drift={snapshot.drift_level}"
        )
        return snapshot

    @classmethod
    def _persist(cls, snapshot: DRLSnapshot) -> None:
        cls._snapshot_path.parent.mkdir(parents=True, exist_ok=True)
        import json

        with open(cls._snapshot_path, "w", encoding="utf-8") as f:
            json.dump(snapshot.to_dict(), f, indent=2, ensure_ascii=False)

    @classmethod
    def load(cls) -> DRLSnapshot | None:
        if cls._snapshot_path.exists():
            import json

            with open(cls._snapshot_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            snapshot = DRLSnapshot()
            snapshot.features = [
                FeatureEntry.from_dict(f) for f in data.get("features", [])
            ]
            snapshot.coverage = data.get("coverage", 0.0)
            snapshot.drift_level = data.get("driftLevel", "low")
            snapshot.last_commit = data.get("lastCommit", "")
            snapshot.missing_count = data.get("missingCount", 0)
            snapshot.outdated_count = data.get("outdatedCount", 0)
            gs = data.get("graphSummary", {})
            snapshot.graph_summary = GraphSummary(
                total_nodes=gs.get("totalNodes", 0),
                total_edges=gs.get("totalEdges", 0),
                node_types=gs.get("nodeTypes", {}),
                generated_at=gs.get("generatedAt", ""),
            )
            snapshot.generated_at = data.get("generated_at", "")
            return snapshot
        return None

    @classmethod
    def update_graph_summary(
        cls, total_nodes: int, total_edges: int, node_types: dict[str, int]
    ) -> None:
        snapshot = cls.load()
        if snapshot:
            snapshot.graph_summary.total_nodes = total_nodes
            snapshot.graph_summary.total_edges = total_edges
            snapshot.graph_summary.node_types = node_types
            snapshot.graph_summary.generated_at = datetime.now(timezone.utc).isoformat()
            cls._persist(snapshot)

    @classmethod
    def get_features_for_frontend(cls) -> list[dict]:
        snapshot = cls.load()
        if not snapshot:
            return []
        return [f.to_dict() for f in snapshot.features]

    @classmethod
    def get_coverage(cls) -> float:
        snapshot = cls.load()
        return snapshot.coverage if snapshot else 0.0

    @classmethod
    def get_drift_level(cls) -> str:
        snapshot = cls.load()
        return snapshot.drift_level if snapshot else "low"
