---
description: Regras de teste para o K.A.O.S
globs: ["assistant/tests/**/*.py"]
---
# Testing Rules

- Testes com pytest + pytest-asyncio
- Nomes: `test_<funcionalidade>` ou `Test<Modulo>::test_<funcionalidade>`
- Fixtures em `tests/fixtures/` ou no proprio arquivo de teste
- Async tests com `@pytest.mark.asyncio`
- Client de teste com `httpx.AsyncClient` + `ASGITransport`
- Mock servicos externos (Ollama, Qdrant, OpenAI) em integration tests
- Arrange-Act-Assert: preparar, executar, verificar
- Coverage minima: 80% modulos audit
- Nao testar implementacao, testar comportamento
- Um assert por teste conceitual (ou grupo logico)
