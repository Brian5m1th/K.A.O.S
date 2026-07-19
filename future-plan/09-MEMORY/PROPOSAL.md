# MEMORY Epic - PROPOSAL: Humanized Memory Integration

## 1. User Profile & Preferences Schemas

We propose adding a **Digital Twin Profile** table inside PostgreSQL:

```sql
CREATE TABLE user_identity (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    role VARCHAR(255),
    bio TEXT,
    preferences JSONB, -- stores layout choices, active models
    people JSONB,      -- lists close collaborators, email targets
    projects JSONB     -- tracks directories, repository links
);
```

---

## 2. Asynchronous Memory Consolidator

When a conversation is inactive for > 15 minutes:
1. Trigger a background process that extracts message logs.
2. Prompts the local FAST model: *"Extract key decisions, preferences, and facts about the user from this chat conversation."*
3. Formulates a list of bullet points.
4. Performs an upsert directly into the `user_identity` profile table and registers semantic vectors in Qdrant.
5. Empties the SQL chat logs table, keeping only a summarized "memory hook" in active context.
