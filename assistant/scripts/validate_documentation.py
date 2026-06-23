#!/usr/bin/env python3
"""
Valida documentação do K.A.O.S.

Lê o coverage-report.json gerado pelo AuditEngine e falha se
a cobertura for menor que o threshold definido.

Uso:
    python assistant/scripts/validate_documentation.py [--min-coverage 90]
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "app"))
from app.audit.runtime_resolver import RuntimePathResolver


REPORT_PATH = RuntimePathResolver.audit_dir() / "coverage-report.json"
DEFAULT_MIN_COVERAGE = 90.0


def load_report(path: Path) -> dict | None:
    if not path.exists():
        print(f"[validate_docs] ERRO: relatorio nao encontrado em {path}")
        print("[validate_docs] Execute uma auditoria primeiro: POST /api/audit/run")
        return None

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate(report: dict, min_coverage: float) -> bool:
    coverage = report.get("coverage", 0)
    total = report.get("totalFeatures", 0)
    documented = report.get("documented", 0)
    missing = report.get("missingDocs", 0)
    stale = report.get("staleDocs", 0)
    orphaned = report.get("orphanedSDDs", 0)
    inconsistent = report.get("inconsistentPhases", 0)
    undocumented_code = report.get("undocumentedCode", 0)

    print("[validate_docs] ==============================")
    print(f"[validate_docs] Cobertura documental: {coverage:.1f}%")
    print(f"[validate_docs] Total de features:   {total}")
    print(f"[validate_docs] Documentadas:        {documented}")
    print(f"[validate_docs] SEM documentacao:    {missing}")
    print(f"[validate_docs] SDDs desatualizados: {stale}")
    print(f"[validate_docs] SDDs orfaos:         {orphaned}")
    print(f"[validate_docs] Fases inconsistentes: {inconsistent}")
    print(f"[validate_docs] Codigo sem doc:      {undocumented_code}")
    print(f"[validate_docs] Threshold minimo:    {min_coverage:.1f}%")
    print("[validate_docs] ==============================")

    if coverage < min_coverage:
        print(
            f"[validate_docs] FALHA: cobertura {coverage:.1f}% abaixo do minimo {min_coverage:.1f}%"
        )
        return False

    if missing > 0:
        print(f"[validate_docs] AVISO: {missing} features sem documentacao")

    if stale > 0:
        print(f"[validate_docs] AVISO: {stale} SDDs desatualizados")

    print(f"[validate_docs] OK: cobertura {coverage:.1f}% atende o threshold")
    return True


def main():
    parser = argparse.ArgumentParser(description="Valida documentacao do K.A.O.S")
    parser.add_argument(
        "--min-coverage",
        type=float,
        default=DEFAULT_MIN_COVERAGE,
        help=f"Cobertura minima (padrao: {DEFAULT_MIN_COVERAGE}%)",
    )
    parser.add_argument(
        "--report-path",
        type=str,
        default=str(REPORT_PATH),
        help=f"Caminho do relatorio (padrao: {REPORT_PATH})",
    )
    args = parser.parse_args()

    report = load_report(Path(args.report_path))
    if report is None:
        sys.exit(1)

    success = validate(report, args.min_coverage)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
