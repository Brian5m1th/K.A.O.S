from enum import Enum


class WorkflowType(str, Enum):
    CHAT = "chat"
    RAG = "rag"
    AGENT = "agent"
    MEMORY = "memory"
    INGEST = "ingest"
