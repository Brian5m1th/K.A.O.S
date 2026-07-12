"""
Unit tests for K.A.O.S Provider Registry and GraphAdapter.

Tests the ProviderRegistry generic container, adapter registration,
activation, and fallback behavior.
"""

import pytest
from app.core.provider_registry import ProviderRegistry, Provider


# ── Test Provider Implementations ───────────────────────────────────────


class FakeGraphProvider(Provider):
    """Mock graph provider for testing."""

    def __init__(self, name="fake"):
        self._name = name
        self.calls = []

    @property
    def name(self):
        return self._name

    async def explain(self, concept: str):
        self.calls.append(("explain", concept))
        return {"id": "test", "label": concept}

    async def path(self, source, target):
        self.calls.append(("path", source, target))
        return {"source": source, "target": target, "hops": 1}

    async def query(self, query):
        self.calls.append(("query", query.text))
        return {"nodes": [], "total_found": 0}

    async def health(self):
        return True


class FailingGraphProvider(FakeGraphProvider):
    """Provider that always fails health checks."""

    async def health(self):
        return False


# ── Tests ───────────────────────────────────────────────────────────────


class TestProviderRegistry:
    """Tests for the generic ProviderRegistry."""

    def test_register_first_provider_auto_activates(self):
        registry = ProviderRegistry[FakeGraphProvider]("test")
        provider = FakeGraphProvider("graphify")
        registry.register("graphify", provider)

        assert registry.active_key == "graphify"
        assert registry.active is provider

    def test_register_multiple_providers(self):
        registry = ProviderRegistry[FakeGraphProvider]("test")
        registry.register("graphify", FakeGraphProvider("graphify"))
        registry.register("networkx", FakeGraphProvider("networkx"))

        assert "graphify" in registry
        assert "networkx" in registry
        assert registry.list_providers() == ["graphify", "networkx"]
        assert registry.active_key == "graphify"  # First registered wins

    def test_activate_switches_provider(self):
        registry = ProviderRegistry[FakeGraphProvider]("test")
        p1 = FakeGraphProvider("graphify")
        p2 = FakeGraphProvider("networkx")
        registry.register("graphify", p1)
        registry.register("networkx", p2)

        assert registry.active is p1
        registry.activate("networkx")
        assert registry.active is p2
        assert registry.active_key == "networkx"

    def test_activate_unknown_key_raises(self):
        registry = ProviderRegistry[FakeGraphProvider]("test")
        with pytest.raises(KeyError):
            registry.activate("nonexistent")

    def test_remove_provider(self):
        registry = ProviderRegistry[FakeGraphProvider]("test")
        registry.register("a", FakeGraphProvider("a"))
        registry.register("b", FakeGraphProvider("b"))

        registry.remove("a")
        assert "a" not in registry
        assert registry.active_key == "b"

    def test_remove_active_provider_falls_back(self):
        registry = ProviderRegistry[FakeGraphProvider]("test")
        registry.register("a", FakeGraphProvider("a"))
        registry.register("b", FakeGraphProvider("b"))
        registry.activate("a")

        registry.remove("a")
        assert registry.active_key == "b"

    def test_empty_registry_active_raises(self):
        registry = ProviderRegistry[FakeGraphProvider]("test")
        with pytest.raises(RuntimeError):
            _ = registry.active

    def test_deactivate_then_active_auto_selects(self):
        registry = ProviderRegistry[FakeGraphProvider]("test")
        registry.register("a", FakeGraphProvider("a"))
        registry.register("b", FakeGraphProvider("b"))

        registry.deactivate()
        assert registry.active_key is None  # No active provider after deactivate
        # Accessing .active triggers lazy auto-select
        _ = registry.active
        assert registry.active_key == "a"  # Auto-select first

    def test_repr_shows_state(self):
        registry = ProviderRegistry[FakeGraphProvider]("graph")
        registry.register("graphify", FakeGraphProvider("graphify"))
        rep = repr(registry)
        assert "graph" in rep
        assert "graphify" in rep

    def test_register_overwrites_existing_key(self):
        registry = ProviderRegistry[FakeGraphProvider]("test")
        p1 = FakeGraphProvider("old")
        p2 = FakeGraphProvider("new")
        registry.register("x", p1)
        registry.register("x", p2)
        assert registry.active is p2


class TestGraphifyAdapter:
    """Tests for the GraphifyAdapter implementation."""

    def test_adapter_has_correct_name(self):
        from app.providers.graph.graphify_adapter import GraphifyAdapter

        adapter = GraphifyAdapter()
        assert adapter.provider_name == "graphify"

    def test_networkx_fallback_has_correct_name(self):
        from app.providers.graph.networkx_fallback import NetworkXFallback

        fallback = NetworkXFallback()
        assert fallback.provider_name == "networkx-fallback"

    def test_networkx_fallback_explain_matches_label(self):
        import asyncio
        from app.providers.graph.networkx_fallback import NetworkXFallback

        fallback = NetworkXFallback()
        fallback.add_node("test_id", "TestNode", "test.py", "code")

        result = asyncio.run(fallback.explain("TestNode"))
        assert result is not None
        assert result.label == "TestNode"

    def test_networkx_fallback_health_always_true(self):
        import asyncio
        from app.providers.graph.networkx_fallback import NetworkXFallback

        fallback = NetworkXFallback()
        assert asyncio.run(fallback.health()) is True


class TestEvidenceEngine:
    """Tests for the EvidenceEngine."""

    def test_engine_has_correct_name(self):
        from app.providers.evidence.engine import EvidenceEngine

        engine = EvidenceEngine()
        assert engine.provider_name == "evidence-engine"

    def test_collect_returns_report(self):
        import asyncio
        from app.providers.evidence.engine import EvidenceEngine

        engine = EvidenceEngine()
        report = asyncio.run(engine.collect())
        assert report is not None
        assert len(report.metrics) > 0
        assert "graphify" in report.sources_checked
