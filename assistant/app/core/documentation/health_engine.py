from typing import Any

class HealthEngine:
    @classmethod
    def calculate_health(cls, audit_data: dict[str, Any]) -> dict[str, Any]:
        """
        Calcula as métricas de saúde com base no resultado da auditoria.
        Fórmula:
        Health = (Coverage + Completeness + Consistency + LinkHealth + KIRLIntegrity + ArchitectureAlignment - DriftPenalty) / 6
        """
        # 1. Coverage Score
        coverage = audit_data.get("coverage", 0.0)

        # 2. Completeness Score (presença das seções obrigatórias)
        completeness = audit_data.get("completeness", 0.0)

        # 3. Consistency Score (alinhamento de status código/docs)
        consistency = audit_data.get("consistency", 0.0)

        # 4. Link Health Score (% de links internos válidos)
        link_health = audit_data.get("link_health", 100.0)

        # 5. KIRL Integrity Score (integridade do grafo e conexões)
        kirl_integrity = audit_data.get("kirl_integrity", 100.0)

        # 6. Architecture Alignment Score (alinhamento com as regras de arquitetura)
        arch_alignment = audit_data.get("arch_alignment", 100.0)

        # 7. Drift Penalty (Penalidade baseada em código sem doc, doc sem código, etc.)
        # Limite: Drift Score <= 10%
        drift_score = audit_data.get("drift_score", 0.0)
        
        # O DriftPenalty deduz do score total se exceder a meta tolerada (ou pode ser o próprio drift_score)
        # Vamos definir Drift Penalty como o próprio drift_score. Se drift for alto, ele diminui a nota de saúde.
        drift_penalty = drift_score

        # Fórmula final
        raw_health = (
            coverage +
            completeness +
            consistency +
            link_health +
            kirl_integrity +
            arch_alignment -
            drift_penalty
        ) / 6.0
        
        doc_health = max(0.0, min(100.0, raw_health))

        return {
            "coverage_score": round(coverage, 1),
            "completeness_score": round(completeness, 1),
            "consistency_score": round(consistency, 1),
            "link_health_score": round(link_health, 1),
            "kirl_integrity_score": round(kirl_integrity, 1),
            "arch_alignment_score": round(arch_alignment, 1),
            "drift_score": round(drift_score, 1),
            "drift_penalty": round(drift_penalty, 1),
            "documentation_health": round(doc_health, 1),
            "passed": doc_health >= 90.0
        }
