import pytest
from httpx import AsyncClient, ASGITransport
from unittest.mock import MagicMock, AsyncMock, patch
from app.main import app
from app.database import get_session


@pytest.fixture
def client() -> AsyncClient:
    app.state.api_key = "test-api-key"
    transport = ASGITransport(app=app)
    return AsyncClient(
        transport=transport,
        base_url="http://test",
        headers={"x-api-key": "test-api-key"},
    )


@pytest.mark.asyncio
async def test_list_workflows_empty_db(client: AsyncClient) -> None:
    # Mock SQL session execute
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = []

    mock_session = AsyncMock()
    mock_session.execute.return_value = mock_result

    # Override get_session dependency
    app.dependency_overrides[get_session] = lambda: mock_session

    response = await client.get("/api/automation/workflows")
    assert response.status_code == 200
    assert response.json() == {"workflows": []}

    # Clean up overrides
    app.dependency_overrides.clear()


@pytest.mark.asyncio
async def test_n8n_callback_unregistered_workflow(client: AsyncClient) -> None:
    # Mock SQL select returning None (no workflow found)
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = None

    mock_session = AsyncMock()
    mock_session.execute.return_value = mock_result

    # We patch async_session_factory context manager used in webhooks callback
    mock_factory = MagicMock()
    mock_factory.__aenter__.return_value = mock_session
    mock_factory.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "app.api.webhooks.async_session_factory", return_value=lambda: mock_factory
    ):
        payload = {
            "workflow_id": "remote-wf-id",
            "execution_id": "exec-abc-123",
            "status": "success",
        }
        response = await client.post("/api/webhooks/n8n/callback", json=payload)
        assert response.status_code == 200
        assert response.json()["status"] == "error"
        assert "not registered" in response.json()["message"]


# ── Marketplace / Templates ────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_list_templates_no_dir(client: AsyncClient) -> None:
    """Quando data/workflows/ nao existe, retorna lista vazia."""
    with patch("pathlib.Path.exists", return_value=False):
        response = await client.get("/api/automation/templates")
        assert response.status_code == 200
        data = response.json()
        assert "templates" in data
        assert data["templates"] == []


@pytest.mark.asyncio
async def test_list_templates_uses_real_files(client: AsyncClient) -> None:
    """Usa os templates reais em data/workflows/ (criados na Fase 7)."""
    response = await client.get("/api/automation/templates")
    assert response.status_code == 200
    data = response.json()
    assert "templates" in data
    # Devem existir ao menos os 6 templates que criamos
    assert len(data["templates"]) >= 6


@pytest.mark.asyncio
async def test_list_templates_has_names(client: AsyncClient) -> None:
    """Templates retornados tem nome e descricao."""
    response = await client.get("/api/automation/templates")
    data = response.json()
    for tpl in data["templates"]:
        assert "name" in tpl
        assert "description" in tpl
        assert "json_name" in tpl
        assert "category" in tpl


@pytest.mark.asyncio
async def test_list_templates_categories_present(client: AsyncClient) -> None:
    """Categorias incluem valores esperados."""
    response = await client.get("/api/automation/templates")
    data = response.json()
    categories = {t["category"] for t in data["templates"]}
    # Deve ter pelo menos IA
    assert "IA" in categories


@pytest.mark.asyncio
async def test_import_workflow_validates_name(client: AsyncClient) -> None:
    """Import sem nome retorna 422."""
    response = await client.post("/api/automation/workflows/import", json={})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_import_workflow_validates_json(client: AsyncClient) -> None:
    """Import sem json_data retorna 422."""
    response = await client.post("/api/automation/workflows/import", json={"name": "Test"})
    assert response.status_code == 422
