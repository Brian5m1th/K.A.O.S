# AI Epic - DECISIONS: AI Engine Decisions

This document logs critical choices made for the AI reasoning engine.

---

## 1. ADR-AI-001: Local vs Cloud Intent Classification

### Context
If we classify intents using cloud APIs (e.g. GPT-4o), we pay token costs and add latency to every single interaction. If we run classification locally, we need a lightweight, fast method.

### Decision
Classify intent locally using a semantic similarity matrix (comparing input embeddings against standard trigger sentences in Qdrant/local cache) or a very fast local model (e.g., Qwen-1.5B) run in a single-turn completion.

### Consequences
- Zero cloud cost for classification.
- TTFT (Time to First Token) classification step remains under 80ms.

---

## 2. ADR-AI-002: Provider-Specific SDK Abstraction

### Context
Decoupling provider APIs means we cannot use provider-specific libraries (like `google-generativeai` or `anthropic`) directly in services.

### Decision
Write custom wrapper adapters using standard HTTP clients (e.g. `httpx` async) to interface with the REST endpoints of cloud providers.

### Consequences
- Eliminates dependency on multiple external SDK packages.
- Simplifies updating adapters when provider endpoints change.
