"""Workspace Intelligence API Router.

SDD-KAOS-EVOLUTION-001: Provides FastAPI routes for Vault analysis, auto-tagging,
                       and connection recommendations.
"""
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import Any, List

from app.capability.workspace_intelligence.service import WorkspaceIntelligenceService
from app.capability.registry import CapabilityRegistry, CapabilityLifecycle

router = APIRouter(prefix="/api/workspace-intelligence", tags=["Workspace Intelligence"])


class AutoTagRequest(BaseModel):
    path: str


class SuggestLinksRequest(BaseModel):
    path: str


@router.post("/auto-tag")
async def auto_tag_endpoint(body: AutoTagRequest):
    """Auto-tags a file inside the Obsidian Vault based on content or neighbors."""
    service = WorkspaceIntelligenceService()
    try:
        CapabilityRegistry.update_status("workspace_intelligence", CapabilityLifecycle.HEALTHY)
        tags = await service.auto_tag(body.path)
        return {"status": "success", "tags": tags}
    except Exception as e:
        CapabilityRegistry.update_status(
            "workspace_intelligence", 
            CapabilityLifecycle.FAILED, 
            error_message=str(e)
        )
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/suggest-connections")
async def suggest_connections_endpoint(body: SuggestLinksRequest):
    """Recommends wiki links for a target markdown document."""
    service = WorkspaceIntelligenceService()
    try:
        recommendations = await service.suggest_links(body.path)
        return {"status": "success", "recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/health")
async def health_endpoint():
    """Checks vault structure sanity metrics."""
    service = WorkspaceIntelligenceService()
    try:
        health_info = service.check_vault_health()
        return {"status": "success", "metrics": health_info}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
