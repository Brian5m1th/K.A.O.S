from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
import json

from loguru import logger

from app.ai.vault_analyzer.vault_reader import VaultReader
from app.audit.feature_registry import FeatureRegistry
from app.audit.sdd_resolver import SDDResolver
from app.audit.runtime_resolver import RuntimePathResolver


@dataclass
class Evidence:
    rule: str
    severity: str  # low | medium | high | critical
    source_files: list[str] = field(default_factory=list)
    source_sdds: list[str] = field(default_factory=list)
    explanation: str = ""
    confidence: float = 1.0

    def to_dict(self) -> dict:
        return {
            "rule": self.rule,
            "severity": self.severity,
            "source_files": self.source_files,
            "source_sdds": self.source_sdds,
            "explanation": self.explanation,
            "confidence": round(self.confidence, 2),
        }


class EvidenceEngine:
    RULES = {
        "missing_documentation": {
            "severity": "high",
            "description": "Feature detected in code but not linked to any SDD.",
        },
        "orphan_feature": {
            "severity": "medium",
            "description": "Feature registered but no code references found.",
        },
        "sdd_without_feature": {
            "severity": "medium",
            "description": "SDD exists but no feature references it.",
        },
        "stale_sdd": {
            "severity": "high",
            "description": "SDD last update is older than the latest commit.",
        },
        "missing_owner": {
            "severity": "low",
            "description": "Feature or node without owner assigned.",
        },
        "cyclic_dependency": {
            "severity": "critical",
            "description": "Circular dependency detected between nodes.",
        },
        "overcoupled_node": {
            "severity": "medium",
            "description": "Node with excessive dependencies.",
        },
    }

    @staticmethod
    def collect() -> list[Evidence]:
        evidences: list[Evidence] = []
        FeatureRegistry.load_from_json()
        SDDResolver.scan_all_sdds()
        vault_nodes = VaultReader.scan_all()

        features = FeatureRegistry.list()
        sdds = SDDResolver.get_all_sdds()

        for feat in features:
            if not feat.docs:
                evidences.append(
                    Evidence(
                        rule="missing_documentation",
                        severity="high",
                        source_files=feat.code_refs,
                        source_sdds=[],
                        explanation=f"Feature '{feat.name}' ({feat.id}) detected in code but not linked to any SDD.",
                        confidence=0.95,
                    )
                )

            if not feat.code_refs:
                evidences.append(
                    Evidence(
                        rule="orphan_feature",
                        severity="medium",
                        source_files=[],
                        source_sdds=feat.docs,
                        explanation=f"Feature '{feat.name}' ({feat.id}) registered but no code references found.",
                        confidence=0.85,
                    )
                )

        vault_feature_nodes = [
            n for n in vault_nodes if n.type in ("feature", "system")
        ]
        for node in vault_feature_nodes:
            matched = any(
                node.id == f.id or node.id in f.docs or f.id in node.links
                for f in features
            )
            if not matched and node.status == "implemented":
                evidences.append(
                    Evidence(
                        rule="sdd_without_feature",
                        severity="medium",
                        source_files=[],
                        source_sdds=[node.path],
                        explanation=f"SDD '{node.title}' exists in docs but no feature references it.",
                        confidence=0.75,
                    )
                )

        for sdd in sdds:
            vault_match = any(
                sdd.id == n.id or sdd.id in n.links for n in vault_feature_nodes
            )
            if not vault_match:
                evidences.append(
                    Evidence(
                        rule="sdd_without_feature",
                        severity="medium",
                        source_files=[],
                        source_sdds=[sdd.id],
                        explanation=f"SDD '{sdd.title}' ({sdd.id}) exists but no vault node references it.",
                        confidence=0.7,
                    )
                )

        for node in vault_nodes:
            if not node.owner or node.owner == "shared":
                evidences.append(
                    Evidence(
                        rule="missing_owner",
                        severity="low",
                        source_files=[node.path],
                        source_sdds=[],
                        explanation=f"Node '{node.title}' ({node.id}) has no owner assigned.",
                        confidence=0.9,
                    )
                )

        EvidenceEngine._detect_cycles(evidences, vault_nodes)
        EvidenceEngine._detect_overcoupled(evidences, vault_nodes)
        EvidenceEngine._persist(evidences)

        logger.info(f"[evidence_engine] collected {len(evidences)} evidences")
        return evidences

    @staticmethod
    def _detect_cycles(evidences: list[Evidence], nodes: list):
        link_map: dict[str, set[str]] = {}
        for node in nodes:
            if node.id not in link_map:
                link_map[node.id] = set()
            for link in node.links:
                link_map[node.id].add(link)
            for wl in node.wikilinks:
                link_map[node.id].add(wl)

        def has_cycle(start: str, visited: set[str], stack: set[str]) -> bool:
            if start in stack:
                return True
            if start in visited:
                return False
            visited.add(start)
            stack.add(start)
            for neighbor in link_map.get(start, set()):
                if neighbor in link_map and has_cycle(neighbor, visited, stack):
                    return True
            stack.discard(start)
            return False

        for node_id in link_map:
            if has_cycle(node_id, set(), set()):
                evidences.append(
                    Evidence(
                        rule="cyclic_dependency",
                        severity="critical",
                        source_files=[f"node:{node_id}"],
                        source_sdds=[],
                        explanation=f"Cyclic dependency detected involving node '{node_id}'.",
                        confidence=0.8,
                    )
                )
                break

    @staticmethod
    def _detect_overcoupled(evidences: list[Evidence], nodes: list):
        for node in nodes:
            total_links = len(node.links) + len(node.wikilinks)
            if total_links > 10:
                evidences.append(
                    Evidence(
                        rule="overcoupled_node",
                        severity="medium",
                        source_files=[node.path],
                        source_sdds=[],
                        explanation=f"Node '{node.title}' has {total_links} dependencies (threshold: 10). Consider splitting.",
                        confidence=0.7,
                    )
                )

    @staticmethod
    def _persist(evidences: list[Evidence]):
        path = RuntimePathResolver.issues_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "version": "1.0",
                    "total": len(evidences),
                    "generated_at": datetime.now(timezone.utc).isoformat(),
                    "evidences": [e.to_dict() for e in evidences],
                },
                f,
                indent=2,
                ensure_ascii=False,
            )
