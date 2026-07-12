"""
FalkorDBAdapter — RetrievalPort implementation backed by FalkorDB.

FalkorDB (formerly RedisGraph) provides graph-native vector search,
combining graph traversal with vector similarity for hybrid retrieval.

Requires: pip install falkordb
Env: FALKORDB_HOST=localhost
     FALKORDB_PORT=6379
     FALKORDB_PASSWORD=
"""

import time
import hashlib

from loguru import logger

from app.domain.ports.retrieval_port import (
    RetrievalPort,
    RetrievalQuery,
    RetrievalResult,
)
from app.config.settings import settings

try:
    from falkordb import FalkorDB as FalkorDBClient

    HAS_FALKORDB = True
except ImportError:
    HAS_FALKORDB = False
    FalkorDBClient = None  # type: ignore


class FalkorDBAdapter(RetrievalPort):
    """RetrievalPort adapter using FalkorDB for hybrid graph+vector search."""

    GRAPH_NAME = "kaos"

    def __init__(self) -> None:
        self._client = None
        self._host = settings.get("FALKORDB_HOST", "localhost")
        self._port = int(settings.get("FALKORDB_PORT", 6379))
        self._password = settings.get("FALKORDB_PASSWORD", None)
        self._enabled = HAS_FALKORDB

    def _connect(self):
        if self._client is None and self._enabled:
            try:
                self._client = FalkorDBClient(
                    host=self._host,
                    port=self._port,
                    password=self._password,
                )
                logger.info("[falkordb] connected to {}:{}", self._host, self._port)
            except Exception as exc:
                logger.warning("[falkordb] connection failed: {}", exc)
                self._enabled = False
        return self._client

    def _graph(self):
        client = self._connect()
        if client:
            return client.select_graph(self.GRAPH_NAME)
        return None

    @property
    def provider_name(self) -> str:
        return "falkordb"

    async def search(self, query: RetrievalQuery) -> list[RetrievalResult]:
        """Hybrid search: Cypher + optional vector similarity."""
        graph = self._graph()
        if not graph:
            return []

        t0 = time.monotonic()
        try:
            # Cypher-based text search over document nodes
            cypher = (
                f"MATCH (d:Document) "
                f"WHERE d.text CONTAINS $text "
                f"RETURN d.text AS text, d.source AS source, d.id AS id "
                f"LIMIT {query.max_results}"
            )
            result = graph.query(cypher, params={"text": query.text})

            docs = []
            for record in result.result_set:
                docs.append(
                    RetrievalResult(
                        score=1.0,
                        payload={"source": record[1] or ""},
                        chunk_id=record[2] or "",
                        source_file=record[1] or "",
                        text=record[0] or "",
                    )
                )

            elapsed = (time.monotonic() - t0) * 1000
            logger.info(
                "[falkordb] search returned {} results in {:.0f}ms",
                len(docs),
                elapsed,
            )
            return docs
        except Exception as exc:
            logger.error("[falkordb] search failed: {}", exc)
            return []

    async def index(self, documents: list[dict]) -> int:
        """Index documents as graph nodes with text property."""
        graph = self._graph()
        if not graph:
            return 0

        count = 0
        try:
            for doc in documents:
                text = doc.get("text") or doc.get("content", "")
                source = doc.get("source") or doc.get("path", "unknown")
                doc_id = doc.get("id") or hashlib.md5(text.encode()).hexdigest()

                cypher = (
                    "MERGE (d:Document {id: $id}) "
                    "SET d.text = $text, d.source = $source "
                    "RETURN d"
                )
                graph.query(
                    cypher, params={"id": doc_id, "text": text, "source": source}
                )
                count += 1

            logger.info("[falkordb] indexed {}/{} documents", count, len(documents))
            return count
        except Exception as exc:
            logger.error("[falkordb] index failed: {}", exc)
            return count

    async def count(self, collection: str = "kaos") -> int:
        """Count document nodes in the graph."""
        graph = self._graph()
        if not graph:
            return 0

        try:
            result = graph.query("MATCH (d:Document) RETURN count(d) AS cnt")
            if result.result_set:
                return result.result_set[0][0]
        except Exception as exc:
            logger.warning("[falkordb] count failed: {}", exc)
        return 0

    async def health(self) -> bool:
        if not self._enabled:
            return False
        try:
            client = self._connect()
            return client is not None
        except Exception:
            return False
