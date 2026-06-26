"""
n8n Workflow Provider Implementation for K.A.O.S.
Communicates with the n8n REST API and triggers webhooks.
"""

import os
from typing import Any
import httpx
from loguru import logger
from app.config.settings import settings
from app.providers.automation.base_workflow_provider import BaseWorkflowProvider


class N8NWorkflowProvider(BaseWorkflowProvider):
    def __init__(self) -> None:
        self.api_url = settings.N8N_API_URL.rstrip("/")
        # We allow reading the API Key from settings or environment
        self.api_key = os.getenv("N8N_API_KEY", "")
        self.timeout = 10.0

    def _get_headers(self) -> dict[str, str]:
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["X-N8N-API-KEY"] = self.api_key
        return headers

    async def import_workflow(
        self, name: str, json_data: dict[str, Any]
    ) -> dict[str, Any]:
        """
        Imports a workflow template.
        Uses POST /api/v1/workflows to create it in n8n.
        """
        url = f"{self.api_url}/api/v1/workflows"
        payload = {
            "name": name,
            "nodes": json_data.get("nodes", []),
            "connections": json_data.get("connections", {}),
            "settings": json_data.get("settings", {}),
            "staticData": json_data.get("staticData", None),
        }

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    url, json=payload, headers=self._get_headers()
                )
                if response.status_code == 201:
                    data = response.json()
                    return {"remote_id": str(data.get("id")), "raw": data}
                else:
                    logger.error(
                        f"[N8NProvider] Failed to import workflow: {response.text}"
                    )
                    raise ValueError(
                        f"n8n API returned status {response.status_code}: {response.text}"
                    )
        except httpx.RequestError as exc:
            logger.error(f"[N8NProvider] Connection error during import: {exc}")
            raise ConnectionError(f"Could not connect to n8n at {url}: {exc}")

    async def export_workflow(self, remote_id: str) -> dict[str, Any]:
        """
        Retrieves a workflow schema by ID from n8n.
        Uses GET /api/v1/workflows/{id}.
        """
        url = f"{self.api_url}/api/v1/workflows/{remote_id}"
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(url, headers=self._get_headers())
                if response.status_code == 200:
                    return response.json()
                else:
                    logger.error(
                        f"[N8NProvider] Failed to export workflow {remote_id}: {response.text}"
                    )
                    raise ValueError(
                        f"n8n API returned status {response.status_code}: {response.text}"
                    )
        except httpx.RequestError as exc:
            logger.error(f"[N8NProvider] Connection error during export: {exc}")
            raise ConnectionError(f"Could not connect to n8n: {exc}")

    async def toggle_workflow(self, remote_id: str, is_active: bool) -> bool:
        """
        Activates or deactivates a workflow.
        Uses POST /api/v1/workflows/{id}/activate or /deactivate.
        """
        action = "activate" if is_active else "deactivate"
        url = f"{self.api_url}/api/v1/workflows/{remote_id}/{action}"
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(url, headers=self._get_headers(), json={})
                if response.status_code == 200:
                    return True
                else:
                    logger.error(
                        f"[N8NProvider] Failed to {action} workflow {remote_id}: {response.text}"
                    )
                    return False
        except httpx.RequestError as exc:
            logger.error(f"[N8NProvider] Connection error toggling workflow: {exc}")
            return False

    async def trigger_workflow(
        self, webhook_path_or_id: str, payload: dict[str, Any]
    ) -> dict[str, Any]:
        """
        Triggers a workflow by invoking its Webhook node.
        webhook_path_or_id can be the path component (e.g. 'kaos-vault-sync').
        Sends X-KAOS-Depth and X-KAOS-Trace-ID headers for loop prevention.
        """
        # Determine URL
        # Webhook node urls are typically at N8N_API_URL/webhook/path or N8N_API_URL/webhook-test/path
        # If N8N_API_URL is http://n8n:5678, webhooks are hosted at same port.
        url = f"{self.api_url}/webhook/{webhook_path_or_id}"

        # Prepare headers for loop tracking and idempotency
        headers = {
            "Content-Type": "application/json",
            "X-KAOS-Depth": str(payload.get("_depth", 0)),
            "X-KAOS-Trace-ID": payload.get("_trace_id", ""),
            "X-Event-ID": payload.get("_event_id", ""),
        }

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(url, json=payload, headers=headers)
                success = response.status_code in (200, 201, 202)
                return {
                    "success": success,
                    "execution_id": response.headers.get("X-N8N-Execution-Id", ""),
                    "response": response.json()
                    if success and response.text
                    else {"status": response.status_code, "text": response.text},
                }
        except httpx.RequestError as exc:
            logger.error(f"[N8NProvider] Connection error triggering webhook: {exc}")
            return {
                "success": False,
                "execution_id": "",
                "error": f"Webhook invocation failed: {exc}",
            }
