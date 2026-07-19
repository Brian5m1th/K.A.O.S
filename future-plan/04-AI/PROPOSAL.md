# AI Epic - PROPOSAL: Cognitive Router & Fallback Chain

## 1. Intent Classifier Execution

We propose placing a lightweight classification stage before prompt execution.

- **Objective:** Detect whether a prompt requires a cloud model (SMART) or can be processed by a local model (FAST).
- **SMART triggers:** Requests for system edits, refactoring plans, architecture audits, code reviews.
- **FAST triggers:** Conversational chitchat, simple definitions, tool queries, note checks.

---

## 2. Circuit Breaker Middleware

Implement stateful circuit breakers for APIs:

```python
class AICircuitBreaker:
    def __init__(self, failure_threshold=3, cooldown_seconds=180):
        self.state = "CLOSED"  # CLOSED, OPEN, HALF-OPEN
        self.failures = 0
        self.failure_threshold = failure_threshold
        self.cooldown_seconds = cooldown_seconds
        self.last_failure_time = None

    async def execute(self, model_call, *args, **kwargs):
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.cooldown_seconds:
                self.state = "HALF-OPEN"
            else:
                # Redirect to local fallback immediately
                return await local_fallback_call(*args, **kwargs)
```
