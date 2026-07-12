"""
Neo4jAdapter — GraphPort implementation backed by Neo4j with Cypher.

Enables property graph queries over code structure using Cypher,
storing nodes (classes, functions, modules) and relationships
(calls, imports, contains).

Requires: pip install neo4j
Env: NEO4J_URI=bolt://localhost:7687
     NEO4J_USER=neo4j
     NEO4J_PASSWORD=password
"""

import time
from typing import Optional

from loguru import logger

from app.domain.ports.graph_port import (
    GraphPort,
    NodeInfo,
    PathInfo,
    GraphQuery,
    GraphResult,
)
from app.config.settings import settings

try:
    from neo4j import GraphDatabase, AsyncGraphDatabase
    from neo4j.exceptions import ServiceUnavailable

    HAS_NEO4J = True
except ImportError:
    HAS_NEO4J = False
    GraphDatabase = None  # type: ignore
    ServiceUnavailable = Exception


class Neo4jAdapter(GraphPort):
    """GraphPort adapter using Neo4j with Cypher queries."""

    def __init__(self) -> None:
        self._driver = None
        self._uri = settings.get("NEO4J_URI", "bolt://localhost:7687")
        self._user = settings.get("NEO4J_USER", "neo4j")
        self._password = settings.get("NEO4J_PASSWORD", "password")
        self._enabled = HAS_NEO4J

    async def _connect(self):
        if self._driver is None and self._enabled:
            try:
                self._driver = AsyncGraphDatabase.driver(
                    self._uri,
                    auth=(self._user, self._password),
                )
                # Verify connectivity
                async with self._driver.session() as session:
                    await session.run("RETURN 1")
                logger.info("[neo4j] connected to {}", self._uri)
            except Exception as exc:
                logger.warning("[neo4j] connection failed: {}", exc)
                self._enabled = False
        return self._driver

    @property
    def provider_name(self) -> str:
        return "neo4j"

    async def explain(self, concept: str) -> Optional[NodeInfo]:
        """Find a code symbol and its connections."""
        driver = await self._connect()
        if not driver:
            return None

        try:
            async with driver.session() as session:
                result = await session.run(
                    """
                    MATCH (n:Symbol)
                    WHERE n.name CONTAINS $concept OR n.id CONTAINS $concept
                    OPTIONAL MATCH (n)-[r]-(connected)
                    RETURN n, count(DISTINCT connected) AS degree,
                           collect(DISTINCT {rel: type(r), target: connected.name}) AS conns
                    LIMIT 1
                    """,
                    concept=concept,
                )
                record = await result.single()
                if not record:
                    return None

                n = record["n"]
                return NodeInfo(
                    id=n.get("id", n.get("name", concept)),
                    label=n.get("name", concept),
                    source_file=n.get("file", ""),
                    type=n.get("type", "code"),
                    degree=record["degree"],
                    connections=[
                        {"relation": c["rel"], "target": c["target"]}
                        for c in record["conns"]
                    ],
                )
        except Exception as exc:
            logger.error("[neo4j] explain failed: {}", exc)
            return None

    async def path(self, source: str, target: str) -> Optional[PathInfo]:
        """Find shortest dependency path between two symbols."""
        driver = await self._connect()
        if not driver:
            return None

        try:
            async with driver.session() as session:
                result = await session.run(
                    """
                    MATCH p = shortestPath(
                        (a:Symbol {name: $source})-[*..10]-(b:Symbol {name: $target})
                    )
                    RETURN p,
                           length(p) AS hops,
                           [n IN nodes(p) | n.name] AS path_nodes
                    """,
                    source=source,
                    target=target,
                )
                record = await result.single()
                if not record:
                    return None

                return PathInfo(
                    source=source,
                    target=target,
                    hops=record["hops"],
                    path=record["path_nodes"],
                    description=f"Path from {source} to {target} ({record['hops']} hops)",
                )
        except Exception as exc:
            logger.error("[neo4j] path failed: {}", exc)
            return None

    async def query(self, query: GraphQuery) -> GraphResult:
        """Execute a neighborhood search from matching nodes."""
        driver = await self._connect()
        if not driver:
            return GraphResult()

        t0 = time.monotonic()
        try:
            async with driver.session() as session:
                result = await session.run(
                    """
                    MATCH (n:Symbol)
                    WHERE n.name CONTAINS $text OR n.id CONTAINS $text
                    OPTIONAL MATCH (n)-[r]-(neighbor)
                    WITH n, collect(DISTINCT neighbor) AS neighbors
                    RETURN n, size(neighbors) AS degree
                    LIMIT $max_results
                    """,
                    text=query.text,
                    max_results=query.max_results,
                )
                records = await result.fetch(query.max_results)
                nodes = [
                    NodeInfo(
                        id=rec["n"].get("id", rec["n"].get("name", "")),
                        label=rec["n"].get("name", ""),
                        source_file=rec["n"].get("file", ""),
                        type=rec["n"].get("type", "code"),
                        degree=rec["degree"],
                    )
                    for rec in records
                ]

                elapsed = (time.monotonic() - t0) * 1000
                return GraphResult(
                    nodes=nodes,
                    total_found=len(nodes),
                    query_time_ms=elapsed,
                )
        except Exception as exc:
            logger.error("[neo4j] query failed: {}", exc)
            return GraphResult()

    async def health(self) -> bool:
        if not self._enabled:
            return False
        driver = await self._connect()
        if not driver:
            return False
        try:
            async with driver.session() as session:
                await session.run("RETURN 1")
            return True
        except Exception:
            return False
