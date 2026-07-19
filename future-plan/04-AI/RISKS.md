# AI Epic - RISKS: Model & Routing Risks

This document analyzes AI engine execution risks.

---

## 1. Risk Register

- **R-AI-01: Local Inference Performance Sluggishness**
  - *Description:* On machines without dedicated Nvidia GPUs, local models (Ollama running Qwen/Llama) can generate tokens at less than 5 tokens/second.
  - *Impact:* Critical. Renders the local fallback unusable for interactive chat.
  - *Mitigation:* Automatically direct to Cloud fallback if local speeds drop below 8 tokens/second, prompting the user with latency warnings.

- **R-AI-02: Intent Classification Misses**
  - *Description:* The local classifier mistakenly flags a complex code refactoring task as "FAST" (local), leading to poor output quality or code corruption.
  - *Impact:* High.
  - *Mitigation:* Allow the user to manually override the routing profiles (e.g., locking the current session to "SMART Cloud Only").
