---
description: Ferramentas Docker para o K.A.O.S
---
# Docker Tools

## docker-build
Build da imagem Docker do backend.
Parametros: tag

## docker-compose-up
Sobe todos os servicos do docker-compose.
Parametros: services (opcional, lista de servicos)

## docker-compose-down
Para todos os servicos.
Parametros: volumes (remover volumes? true/false)

## docker-logs
Logs de um servico especifico.
Parametros: service, lines (numero de linhas)

## docker-healthcheck
Verifica saude de todos os servicos.
Parametros: (nenhum)
