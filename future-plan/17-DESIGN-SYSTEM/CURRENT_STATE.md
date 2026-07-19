# DESIGN SYSTEM Epic - CURRENT STATE: Style Fragmentation

## 1. Fragmentation Analysis

The current front-end codebase (`desktop/src/`) lacks a unified design system:
- **Hardcoded Colors:** File `pages/Dashboard/index.tsx` uses custom hexadecimal color classes (e.g. `bg-[#1e1e24]`), while `pages/Chat/index.tsx` uses custom tailwind classes (e.g., `bg-slate-900`).
- **Inconsistent Blurs:** Different cards use different blur values (`backdrop-blur-sm`, `backdrop-blur-md`, or no blurs).
- **Custom CSS Files:** Component folders contain custom `*.css` files with ad-hoc animation keyframes, creating stylesheet pollution.
- **Button Inconsistency:** Buttons in the Settings page have square corners (`rounded-none`), whereas buttons on the Chat page have round corners (`rounded-full`).
