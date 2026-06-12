Source: Antigravity AI
Tags: #sdd #python #rag #qdrant #embeddings #watchdog #fase4 #fase5 #fase6
Related: [[index]] [[backlog]] [[sdd_fase3_obsidian_service]] [[sdd_obsidian_rag]] [[sdd_obsidian_watcher]] [[sdd_fase5_watcher_langgraph]]

# SDD — Fases 4 e 5: RAG Pipeline + Atualização Automática

## Objetivo

Transformar o Vault Obsidian em um banco de conhecimento semântico consultável. A IA recupera contexto relevante das notas antes de gerar respostas. O `watchdog` mantém o índice vetorial sincronizado automaticamente com qualquer alteração no Vault.

---

## Critério de Sucesso

> O usuário faz uma pergunta sobre um tema que está em uma nota do Vault. A IA responde usando informações da nota sem que a nota tenha sido citada explicitamente na conversa. Ao editar a nota e perguntar novamente, a resposta reflete o conteúdo atualizado.

---

## Status Atual: ✅ CONCLUÍDO (Fases 4-5 + Otimizações)

| Componente | Status | Detalhes |
|------------|--------|----------|
| Qdrant | ✅ | Coleção `obsidian_memory`, COSINE distance, 1024-dim |
| Embedder BGE-M3 | ✅ | `BAAI/bge-m3` (1024-dim), **Singleton** via `get_embedder()` |
| Chunking | ✅ | `MarkdownSplitter` (800 chars, 150 overlap, header-aware) |
| Indexer | ✅ | `VaultIndexer` upsert com ID determinístico (MD5 path+index) |
| Retriever | ✅ | `SemanticRetriever` com `score_threshold=0.3`, folder filter |
| Watcher | ✅ | `VaultWatcher` (watchdog) auto-reindex create/modify/delete/move |
| **Diagnostics** | ✅ | Logs: query, vector_size, scores, paths, payload keys |
| **Warmup** | ✅ | `warmup_embedder()` no lifespan do FastAPI |

---

## Tarefas — Fase 4 (RAG) ✅

- [x] Subir Qdrant via Docker Compose
- [x] Configurar modelo de embeddings (`BAAI/bge-m3`)
- [x] Implementar chunking de documentos (`app/rag/chunking/`)
- [x] Indexar todas as notas existentes (indexação inicial)
- [x] Criar retriever semântico (`app/rag/retriever/`)
- [x] Testar consultas contextuais

## Tarefas — Fase 5 (Atualização Automática) ✅

- [x] Adicionar `watchdog` como dependência
- [x] Detectar eventos de `CREATE`, `MODIFY` e `DELETE`
- [x] Disparar reindexação automática no Qdrant

## Tarefas — Otimizações (Fase 8) ✅

- [x] **Singleton Embedder** — `get_embedder()` evita múltiplas instâncias
- [x] **Score Threshold** — `settings.RAG_SCORE_THRESHOLD=0.3` no `query_points`
- [x] **Logs de Diagnóstico** — Query, vector_size, scores, paths, payload keys
- [x] **Folder Filter** — Validação strip/empty, ignora se vazio
- [x] **Warmup Embedder** — Carregamento antecipado no startup

---

## 1. Estrutura de Módulos

```text
app/
├── rag/
│   ├── __init__.py
│   ├── embeddings/
│   │   └── embedder.py         # Geração de vetores (Sentence Transformers)
│   ├── chunking/
│   │   └── text_splitter.py    # Divisão de Markdown em chunks
│   ├── retriever/
│   │   └── semantic_retriever.py  # Busca no Qdrant por similaridade
│   └── indexer/
│       └── vault_indexer.py    # Orquestra leitura + chunk + embed + upsert
└── obsidian/
    └── watcher/
        └── vault_watcher.py    # Watchdog + disparo de reindexação
```

---

## 2. Embedder (`rag/embeddings/embedder.py`)

```python
from sentence_transformers import SentenceTransformer
from loguru import logger
from app.config.settings import settings

_embedder_instance: "Embedder | None" = None


class Embedder:
    """Gera embeddings de texto usando Sentence Transformers (local, offline)."""

    MODEL_CONFIGS = {
        "bge-m3": {"name": "BAAI/bge-m3", "dim": 1024},
        "nomic": {"name": "nomic-ai/nomic-embed-text-v1.5", "dim": 768},
    }

    def __init__(self, model_key: str = "bge-m3") -> None:
        config = self.MODEL_CONFIGS[model_key]
        self._dim = config["dim"]
        logger.info(f"Carregando modelo de embedding: {config['name']}")
        self._model = SentenceTransformer(config["name"], trust_remote_code=True)

    @property
    def dimension(self) -> int:
        return self._dim

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Gera embeddings para uma lista de textos."""
        vectors = self._model.encode(texts, normalize_embeddings=True)
        return vectors.tolist()

    def embed_single(self, text: str) -> list[float]:
        return self.embed([text])[0]


def get_embedder(model_key: str = "bge-m3") -> Embedder:
    """Retorna instância singleton do Embedder (evita reloads caros)."""
    global _embedder_instance
    if _embedder_instance is None:
        _embedder_instance = Embedder(model_key)
    return _embedder_instance


def warmup_embedder(model_key: str = "bge-m3") -> None:
    """Pré-carrega o modelo para evitar cold start na primeira query."""
    embedder = get_embedder(model_key)
    logger.info("[info] Embedder - warmup")
    _ = embedder.embed_single("warmup")
    logger.debug("[finish] Embedder - warmup")
```

---

## 3. Text Splitter (`rag/chunking/text_splitter.py`)

Divisão preserva estrutura de cabeçalhos Markdown para manter o contexto semântico.

```python
import re
from dataclasses import dataclass

@dataclass
class TextChunk:
    content: str
    chunk_index: int
    source_path: str

class MarkdownSplitter:
    """Divide texto Markdown em chunks respeitando cabeçalhos e parágrafos."""

    def __init__(self, chunk_size: int = 800, overlap: int = 150) -> None:
        self._chunk_size = chunk_size
        self._overlap = overlap

    def split(self, text: str, source_path: str) -> list[TextChunk]:
        # Divide por seções de cabeçalho primeiro
        sections = re.split(r'\n(?=#{1,3} )', text)
        chunks: list[TextChunk] = []
        index = 0

        for section in sections:
            section = section.strip()
            if not section:
                continue

            # Se a seção cabe em um chunk, mantém inteira
            if len(section) <= self._chunk_size:
                chunks.append(TextChunk(content=section, chunk_index=index, source_path=source_path))
                index += 1
            else:
                # Quebra por parágrafos com overlap
                paragraphs = section.split("\n\n")
                buffer = ""
                for para in paragraphs:
                    if len(buffer) + len(para) > self._chunk_size and buffer:
                        chunks.append(TextChunk(content=buffer.strip(), chunk_index=index, source_path=source_path))
                        index += 1
                        # Mantém overlap do chunk anterior
                        buffer = buffer[-self._overlap:] + "\n\n" + para
                    else:
                        buffer += "\n\n" + para if buffer else para
                if buffer.strip():
                    chunks.append(TextChunk(content=buffer.strip(), chunk_index=index, source_path=source_path))
                    index += 1

        return chunks
```

---

## 4. Vault Indexer (`rag/indexer/vault_indexer.py`)

Orquestra o pipeline completo: ler arquivo → chunk → embed → upsert no Qdrant.

```python
import hashlib
from pathlib import Path
from loguru import logger
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance, Filter, FieldCondition, MatchValue
from app.rag.embeddings.embedder import Embedder
from app.rag.chunking.text_splitter import MarkdownSplitter
from app.config.settings import settings

class VaultIndexer:
    COLLECTION = settings.QDRANT_COLLECTION

    def __init__(self) -> None:
        self._client = QdrantClient(host=settings.QDRANT_HOST, port=settings.QDRANT_PORT)
        self._embedder = Embedder(model_key="bge-m3")
        self._splitter = MarkdownSplitter()
        self._ensure_collection()

    def _ensure_collection(self) -> None:
        """Cria a coleção no Qdrant se ainda não existir."""
        existing = [c.name for c in self._client.get_collections().collections]
        if self.COLLECTION not in existing:
            self._client.create_collection(
                collection_name=self.COLLECTION,
                vectors_config=VectorParams(size=self._embedder.dimension, distance=Distance.COSINE),
            )
            logger.info(f"Coleção '{self.COLLECTION}' criada no Qdrant.")

    def _make_point_id(self, path: str, chunk_index: int) -> str:
        """Gera ID determinístico para cada chunk a partir do caminho + índice."""
        return hashlib.md5(f"{path}::{chunk_index}".encode()).hexdigest()

    def index_file(self, file_path: str) -> int:
        """Indexa (ou reindexado) um arquivo Markdown. Retorna quantidade de chunks."""
        path = Path(file_path)
        if not path.exists() or not path.suffix == ".md":
            return 0

        content = path.read_text(encoding="utf-8")
        vault_path = Path(settings.OBSIDIAN_VAULT_PATH)
        relative = str(path.relative_to(vault_path))
        folder = str(path.parent.relative_to(vault_path)) if path.parent != vault_path else ""

        # Remove chunks antigos do arquivo para evitar duplicação
        self.remove_file(relative)

        # Gera novos chunks e embeddings
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
        """Remove todos os chunks de um arquivo do índice vetorial."""
        self._client.delete(
            collection_name=self.COLLECTION,
            points_selector=Filter(
                must=[FieldCondition(key="path", match=MatchValue(value=relative_path))]
            ),
        )

    def index_vault(self) -> dict:
        """Indexa todos os arquivos .md do Vault (indexação inicial)."""
        vault = Path(settings.OBSIDIAN_VAULT_PATH)
        total_files = 0
        total_chunks = 0
        for md_file in vault.rglob("*.md"):
            if not md_file.name.startswith("."):
                total_chunks += self.index_file(str(md_file))
                total_files += 1
        logger.info(f"Indexação completa: {total_files} arquivos, {total_chunks} chunks")
        return {"files": total_files, "chunks": total_chunks}
```

---

## 5. Semantic Retriever (`rag/retriever/semantic_retriever.py`)

```python
from loguru import logger
from qdrant_client import QdrantClient
from qdrant_client.models import FieldCondition, Filter, MatchValue
from app.config.settings import settings
from app.domain.document import SearchResult
from app.rag.embeddings.embedder import get_embedder


class SemanticRetriever:
    """Realiza busca por similaridade semântica no Qdrant com diagnósticos detalhados."""

    def __init__(self) -> None:
        logger.info("[start] SemanticRetriever - __init__")
        self._client = QdrantClient(
            host=settings.QDRANT_HOST, port=settings.QDRANT_PORT
        )
        self._embedder = get_embedder("bge-m3")
        logger.debug("[finish] SemanticRetriever - __init__")

    def search(
        self,
        query: str,
        limit: int = 5,
        folder_filter: str | None = None,
    ) -> list[SearchResult]:
        logger.info("[start] SemanticRetriever - search")
        logger.info(f"[info] SemanticRetriever - query='{query}' limit={limit} folder_filter='{folder_filter}'")
        
        try:
            query_vector = self._embedder.embed_single(query)
            logger.info(f"[info] SemanticRetriever - vector_size={len(query_vector)}")
        except Exception as e:
            logger.error(f"[error] SemanticRetriever - embed_single failed: {e}")
            raise

        search_filter = None
        if folder_filter and folder_filter.strip():
            logger.info(f"[info] SemanticRetriever - filtrando por pasta: {folder_filter}")
            search_filter = Filter(
                must=[
                    FieldCondition(
                        key="folder", match=MatchValue(value=folder_filter.strip())
                    )
                ]
            )
        else:
            logger.info("[info] SemanticRetriever - sem filtro de pasta")

        response = self._client.query_points(
            collection_name=settings.QDRANT_COLLECTION,
            query=query_vector,
            query_filter=search_filter,
            limit=limit,
            score_threshold=settings.RAG_SCORE_THRESHOLD,
            with_payload=True,
        )
        hits = response.points

        logger.info(f"[info] SemanticRetriever - raw_hits={len(hits)}")
        for i, hit in enumerate(hits[:3]):
            logger.info(
                f"[info] SemanticRetriever - hit[{i}] "
                f"score={hit.score:.4f} "
                f"path={hit.payload.get('path')} "
                f"keys={list(hit.payload.keys())}"
            )

        logger.info(f"[info] SemanticRetriever - {len(hits)} resultados")
        logger.debug("[finish] SemanticRetriever - search")
        return [
            SearchResult(
                path=hit.payload["path"],
                score=hit.score,
                excerpt=hit.payload["content"][:300],
            )
            for hit in hits
        ]
```

---

## 6. File Watcher (`obsidian/watcher/vault_watcher.py`)

```python
import asyncio
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent
from loguru import logger
from app.rag.indexer.vault_indexer import VaultIndexer
from app.config.settings import settings

class _VaultEventHandler(FileSystemEventHandler):
    def __init__(self, indexer: VaultIndexer) -> None:
        self._indexer = indexer
        self._debounce: dict[str, asyncio.Task] = {}

    def _is_markdown(self, path: str) -> bool:
        return path.endswith(".md") and not Path(path).name.startswith(".")

    def on_created(self, event: FileSystemEvent) -> None:
        if not event.is_directory and self._is_markdown(event.src_path):
            logger.debug(f"[Watcher] CREATE: {event.src_path}")
            self._indexer.index_file(event.src_path)

    def on_modified(self, event: FileSystemEvent) -> None:
        if not event.is_directory and self._is_markdown(event.src_path):
            logger.debug(f"[Watcher] MODIFY: {event.src_path}")
            self._indexer.index_file(event.src_path)

    def on_deleted(self, event: FileSystemEvent) -> None:
        if not event.is_directory and self._is_markdown(event.src_path):
            vault = Path(settings.OBSIDIAN_VAULT_PATH)
            relative = str(Path(event.src_path).relative_to(vault))
            logger.debug(f"[Watcher] DELETE: {relative}")
            self._indexer.remove_file(relative)

    def on_moved(self, event: FileSystemEvent) -> None:
        if not event.is_directory:
            vault = Path(settings.OBSIDIAN_VAULT_PATH)
            if self._is_markdown(str(event.src_path)):
                old_relative = str(Path(event.src_path).relative_to(vault))
                self._indexer.remove_file(old_relative)
            if self._is_markdown(str(event.dest_path)):
                self._indexer.index_file(str(event.dest_path))


class VaultWatcher:
    """Inicia o monitoramento do Vault e dispara reindexações automaticamente."""

    def __init__(self) -> None:
        self._indexer = VaultIndexer()
        self._observer = Observer()

    def start(self) -> None:
        handler = _VaultEventHandler(self._indexer)
        self._observer.schedule(handler, path=settings.OBSIDIAN_VAULT_PATH, recursive=True)
        self._observer.start()
        logger.info(f"VaultWatcher iniciado em: {settings.OBSIDIAN_VAULT_PATH}")

    def stop(self) -> None:
        self._observer.stop()
        self._observer.join()
        logger.info("VaultWatcher encerrado.")
```

### Integração no `main.py`

```python
# Em main.py — iniciar o watcher junto com a aplicação FastAPI
from app.obsidian.watcher.vault_watcher import VaultWatcher

watcher = VaultWatcher()

@app.on_event("startup")
async def startup_event() -> None:
    watcher.start()

@app.on_event("shutdown")
async def shutdown_event() -> None:
    watcher.stop()
```

---

## 7. Endpoint de Indexação Manual (`api/`)

```python
@router.post("/indexing/full")
async def full_reindex(indexer: VaultIndexer = Depends()) -> dict:
    """Dispara a reindexação completa do Vault via API."""
    return indexer.index_vault()
```

---

## Dependências Desta Fase

- [[sdd_fase3_obsidian_service]] — ObsidianService para leitura de arquivos

## Desbloqueia

- [[sdd_fase5_watcher_langgraph]] — O LangGraph usará o `SemanticRetriever` como primeira etapa do grafo
