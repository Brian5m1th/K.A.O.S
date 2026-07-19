# RISKS Epic - CURRENT STATE: Safety Audits

## 1. Vulnerability Analysis of Current Codebase

The current v2.x architecture exhibits three key risk areas:

### 1.1. Insecure Credential Management
- **Issue:** Sensitive API keys (OpenAI, Anthropic, WhatsApp) are stored in plaintext inside `assistant/.env`. Any process running under the user session can read this file.
- **Threat:** API key theft via malicious packages.

### 1.2. Unbounded Command Execution
- **Issue:** The LangGraph execution loop has direct access to run shell commands in the workspace directory.
- **Threat:** If an agent encounters a prompt injection or plans an incorrect path, it can delete codebase folders, overwrite config files, or corrupt project history.

### 1.3. No Cost Throttling
- **Issue:** While cost is tracked in Grafana, there is no physical system block. If an agent falls into a recursive error loop (e.g. attempting to fix a build error in a loop), it can exhaust API balances in minutes.
- **Threat:** Runaway cloud billing.
