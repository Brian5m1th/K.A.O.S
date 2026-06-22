---
description: Ferramentas K.A.O.S para auditoria e documentacao
---
# KAOS Tools

## audit-run
Executa auditoria documental completa (KIRL).
Parametros: (nenhum)
Retorna: DriftReport (coverage, missing, outdated, driftLevel)

## audit-status
Obtem status da auditoria.
Parametros: (nenhum)
Retorna: DRLSnapshot (features, coverage, driftLevel)

## feature-list
Lista features registradas.
Parametros: phase, status (filtros opcionais)
Retorna: FeatureEntry[]

## feature-register
Registra nova feature.
Parametros: id, name, phase, status, docs, codeRefs

## scan-commits
Escaneia commits e mapeia para features.
Parametros: limit (numero de commits, padrao: 200)

## architecture-analyze
Executa analise arquitetural (AI Vault Analyzer).
Parametros: (nenhum)
Retorna: ArchitectureAnalysis (coverage, drift, issues, suggestions)

## knowledge-graph
Constroi grafo de conhecimento consolidado.
Parametros: (nenhum)
Retorna: KnowledgeGraph (nodes, edges, features, sdds, workflows, agents)
