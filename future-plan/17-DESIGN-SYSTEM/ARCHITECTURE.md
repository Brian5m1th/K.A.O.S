# DESIGN SYSTEM Epic - ARCHITECTURE: Shared Primitives

## 1. Design System Hierarchy

Following Feature-Sliced Design (FSD), all design tokens and primitives live in the `shared/ui` directory:

```text
desktop/src/shared/ui/
├── Button/        # Standard button with glass hover effects
├── Input/         # Glass text area and input text fields
├── Modal/         # Glassmorphic overlay modals
├── Scrollbar/     # Custom thin transparent scrollbars
├── GlassCard/     # Standard container card with backdrop-blur
└── Tooltip/       # Subtle text hints on element hover
```

---

## 2. Token Definitions

Tailwind variables are declared in `tailwind.config.js` to ensure consistent execution:

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        kaos: {
          bg: '#0a0a0c',
          card: 'rgba(18, 18, 22, 0.65)',
          border: 'rgba(255, 255, 255, 0.08)',
          glow: 'rgba(147, 51, 234, 0.25)',
        }
      },
      backdropBlur: {
        kaos: '16px'
      }
    }
  }
}
```
