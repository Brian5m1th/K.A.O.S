# RISKS Epic - RISKS: Risk Analysis Matrix

This document summarizes system-level execution risks for K.A.O.S.

---

## 1. Risk Register

| ID | Risk | Impact | Likelihood | Mitigation | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **R-01** | **API Cost Runway** | High | Medium | Implement Cost-Tracking Guard with hard budget limits. | Proposed |
| **R-02** | **Accidental File Erasure** | Critical | Low | Sandboxing shell runs to active workspace + confirmations. | Proposed |
| **R-03** | **Key Extraction** | Critical | Low | Migrate configurations from `.env` to OS-level Keyrings. | Proposed |
| **R-04** | **CPU Starvation** | Medium | Medium | Guardian checks system resource metrics before starting audits.| Proposed |
| **R-05** | **Model Hallucination** | Medium | High | Integrate Graphify/RAG verification gates inside reflections. | Proposed |
