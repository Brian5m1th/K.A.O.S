from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
import json

from loguru import logger

from app.ai.vault_analyzer.vault_reader import VaultReader
from app.ai.vault_analyzer.drift_engine import DriftEngine
from app.ai.vault_analyzer.evidence_engine import EvidenceEngine, Evidence
from app.audit.feature_registry import FeatureRegistry
from app.audit.runtime_resolver import RuntimePathResolver


@dataclass
class ArchitectureAnalysis:
    coverage_score: float = 0.0
    drift_level: str = "low"
    issues: list[Evidence] = field(default_factory=list)
    suggestions: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    generated_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def to_dict(self) -> dict:
        return {
            "version": "1.0",
            "generated_at": self.generated_at,
            "coverage_score": round(self.coverage_score, 1),
            "drift_level": self.drift_level,
            "total_issues": len(self.issues),
            "issues": [e.to_dict() for e in self.issues],
            "suggestions": self.suggestions,
            "warnings": self.warnings,
        }


class AnalyzerEngine:
    @staticmethod
    def analyze() -> ArchitectureAnalysis:
        # Coletar dados
        vault_nodes = VaultReader.scan_all()
        FeatureRegistry.load_from_json()
        features = FeatureRegistry.list()

        # Drift score
        drift = DriftEngine.calculate()

        # Evidencias
        evidences = EvidenceEngine.collect()

        # Coverage
        total_features = max(len(features), 1)
        documented = sum(1 for f in features if f.docs)
        coverage = (documented / total_features) * 100

        # Sugestoes
        suggestions = AnalyzerEngine._generate_suggestions(evidences)

        # Warnings
        warnings = AnalyzerEngine._generate_warnings(vault_nodes, features)

        analysis = ArchitectureAnalysis(
            coverage_score=coverage,
            drift_level=drift.level,
            issues=evidences,
            suggestions=suggestions,
            warnings=warnings,
        )

        AnalyzerEngine._persist(analysis)
        logger.info(
            f"[analyzer_engine] analysis complete: coverage={coverage:.1f}%, drift={drift.level}"
        )
        return analysis

    @staticmethod
    def _generate_suggestions(evidences: list[Evidence]) -> list[str]:
        suggestions = []
        seen_rules: set[str] = set()

        for ev in evidences:
            if ev.rule in seen_rules:
                continue
            seen_rules.add(ev.rule)

            if ev.rule == "missing_documentation":
                suggestions.append(
                    f"Criar SDDs para as features sem documentacao ({ev.confidence * 100:.0f}% confianca)."
                )
            elif ev.rule == "orphan_feature":
                suggestions.append(
                    "Revisar features orfas: sem codigo referenciado, possivelmente removidas."
                )
            elif ev.rule == "sdd_without_feature":
                suggestions.append(
                    "SDDs sem feature correspondente: revisar se a feature foi removida ou renomeada."
                )
            elif ev.rule == "missing_owner":
                suggestions.append(
                    "Atribuir owners para todos os nodes do vault (backend/frontend/shared/infrastructure)."
                )
            elif ev.rule == "cyclic_dependency":
                suggestions.append(
                    "REQUER ACAO: dependencia ciclica detectada. Revisar arquitetura para quebrar o ciclo."
                )
            elif ev.rule == "overcoupled_node":
                suggestions.append(
                    "Revisar nodes com excesso de dependencias. Considere dividir em modulos menores."
                )

        return suggestions

    @staticmethod
    def _generate_warnings(vault_nodes: list, features: list) -> list[str]:
        warnings = []
        feature_ids = {f.id for f in features}
        vault_ids = {n.id for n in vault_nodes}

        missing_in_vault = feature_ids - vault_ids
        if missing_in_vault:
            warnings.append(
                f"{len(missing_in_vault)} features registradas mas ausentes no vault."
            )

        deprecated_in_vault = {n.id for n in vault_nodes if n.status == "deprecated"}
        if deprecated_in_vault & feature_ids:
            warnings.append(
                "Features marcadas como deprecated mas ainda registradas como ativas."
            )

        return warnings

    @staticmethod
    def _persist(analysis: ArchitectureAnalysis):
        path = RuntimePathResolver.analysis_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(analysis.to_dict(), f, indent=2, ensure_ascii=False)

    @staticmethod
    def load_latest() -> ArchitectureAnalysis | None:
        path = RuntimePathResolver.analysis_path()
        if not path.exists():
            return None
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return ArchitectureAnalysis(**{k: v for k, v in data.items() if k != "issues"})
