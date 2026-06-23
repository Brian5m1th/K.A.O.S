#!/usr/bin/env python3
"""
Wrapper para o DocumentationAuditEngine.

Uso:
    python assistant/scripts/audit_docs.py --mode audit
    python assistant/scripts/audit_docs.py --mode fix
"""

import argparse
import sys
from pathlib import Path

# Add app to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.core.documentation.audit_engine import DocumentationAuditEngine
from app.core.documentation.report_generator import ReportGenerator

def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
        
    parser = argparse.ArgumentParser(description="Audita e normaliza documentação do K.A.O.S")
    parser.add_argument(
        "--mode",
        choices=["audit", "fix"],
        required=True,
        help="audit (dry-run) ou fix (recovery completo)"
    )
    args = parser.parse_args()

    if args.mode == "audit":
        print("[audit_docs] Executando no modo Dry-Run (Somente Auditoria)...")
        results = DocumentationAuditEngine.run_audit(dry_run=True)
        # Salvar os 5 relatórios JSON
        ReportGenerator.write_dry_run_reports(results)
        
        print("\n=================== RESULTADOS ANTE-RECUPERAÇÃO ===================")
        print(f"Cobertura Documental:   {results['coverage']:.1f}%")
        print(f"Total de Features:      {results['total_features']}")
        print(f"Documentadas:           {results['documented_features']}")
        print(f"Sem documentação:       {len(results['missing_docs'])}")
        print(f"Problemas de Encoding:  {len(results['encoding_issues'])}")
        print(f"Links Quebrados:        {len(results['broken_links'])}")
        print(f"Conectividade do Grafo: {results['graph_connectivity']:.1f}%")
        print(f"Drift Score:            {results['drift_score']:.1f}%")
        print(f"Nota de Saúde Geral:    {results['health_metrics']['documentation_health']:.1f}%")
        print("===================================================================\n")
        print("[audit_docs] Arquivos JSON de métricas gerados em docs/generated/")
    
    elif args.mode == "fix":
        print("[audit_docs] Executando no modo Recovery (Correção e Normalização)...")
        results = DocumentationAuditEngine.execute_recovery_flow()
        
        print("\n==================== COMPARATIVO DE RECUPERAÇÃO ====================")
        print("Métrica                 | Antes    | Depois   | Status")
        print("------------------------|----------|----------|-------")
        print(f"Coverage Score          | {results['before']['coverage_score']}%     | {results['after']['coverage_score']}%     | {'[OK]' if results['after']['coverage_score'] >= 90 else '[ERRO]'}")
        print(f"Completeness Score      | {results['before']['completeness_score']}%     | {results['after']['completeness_score']}%     | {'[OK]' if results['after']['completeness_score'] >= 85 else '[ERRO]'}")
        print(f"Consistency Score       | {results['before']['consistency_score']}%     | {results['after']['consistency_score']}%     | {'[OK]' if results['after']['consistency_score'] >= 90 else '[ERRO]'}")
        print(f"Link Health Score       | {results['before']['link_health_score']}%     | {results['after']['link_health_score']}%     | {'[OK]' if results['after']['link_health_score'] >= 95 else '[ERRO]'}")
        print(f"KIRL Integrity Score    | {results['before']['kirl_integrity_score']}%     | {results['after']['kirl_integrity_score']}%     | {'[OK]' if results['after']['kirl_integrity_score'] >= 95 else '[ERRO]'}")
        print(f"Architecture Alignment  | {results['before']['arch_alignment_score']}%     | {results['after']['arch_alignment_score']}%     | {'[OK]' if results['after']['arch_alignment_score'] >= 90 else '[ERRO]'}")
        print(f"Drift Score             | {results['before']['drift_score']}%     | {results['after']['drift_score']}%     | {'[OK]' if results['after']['drift_score'] <= 10 else '[ERRO]'}")
        print(f"Documentation Health    | {results['before']['documentation_health']}%     | {results['after']['documentation_health']}%     | {'[OK]' if results['after']['documentation_health'] >= 90 else '[ERRO]'}")
        print("--------------------------------------------------------------------")
        print(f"Arquivos Corrigidos:    {results['fixed_count']}")
        print(f"Arquivos Gerados:       {results['created_count']}")
        print(f"Arquivos Arquivados:    {results['archived_count']}")
        print("====================================================================\n")
        print("[audit_docs] Relatórios finais md e JSON atualizados.")


if __name__ == "__main__":
    main()
