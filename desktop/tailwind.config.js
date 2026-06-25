/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        canvas: "var(--bg-canvas)",
        surface: "var(--bg-surface)",
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
