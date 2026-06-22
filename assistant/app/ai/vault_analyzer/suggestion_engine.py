from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
import json

from loguru import logger

from app.ai.vault_analyzer.evidence_engine import Evidence


@dataclass
class Suggestion:
    id: str
    title: str
    description: str
    category: str  # documentation | architecture | ownership | dependency | sync
    priority: str  # low | medium | high | critical
    confidence: float  # 0.0 - 1.0
    affected_nodes: list[str] = field(default_factory=list)
    generated_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "priority": self.priority,
            "confidence": round(self.confidence, 2),
            "affected_nodes": self.affected_nodes,
            "generated_at": self.generated_at,
        }


def confidence_label(confidence: float) -> str:
    if confidence >= 0.9:
        return "alta"
    if confidence >= 0.7:
        return "media"
    return "baixa"


class SuggestionEngine:
    @staticmethod
    def generate_from_evidences(evidences: list[Evidence]) -> list[Suggestion]:
        suggestions: list[Suggestion] = []
        seen: set[str] = set()

        for ev in evidences:
            if ev.rule in seen:
                continue
            seen.add(ev.rule)

            sug = SuggestionEngine._evidence_to_suggestion(ev)
            if sug:
                suggestions.append(sug)

        logger.info(f"[suggestion_engine] generated {len(suggestions)} suggestions")
        return suggestions

    @staticmethod
    def _evidence_to_suggestion(ev: Evidence) -> Suggestion | None:
        mapping = {
            "missing_documentation": Suggestion(
                id="sug-doc-missing",
                title="Documentacao ausente para features",
                description=ev.explanation,
                category="documentation",
                priority="high" if ev.severity == "high" else "medium",
                confidence=ev.confidence,
                affected_nodes=ev.source_files + ev.source_sdds,
            ),
            "orphan_feature": Suggestion(
                id="sug-feature-orphan",
                title="Features orfas sem codigo",
                description=ev.explanation,
                category="architecture",
                priority="medium",
                confidence=ev.confidence,
                affected_nodes=ev.source_files + ev.source_sdds,
            ),
            "sdd_without_feature": Suggestion(
                id="sug-sdd-orphan",
                title="SDDs sem feature correspondente",
                description=ev.explanation,
                category="documentation",
                priority="medium",
                confidence=ev.confidence,
                affected_nodes=ev.source_sdds,
            ),
            "missing_owner": Suggestion(
                id="sug-owner-missing",
                title="Owners nao atribuidos",
                description=ev.explanation,
                category="ownership",
                priority="low",
                confidence=ev.confidence,
                affected_nodes=ev.source_files,
            ),
            "cyclic_dependency": Suggestion(
                id="sug-cycle-detected",
                title="Dependencia ciclica detectada",
                description=ev.explanation,
                category="dependency",
                priority="critical",
                confidence=ev.confidence,
                affected_nodes=ev.source_files,
            ),
            "overcoupled_node": Suggestion(
                id="sug-overcoupled",
                title="Nodes com acoplamento excessivo",
                description=ev.explanation,
                category="architecture",
                priority="medium",
                confidence=ev.confidence,
                affected_nodes=ev.source_files,
            ),
        }
        return mapping.get(ev.rule)

    @staticmethod
    def generate_auto_sdd_suggestion(
        feature_id: str, feature_name: str, confidence: float = 0.85
    ) -> Suggestion:
        return Suggestion(
            id=f"sug-auto-sdd-{feature_id}",
            title=f"Gerar SDD para {feature_name}",
            description=f"Feature '{feature_name}' ({feature_id}) nao possui SDD. "
            f"Pode ser gerado automaticamente pelo Auto-Doc Engine.",
            category="documentation",
            priority="high",
            confidence=confidence,
            affected_nodes=[feature_id],
        )

    @staticmethod
    def generate_sync_suggestion(
        source: str, target: str, confidence: float = 0.8
    ) -> Suggestion:
        return Suggestion(
            id="sug-sync-vault",
            title=f"Sincronizar {source} com {target}",
            description=f"Conteudo entre {source} e {target} esta divergente. "
            f"Execute sync para alinhar.",
            category="sync",
            priority="medium",
            confidence=confidence,
            affected_nodes=[source, target],
        )

    @staticmethod
    def persist(suggestions: list[Suggestion]):
        path = Path("docs/runtime/architecture/suggestions.json")
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "version": "1.0",
                    "total": len(suggestions),
                    "generated_at": datetime.now(timezone.utc).isoformat(),
                    "suggestions": [s.to_dict() for s in suggestions],
                },
                f,
                indent=2,
                ensure_ascii=False,
            )
