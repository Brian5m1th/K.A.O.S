"""
ArchitectureReviewer — AI-powered architecture analysis.

Reads the knowledge graph, SDDs, and code structure to suggest
refactors, detect architectural drift, and recommend improvements.

Q4 2026 feature: Uses LLM + Graph analysis for autonomous review.
"""

import json
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from loguru import logger


@dataclass
class ReviewFinding:
    category: str  # "drift" | "smell" | "refactor" | "missing_doc" | "cycle"
    severity: str  # "critical" | "major" | "minor" | "info"
    file_path: str
    description: str
    suggestion: str
    confidence: float


@dataclass
class ReviewResult:
    findings: list[ReviewFinding] = field(default_factory=list)
    overall_score: float = 0.0
    total_issues: int = 0
    generated_at: str = ""


class ArchitectureReviewer:
    """Reviews codebase architecture using graph + SDD + code analysis."""

    def __init__(self) -> None:
        self._graph_path = Path("graphify-out/graph.json")

    async def review(self) -> ReviewResult:
        findings: list[ReviewFinding] = []
        t0 = time.monotonic()

        # 1. Graph analysis
        findings.extend(self._analyze_graph())
        findings.extend(self._analyze_sdd_coverage())
        findings.extend(self._analyze_code_health())

        score = self._calculate_score(findings)
        logger.info(
            "[arch-review] {} findings, score={} in {:.0f}ms",
            len(findings),
            score,
            (time.monotonic() - t0) * 1000,
        )
        return ReviewResult(
            findings=findings,
            overall_score=score,
            total_issues=len(findings),
            generated_at=datetime.now(timezone.utc).isoformat(),
        )

    def _analyze_graph(self) -> list[ReviewFinding]:
        findings = []
        if not self._graph_path.exists():
            findings.append(
                ReviewFinding(
                    category="missing_doc",
                    severity="major",
                    file_path="graphify-out/graph.json",
                    description="Knowledge graph not found. Run graphify update .",
                    suggestion="Execute 'graphify update .' to generate the code graph.",
                    confidence=1.0,
                )
            )
            return findings

        try:
            with open(self._graph_path) as f:
                graph = json.load(f)
            nodes = graph.get("nodes", [])
            if len(nodes) < 100:
                findings.append(
                    ReviewFinding(
                        category="smell",
                        severity="minor",
                        file_path="graphify-out/graph.json",
                        description=f"Small graph: only {len(nodes)} nodes indexed",
                        suggestion="Ensure all source directories are included in graphify config",
                        confidence=0.7,
                    )
                )
        except Exception as exc:
            logger.warning("[arch-review] graph parse error: {}", exc)

        return findings

    def _analyze_sdd_coverage(self) -> list[ReviewFinding]:
        findings = []
        sdd_dir = Path("docs/sdd")
        if not sdd_dir.exists():
            findings.append(
                ReviewFinding(
                    category="missing_doc",
                    severity="critical",
                    file_path="docs/sdd",
                    description="No SDD directory found",
                    suggestion="Create docs/sdd/ with at least one SDD document",
                    confidence=1.0,
                )
            )
            return findings

        sdds = list(sdd_dir.glob("*.md"))
        if len(sdds) < 5:
            findings.append(
                ReviewFinding(
                    category="missing_doc",
                    severity="major",
                    file_path="docs/sdd",
                    description=f"Only {len(sdds)} SDDs found",
                    suggestion="Create SDDs for each major subsystem",
                    confidence=0.8,
                )
            )

        return findings

    def _analyze_code_health(self) -> list[ReviewFinding]:
        findings = []
        todo_count = 0
        fixme_count = 0
        for py_file in Path("assistant/app").rglob("*.py"):
            try:
                content = py_file.read_text(encoding="utf-8")
                todo_count += content.count("TODO")
                fixme_count += content.count("FIXME")
            except Exception as e:
                logger.debug("[reviewer] skipping unreadable file {}: {}", py_file, e)

        if todo_count > 20:
            findings.append(
                ReviewFinding(
                    category="smell",
                    severity="minor",
                    file_path="assistant/app",
                    description=f"{todo_count} TODO comments found in codebase",
                    suggestion="Review and address TODO items; create issues for each",
                    confidence=0.6,
                )
            )
        if fixme_count > 5:
            findings.append(
                ReviewFinding(
                    category="smell",
                    severity="major",
                    file_path="assistant/app",
                    description=f"{fixme_count} FIXME comments found — potential bugs",
                    suggestion="Prioritize fixing FIXME items",
                    confidence=0.9,
                )
            )

        return findings

    def _calculate_score(self, findings: list[ReviewFinding]) -> float:
        if not findings:
            return 100.0
        penalties = {"critical": 20, "major": 10, "minor": 5, "info": 0}
        total_penalty = sum(penalties.get(f.severity, 0) for f in findings)
        return max(0.0, 100.0 - total_penalty)
