# MEMORY Epic - RISKS: Data & Sync Risks

This document maps data integrity and sync security risks.

---

## 1. Risk Register

- **R-MEM-01: Irrecoverable Key Loss**
  - *Description:* Since sync uses strict end-to-end encryption (E2EE), if the user loses their recovery passphrase, they cannot decrypt their digital twin backups.
  - *Impact:* Critical.
  - *Mitigation:* Require double validation of passphrases on creation. Generate a printed "paper recovery key" (like cryptocurrency wallets).

- **R-MEM-02: Vector Storage Size Bloat**
  - *Description:* Continuous note indexing and episodic summarization can bloat the local vector database, consuming gigabytes of disk space.
  - *Impact:* Medium.
  - *Mitigation:* Implement memory pruning rules. Delete episodic logs older than 90 days, keeping only consolidated summaries.
