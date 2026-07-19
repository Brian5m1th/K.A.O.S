# RISKS Epic - GAPS: Safety and Compliance Gaps

The following risk-related features are missing from the current architecture:

| Gap | Impact | Difficulty | Priority |
| :--- | :--- | :--- | :--- |
| **Plaintext .env keys** | High | Medium | **Critical** (Transition to OS Keychain). |
| **Direct Shell Access** | High | High | **Critical** (Sandbox tool runs). |
| **No Cost Interrupter** | High | Low | High (Write budget validation middleware). |
| **Unthrottled CPU Usage**| Medium | Medium | Medium (Add resource hooks in Guardian). |
| **No User Permission Dialog**| High | Low | High (Expose execution verification alerts). |
