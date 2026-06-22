---
description: Convencoes de codigo do K.A.O.S
globs: 
---
# Code Conventions

## Python

### Naming
- Files/directories: `snake_case` (`auth.py`, `event_bus.py`)
- Classes: `PascalCase` (`EventBus`, `FeatureRegistry`)
- Functions/methods: `snake_case` (`run_audit()`, `classify_commit()`)
- Constants: `UPPER_SNAKE_CASE` (`EVENT_REQUEST_STARTED`)
- Private module-level: `_prefix` (`_watcher`, `_embedder_ready`)

### Types
- Use `| None` instead of `Optional` (`x: str | None = None`)
- Use `list[X]` instead of `List[X]` (PEP 585)
- Use `dict[str, X]` instead of `Dict[str, X]` (PEP 585)
- Add `from __future__ import annotations` at top of file
- Full type annotations required on all functions

### Imports
- Standard library first, third-party second, local third
- Absolute imports: `from app.config.settings import settings`

### Logging (Loguru)
- Tag-based: `[start]`, `[finish]`, `[info]`, `[error]`
- `logger.info()`, `logger.warning()`, `logger.error()`, `logger.debug()`
- Structured: `logger.bind(event="auth", user_id=str(uid)).info("login")`

### Error Handling
- Try/catch with specific exceptions
- Log errors with logger.error()
- Silent handling only on non-critical paths

## TypeScript

### Naming
- Files/directories: `kebab-case` (`chat-store.ts`, `ask-ai/`)
- Components: PascalCase export functions
- Hooks: `camelCase` prefixed with `use`
- Interfaces/Types: PascalCase
- Stores: PascalCase with `State` suffix

### Imports
- Absolute with `@/` alias (`@/shared/ui/button`)
- `import type` for type-only imports
- Groups: React first, third-party, local

### Components
- Function components with `interface Props` (not inline types)
- Default exports for page components, named exports for everything else

### Stores (Zustand)
- `create<State>((set) => ({...}))` pattern
- Selector hooks for derived data
- Actions prefixed with `set` or verb (fetch, load, save)
