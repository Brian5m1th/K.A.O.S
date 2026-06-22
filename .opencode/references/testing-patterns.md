---
description: Padroes de teste do K.A.O.S
globs: 
---
# Testing Patterns

## Framework
- pytest + pytest-asyncio + pytest-cov + httpx

## Structure
- `assistant/tests/` mirrors `assistant/app/`
- `tests/unit/` - Unit tests
- `tests/integration/` - Integration tests
- `tests/fixtures/` - Shared fixtures

## Naming
- Files: `test_<module>.py`
- Classes: `Test<Module>`
- Methods: `test_<functionality>`

## Fixture Pattern
```python
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.fixture
def client() -> AsyncClient:
    app.state.api_key = "test-api-key"
    transport = ASGITransport(app=app)
    return AsyncClient(
        transport=transport,
        base_url="http://test",
        headers={"x-api-key": "test-api-key"},
    )
```

## Async Test Pattern
```python
@pytest.mark.asyncio
async def test_health_check(client: AsyncClient) -> None:
    response = await client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
```

## CI Commands
```bash
uv run ruff check .         # Lint
uv run pytest -v            # Tests
uv run pytest --cov=app     # Coverage
cd desktop && npx tsc --noEmit  # TypeScript
```

## Coverage Threshold
- Minimum 80% for audit modules
- CI fails if coverage < 90% (validate_documentation.py)
