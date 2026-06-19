import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.fixture
def client() -> AsyncClient:
    app.state.api_key = "test-api-key"
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test", headers={"x-api-key": "test-api-key"})


@pytest.mark.asyncio
async def test_health_check(client: AsyncClient) -> None:
    response = await client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["version"] == "0.1.0"
