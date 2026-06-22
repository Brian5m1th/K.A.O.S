---
description: Ferramentas de observabilidade para o K.A.O.S
---
# Observability Tools

## query-metrics
Consulta metricas do Prometheus.
Parametros: query (PromQL), range (time range)

## query-logs
Consulta logs no Loki.
Parametros: query (LogQL), limit

## service-health
Verifica health de todos os servicos.
Parametros: (nenhum)
Retorna: status de cada servico (postgres, qdrant, ollama, kaos-api)

## dashboard-url
Retorna URL do Grafana.
Parametros: dashboard (nome do dashboard)
