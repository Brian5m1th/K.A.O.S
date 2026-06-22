---
description: Padroes de API do K.A.O.S
globs: 
---
# API Patterns

## FastAPI Router

```python
from fastapi import APIRouter
from pydantic import BaseModel
from loguru import logger

router = APIRouter(prefix="/api/recurso", tags=["Recurso"])

class RequestSchema(BaseModel):
    campo: str

class ResponseSchema(BaseModel):
    resultado: str

@router.post("/executar", response_model=ResponseSchema)
async def executar(request: RequestSchema):
    logger.info("[recurso] executando")
    return ResponseSchema(resultado="ok")
```

## Auth

- Header: `x-api-key` ou `Authorization: Bearer <key>`
- `ApiKeyMiddleware` checks every request (except public paths)
- Public paths: `/health`, `/docs`, `/openapi.json`
- API key stored in `data/api_key.txt`, generated on first run

## Router Registration

No `assistant/app/main.py`:
```python
from app.api.meu_modulo import router as meu_modulo_router
app.include_router(meu_modulo_router)
```

## Streaming (SSE)

```python
from fastapi.responses import StreamingResponse

async def generate():
    yield f"data: {json.dumps({'token': 'hello'})}\n\n"

return StreamingResponse(generate(), media_type="text/event-stream")
```

## Response Patterns

- Always use `response_model=` with Pydantic schema
- Async routes throughout
- Logger tagging: `[start]`, `[finish]`, `[info]`, `[error]`
- Return standardized error: `{"detail": "mensagem de erro"}`
