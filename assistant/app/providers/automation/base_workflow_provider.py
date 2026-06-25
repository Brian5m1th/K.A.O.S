"""
Base Workflow Provider Interface for K.A.O.S.
Defines the standard contract for orchestrating workflows with different engines.
"""

from abc import ABC, abstractmethod
from typing import Any


class BaseWorkflowProvider(ABC):
    @abstractmethod
    async def import_workflow(self, name: str, json_data: dict[str, Any]) -> dict[str, Any]:
        """
        Imports a workflow template into the external automation engine.
        Returns a dict containing at least {"remote_id": str} and any other metadata.
        """
        pass

    @abstractmethod
    async def export_workflow(self, remote_id: str) -> dict[str, Any]:
        """
        Exports the JSON schema of a workflow from the external engine.
        """
        pass

    @abstractmethod
    async def toggle_workflow(self, remote_id: str, is_active: bool) -> bool:
        """
        Enables or disables the execution of a workflow.
        Returns True if successful, False otherwise.
        """
        pass

    @abstractmethod
    async def trigger_workflow(self, webhook_path_or_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        """
        Invokes/triggers a workflow execution.
        Returns execution details like {"success": bool, "execution_id": str, "response": dict}.
        """
        pass
