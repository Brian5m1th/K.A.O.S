---
id: SDD-TEST-STRATEGY-F6
title: "Estratégia Completa de Testes e Garantia de Qualidade (Fase 6) + Refatoração Arquitetural (Fase 5)"
status: "approved"
version: "1.0"
created_at: "2026-07-08"
updated_at: "2026-07-08"
author: "KAOS Architect"
phase: "Fase 6"
status_emoji: "✅"
---

# SDD: Estratégia de Testes (Fase 6) + Refatoração Arquitetural (Fase 5)

## 1. Objetivo

Garantir que nenhuma funcionalidade do Desktop seja entregue sem validação automatizada e que a arquitetura seja refatorada seguindo Clean Architecture com módulos independentes.

## 2. Pirâmide de Testes

```
                E2E
          (Playwright/Tauri)
        Fluxos completos do usuário
────────────────────────────────────
        Testes de Integração
     APIs • Stores • Hooks • IPC
────────────────────────────────────
        Testes Unitários
 Helpers • Utils • Services • Models
────────────────────────────────────
```

## 3. Estrutura de Testes Implementada

```
desktop/src/__tests__/
├── setup.ts                          # Mocks globais (localStorage, fetch, AbortController)
├── shared/
│   ├── api/
│   │   ├── kaos-client.test.ts       # HTTP wrapper (9 cenários)
│   │   ├── ipc-bridge.test.ts        # IPC bridge (13 cenários)
│   │   └── tauri-store-service.test.ts # Store service (12 cenários)
│   ├── lib/
│   │   ├── event-bus.test.ts         # EventBus (10 cenários)
│   │   ├── command-registry.test.ts  # CommandRegistry (8 cenários)
│   │   └── stores/
│   │       ├── auth-store.test.ts    # Auth store (12 cenários)
│   │       ├── chat-store.test.ts    # Chat store (8 cenários)
│   │       ├── conversation-store.test.ts
│   │       ├── agent-store.test.ts   # Agent store (10 cenários)
│   │       ├── system-store.test.ts  # System store (10 cenários)
│   │       ├── theme-store.test.ts   # Theme store (6 cenários)
│   │       ├── update-store.test.ts  # Update store (10 cenários)
│   │       └── ui-store.test.ts      # UI store (3 cenários)
│   └── ui/
│       ├── button.test.tsx           # Button (4 cenários)
│       ├── card.test.tsx             # Card (4 cenários)
│       ├── badge.test.tsx            # Badge (2 cenários)
│       ├── dropdown.test.tsx         # Dropdown (1 cenário)
│       ├── input.test.tsx            # Input (3 cenários)
│       └── tabs.test.tsx             # Tabs (2 cenários)
├── features/
│   ├── drift-store.test.ts           # DriftStore (3 cenários)
│   ├── heatmap-store.test.ts         # HeatmapStore (4 cenários)
│   ├── graph-builder.test.ts         # GraphBuilder (3 cenários)
│   ├── layout-engine.test.ts         # LayoutEngine (3 cenários)
│   ├── graph-export.test.ts          # GraphExport (3 cenários)
│   ├── drift-engine.test.ts          # DriftEngine (1 cenário)
│   ├── feature-scanner.test.ts       # FeatureScanner (1 cenário)
│   ├── feature-extractor.test.ts     # FeatureExtractor (2 cenários)
│   ├── code-introspector.test.ts     # CodeIntrospector (1 cenário)
│   ├── ask-ai.test.ts                # Smoke test
│   ├── useSettings.test.ts           # Smoke test
│   └── doc-generator.test.ts         # Smoke test
├── integration/
│   ├── auth-chat-flow.test.ts        # Login -> Chat -> Logout
│   └── audit-graph-flow.test.ts      # Audit -> Graph -> Store
└── e2e/
    └── navigation.spec.ts            # Playwright E2E (4 páginas)
```

**Total: 34 arquivos de teste, ~130 cenários**

## 4. Fluxos Críticos Cobertos

| Fluxo | Cobertura | Tipo |
|-------|-----------|------|
| Login → Chat → Logout | ✅ | Integração |
| Audit → Graph Builder → Graph Store → Render | ✅ | Integração |
| Chat streaming com SSE parse | ✅ | Unitário |
| IPC bridge com fallback web | ✅ | Unitário |
| Stores Zustand com chamadas REST | ✅ | Unitário |
| EventBus com eventos de stream | ✅ | Unitário |
| GraphBuilder com force-directed layout | ✅ | Unitário |
| TauriStoreService com localStorage fallback | ✅ | Unitário |
| Autenticação com refresh token | ✅ | Unitário |

## 5. Configurações

### Vitest (desktop/vitest.config.ts)
- **Environment:** jsdom
- **Globals:** true
- **Coverage:** v8 provider, thresholds 90% lines / 85% functions / 80% branches
- **Alias:** `@/` → `src/`

### Playwright (desktop/playwright.config.ts)
- **Browsers:** Chromium, Firefox, WebKit
- **Base URL:** http://localhost:1420
- **WebServer:** `pnpm dev` (auto-start)

### CI/CD (desktop-ci.yml)
- TypeScript type check (`tsc --noEmit`)
- Vitest run with coverage
- Upload coverage artifact
- Coverage gate: 90% minimum

### pytest (assistant/pyproject.toml)
- `[tool.pytest.ini_options]`: testpaths=tests, asyncio_mode=auto
- `[tool.coverage.report]`: fail_under=80

## 6. Cobertura Obrigatória (Regra)

> Todo módulo novo deverá possuir testes unitários, testes de integração, testes E2E (quando possuir interface), cobertura mínima de código, cobertura de fluxos críticos.
>
> **Nenhuma funcionalidade poderá ser considerada concluída sem atender aos critérios acima.**

## 7. Pipeline CI - Bloqueios

O pipeline impede merge quando:
- ❌ Cobertura inferior a 90%
- ❌ Testes falhando
- ❌ TypeScript type check falha
- ❌ Lint falha
- ❌ Build falha
- ❌ Vulnerabilidades críticas

## 8. Métricas Monitoradas

- Cobertura geral
- Cobertura por módulo
- Tempo médio dos testes
- Regressões
- Flaky tests
- Taxa de sucesso do pipeline

---

# Fase 5 — Refatoração Arquitetural

## Estrutura Alvo

```
src/
├── app/          (config, providers, routes)
├── presentation/ (UI, componentes puros)
├── application/  (stores, hooks, casos de uso)
├── domain/       (entidades, regras, modelos)
├── infrastructure/ (HTTP, IPC, Storage, API)
├── platform/     (Tauri, Browser)
├── shared/       (design system, utils)
├── features/     (módulos independentes)
│   ├── chat/
│   ├── dashboard/
│   ├── settings/
│   ├── vault/
│   ├── agents/
│   ├── pipelines/
│   ├── architecture/
│   ├── knowledge-graph/
│   └── observability/
├── entities/
├── widgets/
└── pages/
```

## Roadmap de Migração

| Fase | Descrição | Status |
|------|-----------|--------|
| Fase 0 | Correção de bugs críticos | Pendente |
| **Fase 1** | **Cobertura completa de testes (34 arquivos criados)** | **✅ 85%** |
| Fase 2 | Refatoração dos serviços (infrastructure/) | Pendente |
| Fase 3 | Refatoração das stores (application/stores/) | Pendente |
| Fase 4 | Refatoração dos hooks (application/hooks/) | Pendente |
| Fase 5 | Refatoração dos componentes (presentation/) | Pendente |
| Fase 6 | Refatoração das páginas | Pendente |
| Fase 7 | Modularização completa das features | Pendente |
| Fase 8 | Hardening (segurança, erros) | Pendente |
| Fase 9 | Performance (lazy, code splitting) | Pendente |
| Fase 10 | Documentação definitiva (SDDs, wiki) | Pendente |

## Critérios de Conclusão da Refatoração

1. ✅ 100% das funcionalidades existentes operacionais (sem regressão)
2. 🔄 Cobertura de testes >90% (atual: 85%, ~34 arquivos)
3. ⬜ Todas as páginas com E2E
4. ⬜ Nenhuma store chama API diretamente (via infrastructure/)
5. ⬜ Nenhum hook contém lógica de negócio reutilizável
6. ⬜ Componentes com responsabilidade única, <250 linhas
7. ⬜ Documentação arquitetural sincronizada com implementação