"""
Domain Ports — Abstract interfaces for K.A.O.S capabilities.

Each port defines the contract between the Desktop/Application layer
and the Framework/Infrastructure layer. No port depends on any
specific framework (Graphify, Mem0, Qdrant, etc.).

Hexagonal Architecture: Domain → Ports → Adapters → Frameworks
"""

from app.domain.ports.graph_port import GraphPort, NodeInfo, PathInfo, GraphQuery, GraphResult
from app.domain.ports.memory_port import MemoryPort, MemoryEntry, MemoryQuery, MemoryResult
from app.domain.ports.retrieval_port import RetrievalPort, RetrievalQuery, RetrievalResult
from app.domain.ports.inference_port import InferencePort, InferenceRequest, InferenceResult
from app.domain.ports.planner_port import PlannerPort, PlanRequest, PlanResult
from app.domain.ports.evidence_port import EvidencePort, EvidenceReport, EvidenceMetric

__all__ = [
    # Graph
    "GraphPort", "NodeInfo", "PathInfo", "GraphQuery", "GraphResult",
    # Memory
    "MemoryPort", "MemoryEntry", "MemoryQuery", "MemoryResult",
    # Retrieval
    "RetrievalPort", "RetrievalQuery", "RetrievalResult",
    # Inference
    "InferencePort", "InferenceRequest", "InferenceResult",
    # Planner
    "PlannerPort", "PlanRequest", "PlanResult",
    # Evidence
    "EvidencePort", "EvidenceReport", "EvidenceMetric",
]
