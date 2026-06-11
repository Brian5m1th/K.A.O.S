from pydantic import BaseModel, Field
from datetime import datetime


class NoteCreateRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    folder: str = Field(default="Inbox")
    content: str = Field(..., min_length=1)


class NoteUpdateRequest(BaseModel):
    path: str = Field(..., description="Caminho relativo à raiz do Vault")
    content: str
    mode: str = Field(default="overwrite", pattern="^(overwrite|append)$")


class NoteResponse(BaseModel):
    status: str
    path: str


class NoteReadResult(BaseModel):
    path: str
    content: str
    last_modified: datetime


class SearchResult(BaseModel):
    path: str
    score: float = 1.0
    excerpt: str


class SearchResponse(BaseModel):
    query: str
    total: int
    documents: list[SearchResult]
