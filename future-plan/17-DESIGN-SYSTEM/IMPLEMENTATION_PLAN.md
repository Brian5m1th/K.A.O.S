# DESIGN SYSTEM Epic - IMPLEMENTATION PLAN: Rebuilding Primitives

This plan schedules the styling cleanup and UI kit creation.

---

## 1. Design System Milestones

```text
Phase 1: Config ────────► Phase 2: Primitives ────► Phase 3: Refactor Pages
(Tailwind theme setup)    (Create Button/Card)    (Remove inline hex colors)
```

### Phase 1: Tailwind Setup (Sprint 1)
- Edit `desktop/tailwind.config.js` to map colors and backdrop blur tokens.
- Import fonts in `desktop/src/app/index.html`.

### Phase 2: Write Primitives (Sprint 2)
- Create `desktop/src/shared/ui/Button/` and `Input/`.
- Export all components from a single index file `desktop/src/shared/ui/index.ts`.
- Write Storybook stories or local tests to check hover animations.

### Phase 3: Refactor Pages (Sprint 3-4)
- Search for instances of `bg-[#` to replace with class utility classes.
- Replace custom button definitions with `<Button variant="glass">` calls.
