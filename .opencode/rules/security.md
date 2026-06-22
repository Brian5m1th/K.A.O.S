---
description: Regras de seguranca para o K.A.O.S
globs: []
---
# Security Rules

- API Key nunca hardcoded — sempre via `data/api_key.txt` ou env var
- CORS restrito em producao (`allow_origins` especifico)
- Senhas Postgres via `.env`, nunca no docker-compose.yml
- Nao commitar `.env` ou `data/api_key.txt` no repositorio
- Validacao de input em todos os endpoints (Pydantic)
- Headers de autenticacao verificados em middleware
- Path traversal: validar caminhos antes de ler arquivos
- SQL Injection: usar SQLAlchemy parametrizado
- Nao expor informacoes internas em mensagens de erro
