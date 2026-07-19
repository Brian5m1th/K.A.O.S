# AI Epic - CURRENT STATE: Static Provider Mapping

## 1. Existing System Setup

- **Model selection:** Driven by simple if/else logic on environment configuration (`OLLAMA_MODEL`, `OPENAI_API_KEY`).
- **File location:** Logic is contained in `assistant/app/providers/llm.py` and `assistant/app/api/chat.py`.
- **Fallback system:** Statically coded to retry OpenAI endpoints, defaulting to Ollama if an API exception is thrown. No stateful circuit-breakers or automated dead letter queues are implemented.
- **Routing:** No dynamic Intent Classifier exists. All prompts run through the same model selected in settings.
