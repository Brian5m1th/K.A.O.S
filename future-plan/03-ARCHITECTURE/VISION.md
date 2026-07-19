# ARCHITECTURE Epic - VISION: Capability-Driven System Architecture

## 1. Core Architectural Pillars

The architectural goal of the K.A.O.S Cognitive OS is to transition from a technical layered structure (API ➔ Service ➔ Database) to a **Capability-Driven Domain Architecture**.

This shift enforces the following key principles:
1. **Domain Independence:** Every capability (Think, Remember, Observe, Act, etc.) is a self-contained module containing its own API routes, database schemas, background workers, and automated tests.
2. **Loosely Coupled Event Bus:** Domain modules communicate primarily by publishing and subscribing to events asynchronously, avoiding synchronous imports or direct HTTP calls between internal services.
3. **Dynamic Autodiscovery (Manifest-Driven):** Capabilities declare their routes, schemas, and tools via a `manifest.yaml`. At boot, the main server parses these manifests and registers routes and tools dynamically.
4. **Boundary Abstraction:** Interfaces (CLI, Tauri UI, Voice APIs) and infrastructure drivers (Ollama, Qdrant, WhatsApp API) are decoupled boundaries. The business logic depends on interface ports, not physical drivers.
