---
description: Regras Python para o K.A.O.S
globs: ["assistant/**/*.py"]
---
# Python Rules

- Use `from __future__ import annotations` no topo de todo arquivo
- Type hints obrigatorios em todas as funcoes: `def func(x: str) -> int:`
- Use `| None` em vez de `Optional` (`x: str | None = None`)
- Use `list[X]` em vez de `List[X]` (PEP 585, Python 3.13)
- Use `dict[str, X]` em vez de `Dict[str, X]`
- Imports: stdlib primeiro, terceiros segundo, locais terceiro
- Imports absolutos: `from app.config.settings import settings`
- Nao use `from typing import ...` para tipos basicos
- Logs com loguru: `logger.info()`, `logger.warning()`, `logger.error()`
- Tags em logs: `[start]`, `[finish]`, `[info]`, `[error]`, `[fallback]`, `[auth]`
- Dataclasses para modelos simples, Pydantic para validacao
- Pydantic v2: `BaseModel` + `field_validator` + `model_config`
- Async em todas as rotas FastAPI
- Nao deixe `TODO`, `FIXME`, `pass` ou `NotImplementedError` em codigo final
- Nao use `import *` em nenhuma circunstancia
- Mantenha funcoes com menos de 50 linhas
- Nao use variaveis nao utilizadas (F841)
