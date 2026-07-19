# AI Epic - ARCHITECTURE: Cognitive Model Router

## 1. Routing & Fallback Topology

The model routing engine decouples LLMs from application pipelines.

```text
              [Input Task]
                   │
                   ▼
         [Intent Classifier]  ──► Classifies task complexity (FAST/SMART)
                   │
                   ▼
         [Model Router API]
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
    [Local Port]        [Cloud Port]
    (Ollama / AirLLM)   (OpenAI / Gemini / Claude)
         │                   │
         └─────────┬─────────┘
                   ▼
     [Circuit Breaker Middleware] ──► Retries 3x, falls back from Cloud to Local
                   │
                   ▼
            [Inference Stream]
```

---

## 2. API Contracts

Every AI Adapter implements a common interface:

```python
class AICognitivePort(ABC):
    @abstractmethod
    async def generate_stream(
        self, 
        prompt: str, 
        history: list[Message], 
        temperature: float = 0.7
    ) -> AsyncGenerator[str, None]:
        pass

    @abstractmethod
    async def classify_intent(self, text: str) -> IntentClassification:
        pass
```
