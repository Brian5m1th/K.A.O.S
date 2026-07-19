# UX Epic - VISION: Conversational & Mind States UX

## 1. Visual Identity & Aesthetic Principles

K.A.O.S requires a premium, interactive user experience. Users should feel they are interacting with a living "mind" rather than a cold database. The design utilizes:
- **Glassmorphism:** Frosted borders, transparent containers, and deep background gradients (dark HSL palettes) to create depth.
- **Micro-Animations:** Fluid transitions (Framer Motion) on element hovers, showing progress spinners, and fading components dynamically.
- **Aesthetic Typography:** Clean, modern font pairing (Outfit for headings, Inter for interface elements) to enhance readability.

---

## 2. Mental State Visual Indicators

The UI reflects the backend's current mental state. Visual indicators should be placed in the top navigation header:

```text
[◉ Thinking] ──► Icon rotates and glows, background turns soft purple.
[◉ Executing] ──► Terminal prompt slides in, showing tool name in green.
[◉ Sleeping] ──► Icons fade, background darkens, system enters low-power.
[◉ Emergency] ──► Border pulses red, desktop toast triggers alert details.
```

- **Transitions:** Each state transition is animated smoothly.
- **Resource Stats:** Memory and CPU metrics are visible in a compact "Mind Gauge" at the top of the interface.
