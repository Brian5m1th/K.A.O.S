import sqlite3
import hashlib
import json
import time
from pathlib import Path


class DocumentEmbeddingCache:
    def __init__(
        self, db_path: str = "data/document_embeddings.db", ttl_days: int = 30
    ):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.ttl_seconds = ttl_days * 86400
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("PRAGMA journal_mode=WAL")
            conn.execute("""
                CREATE TABLE IF NOT EXISTS doc_embeddings (
                    file_hash TEXT PRIMARY KEY,
                    file_path TEXT NOT NULL,
                    model TEXT NOT NULL,
                    chunks_json TEXT NOT NULL,
                    created_at REAL NOT NULL
                )
            """)
            conn.execute(
                "CREATE INDEX IF NOT EXISTS idx_model ON doc_embeddings(model)"
            )

    def _file_hash(self, content: str) -> str:
        return hashlib.sha256(content.encode()).hexdigest()

    def get(self, file_path: str, content: str, model: str) -> list[dict] | None:
        h = self._file_hash(content)
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT chunks_json, created_at FROM doc_embeddings WHERE file_hash=? AND model=?",
                (h, model),
            ).fetchone()
            if row:
                chunks_json, created_at = row
                if time.time() - created_at > self.ttl_seconds:
                    return None
                return json.loads(chunks_json)
        return None

    def set(self, file_path: str, content: str, model: str, chunks: list[dict]) -> None:
        h = self._file_hash(content)
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO doc_embeddings (file_hash, file_path, model, chunks_json, created_at)
                VALUES (?, ?, ?, ?, ?)
            """,
                (h, file_path, model, json.dumps(chunks), time.time()),
            )

    def stats(self) -> dict:
        with sqlite3.connect(self.db_path) as conn:
            total = conn.execute("SELECT COUNT(*) FROM doc_embeddings").fetchone()[0]
            size_mb = self.db_path.stat().st_size / 1024 / 1024
            return {"entries": total, "size_mb": round(size_mb, 2)}
