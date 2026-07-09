import pytest
from unittest.mock import MagicMock
from app.ai.vault_analyzer.evidence_engine import EvidenceEngine, Evidence
from app.ai.vault_analyzer.vault_reader import VaultNode


class TestEvidenceEngineContradictions:
    def test_detect_phase_contradiction(self) -> None:
        # Phase 1 node depending on Phase 2 node (contradiction!)
        node_p1 = MagicMock(spec=VaultNode)
        node_p1.id = "feature-core"
        node_p1.title = "Core Feature"
        node_p1.path = "docs/sdd/core.md"
        node_p1.phase = "Phase 1"
        node_p1.status = "implemented"
        node_p1.links = ["feature-advanced"]
        node_p1.wikilinks = []

        node_p2 = MagicMock(spec=VaultNode)
        node_p2.id = "feature-advanced"
        node_p2.title = "Advanced Feature"
        node_p2.path = "docs/sdd/advanced.md"
        node_p2.phase = "Phase 2"
        node_p2.status = "roadmap"
        node_p2.links = []
        node_p2.wikilinks = []

        evidences: list[Evidence] = []
        nodes = [node_p1, node_p2]

        EvidenceEngine._detect_contradictions(evidences, nodes)

        # We expect a logical contradiction evidence
        assert len(evidences) == 1
        ev = evidences[0]
        assert ev.rule == "logical_contradiction"
        assert ev.severity == "high"
        assert "Contradição de Cronograma" in ev.explanation
        assert "feature-core" in ev.explanation or "Core Feature" in ev.explanation

    def test_detect_deprecated_contradiction(self) -> None:
        # Implemented node depending on a deprecated node (contradiction!)
        node_active = MagicMock(spec=VaultNode)
        node_active.id = "active-module"
        node_active.title = "Active Module"
        node_active.path = "docs/sdd/active.md"
        node_active.phase = "Phase 1"
        node_active.status = "implemented"
        node_active.links = ["old-module"]
        node_active.wikilinks = []

        node_deprecated = MagicMock(spec=VaultNode)
        node_deprecated.id = "old-module"
        node_deprecated.title = "Old Module"
        node_deprecated.path = "docs/sdd/old.md"
        node_deprecated.phase = "Phase 1"
        node_deprecated.status = "deprecated"
        node_deprecated.links = []
        node_deprecated.wikilinks = []

        evidences: list[Evidence] = []
        nodes = [node_active, node_deprecated]

        EvidenceEngine._detect_contradictions(evidences, nodes)

        assert len(evidences) == 1
        ev = evidences[0]
        assert ev.rule == "logical_contradiction"
        assert ev.severity == "high"
        assert "Contradição de Status" in ev.explanation
        assert "old-module" in ev.explanation or "Old Module" in ev.explanation

    def test_no_contradiction_when_valid(self) -> None:
        # Phase 2 node depending on Phase 1 node (valid!)
        node_p1 = MagicMock(spec=VaultNode)
        node_p1.id = "feature-core"
        node_p1.title = "Core Feature"
        node_p1.path = "docs/sdd/core.md"
        node_p1.phase = "Phase 1"
        node_p1.status = "implemented"
        node_p1.links = []
        node_p1.wikilinks = []

        node_p2 = MagicMock(spec=VaultNode)
        node_p2.id = "feature-advanced"
        node_p2.title = "Advanced Feature"
        node_p2.path = "docs/sdd/advanced.md"
        node_p2.phase = "Phase 2"
        node_p2.status = "roadmap"
        node_p2.links = ["feature-core"]
        node_p2.wikilinks = []

        evidences: list[Evidence] = []
        nodes = [node_p1, node_p2]

        EvidenceEngine._detect_contradictions(evidences, nodes)

        assert len(evidences) == 0
