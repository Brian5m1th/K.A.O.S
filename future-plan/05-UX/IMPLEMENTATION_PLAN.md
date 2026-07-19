# UX Epic - IMPLEMENTATION PLAN: Interface Restructuring

This document plans the front-end layout reorganization.

---

## 1. UI Roadmap

```text
Phase 1: Design Tokens ──► Phase 2: Top Bar State ──► Phase 3: Consolidation
(Tailwind glass classes)   (Transitions & animations) (Merge pages to 3 panels)
```

### Phase 1: CSS Glassmorphism setup (Sprint 1)
- Write `.glass-card` classes into `desktop/src/app/index.css`.
- Update Tailwind config to include glow classes.
- Replace basic panels with glass cards in `pages/Chat/`.

### Phase 2: Top Bar State indicators (Sprint 2)
- Create `desktop/src/widgets/Topbar/MentalStateIndicator.tsx`.
- Bind component state to the global Zustand `useMindStore`.
- Implement pulse glows using Framer Motion animations.

### Phase 3: Interface Consolidation (Sprint 3-4)
- Group components under `desktop/src/pages/MissionControl/`.
- Mount Graphify canvas inside the "Remember" vault explorer tab as a pop-out panel.
- Remove old page routes from React Router layout configuration.
