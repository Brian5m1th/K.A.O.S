# AI Epic - VISION: Cognitive Abstractions & Route Fallbacks

## 1. Core Vision

The K.A.O.S AI Engine shifts from a single model provider to a fully abstract **Cognitive Router** that selects and executes tasks based on capability requirements, pricing limits, and local/cloud availability. 

### Core AI Principles:
1. **Fallback Chains:** Default to local models (e.g. Qwen, Llama via Ollama/AirLLM) for fast, free execution. Automatically fallback to cloud providers (OpenAI, Gemini, Anthropic) if local constraints fail.
2. **Dynamic Model Profiles:** Models are categorized by capability:
  - **Fast (Local):** Quick completions, simple chat, initial reasoning (e.g. Qwen 7B).
  - **Smart (Cloud/Local Heavy):** Complex agent planning, architectural audit, deep reflection (e.g. Claude 3.5 Sonnet, Llama 70B).
  - **Vision:** Image analysis, mockup processing.
3. **API-Independence:** Capabilities call standard reasoning interfaces (Ports); provider drivers handle the API translations.
