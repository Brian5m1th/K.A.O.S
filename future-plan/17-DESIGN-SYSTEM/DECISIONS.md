# DESIGN SYSTEM Epic - DECISIONS: Styling Standards

This document records the UI styling choices for K.A.O.S.

---

## 1. ADR-DS-001: Color Token Format

### Context
Using HEX colors inside component styles makes it difficult to adjust transparency dynamically. Tailwind support for HSL variables is highly customizable.

### Decision
Standardize all color tokens using HSL CSS variables, declared in `:root` and mapped in Tailwind.

### Consequences
- Allows transparent backgrounds via CSS overlays (e.g. `hsla(var(--primary-color), 0.25)`).
- Simplifies dynamic theme switching.

---

## 2. ADR-DS-002: Tailwind as Utility Standard

### Context
We want to avoid bloating stylesheets. Some components use custom standard CSS files.

### Decision
Enforce Tailwind CSS for 95% of components. Custom CSS files are only allowed for complex layout animations that cannot be easily written in utility class names.

### Consequences
- Decreases bundler size.
- Standardizes formatting and layouts.
