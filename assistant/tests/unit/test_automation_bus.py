import pytest
import asyncio
from unittest.mock import MagicMock, AsyncMock, patch
from app.core.automation_bus import AutomationBus


@pytest.mark.asyncio
async def test_automation_bus_publish_depth_limit():
    # Reset queue
    while not AutomationBus._queue.empty():
        AutomationBus._queue.get_nowait()

    # Try to publish with depth > 3
    await AutomationBus.publish("test_event", {"val": "x"}, depth=4)
    
    # Assert queue is empty (event was dropped)
    assert AutomationBus._queue.empty()


@pytest.mark.asyncio
async def test_automation_bus_publish_and_consume():
    # Reset queue
    while not AutomationBus._queue.empty():
        AutomationBus._queue.get_nowait()

    # Mock provider
    mock_provider = MagicMock()
    mock_provider.trigger_workflow = AsyncMock(return_value={"success": True, "execution_id": "mock_exec"})
    AutomationBus._provider = mock_provider

    # Start worker
    await AutomationBus.start_worker()

    # Publish valid event
    await AutomationBus.publish("vault.analysis.completed", {"val": "sync_notes"}, depth=0)
    
    # Wait for queue to be processed
    await asyncio.sleep(0.1)

    # Verify provider trigger was called with correct webhook path
    mock_provider.trigger_workflow.assert_called_once()
    args, kwargs = mock_provider.trigger_workflow.call_args
    assert args[0] == "kaos-vault-sync"
    assert args[1]["_depth"] == 1
    assert args[1]["data"]["val"] == "sync_notes"

    # Stop worker
    await AutomationBus.stop_worker()
