# DESIGN SYSTEM Epic - RISKS: Migration Challenges

This document maps layout and styling regression risks.

---

## 1. Risk: Visual Regressions during Page Refactoring

### Description
Replacing custom pages and buttons with shared primitives can break complex layouts, particularly in forms and alignment grids.

### Impact
- **Medium:** Broken UI interfaces, alignment bugs.

### Mitigation
- Refactor one page at a time.
- Verify layouts using Vitest visual regressions or manually checking elements against original screenshots after each replacement.

---

## 2. Risk: Custom Component Bloat

### Description
Developers might bypass the design system and create custom elements inside `pages/` directory instead of extracting them to `shared/ui/`.

### Impact
- **Low:** Leads to styling drift over time.

### Mitigation
- Run KIRL checks to audit component structure and flag pages containing direct inline color declarations.
