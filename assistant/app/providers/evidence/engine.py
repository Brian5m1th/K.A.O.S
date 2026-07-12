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
    EvidencePort,
    EvidenceReport,
    EvidenceMetric,
    EvidenceLevel,
)


class EvidenceEngine(EvidencePort):
    """Multi-source evidence collection engine."""

    def __init__(self):
        self._sources: dict[str, bool] = {
            "graphify": True,
            "git": True,
            "tests": True,
            "benchmarks": True,
            "adrs": True,
            "runtime": True,
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

        # Tests — test suite health
        if self._sources["tests"]:
            report.sources_checked.append("tests")
            metrics.extend(await self._collect_test_evidence())

        # Benchmarks — performance baselines
        if self._sources["benchmarks"]:
            report.sources_checked.append("benchmarks")
            metrics.extend(await self._collect_benchmark_evidence())

        # Runtime — live system metrics
        if self._sources["runtime"]:
            report.sources_checked.append("runtime")
            metrics.extend(await self._collect_runtime_evidence())

        report.metrics = metrics
        report.overall_score = self._calculate_score(metrics)
        report.level = self._assess_level(report.overall_score)

        # Persist snapshot for historical queries
        self._save_snapshot(report)

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

            metrics.append(
                EvidenceMetric(
                    name="graph_nodes",
                    value=node_count,
                    level=EvidenceLevel.HEALTHY
                    if node_count > 1000
                    else EvidenceLevel.WARNING,
                    source="graphify",
                    description=f"{node_count} code symbols indexed",
                )
            )

            metrics.append(
                EvidenceMetric(
                    name="graph_edges",
                    value=edge_count,
                    level=EvidenceLevel.HEALTHY,
                    source="graphify",
                    description=f"{edge_count} code relationships mapped",
                )
            )

        return metrics

    async def _collect_git_evidence(self) -> list[EvidenceMetric]:
        """Collect evidence from Git history."""
        metrics = []
        try:
            result = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if result.returncode == 0:
                metrics.append(
                    EvidenceMetric(
                        name="git_commit",
                        value=1.0,
                        level=EvidenceLevel.HEALTHY,
                        source="git",
                        description=f"HEAD: {result.stdout.strip()[:8]}",
                    )
                )

            # Count recent commits (last 30 days)
            result = subprocess.run(
                ["git", "rev-list", "--count", "--since=30.days", "HEAD"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if result.returncode == 0:
                commit_count = int(result.stdout.strip() or "0")
                level = (
                    EvidenceLevel.HEALTHY if commit_count > 5 else EvidenceLevel.WARNING
                )
                metrics.append(
                    EvidenceMetric(
                        name="git_recent_commits",
                        value=commit_count,
                        level=level,
                        threshold_good=5,
                        threshold_bad=1,
                        source="git",
                        description=f"{commit_count} commits in last 30 days",
                    )
                )
        except Exception as e:
            logger.warning(f"[evidence:git] Failed: {e}")

        return metrics

    async def _collect_test_evidence(self) -> list[EvidenceMetric]:
        """Collect evidence from test suite results."""
        metrics = []
        report_path = Path("data/test_report.json")
        if report_path.exists():
            try:
                with open(report_path) as f:
                    data = json.load(f)
                total = data.get("total", 0)
                passed = data.get("passed", 0)
                failed = data.get("failed", 0)
                skipped = data.get("skipped", 0)

                pass_rate = (passed / total * 100) if total > 0 else 0
                metrics.append(
                    EvidenceMetric(
                        name="test_pass_rate",
                        value=round(pass_rate, 1),
                        level=EvidenceLevel.HEALTHY
                        if pass_rate >= 90
                        else EvidenceLevel.WARNING
                        if pass_rate >= 70
                        else EvidenceLevel.CRITICAL,
                        source="tests",
                        description=f"{passed}/{total} passed ({failed} failed, {skipped} skipped)",
                    )
                )

                metrics.append(
                    EvidenceMetric(
                        name="test_total",
                        value=total,
                        level=EvidenceLevel.HEALTHY
                        if total > 10
                        else EvidenceLevel.WARNING,
                        threshold_good=10,
                        threshold_bad=1,
                        source="tests",
                        description=f"{total} test cases",
                    )
                )
            except (json.JSONDecodeError, OSError) as exc:
                logger.warning(f"[evidence:tests] Failed to read test report: {exc}")
        else:
            # Count test files as proxy
            test_files = list(Path("assistant/tests").rglob("test_*.py"))
            test_count = len(test_files)
            metrics.append(
                EvidenceMetric(
                    name="test_files",
                    value=test_count,
                    level=EvidenceLevel.HEALTHY
                    if test_count > 5
                    else EvidenceLevel.WARNING,
                    threshold_good=5,
                    threshold_bad=1,
                    source="tests",
                    description=f"{test_count} test files found",
                )
            )

        return metrics

    async def _collect_benchmark_evidence(self) -> list[EvidenceMetric]:
        """Collect evidence from benchmark results."""
        metrics = []
        bench_path = Path("data/benchmark_results.json")
        if bench_path.exists():
            try:
                with open(bench_path) as f:
                    data = json.load(f)
                for bench, result in data.items():
                    metrics.append(
                        EvidenceMetric(
                            name=f"benchmark_{bench}",
                            value=result.get("score", 0),
                            level=EvidenceLevel(result.get("level", "warning")),
                            source="benchmarks",
                            description=result.get("description", ""),
                        )
                    )
            except (json.JSONDecodeError, OSError) as exc:
                logger.warning(f"[evidence:benchmarks] Failed to read: {exc}")

        # If no benchmark file, report as warning
        if not metrics:
            metrics.append(
                EvidenceMetric(
                    name="benchmark_data",
                    value=0,
                    level=EvidenceLevel.WARNING,
                    source="benchmarks",
                    description="No benchmark data available",
                )
            )

        return metrics

    async def _collect_runtime_evidence(self) -> list[EvidenceMetric]:
        """Collect evidence from live runtime metrics."""
        metrics = []

        # Check API health
        try:
            import httpx

            async with httpx.AsyncClient(timeout=3) as c:
                r = await c.get("http://localhost:1010/health")
                if r.is_success:
                    metrics.append(
                        EvidenceMetric(
                            name="api_health",
                            value=1.0,
                            level=EvidenceLevel.HEALTHY,
                            source="runtime",
                            description="API is responding",
                        )
                    )
                else:
                    metrics.append(
                        EvidenceMetric(
                            name="api_health",
                            value=0.0,
                            level=EvidenceLevel.CRITICAL,
                            source="runtime",
                            description=f"API returned {r.status_code}",
                        )
                    )
        except Exception as exc:
            metrics.append(
                EvidenceMetric(
                    name="api_health",
                    value=0.0,
                    level=EvidenceLevel.WARNING,
                    source="runtime",
                    description=f"API unreachable: {exc}",
                )
            )

        # Check Qdrant health
        try:
            import httpx

            async with httpx.AsyncClient(timeout=2) as c:
                r = await c.get("http://localhost:6333/")
                if r.is_success:
                    metrics.append(
                        EvidenceMetric(
                            name="qdrant_health",
                            value=1.0,
                            level=EvidenceLevel.HEALTHY,
                            source="runtime",
                            description="Qdrant is responding",
                        )
                    )
                else:
                    metrics.append(
                        EvidenceMetric(
                            name="qdrant_health",
                            value=0.0,
                            level=EvidenceLevel.CRITICAL,
                            source="runtime",
                            description=f"Qdrant returned {r.status_code}",
                        )
                    )
        except Exception as exc:
            metrics.append(
                EvidenceMetric(
                    name="qdrant_health",
                    value=0.0,
                    level=EvidenceLevel.WARNING,
                    source="runtime",
                    description=f"Qdrant unreachable: {exc}",
                )
            )

        return metrics

    async def _collect_adr_evidence(self) -> list[EvidenceMetric]:
        """Collect evidence from Architecture Decision Records."""
        adr_dir = (
            Path("docs/adr")
            if (Path("docs/adr").exists())
            else Path("kaos-research/adrs")
        )
        adr_count = len(list(adr_dir.glob("*.md"))) if adr_dir.exists() else 0

        return [
            EvidenceMetric(
                name="adr_count",
                value=adr_count,
                level=EvidenceLevel.HEALTHY
                if adr_count >= 3
                else EvidenceLevel.WARNING,
                threshold_good=3,
                threshold_bad=1,
                source="adrs",
                description=f"{adr_count} Architecture Decision Records",
            )
        ]

    async def get_metric(self, name: str) -> Optional[EvidenceMetric]:
        report = await self.collect()
        for m in report.metrics:
            if m.name == name:
                return m
        return None

    async def get_history(self, metric: str, days: int = 30) -> list[EvidenceMetric]:
        """Retrieve historical evidence snapshots for a given metric."""
        history_file = self._history_path()
        if not history_file.exists():
            logger.info("[evidence] No history file found, returning empty")
            return []

        try:
            with open(history_file) as f:
                snapshots = json.load(f)
        except (json.JSONDecodeError, OSError) as exc:
            logger.warning(f"[evidence] Failed to read history file: {exc}")
            return []

        cutoff = datetime.now(timezone.utc).timestamp() - (days * 86400)
        result = []

        for snapshot in snapshots:
            ts = snapshot.get("timestamp", 0)
            if ts < cutoff:
                continue

            for m in snapshot.get("metrics", []):
                if m.get("name") == metric:
                    result.append(
                        EvidenceMetric(
                            name=m["name"],
                            value=m.get("value", 0),
                            level=EvidenceLevel(m.get("level", "warning")),
                            source=m.get("source", "unknown"),
                            description=m.get("description", ""),
                            threshold_good=m.get("threshold_good"),
                            threshold_bad=m.get("threshold_bad"),
                        )
                    )

        return result

    def _save_snapshot(self, report: EvidenceReport) -> None:
        """Persist an evidence report snapshot to the history file."""
        history_file = self._history_path()
        history_file.parent.mkdir(parents=True, exist_ok=True)

        snapshots = []
        if history_file.exists():
            try:
                with open(history_file) as f:
                    snapshots = json.load(f)
            except (json.JSONDecodeError, OSError):
                snapshots = []

        snapshot = {
            "timestamp": datetime.now(timezone.utc).timestamp(),
            "date": datetime.now(timezone.utc).isoformat(),
            "overall_score": report.overall_score,
            "level": report.level.value,
            "metrics": [
                {
                    "name": m.name,
                    "value": m.value,
                    "level": m.level.value,
                    "source": m.source,
                    "description": m.description,
                    "threshold_good": m.threshold_good,
                    "threshold_bad": m.threshold_bad,
                }
                for m in report.metrics
            ],
        }

        snapshots.append(snapshot)

        # Keep only last 365 snapshots (max ~1 year of daily runs)
        if len(snapshots) > 365:
            snapshots = snapshots[-365:]

        try:
            with open(history_file, "w") as f:
                json.dump(snapshots, f, indent=2)
            logger.info(f"[evidence] Snapshot saved ({len(report.metrics)} metrics)")
        except OSError as exc:
            logger.warning(f"[evidence] Failed to save snapshot: {exc}")

    def _history_path(self) -> Path:
        """Path to the evidence history JSON file."""
        return Path("data/evidence_history.json")

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
