"""
EvidenceEngine — Multi-source evidence collector.

Aggregates evidence from Graphify, Git history, test results,
benchmarks, ADRs, and runtime metrics into unified reports.

This is the heart of the Evidence-Driven Decision system (Phase 8 evolution).
"""

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from loguru import logger
from app.domain.ports.evidence_port import (
    EvidencePort, EvidenceReport, EvidenceMetric, EvidenceLevel,
)


class EvidenceEngine(EvidencePort):
    """Multi-source evidence collection engine."""

    def __init__(self):
        self._sources: dict[str, bool] = {
            "graphify": True,
            "git": True,
            "tests": False,
            "benchmarks": False,
            "adrs": True,
            "runtime": False,
        }

    @property
    def provider_name(self) -> str:
        return "evidence-engine"

    async def collect(self) -> EvidenceReport:
        """Collect evidence from all available sources."""
        report = EvidenceReport(sources_checked=[])
        metrics = []

        # Graphify — structural evidence
        if self._sources["graphify"]:
            report.sources_checked.append("graphify")
            metrics.extend(await self._collect_graphify_evidence())

        # Git — commit history
        if self._sources["git"]:
            report.sources_checked.append("git")
            metrics.extend(await self._collect_git_evidence())

        # ADRs — decision health
        if self._sources["adrs"]:
            report.sources_checked.append("adrs")
            metrics.extend(await self._collect_adr_evidence())

        report.metrics = metrics
        report.overall_score = self._calculate_score(metrics)
        report.level = self._assess_level(report.overall_score)

        if report.overall_score < 70:
            report.recommendations.append("Run full architecture audit")
        if report.overall_score < 50:
            report.recommendations.append("Address critical drift issues immediately")

        return report

    async def _collect_graphify_evidence(self) -> list[EvidenceMetric]:
        """Collect structural evidence from Graphify graph."""
        metrics = []

        # Check graph.json stats
        graph_path = Path("graphify-out/graph.json")
        if graph_path.exists():
            with open(graph_path) as f:
                data = json.load(f)
            node_count = len(data.get("nodes", []))
            edge_count = len(data.get("links", []))

            metrics.append(EvidenceMetric(
                name="graph_nodes",
                value=node_count,
                level=EvidenceLevel.HEALTHY if node_count > 1000 else EvidenceLevel.WARNING,
                source="graphify",
                description=f"{node_count} code symbols indexed",
            ))

            metrics.append(EvidenceMetric(
                name="graph_edges",
                value=edge_count,
                level=EvidenceLevel.HEALTHY,
                source="graphify",
                description=f"{edge_count} code relationships mapped",
            ))

        return metrics

    async def _collect_git_evidence(self) -> list[EvidenceMetric]:
        """Collect evidence from Git history."""
        metrics = []
        try:
            result = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                capture_output=True, text=True, timeout=5,
            )
            if result.returncode == 0:
                metrics.append(EvidenceMetric(
                    name="git_commit",
                    value=1.0,
                    level=EvidenceLevel.HEALTHY,
                    source="git",
                    description=f"HEAD: {result.stdout.strip()[:8]}",
                ))

            # Count recent commits (last 30 days)
            result = subprocess.run(
                ["git", "rev-list", "--count", "--since=30.days", "HEAD"],
                capture_output=True, text=True, timeout=5,
            )
            if result.returncode == 0:
                commit_count = int(result.stdout.strip() or "0")
                level = EvidenceLevel.HEALTHY if commit_count > 5 else EvidenceLevel.WARNING
                metrics.append(EvidenceMetric(
                    name="git_recent_commits",
                    value=commit_count,
                    level=level,
                    threshold_good=5,
                    threshold_bad=1,
                    source="git",
                    description=f"{commit_count} commits in last 30 days",
                ))
        except Exception as e:
            logger.warning(f"[evidence:git] Failed: {e}")

        return metrics

    async def _collect_adr_evidence(self) -> list[EvidenceMetric]:
        """Collect evidence from Architecture Decision Records."""
        adr_dir = Path("docs/adr") if (Path("docs/adr").exists()) else Path("kaos-research/adrs")
        adr_count = len(list(adr_dir.glob("*.md"))) if adr_dir.exists() else 0

        return [EvidenceMetric(
            name="adr_count",
            value=adr_count,
            level=EvidenceLevel.HEALTHY if adr_count >= 3 else EvidenceLevel.WARNING,
            threshold_good=3,
            threshold_bad=1,
            source="adrs",
            description=f"{adr_count} Architecture Decision Records",
        )]

    async def get_metric(self, name: str) -> Optional[EvidenceMetric]:
        report = await self.collect()
        for m in report.metrics:
            if m.name == name:
                return m
        return None

    async def get_history(self, metric: str, days: int = 30) -> list[EvidenceMetric]:
        # Stub — historical tracking requires persistent storage
        return []

    async def health(self) -> bool:
        return True

    def _calculate_score(self, metrics: list[EvidenceMetric]) -> float:
        if not metrics:
            return 0.0
        scores = []
        weights = {
            "graph_nodes": 0.3,
            "git_recent_commits": 0.2,
            "adr_count": 0.2,
        }
        for m in metrics:
            w = weights.get(m.name, 0.1)
            score = 0.0
            if m.level == EvidenceLevel.HEALTHY:
                score = 100.0 * w
            elif m.level == EvidenceLevel.WARNING:
                score = 50.0 * w
            scores.append(score)
        return sum(scores) / len(scores) * 100 if scores else 0.0

    def _assess_level(self, score: float) -> EvidenceLevel:
        if score >= 80:
            return EvidenceLevel.HEALTHY
        elif score >= 50:
            return EvidenceLevel.WARNING
        return EvidenceLevel.CRITICAL
