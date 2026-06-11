import pytest
from app.rag.chunking.text_splitter import MarkdownSplitter, TextChunk


class TestMarkdownSplitter:
    def test_split_simple_text(self) -> None:
        splitter = MarkdownSplitter(chunk_size=800, overlap=150)
        chunks = splitter.split("# Titulo\n\nConteudo simples.", "nota.md")
        assert len(chunks) == 1
        assert chunks[0].source_path == "nota.md"
        assert chunks[0].chunk_index == 0

    def test_split_preserves_sections(self) -> None:
        splitter = MarkdownSplitter(chunk_size=800, overlap=150)
        text = "# Secao 1\n\nConteudo 1\n\n## Secao 2\n\nConteudo 2"
        chunks = splitter.split(text, "nota.md")
        assert len(chunks) >= 2

    def test_chunk_index_increments(self) -> None:
        splitter = MarkdownSplitter(chunk_size=50, overlap=10)
        text = "# Secao\n\n" + "\n\n".join([f"Paragrafo {i}" for i in range(20)])
        chunks = splitter.split(text, "nota.md")
        for i, chunk in enumerate(chunks):
            assert chunk.chunk_index == i

    def test_empty_text_returns_empty(self) -> None:
        splitter = MarkdownSplitter()
        chunks = splitter.split("", "nota.md")
        assert chunks == []

    def test_chunk_size_boundary(self) -> None:
        splitter = MarkdownSplitter(chunk_size=100, overlap=20)
        text = "# Grande\n\n" + "A" * 250
        chunks = splitter.split(text, "nota.md")
        assert len(chunks) > 1
        assert all(len(c.content) <= 280 for c in chunks)

    def test_single_paragraph_fits_in_chunk(self) -> None:
        splitter = MarkdownSplitter(chunk_size=500, overlap=100)
        text = "# Secao\n\n" + "B" * 300
        chunks = splitter.split(text, "nota.md")
        assert len(chunks) == 1

    def test_overlap_between_chunks(self) -> None:
        splitter = MarkdownSplitter(chunk_size=100, overlap=30)
        text = "# Secao\n\n" + "\n\n".join(["C" * 60 for _ in range(10)])
        chunks = splitter.split(text, "nota.md")
        assert len(chunks) > 1
        for i in range(1, len(chunks)):
            assert chunks[i].chunk_index == i
