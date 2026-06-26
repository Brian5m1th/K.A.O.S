import pytest
from unittest.mock import MagicMock, AsyncMock, patch
from app.providers.automation.n8n_workflow_provider import N8NWorkflowProvider


@pytest.mark.asyncio
async def test_n8n_provider_import_workflow():
    provider = N8NWorkflowProvider()

    mock_response = MagicMock()
    mock_response.status_code = 201
    mock_response.json.return_value = {"id": "remote_wf_123", "name": "Test Workflow"}

    with patch("httpx.AsyncClient.post", new_callable=AsyncMock) as mock_post:
        mock_post.return_value = mock_response
        res = await provider.import_workflow("Test Workflow", {"nodes": []})
        assert res["remote_id"] == "remote_wf_123"
        assert res["raw"]["name"] == "Test Workflow"


@pytest.mark.asyncio
async def test_n8n_provider_toggle_workflow():
    provider = N8NWorkflowProvider()

    mock_response = MagicMock()
    mock_response.status_code = 200

    with patch("httpx.AsyncClient.post", new_callable=AsyncMock) as mock_post:
        mock_post.return_value = mock_response
        success = await provider.toggle_workflow("remote_wf_123", True)
        assert success is True


@pytest.mark.asyncio
async def test_n8n_provider_trigger_workflow():
    provider = N8NWorkflowProvider()

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.headers = {"X-N8N-Execution-Id": "exec_999"}
    mock_response.text = '{"status": "running"}'
    mock_response.json.return_value = {"status": "running"}

    with patch("httpx.AsyncClient.post", new_callable=AsyncMock) as mock_post:
        mock_post.return_value = mock_response
        res = await provider.trigger_workflow(
            "kaos-vault-sync",
            {"_trace_id": "abc-123", "_depth": 1, "event": "vault.analysis.completed"},
        )
        assert res["success"] is True
        assert res["execution_id"] == "exec_999"
        assert res["response"]["status"] == "running"
