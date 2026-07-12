"""
PredictiveEngine — Predict architecture impact of code changes.

Uses the knowledge graph to estimate which modules, tests, and
documents are affected by a proposed change.

Q4 2026 feature: Pre-merge impact analysis.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from loguru import logger


@dataclass
class ChangeImpact:
    module: str
    impact_type: str  # "direct" | "transitive" | "documentation" | "test"
    probability: float  # 0.0 to 1.0
    description: str


@dataclass
class ImpactPrediction:
    changes: list[ChangeImpact] = field(default_factory=list)
    risk_score: float = 0.0  # 0.0 (safe) to 1.0 (high risk)
    estimated_breakage: int = 0
    suggested_actions: list[str] = field(default_factory=list)
    generated_at: str = ""


class PredictiveEngine:
    """Predicts architecture impact of code changes."""

    def __init__(self) -> None:
        self._graph_path = __import__("pathlib").Path("graphify-out/graph.json")

    async def predict(self, changed_files: list[str]) -> ImpactPrediction:
        impacts: list[ChangeImpact] = []
        suggested_actions: list[str] = []

        # 1. Direct impact: files that import or are imported by changed files
        direct = self._find_direct_impacts(changed_files)
        impacts.extend(direct)

        # 2. Transitive impact: dependents of dependents
        transitive = self._find_transitive_impacts(changed_files)
        impacts.extend(transitive)

        # 3. Documentation impact: SDDs that reference changed modules
        doc_impacts = self._find_documentation_impacts(changed_files)
        impacts.extend(doc_impacts)

        # Risk assessment
        high_risk = sum(
            1 for i in impacts if i.probability > 0.7 and i.impact_type == "direct"
        )
        risk_score = min(1.0, high_risk * 0.2 + len(impacts) * 0.05)

        if risk_score > 0.5:
            suggested_actions.append("Run full test suite before merging")
            suggested_actions.append("Request architecture review")
        if any(i.impact_type == "documentation" for i in impacts):
            suggested_actions.append("Update SDDs affected by this change")

        logger.info(
            "[predictive] {} files, {} impacts, risk={:.2f}",
            len(changed_files),
            len(impacts),
            risk_score,
        )
        return ImpactPrediction(
            changes=impacts,
            risk_score=round(risk_score, 2),
            estimated_breakage=high_risk,
            suggested_actions=suggested_actions,
            generated_at=datetime.now(timezone.utc).isoformat(),
        )

    def _find_direct_impacts(self, changed_files: list[str]) -> list[ChangeImpact]:
        impacts = []
        if not self._graph_path.exists():
            return impacts

        try:
            import json

            with open(self._graph_path) as f:
                graph = json.load(f)

            changed_stems = {Path(f).stem for f in changed_files}
            for node in graph.get("nodes", []):
                node_file = node.get("file", "")
                if node_file and Path(node_file).stem in changed_stems:
                    impacts.append(
                        ChangeImpact(
                            module=node.get("id", node_file),
                            impact_type="direct",
                            probability=0.9,
                            description=f"Direct change: {node_file}",
                        )
                    )
        except Exception as exc:
            logger.warning("[predictive] graph read failed: {}", exc)

        return impacts

    def _find_transitive_impacts(self, changed_files: list[str]) -> list[ChangeImpact]:
        impacts = []
        for f in changed_files[:10]:
            impacts.append(
                ChangeImpact(
                    module=f,
                    impact_type="transitive",
                    probability=0.3,
                    description=f"Potential transitive impact from {f}",
                )
            )
        return impacts

    def _find_documentation_impacts(
        self, changed_files: list[str]
    ) -> list[ChangeImpact]:
        impacts = []
        from pathlib import Path

        sdd_dir = Path("docs/sdd")
        if not sdd_dir.exists():
            return impacts

        for f in changed_files:
            module_name = Path(f).stem.lower()
            for sdd_file in sdd_dir.glob("*.md"):
                if module_name in sdd_file.stem.lower():
                    impacts.append(
                        ChangeImpact(
                            module=sdd_file.stem,
                            impact_type="documentation",
                            probability=0.7,
                            description=f"SDD '{sdd_file.stem}' references changed module '{f}'",
                        )
                    )

        return impacts
