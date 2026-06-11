import re
from dataclasses import dataclass
from loguru import logger


@dataclass
class TextChunk:
    content: str
    chunk_index: int
    source_path: str


class MarkdownSplitter:
    def __init__(self, chunk_size: int = 800, overlap: int = 150) -> None:
        logger.info("[start] MarkdownSplitter - __init__")
        self._chunk_size = chunk_size
        self._overlap = overlap
        logger.debug("[finish] MarkdownSplitter - __init__")

    def split(self, text: str, source_path: str) -> list[TextChunk]:
        logger.info("[start] MarkdownSplitter - split")
        sections = re.split(r"\n(?=#{1,3} )", text)
        chunks: list[TextChunk] = []
        index = 0

        for section in sections:
            section = section.strip()
            if not section:
                continue

            if len(section) <= self._chunk_size:
                chunks.append(
                    TextChunk(
                        content=section,
                        chunk_index=index,
                        source_path=source_path,
                    )
                )
                index += 1
            else:
                paragraphs = section.split("\n\n")
                buffer = ""
                for para in paragraphs:
                    if len(buffer) + len(para) > self._chunk_size and buffer:
                        chunks.append(
                            TextChunk(
                                content=buffer.strip(),
                                chunk_index=index,
                                source_path=source_path,
                            )
                        )
                        index += 1
                        buffer = buffer[-self._overlap :] + "\n\n" + para
                    else:
                        buffer += "\n\n" + para if buffer else para
                if buffer.strip():
                    chunks.append(
                        TextChunk(
                            content=buffer.strip(),
                            chunk_index=index,
                            source_path=source_path,
                        )
                    )
                    index += 1

        logger.info(f"[info] MarkdownSplitter - {len(chunks)} chunks de {source_path}")
        logger.debug("[finish] MarkdownSplitter - split")
        return chunks
