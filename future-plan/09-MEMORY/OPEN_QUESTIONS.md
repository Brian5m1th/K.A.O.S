# MEMORY Epic - OPEN QUESTIONS: Memory Systems Issues

The following design decisions remain open:

---

## 1. Vector Database Synchronization
- **Issue:** Relational databases are easy to dump and sync. Vector indexes (like Qdrant storage folders) are binary-heavy and platform-specific.
- **Options:**
  - **Re-embed on target device:** Sync the raw text files (notes, profile logs) and recalculate vectors locally on the secondary device. (Recommended to save cloud bandwidth).
  - **Dump and transfer:** Export vectors to snapshot files and sync them via the relay.

---

## 2. Consolidation Target Model
- **Question:** Should we allow the FAST local model to handle memory consolidation, or force a SMART cloud model run to prevent losing nuance?
- **Discussion:** Local models sometimes hallucinate or ignore negative facts. Using a cloud run (e.g. Claude Haiku or Gemini Flash) costs fractions of a cent but guarantees high quality.
