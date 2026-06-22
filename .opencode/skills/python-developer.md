---
description: Skill para desenvolvimento Python no K.A.O.S
---
# Python Developer

## Descricao
Desenvolvimento backend com Python 3.13, FastAPI, LangGraph, SQLAlchemy e KIRL.

## Responsabilidades
- Criar e manter rotas FastAPI com padrao APIRouter
- Implementar providers (Chat, Embedding, Vector, Memory)
- Criar workflows LangGraph
- Manter KIRL (FeatureRegistry, AuditEngine, DRLSnapshot)
- Escrever testes com pytest-asyncio
- Seguir typing hints estritos (PEP 585, `| None`)

## Criterios de Qualidade
- Type hints em todas as funcoes
- Logging com loguru (tags `[info]`, `[error]`)
- Testes com cobertura > 80%
- Async em todas as rotas
- Pydantic v2 para validacao
