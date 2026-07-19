# MEMORY Epic - CURRENT STATE: Raw Conversational Logs

## 1. Existing System Setup

- **Chat Logs:** Stored in PostgreSQL using standard relational schemas containing `session_id`, `message_role`, and `message_content`.
- **Note Memory:** Processed via text chunking and saved to a Qdrant collection called `obsidian_memory`.
- **State files:** Config settings are saved in a plaintext JSON config file.
- **Lacks Integration:** There is no cross-linking between chat logs and notes in vector storage. The system cannot recall what the user's role is, what active projects exist, or what tools were executed yesterday unless specified in the active prompt.
