import json
from pathlib import Path
from typing import Any
from app.audit.runtime_resolver import RuntimePathResolver


class ReportGenerator:
    @classmethod
    def get_generated_dir(cls) -> Path:
        target = RuntimePathResolver.docs_root() / "generated"
        target.mkdir(parents=True, exist_ok=True)
        return target

    @classmethod
    def write_dry_run_reports(cls, audit_data: dict[str, Any]) -> None:
        """Salva os 5 arquivos de relatório no formato dry-run."""
        gen_dir = cls.get_generated_dir()

        # 1. coverage.json
        with open(gen_dir / "coverage.json", "w", encoding="utf-8") as f:
            json.dump(
                {
                    "coverage": audit_data.get("coverage", 0.0),
                    "total_features": audit_data.get("total_features", 0),
                    "documented_features": audit_data.get("documented_features", 0),
                },
                f,
                indent=2,
                ensure_ascii=False,
            )

        # 2. documentation_health.json
        with open(gen_dir / "documentation_health.json", "w", encoding="utf-8") as f:
            json.dump(
                audit_data.get("health_metrics", {}), f, indent=2, ensure_ascii=False
            )

        # 3. missing_docs.json
        with open(gen_dir / "missing_docs.json", "w", encoding="utf-8") as f:
            json.dump(
                audit_data.get("missing_docs", []), f, indent=2, ensure_ascii=False
            )

        # 4. broken_links.json
        with open(gen_dir / "broken_links.json", "w", encoding="utf-8") as f:
            json.dump(
                audit_data.get("broken_links", []), f, indent=2, ensure_ascii=False
            )

        # 5. encoding_issues.json
        with open(gen_dir / "encoding_issues.json", "w", encoding="utf-8") as f:
            json.dump(
                audit_data.get("encoding_issues", []), f, indent=2, ensure_ascii=False
            )

        # 6. audit_context.json (preparação para Fase 2)
        cls.write_audit_context(audit_data)

    @classmethod
    def write_audit_context(cls, audit_data: dict[str, Any]) -> None:
        """Gera docs/generated/audit_context.json para consumo do AI Vault Analyzer."""
        gen_dir = cls.get_generated_dir()

        context_data = {
            "coverage": {
                "score": audit_data.get("coverage", 0.0),
                "total": audit_data.get("total_features", 0),
                "documented": audit_data.get("documented_features", 0),
            },
            "missing_docs": audit_data.get("missing_docs", []),
            "orphan_docs": audit_data.get("orphan_docs", []),
            "undocumented_code": audit_data.get("undocumented_code", []),
            "broken_links": audit_data.get("broken_links", []),
            "graph_metrics": {
                "connectivity": audit_data.get("graph_connectivity", 100.0),
                "orphan_notes": audit_data.get("orphan_notes", []),
            },
            "health_metrics": audit_data.get("health_metrics", {}),
        }

        with open(gen_dir / "audit_context.json", "w", encoding="utf-8") as f:
            json.dump(context_data, f, indent=2, ensure_ascii=False)

    @classmethod
    def generate_markdown_report(
        cls,
        before_metrics: dict[str, Any],
        after_metrics: dict[str, Any],
        fixed_files: list[dict],
        created_files: list[str],
        archived_files: list[dict],
        remaining_gaps: list[str],
    ) -> Path:
        """Gera o audit-report.md final com comparativo de métricas."""
        report_path = RuntimePathResolver.docs_root() / "audit-report.md"

        lines = [
            "# Relatório de Auditoria e Normalização de Documentação — K.A.O.S",
            "",
            f"**Data da Auditoria:** {datetime_now_str()}",
            "**Branch Executada:** `docs-recovery-20260623`",
            "",
            "## 1. Comparativo de Métricas (Antes vs Depois)",
            "",
            "| Métrica | Antes | Depois | Meta | Status |",
            "|---|---|---|---|---|",
            f"| **Coverage Score** | {before_metrics.get('coverage_score')}% | {after_metrics.get('coverage_score')}% | >= 90% | {'🟢 Ok' if after_metrics.get('coverage_score', 0) >= 90 else '🔴 Pendente'} |",
            f"| **Completeness Score** | {before_metrics.get('completeness_score')}% | {after_metrics.get('completeness_score')}% | >= 85% | {'🟢 Ok' if after_metrics.get('completeness_score', 0) >= 85 else '🔴 Pendente'} |",
            f"| **Consistency Score** | {before_metrics.get('consistency_score')}% | {after_metrics.get('consistency_score')}% | >= 90% | {'🟢 Ok' if after_metrics.get('consistency_score', 0) >= 90 else '🔴 Pendente'} |",
            f"| **Link Health Score** | {before_metrics.get('link_health_score')}% | {after_metrics.get('link_health_score')}% | >= 95% | {'🟢 Ok' if after_metrics.get('link_health_score', 0) >= 95 else '🔴 Pendente'} |",
            f"| **KIRL Integrity Score** | {before_metrics.get('kirl_integrity_score')}% | {after_metrics.get('kirl_integrity_score')}% | >= 95% | {'🟢 Ok' if after_metrics.get('kirl_integrity_score', 0) >= 95 else '🔴 Pendente'} |",
            f"| **Architecture Alignment** | {before_metrics.get('arch_alignment_score')}% | {after_metrics.get('arch_alignment_score')}% | >= 90% | {'🟢 Ok' if after_metrics.get('arch_alignment_score', 0) >= 90 else '🔴 Pendente'} |",
            f"| **Documentation Drift** | {before_metrics.get('drift_score')}% | {after_metrics.get('drift_score')}% | <= 10% | {'🟢 Ok' if after_metrics.get('drift_score', 100) <= 10 else '🔴 Drift Alto'} |",
            f"| **Documentation Health** | {before_metrics.get('documentation_health')}% | {after_metrics.get('documentation_health')}% | >= 90% | {'🟢 Ok' if after_metrics.get('documentation_health', 0) >= 90 else '🔴 Degrada'} |",
            "",
            "---",
            "",
            "## 2. Sumário Executivo de Ações",
            "",
            f"- **Arquivos Corrigidos (Encoding/Estrutura):** {len(fixed_files)}",
            f"- **Documentos Gerados/Recuperados:** {len(created_files)}",
            f"- **Arquivos Arquivados (docs/archive/):** {len(archived_files)}",
            "",
            "### Arquivos Corrigidos Detalhes:",
        ]

        for f in fixed_files:
            lines.append(
                f"  - `{f['path']}` (Encoding={f['encoding']}, Estrutura={f['structure']}, Protegido={f['protected']})"
            )

        if created_files:
            lines.append("\n### Documentos Gerados:")
            for cf in created_files:
                lines.append(f"  - `{cf}`")

        if archived_files:
            lines.append("\n### Arquivos Arquivados (docs/archive/):")
            for af in archived_files:
                lines.append(f"  - `{af['path']}` -> `{af['target']}`")

        lines.append("")
        lines.append("## 3. Lacunas Restantes (Gaps de Conhecimento)")
        if remaining_gaps:
            for gap in remaining_gaps:
                lines.append(f"- `{gap}`")
        else:
            lines.append(
                "- Nenhuma lacuna crítica pendente. Documentação 100% cobrindo o código atual."
            )

        lines.append("")
        lines.append("## 4. Recomendações Futuras")
        lines.append(
            "1. **Continuous Sync:** Executar sempre o `sync_github_registry.py` antes de novos builds para evitar drifts."
        )
        lines.append(
            "2. **Obsidian Hook:** Integrar o watch-service do Obsidian para disparar validação de wikilinks localmente."
        )
        lines.append(
            "3. **Fase 2 Readiness:** Iniciar o AI Vault Analyzer utilizando o `audit_context.json` gerado para detecção de conhecimento implícito no código."
        )

        with open(report_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        return report_path


def datetime_now_str() -> str:
    from datetime import datetime

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
