# DESIGN SYSTEM Epic - OPEN QUESTIONS: Design System Architecture

The following questions remain open:

---

## 1. High Contrast & Accessibility
- **Issue:** Glassmorphism and transparent background card layouts naturally have low contrast ratios (often failing WCAG AA guidelines).
- **Options:**
  - **Ignore standard guidelines:** Treat it strictly as a developer utility tool focusing on aesthetics.
  - **High Contrast Toggle:** Offer a flat CSS theme that removes blurs and transparent gradients, replacing them with high-contrast text and border styling for accessibility compliance. (Recommended).

---

## 2. Tailwind CSS Version Upgrade
- **Question:** Should we migrate to Tailwind CSS v4 or stay on v3?
- **Trade-offs:**
  - **Tailwind v4:** Faster builds, uses native CSS variables configuration, matches glassmorphism theme requirements.
  - **Tailwind v3:** Stable, matches current template code, requires no bundle adjustments.
