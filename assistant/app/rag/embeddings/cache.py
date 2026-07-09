import sqlite3
import hashlib
import json
from pathlib import Path


class EmbeddingCache:
    def __init__(self, db_path: str = "data/chunk_embeddings.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("PRAGMA journal_mode=WAL")
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS chunk_embeddings (
                        text_hash TEXT PRIMARY KEY,
                        model TEXT NOT NULL,
                        vector_json TEXT NOT NULL
                    )
                """)
                conn.execute(
                    "CREATE INDEX IF NOT EXISTS idx_model ON chunk_embeddings(model)"
                )
        except Exception:
            pass

    def _hash(self, text: str) -> str:
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    def get(self, text: str, model: str) -> list[float] | None:
        h = self._hash(text)
        try:
            with sqlite3.connect(self.db_path) as conn:
                row = conn.execute(
                    "SELECT vector_json FROM chunk_embeddings WHERE text_hash=? AND model=?",
                    (h, model),
                ).fetchone()
                if row:
                    return json.loads(row[0])
        except Exception:
            pass
        return None

    def set(self, text: str, model: str, vector: list[float]) -> None:
        h = self._hash(text)
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute(
                    """
                    INSERT OR REPLACE INTO chunk_embeddings (text_hash, model, vector_json)
                    VALUES (?, ?, ?)
                """,
                    (h, model, json.dumps(vector)),
                )
        except Exception:
            pass
