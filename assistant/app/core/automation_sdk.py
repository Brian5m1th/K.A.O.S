"""
K.A.O.S Internal Automation SDK.
Exposes standard hooks for agent nodes, managers, and other services to trigger or wait on workflows.
"""

import asyncio
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4
from loguru import logger
from sqlalchemy import select

from app.database import async_session_factory
from app.models.automation_registry import AutomationExecution
from app.core.automation_bus import AutomationBus


class AutomationService:
    @classmethod
    async def trigger(
        cls, workflow_id_or_path: str, payload: dict[str, Any]
    ) -> dict[str, Any]:
        """
        Triggers a workflow run via the active provider.
        Returns a dict: {"success": bool, "execution_id": str, "error": str | None}
        """
        provider = AutomationBus.get_provider()

        # Inject standard loop tracing metadata
        payload.setdefault("_trace_id", str(uuid4()))
        payload.setdefault("_event_id", str(uuid4()))
        payload.setdefault("_depth", 1)

        logger.info(f"[AutomationSDK] Triggering workflow '{workflow_id_or_path}'")
        res = await provider.trigger_workflow(workflow_id_or_path, payload)

        return {
            "success": res.get("success", False),
            "execution_id": res.get("execution_id", ""),
            "error": res.get("error"),
            "response": res.get("response"),
        }

    @classmethod
    async def emit(cls, event_name: str, data: dict[str, Any]) -> None:
        """
        Publishes an event to the Automation Bus queue.
        This is non-blocking.
        """
        await AutomationBus.publish(event_name, data, depth=0)

    @classmethod
    async def wait_for(
        cls, execution_id: str, timeout_seconds: int = 120
    ) -> dict[str, Any]:
        """
        Blocks and waits until the execution is completed (success or failed) in the database.
        Used for human-in-the-loop scenarios or long-running tasks.
        """
        start_time = datetime.now(timezone.utc)
        polling_interval = 2.0

        logger.info(
            f"[AutomationSDK] Waiting for execution '{execution_id}' (timeout={timeout_seconds}s)"
        )

        while True:
            # Check elapsed time
            elapsed = (datetime.now(timezone.utc) - start_time).total_seconds()
            if elapsed > timeout_seconds:
                logger.warning(
                    f"[AutomationSDK] Wait timeout for execution '{execution_id}'"
                )
                return {
                    "success": False,
                    "status": "timeout",
                    "error": "Execution wait timeout exceeded",
                }

            # Query db for execution status
            factory = async_session_factory()
            async with factory() as session:
                stmt = select(AutomationExecution).where(
                    (AutomationExecution.id == execution_id)
                    | (AutomationExecution.n8n_execution_id == execution_id)
                )
                result = await session.execute(stmt)
                execution = result.scalar_one_or_none()

                if execution:
                    if execution.status in ("success", "failed"):
                        logger.info(
                            f"[AutomationSDK] Execution '{execution_id}' finished with status: {execution.status}"
                        )
                        return {
                            "success": execution.status == "success",
                            "status": execution.status,
                            "response": execution.response,
                        }
                    else:
                        logger.debug(
                            f"[AutomationSDK] Execution '{execution_id}' is still in state: {execution.status}"
                        )
                else:
                    logger.debug(
                        f"[AutomationSDK] Execution '{execution_id}' not found in DB yet, continuing poll."
                    )

            await asyncio.sleep(polling_interval)
