"""
EvidencePort — Architecture evidence and decision support capability.

Aggregates multiple data sources (Graphify, Git, Tests, Coverage,
Benchmarks, ADRs, Runtime Metrics) to produce evidence-based
architectural health reports.

This is the foundation for the Technology Observatory and the
Evidence-Driven Decision process (K.A.O.S Phase 8 evolution).
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from enum import Enum


class EvidenceLevel(str, Enum):
    HEALTHY = "healthy"
    WARNING = "warning"
    CRITICAL = "critical"
    UNKNOWN = "unknown"


@dataclass
class EvidenceMetric:
    """A single evidence data point."""
    name: str
    value: float
    level: EvidenceLevel = EvidenceLevel.UNKNOWN
    threshold_good: float = 0.0
    threshold_bad: float = 0.0
    source: str = ""  # graphify | git | tests | benchmarks | adrs
    description: str = ""


@dataclass
class EvidenceReport:
    """Aggregated evidence report from all sources."""
    generated_at: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )
    metrics: list[EvidenceMetric] = field(default_factory=list)
    overall_score: float = 0.0  # 0-100
    level: EvidenceLevel = EvidenceLevel.UNKNOWN
    recommendations: list[str] = field(default_factory=list)
    sources_checked: list[str] = field(default_factory=list)


class EvidencePort(ABC):
    """
    Interface for evidence collection and architectural health assessment.

    Sources aggregated by the Evidence Engine:
      - Graphify: AST structure, cycles, god objects, dependencies
      - Git: commit frequency, churn, ownership
      - Tests: coverage, mutation score, pass rate
      - Benchmarks: latency, throughput, quality
      - ADRs: decision history, freshness, compliance
      - Runtime: service health, uptime, error rates

    Note: No single source (including Graphify) is the sole authority.
    The Evidence Engine weighs multiple sources for each metric.
    """

    @property
    @abstractmethod
    def provider_name(self) -> str:
        ...

    @abstractmethod
    async def collect(self) -> EvidenceReport:
        """Collect evidence from all configured sources."""
        ...

    @abstractmethod
    async def get_metric(self, name: str) -> Optional[EvidenceMetric]:
        """Get a specific evidence metric by name."""
        ...

    @abstractmethod
    async def get_history(self, metric: str, days: int = 30) -> list[EvidenceMetric]:
        """Get historical evidence data for trend analysis."""
        ...

    @abstractmethod
    async def health(self) -> bool:
        """Check if all evidence sources are available."""
        ...
