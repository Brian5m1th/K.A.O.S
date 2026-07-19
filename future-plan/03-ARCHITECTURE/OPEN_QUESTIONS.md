# ARCHITECTURE Epic - OPEN QUESTIONS: System Architect Issues

The following technical design questions remain open:

---

## 1. Capability-Specific Database Migrations
- **Issue:** Traditional Alembic has one central `migrations/` folder. With capability-first packaging, it is better if database schemas and migration files live inside the capability itself (e.g., `app/capabilities/chat/migrations/`).
- **Discussion:** Alembic supports multiple database locations, but it makes running `alembic upgrade head` complex. We need to decide whether to maintain a single root migrations catalog or write a custom migration runner that gathers revisions from all capability subdirectories.

---

## 2. Event Bus Broker selection
- **Issue:** Should we keep the EventBus purely in-process (`asyncio`), or support external brokers (Redis/RabbitMQ) for users who run n8n or heavy automation?
- **Options:**
  - **In-process only:** Simple, zero-dependency.
  - **Pluggable Broker:** Abstract `EventBus` into a port, allowing a local `AsyncIOEventBus` driver for community tier, and a `RedisEventBus` driver for enterprise tiers. (Recommended).
