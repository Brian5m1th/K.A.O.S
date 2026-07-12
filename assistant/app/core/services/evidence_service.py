"""
EvidenceService — Architecture evidence and health orchestrator.

Aggregates multiple sources (Graphify, Git, Tests, Coverage,
Benchmarks, ADRs, Runtime) into unified evidence reports.
"""

from app.core.provider_registry import ProviderRegistry
from app.domain.ports.evidence_port import EvidencePort, EvidenceReport, EvidenceMetric


class EvidenceService:
    """Service for evidence collection and architectural health assessment."""

    def __init__(self):
        self.registry = ProviderRegistry[EvidencePort]("evidence")

    async def collect(self) -> EvidenceReport:
        return await self.registry.active.collect()

    async def get_metric(self, name: str) -> EvidenceMetric | None:
        return await self.registry.active.get_metric(name)

    async def get_history(self, metric: str, days: int = 30) -> list[EvidenceMetric]:
        return await self.registry.active.get_history(metric, days)

    async def health(self) -> dict:
        provider = self.registry.active_key or "none"
        ok = await self.registry.active.health()
        return {
            "service": "evidence",
            "healthy": ok,
            "active_provider": provider,
            "available_providers": self.registry.list_providers(),
        }
