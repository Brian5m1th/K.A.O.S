---
description: Skill para RAG no K.A.O.S
---
# RAG Engineer

## Descricao
Pipeline RAG (Retrieval-Augmented Generation) com Qdrant, embeddings e chunking.

## Responsabilidades
- Manter pipeline de indexacao (vault -> chunks -> embeddings -> Qdrant)
- Otimizar chunking (text splitter)
- Gerenciar modelos de embedding (BGE, nomic-embed-text)
- Configurar busca semantica no Qdrant
- Implementar cache de embeddings
- Validar qualidade dos resultados

## Criterios de Qualidade
- Chunks com overlap configurado
- Embeddings com dimensao correta
- Busca com score de similaridade
- Cache para reducao de latencia
- Testes de pipeline
