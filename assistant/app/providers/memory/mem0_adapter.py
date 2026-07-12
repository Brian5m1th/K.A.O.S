"""
Mem0Adapter — MemoryPort implementation backed by Mem0.

Mem0 provides persistent user identity memory with semantic search,
enabling the agent to remember user preferences, facts, and conversation
context across sessions.

Requires: pip install mem0ai
Env: MEM0_API_KEY=... (optional, uses local embedding by default)
"""

import time
from datetime import datetime, timezone
from typing import Optional

from loguru import logger

from app.domain.ports.memory_port import (
    MemoryPort,
    MemoryEntry,
    MemoryQuery,
    MemoryResult,
)

try:
    from mem0 import Memory as Mem0Client

    HAS_MEM0 = True
except ImportError:
    HAS_MEM0 = False
    Mem0Client = None  # type: ignore


class Mem0Adapter(MemoryPort):
    """MemoryPort adapter using Mem0 for persistent user memory."""

    def __init__(self, config: Optional[dict] = None) -> None:
        self._client: Optional[Mem0Client] = None
        self._config = config or {}
        self._enabled = HAS_MEM0

    def _ensure_client(self) -> Optional[Mem0Client]:
        if self._client is None and self._enabled:
            try:
                self._client = Mem0Client.from_config(self._config)
                logger.info("[mem0] client initialized")
            except Exception as exc:
                logger.warning(f"[mem0] failed to initialize: {exc}")
                self._enabled = False
        return self._client

    @property
    def provider_name(self) -> str:
        return "mem0"

    async def store(self, entry: MemoryEntry) -> str:
        """Store a memory entry via Mem0."""
        client = self._ensure_client()
        if not client:
            logger.warning("[mem0] not available, falling back to no-op")
            return ""

        user_id = entry.user_id or "default"
        try:
            result = client.add(
                data=entry.content,
                user_id=user_id,
                metadata={
                    "type": entry.type,
                    **(entry.metadata or {}),
                },
            )
            mem_id = result.get("id", "")
            logger.info(
                "[mem0] stored memory for user={} type={} id={}",
                user_id,
                entry.type,
                mem_id,
            )
            return mem_id
        except Exception as exc:
            logger.error(f"[mem0] store failed: {exc}")
            return ""

    async def search(self, query: MemoryQuery) -> MemoryResult:
        """Search memories by semantic similarity."""
        client = self._ensure_client()
        if not client:
            return MemoryResult()

        t0 = time.monotonic()
        try:
            results = client.search(
                query=query.text,
                user_id=query.user_id,
                limit=query.max_results,
            )
            matches = []
            for item in (
                results if isinstance(results, list) else results.get("results", [])
            ):
                matches.append(
                    MemoryEntry(
                        id=item.get("id", ""),
                        user_id=query.user_id or "",
                        type=item.get("metadata", {}).get("type", "semantic"),
                        content=item.get("memory", item.get("text", "")),
                        metadata=item.get("metadata", {}),
                        created_at=datetime.now(timezone.utc),
                    )
                )

            elapsed = (time.monotonic() - t0) * 1000
            logger.info(
                "[mem0] search returned {} results in {:.0f}ms", len(matches), elapsed
            )
            return MemoryResult(
                matches=matches, total_found=len(matches), query_time_ms=elapsed
            )
        except Exception as exc:
            logger.error(f"[mem0] search failed: {exc}")
            return MemoryResult()

    async def get(self, memory_id: str) -> Optional[MemoryEntry]:
        """Retrieve a specific memory by ID."""
        client = self._ensure_client()
        if not client:
            return None

        try:
            result = client.get(memory_id)
            if not result:
                return None
            return MemoryEntry(
                id=result.get("id", memory_id),
                user_id=result.get("user_id", ""),
                type=result.get("metadata", {}).get("type", "semantic"),
                content=result.get("memory", result.get("text", "")),
                metadata=result.get("metadata", {}),
                created_at=datetime.now(timezone.utc),
            )
        except Exception as exc:
            logger.error(f"[mem0] get failed: {exc}")
            return None

    async def delete(self, memory_id: str) -> bool:
        """Delete a memory entry."""
        client = self._ensure_client()
        if not client:
            return False

        try:
            client.delete(memory_id)
            logger.info("[mem0] deleted memory id={}", memory_id)
            return True
        except Exception as exc:
            logger.error(f"[mem0] delete failed: {exc}")
            return False

    async def health(self) -> bool:
        return self._enabled and self._ensure_client() is not None
