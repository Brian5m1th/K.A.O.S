# UX Epic - RISKS: Interface Performance Risks

This document analyzes front-end performance risks.

---

## 1. Risk: Graph Canvas Rendering Starvation

### Description
The Graphify visualizer renders thousands of nodes. Rendering this directly on the main CPU thread will freeze the Tauri UI, locking out inputs.

### Impact
- **High:** Leads to a laggy interface.

### Mitigation
- Offload the node layout calculations (e.g. force-directed layout) to a Web Worker thread.
- Use WebGL or canvas-based rendering (PixiJS/G6) instead of standard DOM/SVG components for graphs containing > 1,000 elements.

---

## 2. Risk: Animation overhead on Integrated GPUs

### Description
Heavy glassmorphism (specifically, CSS `backdrop-filter: blur()`) paired with constant Framer Motion transforms can drop frame rates on computers without dedicated GPUs.

### Impact
- **Medium:** Bad UX, stuttering interfaces.

### Mitigation
- Implement a "Reduce Motion" setting that disables card blurs and transitions, falling back to flat backgrounds on low-spec systems.
