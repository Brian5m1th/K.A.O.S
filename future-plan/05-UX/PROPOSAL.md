# UX Epic - PROPOSAL: Consolidation and Interface Polish

## 1. Unified Interface Model

We propose consolidating the 21 disjointed pages into a clean **3-Core Layout**:

1. **Mission Control (Home):** Active mission state, goal graph trees, command prompt, active agent terminal log.
2. **Remember (Memory Vault):** Obsidian note search, indexer stats, Graphify visualizer.
3. **Control Center (Settings):** Observability graphs, model setup, credential storage dashboard, active plugins.

---

## 2. Design Tokens: Glassmorphism Specifications

To establish a premium aesthetic, the Tailwind configuration is updated with uniform tokens:

```css
:root {
  --bg-primary: hsl(240, 10%, 4%);
  --bg-card: hsla(240, 5%, 8%, 0.6);
  --border-glass: hsla(240, 5%, 15%, 0.4);
  --glow-thinking: hsla(270, 70%, 50%, 0.3);
  --glow-executing: hsla(140, 70%, 50%, 0.3);
}

.glass-card {
  background: var(--bg-card);
  backdrop-filter: blur(12px);
  border: 1px solid var(--border-glass);
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}
```

---

## 3. Micro-Animations with Framer Motion

- **State Transition:** When the state shifts (e.g. Thinking ➔ Executing), the top bar glow transitions HSL colors over 500ms.
- **Goal Checking:** Checking off a subgoal runs a green checkmark check animation and shifts the goal card background.
