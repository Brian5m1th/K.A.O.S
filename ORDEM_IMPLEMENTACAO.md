# Ordem de Implementação — K.A.O.S

> Consolidado em: 2026-07-12
> Baseado em: SDD-Roadmap-Expansion-v2, SDD_Roadmap, PLANO_IMPLEMENTACAO.md,
> auditoria estrutural, análise de código (backend + frontend), graphify report

---

## Legenda

| Símbolo | Significado |
|---------|-------------|
| 🟢 Fase 0 | Concluída |
| 🔵 Sprint N | Próximas execuções |
| 🔴 Prioridade | Bloqueante para outras entregas |
| 🟡 Prioridade | Importante mas não bloqueante |
| 🔵 Prioridade | Melhoria contínua |

---

## SPRINT 1 — Critical Path (Backend) 🔴

> **Foco**: Eliminar stubs que quebram o fluxo de orquestração.
> **Planos relacionados**: RF-A02, RF-A03 (SDD-Roadmap-Expansion-v2), Fase 8 SDD_Roadmap

| # | Tarefa | Arquivo | Esforço | Status |
|---|--------|---------|---------|--------|
| 1.1 | Corrigir `LangGraphAdapter.plan()` — `PlannerNode` é função, não classe | `providers/planner/langgraph_adapter.py` | 1h | ✅ |
| 1.2 | Implementar `LangGraphAdapter.execute()` real iterando steps | `providers/planner/langgraph_adapter.py` | 3h | ✅ |
| 1.3 | Implementar `LangGraphAdapter.status()` real | `providers/planner/langgraph_adapter.py` | 2h | ✅ |
| 1.4 | Implementar `EvidenceEngine.get_history()` com persistência JSON | `providers/evidence/engine.py` | 3h | ✅ |
| 1.5 | Implementar `QdrantAdapter.index()` real | `providers/retrieval/qdrant_adapter.py` | 3h | ✅ |
| 1.6 | Implementar `clear()` real no `PostgresMemoryProvider` | `providers/memory/postgres.py` | 1h | ✅ |
| 1.7 | Implementar `clear()` real no `ObsidianMemoryProvider` | `providers/memory/obsidian.py` | 1h | ✅ |
| 1.8 | Substituir `except Exception: pass` por logging | `api/integrations.py`, `api/architecture.py`, `qdrant_adapter.py` | 1h | ✅ |

---

## SPRINT 2 — Fortalecimento (Backend) 🔴

> **Foco**: Ativar fontes de evidência, completar providers, implementar APIs do roadmap.
> **Planos relacionados**: RF-B01 a RF-B05, RF-C01 a RF-C05, RF-D01 a RF-D07 (SDD-Roadmap-Expansion-v2)

| # | Tarefa | Arquivo | Esforço | Depende de |
|---|--------|---------|---------|------------|
| 2.1 | Ativar fontes tests/benchmarks/runtime no EvidenceEngine | `providers/evidence/engine.py` | 4h | 1.4 |
| 2.2 | Implementar WhatsApp receive/listen | `providers/whatsapp/` | 4h | — |
| 2.3 | Implementar `ObsidianMemoryProvider.load()` real (sem placeholders) | `providers/memory/obsidian.py` | 2h | — |
| 2.4 | Implementar `CredentialService` real (get/set/delete com criptografia) | `core/credential_service.py` | 2h | — |
| 2.5 | Expor `POST /api/vault/analyze` | `api/vault_analyzer.py` (criar) | 3h | — |
| 2.6 | Expor `GET /api/vault/analysis` + `GET /api/vault/suggestions` | `api/vault_analyzer.py` | 2h | 2.5 |
| 2.7 | Expor `GET /api/mcp/tools` + `POST /api/mcp/servers` | `api/mcp.py` | 3h | — |
| 2.8 | Bridge MCP → LangGraph Tool Registry | `tools/mcp_adapter.py` | 4h | 2.7 |
| 2.9 | Implementar Session History persistence + API | `api/conversations.py` + migration | 4h | — |
| 2.10 | Implementar `MCPServerBase` com ciclo de vida real | `core/mcp_server_base.py` | 4h | — |

---

## SPRINT 3 — Frontend Core 🟡

> **Foco**: Eliminar `alert()`, testes stub, tipagem `any`, diretórios vazios.
> **Planos relacionados**: Fases 3-6 desktop-roadmap-alignment.md

| # | Tarefa | Arquivo | Esforço | Depende de |
|---|--------|---------|---------|------------|
| 3.1 | Substituir `alert()` por Toast/Notificação | 6 páginas (login, welcome, setup, tools, costs, knowledge-graph) | 4h | — |
| 3.2 | Implementar testes reais (remover `expect(true).toBe(true)`) | 3 arquivos de teste | 3h | — |
| 3.3 | Tipar stores e páginas (reduzir 91 `any`) | Múltiplos arquivos | 6h | — |
| 3.4 | Implementar domain entities | `domain/entities/` (vazio) | 4h | — |
| 3.5 | Implementar application services | `application/services/` (vazio) | 4h | — |
| 3.6 | Implementar presentation layouts | `presentation/layouts/` (vazio) | 3h | — |

---

## SPRINT 4 — Documentação 🟡

> **Foco**: Executar o plano de auditoria documental, eliminar duplicação, sync wiki↔vault.
> **Planos relacionados**: PLANO_IMPLEMENTACAO.md, docs/audit-report-estrutural.md

| # | Tarefa | Esforço | Depende de |
|---|--------|---------|------------|
| 4.1 | Fase 1: Criar script `scripts/sync-vault.ps1` | 2h | — |
| 4.2 | Fase 1: Configurar pre-commit hook | 1h | 4.1 |
| 4.3 | Fase 2: Deduplicar SDDs (remover cópias do wiki+vault) | 3h | 4.1 |
| 4.4 | Fase 3: Organizar docs órfãos em diretórios | 1h | — |
| 4.5 | Fase 4: Criar mapa de correspondência arquitetural | 4h | 4.4 |
| 4.6 | Fase 5: Unificar governance/changelog | 30min | 4.1 |
| 4.7 | Fase 6: Scripts de automação + CI/CD | 2h | 4.1 |

---

## SPRINT 5 — N8N & Custos 🟡

> **Foco**: N8N container, webhooks, cost dashboard.
> **Planos relacionados**: RF-E01 a RF-E05, RF-F01 a RF-F04 (SDD-Roadmap-Expansion-v2)

| # | Tarefa | Arquivo | Esforço | Depende de |
|---|--------|---------|---------|------------|
| 5.1 | Adicionar N8N ao docker-compose | `infra/docker/docker-compose.yml` | 1h | — |
| 5.2 | Implementar WebhookTool no TOOL_REGISTRY | `tools/n8n_webhook_tool.py` | 2h | 5.1 |
| 5.3 | Expor `GET /api/n8n/flows` | `api/automation.py` | 2h | 5.1 |
| 5.4 | Expor `GET /api/observability/costs` | `api/observability.py` | 3h | — |
| 5.5 | Expor `GET /api/observability/costs/summary` | `api/observability.py` | 2h | 5.4 |
| 5.6 | Implementar widget de custos no desktop | `desktop/src/pages/costs/` | 3h | 5.4 |

---

## SPRINT 6 — Self-Reviewer & Evolution 🟢

> **Foco**: AI Self-Reviewer, workspace management, resolvers de dívida técnica.
> **Planos relacionados**: RF-G01 a RF-G05, RF-H01 a RF-H05 (SDD-Roadmap-Expansion-v2)

| # | Tarefa | Arquivo | Esforço | Depende de |
|---|--------|---------|---------|------------|
| 6.1 | Expor `POST /api/kirl/review` | `api/kirl.py` | 3h | 2.5 |
| 6.2 | Implementar AuditScheduler automático | `audit/drift_subscriber.py` | 2h | 6.1 |
| 6.3 | Implementar multi-workspace API | `api/workspace_intelligence.py` | 4h | — |
| 6.4 | Resolver 7 ciclos de importação (frontend) | Múltiplos | 4h | — |
| 6.5 | Integrar cobertura de testes no CI | `.github/workflows/` | 2h | — |
| 6.6 | Remover CodeScanner residual (1 import em test) | `assistant/tests/` | 1h | — |

---

## SPRINT 7 — Futuro (Roadmap Expansion v2) 🟢

> **Foco**: Adaptadores futuros, grafos de conhecimento, memória avançada.
> **Planos relacionados**: SDD-Roadmap-Expansion-v2 Fases 13-14, ADR-001/002/003

| # | Tarefa | Esforço | Depende de |
|---|--------|---------|------------|
| 7.1 | Implementar adaptador Mem0 para memória de longo prazo | 6h | 2.3 |
| 7.2 | Implementar adaptador Neo4j para graph port | 4h | — |
| 7.3 | Implementar adaptador FalkorDB para retrieval port | 4h | — |
| 7.4 | Implementar GraphRAG experiment (H3 2026) | 8h | — |
| 7.5 | Implementar auto-tagging de notas com ML | 4h | — |

---

## Mapa de Dependências entre Sprints

```
Sprint 1 (Critical Path)
    ├──► Sprint 2 (Fortalecimento) — depende de 1.4, 1.5
    │       ├──► Sprint 4 (Documentação) — paralelo
    │       └──► Sprint 5 (N8N & Custos) — paralelo
    ├──► Sprint 3 (Frontend) — independente
    └──► Sprint 6 (Self-Reviewer) — depende de 2.5
            └──► Sprint 7 (Futuro) — depende de 2.3
```

---

## Cronograma Recomendado

| Sprint | Horas | Prioridade | Início Recomendado |
|--------|-------|------------|-------------------|
| Sprint 1 — Critical Path | 15h | 🔴 Alta | **AGORA** |
| Sprint 2 — Fortalecimento | 32h | 🔴 Alta | Após Sprint 1 |
| Sprint 3 — Frontend Core | 24h | 🟡 Média | Paralelo ao Sprint 2 |
| Sprint 4 — Documentação | 13h30 | 🟡 Média | Paralelo ao Sprint 2 |
| Sprint 5 — N8N & Custos | 13h | 🟡 Média | Após Sprint 2 |
| Sprint 6 — Self-Reviewer | 16h | 🟢 Baixa | Após Sprint 2 |
| Sprint 7 — Futuro | 26h | 🟢 Baixa | Após Sprint 6 |
| **Total** | **~139h** | | |

---

## Status Atual do Projeto

| Métrica | Valor | Meta |
|---------|-------|------|
| Overall Score (PROJECT_HEALTH.md) | 72/100 | > 85 |
| Mock Elimination | 100% ✅ | 100% |
| Constitution Compliance | 100% ✅ | 100% |
| Architecture Fit | 85% ⚠️ | > 90% |
| Evidence Engine | 50% ⚠️ | > 80% |
| Test Coverage | Unknown ⚠️ | > 70% |
| Documentation Coverage | Unknown ⚠️ | > 90% |
| Import Cycles (Frontend) | 7 ⚠️ | 0 |
