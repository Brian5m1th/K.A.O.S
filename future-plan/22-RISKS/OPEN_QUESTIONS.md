# RISKS Epic - OPEN QUESTIONS: Security Issues

The following safety and compliance decisions remain open:

---

## 1. Native Windows Sandbox (WDAG) Integration
- **Issue:** To run generated Python or JS scripts, should K.A.O.S utilize Windows Sandbox or a lightweight Docker container for true isolation?
- **Trade-offs:**
  - **Docker:** Cross-platform (Windows/Linux/macOS), but requires Docker Desktop to be running, which consumes significant memory.
  - **Windows Sandbox:** Built-in to Windows Pro, lightweight, but not available on Windows Home or other operating systems, and has slower startup times.

---

## 2. Telemetry and Audit Exports
- **Question:** Should enterprise installations support auditing data exports to telemetry collectors (e.g. Jaeger or OpenTelemetry collectors in cloud)?
- **Discussion:** This allows IT administrators to audit AI actions, but breaks the strictly local data rule unless the endpoint is fully whitelisted and encrypted.
