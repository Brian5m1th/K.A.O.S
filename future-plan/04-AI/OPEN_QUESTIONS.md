# AI Epic - OPEN QUESTIONS: AI Architecture Questions

The following questions remain open:

---

## 1. Local Vision Models
- **Issue:** Image/UI parsing requires vision support (LLaVA/Qwen2-VL). Local vision inference is memory-heavy.
- **Options:**
  - **Cloud Only:** Vision tasks are restricted to OpenAI/Gemini APIs.
  - **Hybrid (Recommended):** If the host system has > 6GB VRAM, load a local LLaVA/Qwen-VL adapter; otherwise, default to cloud.

---

## 2. Dynamic Temperature Adjuster
- **Question:** Should K.A.O.S adjust generation temperature dynamically based on the current mental state?
- **Discussion:** In "Reflecting" and "Planning" states, a lower temperature (e.g. 0.1) is desired for strict logic adherence. In "Thinking" or "Listening" states, a higher temperature (e.g. 0.7) makes dialogue natural.
