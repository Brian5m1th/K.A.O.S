import pytest
from unittest.mock import MagicMock, AsyncMock, patch
from app.core.automation_sdk import AutomationService
from app.models.automation_registry import AutomationExecution


@pytest.mark.asyncio
async def test_automation_service_trigger():
    mock_provider = MagicMock()
    mock_provider.trigger_workflow = AsyncMock(
        return_value={"success": True, "execution_id": "exec_abc"}
    )

    with patch(
        "app.core.automation_bus.AutomationBus.get_provider", return_value=mock_provider
    ):
        res = await AutomationService.trigger("wf-test", {"param": 1})
        assert res["success"] is True
        assert res["execution_id"] == "exec_abc"
        mock_provider.trigger_workflow.assert_called_once()


@pytest.mark.asyncio
async def test_automation_service_emit():
    with patch(
        "app.core.automation_bus.AutomationBus.publish", new_callable=AsyncMock
    ) as mock_pub:
        await AutomationService.emit("test_event", {"some": "data"})
        mock_pub.assert_called_once_with("test_event", {"some": "data"}, depth=0)


@pytest.mark.asyncio
async def test_automation_service_wait_for():
    # We will mock the database session/execute flow
    mock_execution = MagicMock(spec=AutomationExecution)
    mock_execution.status = "success"
    mock_execution.response = {"result": "ok"}

    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = mock_execution

    mock_session = AsyncMock()
    mock_session.execute.return_value = mock_result

    # We use a context manager mock for the factory
    mock_factory_instance = MagicMock()
    mock_factory_instance.__aenter__.return_value = mock_session
    mock_factory_instance.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "app.core.automation_sdk.async_session_factory",
        return_value=lambda: mock_factory_instance,
    ):
        res = await AutomationService.wait_for("exec_111", timeout_seconds=5)
        assert res["success"] is True
        assert res["status"] == "success"
        assert res["response"]["result"] == "ok"
