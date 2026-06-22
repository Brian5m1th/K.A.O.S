from app.audit.commit_classifier import (
    classify_commit,
    classify_commits,
    classify_type,
    extract_scope,
    is_breaking,
    assess_impact,
    extract_features,
    CommitType,
    ImpactLevel,
)


class TestCommitClassifier:
    def test_classify_type_feat(self):
        assert classify_type("feat: new feature") == CommitType.FEAT
        assert classify_type("feat(core): new feature") == CommitType.FEAT

    def test_classify_type_fix(self):
        assert classify_type("fix: bug fix") == CommitType.FIX
        assert classify_type("fix(api): fix endpoint") == CommitType.FIX

    def test_classify_type_merge(self):
        assert classify_type("merge branch 'dev'") == CommitType.MERGE
        assert (
            classify_type("Merge remote-tracking branch 'origin/dev'")
            == CommitType.MERGE
        )

    def test_classify_type_test(self):
        assert classify_type("test: add tests") == CommitType.TEST

    def test_classify_type_style(self):
        assert classify_type("style: format code") == CommitType.STYLE

    def test_classify_type_unknown(self):
        assert classify_type("random message") == CommitType.UNKNOWN

    def test_extract_scope(self):
        assert extract_scope("feat(core): new feature") == "core"
        assert extract_scope("fix(api): fix endpoint") == "api"
        assert extract_scope("feat: no scope") is None

    def test_is_breaking(self):
        assert is_breaking("feat!: breaking change") is True
        assert is_breaking("feat: normal change") is False

    def test_assess_impact_high(self):
        assert assess_impact("event bus integration") == ImpactLevel.HIGH
        assert assess_impact("workflow engine") == ImpactLevel.HIGH
        assert assess_impact("model router") == ImpactLevel.HIGH

    def test_assess_impact_medium(self):
        assert assess_impact("api endpoint") == ImpactLevel.MEDIUM
        assert assess_impact("database migration") == ImpactLevel.MEDIUM

    def test_assess_impact_low(self):
        assert assess_impact("typo fix") == ImpactLevel.LOW
        assert assess_impact("readme update") == ImpactLevel.LOW

    def test_extract_features_observability(self):
        features = extract_features("feat: prometheus metrics")
        assert "observability" in features

    def test_extract_features_event_bus(self):
        features = extract_features("feat: event bus subscriber")
        assert "event-bus" in features

    def test_extract_features_workflow(self):
        features = extract_features("feat: new workflow engine")
        assert "workflow-engine" in features

    def test_extract_features_multiple(self):
        features = extract_features("feat: event bus and observability")
        assert "event-bus" in features
        assert "observability" in features

    def test_classify_commit(self):
        result = classify_commit("abc123", "feat: N8N integration")
        assert result.hash == "abc123"
        assert result.type == CommitType.FEAT
        assert result.impact == ImpactLevel.HIGH
        assert "n8n-integration" in result.features_mentioned

    def test_classify_commits(self):
        commits = [
            ("abc", "feat: workflow engine"),
            ("def", "fix: bug fix"),
        ]
        results = classify_commits(commits)
        assert len(results) == 2
        assert results[0].type == CommitType.FEAT
        assert results[1].type == CommitType.FIX
