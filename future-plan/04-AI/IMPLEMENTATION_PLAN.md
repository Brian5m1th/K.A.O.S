# AI Epic - IMPLEMENTATION PLAN: Routing Engine Rollout

This document schedules the AI routing refactoring.

---

## 1. Engine Milestones

```text
Phase 1: Abstract Adapters ──► Phase 2: Build Circuit Breaker ──► Phase 3: Classifier Run
(Decouple provider classes)    (Stateful fallback wrapper)        (Dynamic route classify)
```

### Phase 1: Abstract Adapters (Sprint 1)
- Refactor `app/providers/llm.py` into a ports/adapters architecture.
- Create `app/capabilities/chat/adapters/openai_adapter.py`, `ollama_adapter.py`, and `anthropic_adapter.py`.
- Run baseline unit tests to guarantee chat streaming works.

### Phase 2: Circuit Breakers (Sprint 2)
- Implement `app/core/ai/circuit_breaker.py`.
- Wrap model adapters inside the Circuit Breaker instance.
- Simulate API timeout failures and verify that the system redirects stream requests to Ollama immediately.

### Phase 3: Intent Classification (Sprint 3)
- Write the classifier prompt template or load a local semantic classifier (using embeddings).
- Intercept chat posts and route prompts to the designated adapter.
