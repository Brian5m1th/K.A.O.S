"""
Core Services — Application-layer orchestrators for K.A.O.S capabilities.

Each service wraps a domain Port with a ProviderRegistry, enabling
runtime switching of backend implementations without Desktop changes.

Architecture:
    Desktop → REST API → Service → Port → Adapter → Framework

The service layer is the bridge between HTTP and domain logic.
"""

from app.core.services.graph_service import GraphService
from app.core.services.memory_service import MemoryService
from app.core.services.retrieval_service import RetrievalService
from app.core.services.inference_service import InferenceService
from app.core.services.planner_service import PlannerService
from app.core.services.evidence_service import EvidenceService
from app.core.services.knowledge_service import KnowledgeService

__all__ = [
    "GraphService",
    "MemoryService",
    "RetrievalService",
    "InferenceService",
    "PlannerService",
    "EvidenceService",
    "KnowledgeService",
]
