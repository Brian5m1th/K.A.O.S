import hashlib
from pathlib import Path

from loguru import logger
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    FieldCondition,
    Filter,
    MatchValue,
    PointStruct,
    VectorParams,
)

from app.config.settings import settings
from app.rag.chunking.text_splitter import MarkdownSplitter
from app.rag.embeddings.embedder import Embedder


class VaultIndexer:
    COLLECTION = settings.QDRANT_COLLECTION

    def __init__(self) -> None:
        self._client = QdrantClient(
            host=settings.QDRANT_HOST, port=settings.QDRANT_PORT
        )
        self._embedder = Embedder(model_key="bge-m3")
        self._splitter = MarkdownSplitter()
        self._ensure_collection()

    def _ensure_collection(self) -> None:
        existing = [c.name for c in self._client.get_collections().collections]
        if self.COLLECTION not in existing:
            self._client.create_collection(
                collection_name=self.COLLECTION,
                vectors_config=VectorParams(
                    size=self._embedder.dimension, distance=Distance.COSINE
                ),
            )
            logger.info(f"Coleção '{self.COLLECTION}' criada no Qdrant.")

    def _make_point_id(self, path: str, chunk_index: int) -> str:
        return hashlib.md5(f"{path}::{chunk_index}".encode()).hexdigest()

    def index_file(self, file_path: str) -> int:
        path = Path(file_path)
        if not path.exists() or not path.suffix == ".md":
            return 0

        content = path.read_text(encoding="utf-8")
        vault_path = Path(settings.OBSIDIAN_VAULT_PATH)
        relative = str(path.relative_to(vault_path))
        folder = (
            str(path.parent.relative_to(vault_path))
            if path.parent != vault_path
            else ""
        )

        self.remove_file(relative)

        chunks = self._splitter.split(content, source_path=relative)
        if not chunks:
            return 0

        texts = [c.content for c in chunks]
        vectors = self._embedder.embed(texts)

        points = [
            PointStruct(
                id=self._make_point_id(relative, chunk.chunk_index),
                vector=vector,
                payload={
                    "path": relative,
                    "folder": folder,
                    "chunk_index": chunk.chunk_index,
                    "content": chunk.content,
                    "file_name": path.stem,
                },
            )
            for chunk, vector in zip(chunks, vectors)
        ]

        self._client.upsert(collection_name=self.COLLECTION, points=points)
        logger.info(f"Indexado: {relative} ({len(points)} chunks)")
        return len(points)

    def remove_file(self, relative_path: str) -> None:
        self._client.delete(
            collection_name=self.COLLECTION,
            points_selector=Filter(
                must=[
                    FieldCondition(
                        key="path", match=MatchValue(value=relative_path)
                    )
                ]
            ),
        )

    def index_vault(self) -> dict:
        vault = Path(settings.OBSIDIAN_VAULT_PATH)
        total_files = 0
        total_chunks = 0
        for md_file in vault.rglob("*.md"):
            if not md_file.name.startswith("."):
                total_chunks += self.index_file(str(md_file))
                total_files += 1
        logger.info(
            f"Indexação completa: {total_files} arquivos, {total_chunks} chunks"
        )
        return {"files": total_files, "chunks": total_chunks}
