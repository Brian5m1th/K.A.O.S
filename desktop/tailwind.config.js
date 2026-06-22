/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        canvas: "#0B0F14",
        surface: "#121826",
        "bg-active": "#1A2338",
        overlay: "rgba(11, 15, 20, 0.85)",
        "accent-primary": "#3B82F6",
        "accent-neon": "#8B5CF6",
        "accent-glow": "rgba(139, 92, 246, 0.15)",
        success: "#10B981",
        warning: "#F59E0B",
        error: "#EF4444",
        "text-primary": "#F3F4F6",
        "text-muted": "#9CA3AF",
        "text-dim": "#4B5563",
        "border-subtle": "rgba(255,255,255,0.06)",
        "border-hover": "rgba(255,255,255,0.12)",
        "border-focus": "#3B82F6",
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
