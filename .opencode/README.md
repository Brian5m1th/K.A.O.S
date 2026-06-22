# OpenCode Configuration — K.A.O.S

Esta pasta contem a configuracao OpenCode para o projeto K.A.O.S, permitindo que o agente de codigo entenda a arquitetura, convencoes e ferramentas do projeto.

## Estrutura

```
.opencode/
├── references/   (6)  - Documentos de referencia (arquitetura, convencoes, APIs, testes, diretorios, MCP)
├── rules/        (10) - Regras de codigo por tecnologia (python, typescript, react, docker, GA, n8n, mcp, testing, security, documentation)
├── skills/       (10) - Habilidades especializadas (python, react, docker, n8n, mcp, observability, rag, agent, code-review, docs)
├── tools/        (4)  - Ferramentas (github, docker, kaos, observability)
├── agents/       (8)  - Agentes especializados (architect, backend, frontend, devops, security, docs, mcp, auditor)
└── README.md           - Este arquivo
```

## Uso

O OpenCode carrega automaticamente os arquivos desta pasta quando executado na raiz do projeto.

### Referencias
Contem conhecimento arquitetural e convencoes do K.A.O.S. Use como fonte de verdade para decisoes de design.

### Regras
Regras de qualidade que o OpenCode deve seguir ao gerar ou modificar codigo. Cada regra se aplica a tipos de arquivo especificos.

### Skills
Habilidades especializadas que o OpenCode pode usar para tarefas especificas (desenvolvimento Python, React, Docker, etc.).

### Tools
Ferramentas customizadas que expoem comandos do ecossistema K.A.O.S:
- **kaos-tools**: auditoria, features, scan, architecture analyze, knowledge graph
- **docker-tools**: build, compose, logs, healthcheck
- **github-tools**: PR, workflow, issues
- **observability-tools**: metrics, logs, health

### Agents
Agentes especializados para tarefas especificas, cada um com tools, skills e rules vinculadas.

## Manutencao

Ao adicionar novos modulos ao K.A.O.S:
1. Atualize `references/architecture.md` e `references/directory-structure.md`
2. Adicione rules se houver novas tecnologias
3. Adicione skills se houver novas capacidades
4. Adicione tools se houver novos comandos uteis
5. Crie agents se houver novos papeis de automacao

## Total

| Categoria | Quantidade |
|-----------|:--------:|
| References | 6 |
| Rules | 10 |
| Skills | 10 |
| Tools | 4 |
| Agents | 8 |
| **Total** | **39** |
