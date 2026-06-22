from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import json

from loguru import logger

from app.ai.vault_analyzer.vault_reader import VaultReader
from app.audit.feature_registry import FeatureRegistry
from app.audit.code_scanner import CodeScanner
from app.audit.sdd_resolver import SDDResolver


@dataclass
class DriftScore:
    score: float
    level: str  # low | medium | high | critical
    missing_links: int = 0
    sdd_mismatch: int = 0
    code_vs_vault_diff: int = 0
    generated_at: str = ""

    WEIGHTS = {
        "missing_links": 0.4,
        "sdd_mismatch": 0.3,
        "code_vs_vault_diff": 0.3,
    }

    def to_dict(self) -> dict:
        return {
            "score": round(self.score, 2),
            "level": self.level,
            "missing_links": self.missing_links,
            "sdd_mismatch": self.sdd_mismatch,
            "code_vs_vault_diff": self.code_vs_vault_diff,
            "generated_at": self.generated_at,
        }


class DriftEngine:
    @staticmethod
    def calculate() -> DriftScore:
        vault_nodes = VaultReader.scan_all()
        FeatureRegistry.load_from_json()
        features = FeatureRegistry.list()
        SDDResolver.scan_all_sdds()
        code = CodeScanner.scan_all()

        vault_ids = {n.id for n in vault_nodes}
        code_refs = set(
            code.stores
            + code.routes
            + code.tools
            + code.events
            + code.agents
            + code.workflows
            + code.providers
            + code.components
            + code.hooks
        )

        vault_links = set()
        for node in vault_nodes:
            for link in node.links + node.wikilinks:
                vault_links.add(link)
        total_possible_links = max(len(vault_ids) * 3, 1)
        missing_links_count = total_possible_links - len(vault_links)
        if missing_links_count < 0:
            missing_links_count = 0
        missing_links_score = missing_links_count / total_possible_links

        documented_features = {f.id for f in features if f.docs}
        total_features = max(len(features), 1)
        sdd_mismatch_count = total_features - len(documented_features)
        sdd_mismatch_score = sdd_mismatch_count / total_features

        vault_code_count = len(vault_ids & code_refs)
        total_code_refs = max(len(code_refs), 1)
        code_vs_vault_diff_count = len(code_refs) - vault_code_count
        if code_vs_vault_diff_count < 0:
            code_vs_vault_diff_count = 0
        code_vs_vault_diff_score = code_vs_vault_diff_count / total_code_refs

        final_score = (
            missing_links_score * DriftScore.WEIGHTS["missing_links"]
            + sdd_mismatch_score * DriftScore.WEIGHTS["sdd_mismatch"]
            + code_vs_vault_diff_score * DriftScore.WEIGHTS["code_vs_vault_diff"]
        )
        final_score = min(final_score * 3, 3.0)

        if final_score > 2.5:
            level = "critical"
        elif final_score > 1.5:
            level = "high"
        elif final_score > 0.5:
            level = "medium"
        else:
            level = "low"

        score = DriftScore(
            score=final_score,
            level=level,
            missing_links=missing_links_count,
            sdd_mismatch=sdd_mismatch_count,
            code_vs_vault_diff=code_vs_vault_diff_count,
            generated_at=datetime.now(timezone.utc).isoformat(),
        )

        DriftEngine._persist(score)
        logger.info(f"[drift_engine] score={final_score:.2f} level={level}")
        return score

    @staticmethod
    def load_latest() -> DriftScore | None:
        path = Path("docs/runtime/architecture/analysis.json")
        if not path.exists():
            return None
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return DriftScore(**data)

    @staticmethod
    def get_level_label(level: str) -> str:
        labels = {
            "low": "🟢 Baixo",
            "medium": "🟡 Medio",
            "high": "🔴 Alto",
            "critical": "🚨 Critico",
        }
        return labels.get(level, "⚪ Desconhecido")

    @staticmethod
    def _persist(score: DriftScore):
        path = Path("docs/runtime/architecture/analysis.json")
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(score.to_dict(), f, indent=2, ensure_ascii=False)

        history_dir = Path("docs/runtime/architecture/history")
        history_dir.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        history_path = history_dir / f"{date_str}.json"
        if not history_path.exists():
            with open(history_path, "w", encoding="utf-8") as f:
                json.dump(score.to_dict(), f, indent=2, ensure_ascii=False)
