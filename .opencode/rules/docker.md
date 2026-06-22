---
description: Regras Docker para o K.A.O.S
globs: ["**/Dockerfile*", "**/docker-compose*", "**/Dockerfile.*"]
---
# Docker Rules

- Multi-stage builds: `builder` + `runtime` stages
- Nao use `root` como usuario — crie usuario nao-root
- `HEALTHCHECK` obrigatorio em servicos de producao
- Use `--no-cache` ou `--frozen` para reproducibilidade
- Variaveis sensiveis via arquivo `.env`, nunca hardcoded
- Named volumes para dados persistentes
- Servicos no docker-compose com `depends_on` e `healthcheck`
- Portas mapeadas explicitamente (sem `ports: "8000"`)
- Redes separadas para backend e frontend quando aplicavel
