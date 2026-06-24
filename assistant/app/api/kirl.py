"""
KIRL API — Self-Review pipeline.

RF-H01: POST /api/kirl/review — complete Audit → Analyze → Suggest pipeline
"""

from datetime import datetime
from pathlib import Path

from fastapi import APIRouter, HTTPException
from loguru import logger
from pydantic import BaseModel

from app.audit.audit_engine import AuditEngine, DriftReport
from app.audit.runtime_resolver import RuntimePathResolver
from app.ai.vault_analyzer.analyzer_engine import AnalyzerEngine
from app.ai.vault_analyzer.suggestion_engine import SuggestionEngine, Suggestion

router = APIRouter(prefix="/api/kirl", tags=["KIRL"])


class KIRLIssueResponse(BaseModel):
    type: str
    path: str
    severity: str


class KIRLReviewResponse(BaseModel):
    coverage_score: float
    drift_level: str
    total_issues: int
    suggestions: list[str]
    report_path: str
    generated_at: str


def _generate_report_markdown(
    audit: DriftReport,
    analysis_suggestions: list[str],
    suggestions: list[Suggestion],
) -> str:
    """Generate a self-review report in markdown format."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "---",
        "type: self-review",
        f"generated_at: {now}",
        "---",
        "",
        f"# KIRL Self-Review Report — {now}",
        "",
        "## Summary",
        "",
        f"- **Coverage Score:** {audit.coverage:.1f}%",
        f"- **Drift Level:** {audit.drift_level}",
        f"- **Missing Features:** {len(audit.missing_features)}",
        f"- **Outdated Docs:** {len(audit.outdated_docs)}",
        f"- **Orphaned SDDs:** {len(audit.orphaned_sdds)}",
        f"- **Undocumented Code:** {len(audit.undocumented_code)}",
        "",
        "## Missing Features",
    ]
    for f in audit.missing_features:
        lines.append(f"- {f}")
    lines.extend(["", "## Outdated Docs"])
    for d in audit.outdated_docs:
        lines.append(f"- {d}")
    lines.extend(["", "## Suggestions"])
    for s in analysis_suggestions:
        lines.append(f"- {s}")
    for s in suggestions:
        lines.append(f"- [{s.priority}] {s.title}: {s.description[:120]}")
    lines.append("")
    return "\n".join(lines)


@router.post("/review", response_model=KIRLReviewResponse)
async def run_kirl_review():
    """RF-H01: Pipeline completo DocumentationAudit → VaultAnalyzer → Suggestions.

    Executa a auditoria completa do KIRL e gera relatório Markdown.
    Se drift_score > 15%, notificação é enviada aos admins.
    """
    logger.info("[kirl/review] starting full review pipeline")

    # 1. DocumentationAudit
    try:
        audit = AuditEngine.run_audit()
        logger.info("[kirl/review] audit complete: coverage={:.1f}%", audit.coverage)
    except Exception as exc:
        logger.error("[kirl/review] audit failed: {}", exc)
        raise HTTPException(status_code=500, detail=f"AuditEngine failed: {exc}")

    # 2. VaultAnalyzer
    try:
        analysis = await AnalyzerEngine.analyze_async()
        logger.info("[kirl/review] analysis complete: drift={}", analysis.drift_level)
    except Exception as exc:
        logger.error("[kirl/review] analyzer failed: {}", exc)
        analysis = None

    # 3. Suggestions
    suggestions: list[Suggestion] = []
    analysis_suggestions: list[str] = []
    if analysis:
        analysis_suggestions = analysis.suggestions
        # Get detailed suggestions from evidence
        try:
            from app.ai.vault_analyzer.evidence_engine import EvidenceEngine

            evidences = EvidenceEngine.collect()
            suggestions = SuggestionEngine.generate_from_evidences(evidences)
        except Exception as exc:
            logger.warning("[kirl/review] suggestion engine failed: {}", exc)

    # 4. Generate report markdown
    report = _generate_report_markdown(audit, analysis_suggestions, suggestions)
    report_dir = Path(RuntimePathResolver.analysis_path()).parent
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / f"self-review-{datetime.now().strftime('%Y-%m-%d')}.md"
    report_path.write_text(report, encoding="utf-8")
    logger.info("[kirl/review] report saved to {}", report_path)

    # 5. Notify if drift > 15%
    if audit.coverage < 85:
        try:
            from app.notifications.service import NotificationService

            await NotificationService.notify_admins(
                title="KIRL Self-Review: Drift above threshold",
                message=(
                    f"Drift score is {100 - audit.coverage:.1f}% "
                    f"(coverage: {audit.coverage:.1f}%). "
                    f"Review the report at {report_path}"
                ),
            )
            logger.info("[kirl/review] admin notification sent")
        except Exception as exc:
            logger.warning("[kirl/review] notification failed: {}", exc)

    return KIRLReviewResponse(
        coverage_score=round(audit.coverage, 1),
        drift_level=audit.drift_level,
        total_issues=len(audit.missing_features) + len(audit.outdated_docs),
        suggestions=analysis_suggestions,
        report_path=str(report_path),
        generated_at=datetime.now().isoformat(),
    )
