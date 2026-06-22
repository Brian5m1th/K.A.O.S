import pytest
from app.audit.audit_engine import DriftReport, AuditEngine
from app.audit.feature_registry import FeatureEntry, FeatureRegistry


class TestDriftReport:
    def test_create_default(self):
        report = DriftReport(coverage=0)
        assert report.coverage == 0
        assert report.missing_features == []
        assert report.outdated_docs == []
        assert report.inconsistent_phases == []

    def test_create_with_data(self):
        report = DriftReport(
            coverage=75.5,
            missing_features=["feature-a", "feature-b"],
            outdated_docs=["SDD-OLD.md"],
        )
        assert report.coverage == 75.5
        assert len(report.missing_features) == 2
        assert len(report.outdated_docs) == 1


class TestAuditEngine:
    def setup_method(self):
        FeatureRegistry.clear()

    def test_get_drift_level_low(self):
        assert AuditEngine.get_drift_level(95) == "low"
        assert AuditEngine.get_drift_level(100) == "low"

    def test_get_drift_level_medium(self):
        assert AuditEngine.get_drift_level(85) == "medium"
        assert AuditEngine.get_drift_level(80) == "medium"

    def test_get_drift_level_high(self):
        assert AuditEngine.get_drift_level(50) == "high"
        assert AuditEngine.get_drift_level(30) == "high"

    def test_run_audit_returns_report(self):
        FeatureRegistry.register(FeatureEntry(
            id="test-feature", name="Test Feature", phase="p1", status="done",
            docs=["SDD-TEST.md"], code_refs=["src/test.py"]
        ))
        report = AuditEngine.run_audit()
        assert isinstance(report, DriftReport)
        assert isinstance(report.coverage, float)
        assert isinstance(report.missing_features, list)
        assert isinstance(report.outdated_docs, list)
        assert isinstance(report.inconsistent_phases, list)
        assert isinstance(report.orphaned_sdds, list)
        assert isinstance(report.undocumented_code, list)
        assert report.generated_at != ""

    def test_load_latest_report(self):
        FeatureRegistry.register(FeatureEntry(
            id="test", name="Test", phase="p1", status="done"
        ))
        AuditEngine.run_audit()
        report = AuditEngine.load_latest_report()
        assert report is not None
        assert isinstance(report.coverage, float)