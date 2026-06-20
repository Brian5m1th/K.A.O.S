/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        canvas: "#09090b",
        surface: "#121214",
        elevated: "#18181b",
        overlay: "rgba(22,22,26,0.7)",
        "border-subtle": "rgba(255,255,255,0.06)",
        "border-hover": "rgba(255,255,255,0.12)",
        "border-focus": "#3b82f6",
        "text-primary": "#f4f4f5",
        "text-secondary": "#a1a1aa",
        "text-muted": "#71717a",
        accent: "#1976d2",
        "success": "#22c55e",
        "warning": "#f59e0b",
        "error": "#ef4444",
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
