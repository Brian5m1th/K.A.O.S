from unittest.mock import MagicMock, patch

import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app


@pytest.fixture
def client() -> AsyncClient:
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


@pytest.mark.asyncio
async def test_full_reindex_endpoint(client: AsyncClient) -> None:
    mock_indexer = MagicMock()
    mock_indexer.index_vault.return_value = {"files": 10, "chunks": 42}
    with patch("app.api.indexing._get_indexer", return_value=mock_indexer):
        response = await client.post("/indexing/full")

    assert response.status_code == 200
    data = response.json()
    assert data["files"] == 10
    assert data["chunks"] == 42
