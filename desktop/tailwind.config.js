/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        canvas: "var(--bg-canvas)",
        surface: "var(--bg-surface)",
        "surface-raised": "var(--surface-raised)",
        "surface-elevated": "var(--surface-elevated)",
        "surface-hover": "var(--surface-hover)",
        "bg-active": "var(--bg-active)",
        overlay: "var(--bg-canvas)",
        "accent-primary": "var(--accent-primary)",
        "accent-neon": "var(--accent-neon)",
        "accent-glow": "rgba(59, 130, 246, 0.15)",
        success: "#10B981",
        warning: "#F59E0B",
        error: "#EF4444",
        "text-primary": "var(--text-primary)",
        "text-muted": "var(--text-muted)",
        "text-dim": "var(--text-dim)",
        "border-subtle": "var(--border-subtle)",
        "border-hover": "rgba(255,255,255,0.12)",
        "border-focus": "var(--accent-primary)",
      },
      boxShadow: {
        sm: "var(--shadow-sm)",
        md: "var(--shadow-md)",
        lg: "var(--shadow-lg)",
        xl: "var(--shadow-xl)",
      },
      borderRadius: {
        sm: "var(--radius-sm)",
        md: "var(--radius-md)",
        lg: "var(--radius-lg)",
        xl: "var(--radius-xl)",
      },
      transitionDuration: {
        fast: "var(--duration-fast)",
        normal: "var(--duration-normal)",
        slow: "var(--duration-slow)",
      },
      fontFamily: {
        sans: ["Inter", "system-ui", "-apple-system", "sans-serif"],
        mono: ["JetBrains Mono", "Fira Code", "monospace"],
      },
      backdropBlur: {
        desktop: "12px",
      },
    },
  },
  plugins: [],
};
