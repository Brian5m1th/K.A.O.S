# DESIGN SYSTEM Epic - PROPOSAL: Consolidated UI Primitives

## 1. Reusable Component Specifications

We propose building a standard UI kit inside `desktop/src/shared/ui/`:

### 1.1. GlassCard Component
```typescript
import React from 'react';

interface GlassCardProps {
  children: React.ReactNode;
  className?: string;
  glow?: 'thinking' | 'executing' | 'none';
}

export const GlassCard: React.FC<GlassCardProps> = ({ children, className, glow = 'none' }) => {
  const glowClass = 
    glow === 'thinking' ? 'shadow-[0_0_15px_var(--glow-thinking)]' :
    glow === 'executing' ? 'shadow-[0_0_15px_var(--glow-executing)]' : '';

  return (
    <div className={`backdrop-blur-kaos bg-kaos-card border border-kaos-border rounded-xl p-4 transition-all duration-300 ${glowClass} ${className}`}>
      {children}
    </div>
  );
};
```

---

## 2. Iconography & Font Pairings

- **Icons:** Standardize on `lucide-react`. Do not import raw SVGs directly in pages.
- **Fonts:**
  - Headers (`h1`, `h2`, `h3`): **Outfit** (Sans-serif, light weights).
  - Body & Labels: **Inter** (Regular, Medium weights).
  - Code & Logs: **Fira Code** (Monospace, ligatures enabled).
