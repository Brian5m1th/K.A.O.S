import asyncio
import json
from pathlib import Path
from typing import Any
from uuid import uuid4
from loguru import logger
import httpx
from sqlalchemy import select

from app.database import async_session_factory
from app.models.automation_registry import AutomationWorkflow
from app.providers.automation.n8n_workflow_provider import N8NWorkflowProvider
from app.providers.automation.base_workflow_provider import BaseWorkflowProvider


class AutomationBus:
    _queue: asyncio.Queue[dict[str, Any]] = asyncio.Queue()
    _worker_task: asyncio.Task | None = None
    _provider: BaseWorkflowProvider | None = None

    @classmethod
    def get_provider(cls) -> BaseWorkflowProvider:
        """Resolves the configured automation workflow provider."""
        if cls._provider is None:
            # Under clean architecture, we resolve based on env settings.
            # Currently, n8n is the primary supported provider.
            cls._provider = N8NWorkflowProvider()
        return cls._provider

    @classmethod
    async def auto_import_workflows(cls) -> None:
        """
        Polls n8n health status, scans data/workflows/ JSON templates,
        and auto-imports any that are not registered.
        """
        provider = cls.get_provider()
        # provider.api_url is e.g. http://n8n:5678
        health_url = f"{provider.api_url}/healthz"

        logger.info(f"[AutomationBus] Waiting for workflow engine at {health_url}...")

        retries = 5
        delay = 2.0
        online = False
        for attempt in range(retries):
            try:
                async with httpx.AsyncClient(timeout=3.0) as client:
                    res = await client.get(health_url)
                    if res.status_code == 200:
                        online = True
                        break
            except Exception:
                pass
            logger.debug(
                f"[AutomationBus] Connection attempt {attempt + 1}/{retries} failed. Retrying in {delay}s..."
            )
            await asyncio.sleep(delay)
            delay *= 2.0

        if not online:
            logger.warning(
                "[AutomationBus] Workflow engine is offline. Skipping default workflows auto-import."
            )
            return

        logger.info(
            "[AutomationBus] Workflow engine is online. Running template auto-import..."
        )

        workflows_dir = Path("data/workflows")
        if not workflows_dir.exists():
            logger.info(
                "[AutomationBus] Workflows directory 'data/workflows' does not exist."
            )
            return

        for path in workflows_dir.glob("*.json"):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    wf_data = json.load(f)
                wf_name = wf_data.get("name", path.stem)

                # Check if registered locally
                factory = async_session_factory()
                async with factory() as session:
                    stmt = select(AutomationWorkflow).where(
                        AutomationWorkflow.name == wf_name
                    )
                    result = await session.execute(stmt)
                    existing = result.scalar_one_or_none()

                    if existing:
                        logger.debug(
                            f"[AutomationBus] Workflow '{wf_name}' already registered in local DB."
                        )
                        continue

                    # Import to external engine
                    logger.info(
                        f"[AutomationBus] Auto-importing default workflow '{wf_name}'..."
                    )
                    res = await provider.import_workflow(wf_name, wf_data)
                    remote_id = res.get("remote_id")

                    # Register in local DB
                    new_wf = AutomationWorkflow(
                        n8n_workflow_id=remote_id,
                        name=wf_name,
                        description=f"Auto-imported from {path.name}",
                        is_active=True,
                        json_data=wf_data,
                        version=1,
                    )
                    session.add(new_wf)
                    await session.commit()
                    logger.info(
                        f"[AutomationBus] Registered auto-imported workflow '{wf_name}' with ID {remote_id}"
                    )
            except Exception as e:
                logger.error(
                    f"[AutomationBus] Failed to auto-import '{path.name}': {e}"
                )

    @classmethod
    async def publish(
        cls, event_name: str, data: dict[str, Any], depth: int = 0
    ) -> None:
        """
        Publishes an event to the automation queue.
        Enforces cascading loop limits.
        """
        # Depth check for cascading loop protection
        if depth > 3:
            logger.warning(
                f"[AutomationBus] Loop cascade detected for event '{event_name}' (depth={depth}). Event dropped."
            )
            return

        # Prepare payload with metadata
        trace_id = data.get("_trace_id") or str(uuid4())
        event_id = data.get("_event_id") or str(uuid4())

        event_payload = {
            "event": event_name,
            "data": data,
            "_trace_id": trace_id,
            "_event_id": event_id,
            "_depth": depth + 1,
        }

        await cls._queue.put(event_payload)
        logger.debug(
            f"[AutomationBus] Event '{event_name}' enqueued (trace_id={trace_id}, depth={depth})"
        )

    @classmethod
    async def start_worker(cls) -> None:
        """Starts the background worker queue consumer."""
        if cls._worker_task is not None:
            return

        cls._worker_task = asyncio.create_task(cls._consume_queue())
        logger.info("[AutomationBus] Queue worker started successfully.")

    @classmethod
    async def stop_worker(cls) -> None:
        """Stops the background worker consumer."""
        if cls._worker_task is not None:
            cls._worker_task.cancel()
            try:
                await cls._worker_task
            except asyncio.CancelledError:
                pass
            cls._worker_task = None
            logger.info("[AutomationBus] Queue worker stopped.")

    @classmethod
    async def _consume_queue(cls) -> None:
        """Worker consumption loop."""
        provider = cls.get_provider()
        while True:
            event = None
            try:
                event = await cls._queue.get()
                event_name = event["event"]
                trace_id = event["_trace_id"]
                depth = event["_depth"]

                logger.debug(
                    f"[AutomationBus] Processing event '{event_name}' (trace_id={trace_id}, depth={depth})"
                )

                # Determine webhook path/routing
                # Map K.A.O.S events to specific n8n webhook path triggers
                webhook_path = cls._resolve_webhook_path(event_name)

                # Trigger the provider
                res = await provider.trigger_workflow(webhook_path, event)
                if not res.get("success"):
                    logger.warning(
                        f"[AutomationBus] Webhook trigger failed for '{event_name}' (path={webhook_path}): {res.get('error')}"
                    )
                else:
                    logger.debug(
                        f"[AutomationBus] Event '{event_name}' delivered. Execution ID: {res.get('execution_id')}"
                    )

            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"[AutomationBus] Error in queue consumer worker: {e}")
                await asyncio.sleep(1.0)  # Rate limit error backoff
            finally:
                if event is not None:
                    cls._queue.task_done()

    @classmethod
    def _resolve_webhook_path(cls, event_name: str) -> str:
        """Maps EventBus event names to n8n webhook trigger URL path keys."""
        # Clean mapping to match templates
        mapping = {
            "vault.analysis.completed": "kaos-vault-sync",
            "workflow_completed": "kaos-cost-event",
            "llm_response": "kaos-cost-event",
        }
        return mapping.get(event_name, "kaos-event")
