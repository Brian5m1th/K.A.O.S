# RISKS Epic - DECISIONS: Security Standards

This document records the security design decisions for the platform.

---

## 1. ADR-RISK-001: Keyring API Selection

### Context
Plaintext keys in `.env` are vulnerable. We need a secure OS-level storage alternative.

### Decision
Integrate Python's `keyring` library, falling back to an AES-256-GCM encrypted file stored under the user's home profile (`~/.kaos/secrets.enc`) if the OS keyring service fails or is blocked by permissions.

### Consequences
- Secures OpenAI and Anthropic cloud credentials natively.
- Fallback ensures local compilation runs fine on restricted Linux environments or inside Docker containers.

---

## 2. ADR-RISK-002: Command Whitelist vs Blacklist

### Context
Preventing destructive shell commands is critical, but blacklists are notoriously easy to bypass (e.g. using base64 obfuscation or file system links).

### Decision
Implement a **Hybrid Verification Model**:
- Maintain a strict blacklist of destructive words (e.g. `rm`, `Diskpart`, `del`) for immediate termination.
- For all other shell tools, prompt the user for permission in the Tauri UI, displaying the command line string exactly as it will run.

### Consequences
- Guarantees 100% protection against silent destructive operations.
- Moderately increases prompt friction, which is acceptable for security.
