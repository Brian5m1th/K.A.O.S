---
description: Skill para observabilidade no K.A.O.S
---
# Observability Engineer

## Descricao
Gerenciamento de observabilidade com Prometheus, Loki, Grafana e EventBus.

## Responsabilidades
- Configurar metricas Prometheus (custom + instrumentator)
- Manter dashboards Grafana
- Configurar Loki + Promtail para logs
- Implementar subscribers do EventBus (logger, metrics, tracing, cost, audit)
- Configurar tracing OpenTelemetry
- Manter alerts e health checks

## Criterios de Qualidade
- Metricas com labels semanticas
- Logs estruturados JSON em producao
- Spans OpenTelemetry para tracing
- Dashboards com visao por servico
- Alertas com thresholds definidos
