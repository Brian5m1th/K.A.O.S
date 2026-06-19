# K.A.O.S Architecture Overview

The K.A.O.S system is a modular AI assistant built with FastAPI and LangGraph.
It uses RAG for knowledge retrieval and Ollama for LLM inference.

## Key Components

### FastAPI Backend
The main entry point is `main.py`, which sets up the FastAPI application,
registers routes (chat, health, indexing), and initializes middleware.

### LangGraph Agent
The agent graph orchestrates conversation flow through nodes:
- Intent classification
- Planning
- Retrieval (RAG)
- Tool execution
- Response synthesis

### RAG Pipeline
Documents are indexed via Qdrant vector store with embeddings from Ollama.
The retriever searches by semantic similarity and returns ranked results.

### Wiki Tools
Obsidian vault tools allow creating notes, entities, concepts, and sources.
The wiki-first approach prioritizes vault knowledge over raw vector search.

## Technologies
- Python 3.12
- FastAPI
- LangGraph
- Qdrant
- Ollama (deepseek-r1:14b)
- Obsidian vault
