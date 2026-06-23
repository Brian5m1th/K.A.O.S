from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional

from loguru import logger

from app.audit.feature_registry import FeatureRegistry, FeatureEntry
from app.audit.code_scanner import CodeScanner, CodeSnapshot
from app.audit.sdd_resolver import SDDResolver
from app.audit.commit_mapper import CommitMapper
from app.audit.runtime_resolver import RuntimePathResolver


@dataclass
class DriftReport:
    coverage: float
    missing_features: list[str] = field(default_factory=list)
    undocumented_code: list[str] = field(default_factory=list)
    outdated_docs: list[str] = field(default_factory=list)
    inconsistent_phases: list[str] = field(default_factory=list)
    orphaned_sdds: list[str] = field(default_factory=list)
    generated_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


class AuditEngine:
    _audit_dir = RuntimePathResolver.audit_dir()
    _high_drift_threshold = 30.0
    _medium_drift_threshold = 15.0

    @classmethod
    def run_audit(cls) -> DriftReport:
        FeatureRegistry.load_from_json()
        CommitMapper.generate_map()
        SDDResolver.scan_all_sdds()
        code_snapshot = CodeScanner.scan_all()

        features = FeatureRegistry.list()
        sdds = SDDResolver.get_all_sdds()

        missing = cls._find_missing_features(features, sdds)
        undocumented = cls._find_undocumented_code(features, code_snapshot)
        outdated = cls._find_outdated_docs(features)
        inconsistent = cls._find_inconsistent_phases(features)
        orphaned = cls._find_orphaned_sdds(features, sdds)

        total = len(features)
        documented = len([f for f in features if f.docs])
        coverage = (documented / total * 100) if total > 0 else 100.0

        report = DriftReport(
            coverage=coverage,
            missing_features=missing,
            undocumented_code=undocumented,
            outdated_docs=outdated,
            inconsistent_phases=inconsistent,
            orphaned_sdds=orphaned,
        )

        cls._persist_report(report)
        logger.info(
            f"[audit_engine] audit complete: coverage={coverage:.1f}%, missing={len(missing)}, outdated={len(outdated)}"
        )
        return report

    @classmethod
    def _find_missing_features(cls, features: list[FeatureEntry], sdds) -> list[str]:
        missing = []
        for feat in features:
            if not feat.docs:
                sdd_status = SDDResolver.get_sdd_status(feat.id)
                if sdd_status == "missing":
                    missing.append(feat.id)
        return missing

    @classmethod
    def _find_undocumented_code(
        cls, features: list[FeatureEntry], code: CodeSnapshot
    ) -> list[str]:
        undocumented = []
        known_ids = {f.id for f in features}
        all_code_refs = (
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
        for ref in all_code_refs:
            if ref not in known_ids and not any(ref in f.code_refs for f in features):
                undocumented.append(ref)
        return list(set(undocumented))

    @classmethod
    def _find_outdated_docs(cls, features: list[FeatureEntry]) -> list[str]:
        outdated = []
        commits = CommitMapper.load()
        if not commits:
            return outdated

        latest_commit = commits[0].hash if commits else ""
        for feat in features:
            if feat.docs and feat.last_commit and feat.last_commit != latest_commit:
                outdated.append(feat.id)
        return outdated

    @classmethod
    def _find_inconsistent_phases(cls, features: list[FeatureEntry]) -> list[str]:
        inconsistent = []
        for feat in features:
            if feat.status == "done" and not feat.docs:
                inconsistent.append(f"{feat.id}: status=done but no docs")
            if feat.status == "planned" and feat.code_refs:
                inconsistent.append(f"{feat.id}: status=planned but has code refs")
        return inconsistent

    @classmethod
    def _find_orphaned_sdds(cls, features: list[FeatureEntry], sdds) -> list[str]:
        known_features = {f.id.lower() for f in features}
        orphaned = []
        for sdd in sdds:
            has_known = any(f in known_features for f in sdd.linked_features)
            if not has_known and sdd.linked_features:
                orphaned.append(sdd.id)
        return orphaned

    @classmethod
    def _persist_report(cls, report: DriftReport) -> None:
        cls._audit_dir.mkdir(parents=True, exist_ok=True)

        coverage_path = cls._audit_dir / "coverage-report.json"
        with open(coverage_path, "w", encoding="utf-8") as f:
            import json

            json.dump(
                {
                    "coverage": round(report.coverage, 1),
                    "totalFeatures": len(FeatureRegistry.list()),
                    "documented": len([f for f in FeatureRegistry.list() if f.docs]),
                    "missingDocs": len(report.missing_features),
                    "staleDocs": len(report.outdated_docs),
                    "orphanedSDDs": len(report.orphaned_sdds),
                    "inconsistentPhases": len(report.inconsistent_phases),
                    "undocumentedCode": len(report.undocumented_code),
                    "generatedAt": report.generated_at,
                },
                f,
                indent=2,
                ensure_ascii=False,
            )

        missing_path = cls._audit_dir / "undocumented-features.json"
        with open(missing_path, "w", encoding="utf-8") as f:
            import json

            json.dump(report.missing_features, f, indent=2, ensure_ascii=False)

        inconsistent_path = cls._audit_dir / "inconsistencies.json"
        with open(inconsistent_path, "w", encoding="utf-8") as f:
            import json

            json.dump(
                {
                    "outdatedDocs": report.outdated_docs,
                    "inconsistentPhases": report.inconsistent_phases,
                    "orphanedSDDs": report.orphaned_sdds,
                    "undocumentedCode": report.undocumented_code,
                },
                f,
                indent=2,
                ensure_ascii=False,
            )

    @classmethod
    def get_drift_level(cls, coverage: float) -> str:
        missing_pct = 100 - coverage
        if missing_pct >= cls._high_drift_threshold:
            return "high"
        if missing_pct >= cls._medium_drift_threshold:
            return "medium"
        return "low"

    @classmethod
    def load_latest_report(cls) -> Optional[DriftReport]:
        coverage_path = cls._audit_dir / "coverage-report.json"
        if coverage_path.exists():
            import json

            with open(coverage_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            missing_path = cls._audit_dir / "undocumented-features.json"
            missing = []
            if missing_path.exists():
                with open(missing_path, "r", encoding="utf-8") as f:
                    missing = json.load(f)
            inc_path = cls._audit_dir / "inconsistencies.json"
            inc = {}
            if inc_path.exists():
                with open(inc_path, "r", encoding="utf-8") as f:
                    inc = json.load(f)
            return DriftReport(
                coverage=data.get("coverage", 0),
                missing_features=missing,
                outdated_docs=inc.get("outdatedDocs", []),
                inconsistent_phases=inc.get("inconsistentPhases", []),
                orphaned_sdds=inc.get("orphanedSDDs", []),
                undocumented_code=inc.get("undocumentedCode", []),
                generated_at=data.get("generatedAt", ""),
            )
        return None
