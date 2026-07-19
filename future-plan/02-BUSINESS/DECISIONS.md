# BUSINESS Epic - DECISIONS: Commercial Licensing ADRs

This document logs commercial and licensing decisions for K.A.O.S.

---

## 1. ADR-BUS-001: Open Source Licensing Strategy

### Context
K.A.O.S relies heavily on the open-source community (Ollama, Qdrant, LangGraph, Tauri). We need to select a license that encourages adoption and transparency while preventing competing SaaS services from stripping K.A.O.S features and offering them under closed platforms.

### Decision
Apply a **Dual-Licensing Model**:
- **Community Edition:** GNU GPLv3.
- **Enterprise Edition:** Commercial Proprietary License (permits closed integration, compliance dashboards, and customized services).

### Consequences
- Protects the project from being repackaged directly by cloud providers without contributing code back.
- Allows clear monetization pathways for enterprise sales.

---

## 2. ADR-BUS-002: End-to-End Encryption (E2EE) for Sync

### Context
Charging for cloud backup means we must manage user databases. If we store the user's "Personal Digital Twin" (which contains sensitive notes, code snippets, calendar events, and credentials) in plaintext on our servers, we create a massive security risk and run into LGPD/GDPR compliance issues.

### Decision
Implement E2EE for all syncing features. The encryption key is derived from the user's password locally and is never sent to the K.A.O.S auth servers.

### Consequences
- Reduces security liability.
- Minimizes compliance audit costs.
- Prevents K.A.O.S from analyzing user data on the sync servers, reinforcing the "Privacy First" principle.
