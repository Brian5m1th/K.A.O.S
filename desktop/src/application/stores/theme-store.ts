import { create } from "zustand";
import { kaosFetch } from "@/infrastructure";

type ThemeMode = "dark" | "light" | "kaos-blue" | "purple" | "terminal" | "cyberpunk" | "nordic" | "forest";

const ACCENT_COLORS: Record<string, string> = {
  "#3B82F6": "Blue",
  "#8B5CF6": "Purple",
  "#10B981": "Emerald",
  "#F59E0B": "Amber",
  "#EF4444": "Red",
  "#06B6D4": "Cyan",
};

const THEME_VARS: Record<ThemeMode, Record<string, string>> = {
  dark: {
    "--bg-canvas": "#09090b",
    "--bg-surface": "#18181b",
    "--bg-active": "#27272a",
    "--text-primary": "#fafafa",
    "--text-muted": "#a1a1aa",
    "--text-dim": "#71717a",
    "--border-subtle": "#27272a",
    "--surface-raised": "#202023",
    "--surface-elevated": "#2d2d30",
    "--surface-hover": "#2d2d30",
    "--shadow-color": "rgba(0, 0, 0, 0.5)",
  },
  light: {
    "--bg-canvas": "#ffffff",
    "--bg-surface": "#f4f4f5",
    "--bg-active": "#e4e4e7",
    "--text-primary": "#18181b",
    "--text-muted": "#71717a",
    "--text-dim": "#a1a1aa",
    "--border-subtle": "#e4e4e7",
    "--surface-raised": "#fafafa",
    "--surface-elevated": "#ffffff",
    "--surface-hover": "#f4f4f5",
    "--shadow-color": "rgba(0, 0, 0, 0.08)",
  },
  "kaos-blue": {
    "--bg-canvas": "#0c0f1a",
    "--bg-surface": "#1a1f35",
    "--bg-active": "#252b45",
    "--text-primary": "#e8edff",
    "--text-muted": "#8892c0",
    "--text-dim": "#5d6785",
    "--border-subtle": "#252b45",
    "--surface-raised": "#202640",
    "--surface-elevated": "#2c3355",
    "--surface-hover": "#252b45",
    "--shadow-color": "rgba(0, 0, 0, 0.6)",
  },
  purple: {
    "--bg-canvas": "#130c1a",
    "--bg-surface": "#241a35",
    "--bg-active": "#322545",
    "--text-primary": "#f0e8ff",
    "--text-muted": "#9888c0",
    "--text-dim": "#6d5d85",
    "--border-subtle": "#322545",
    "--surface-raised": "#2b1f40",
    "--surface-elevated": "#3a2b55",
    "--surface-hover": "#322545",
    "--shadow-color": "rgba(0, 0, 0, 0.6)",
  },
  terminal: {
    "--bg-canvas": "#0d1a0d",
    "--bg-surface": "#1a2e1a",
    "--bg-active": "#244224",
    "--text-primary": "#00ff41",
    "--text-muted": "#00cc33",
    "--text-dim": "#008a22",
    "--border-subtle": "#244224",
    "--surface-raised": "#1d331d",
    "--surface-elevated": "#294a29",
    "--surface-hover": "#244224",
    "--shadow-color": "rgba(0, 0, 0, 0.7)",
  },
  cyberpunk: {
    "--bg-canvas": "#05000a",
    "--bg-surface": "#120024",
    "--bg-active": "#22003c",
    "--text-primary": "#00ffcc",
    "--text-muted": "#ff007f",
    "--text-dim": "#bc00dd",
    "--border-subtle": "#22003c",
    "--surface-raised": "#190033",
    "--surface-elevated": "#2a004a",
    "--surface-hover": "#22003c",
    "--shadow-color": "rgba(0, 0, 0, 0.8)",
  },
  nordic: {
    "--bg-canvas": "#2e3440",
    "--bg-surface": "#3b4252",
    "--bg-active": "#434c5e",
    "--text-primary": "#eceff4",
    "--text-muted": "#d8dee9",
    "--text-dim": "#81a1c1",
    "--border-subtle": "#434c5e",
    "--surface-raised": "#353d4c",
    "--surface-elevated": "#4c566a",
    "--surface-hover": "#434c5e",
    "--shadow-color": "rgba(0, 0, 0, 0.35)",
  },
  forest: {
    "--bg-canvas": "#081008",
    "--bg-surface": "#102010",
    "--bg-active": "#1b331b",
    "--text-primary": "#e2efe2",
    "--text-muted": "#8fb38f",
    "--text-dim": "#5c8a5c",
    "--border-subtle": "#1b331b",
    "--surface-raised": "#142914",
    "--surface-elevated": "#244724",
    "--surface-hover": "#1b331b",
    "--shadow-color": "rgba(0, 0, 0, 0.7)",
  },
};

interface ThemeState {
  mode: ThemeMode;
  accentColor: string;
  initialized: boolean;
  setMode: (mode: ThemeMode) => void;
  setAccentColor: (color: string) => void;
  loadFromBackend: () => Promise<void>;
  saveToBackend: () => Promise<void>;
}

function applyTheme(mode: ThemeMode, accent: string) {
  const vars = THEME_VARS[mode] || THEME_VARS.dark;
  for (const [key, val] of Object.entries(vars)) {
    document.documentElement.style.setProperty(key, val);
  }
  document.documentElement.style.setProperty("--accent-primary", accent);
  document.documentElement.style.setProperty("--accent-neon", accent);
}

// Load saved theme from localStorage on init
function loadLocalTheme(): { mode: ThemeMode; accent: string } | null {
  try {
    const saved = localStorage.getItem("kaos-theme");
    if (saved) return JSON.parse(saved);
  } catch {}
  return null;
}

function saveLocalTheme(mode: ThemeMode, accent: string) {
  try {
    localStorage.setItem("kaos-theme", JSON.stringify({ mode, accent }));
  } catch {}
}

export const useThemeStore = create<ThemeState>((set, get) => {
  // Apply saved theme on load
  const local = loadLocalTheme();
  if (local) {
    applyTheme(local.mode, local.accent);
  } else {
    applyTheme("dark", "#3B82F6");
  }

  return {
    mode: local?.mode || "dark",
    accentColor: local?.accent || "#3B82F6",
    initialized: true,

    setMode: (mode) => {
      applyTheme(mode, get().accentColor);
      saveLocalTheme(mode, get().accentColor);
      set({ mode });
    },

    setAccentColor: (accentColor) => {
      applyTheme(get().mode, accentColor);
      saveLocalTheme(get().mode, accentColor);
      set({ accentColor });
    },

    loadFromBackend: async () => {
      try {
        const res = await kaosFetch("/api/settings", "");
        if (res.ok) {
          const data = await res.json();
          const mode = data.theme || "dark";
          const accent = data.accent_color || "#3B82F6";
          applyTheme(mode, accent);
          saveLocalTheme(mode, accent);
          set({ mode, accentColor: accent });
        }
      } catch {}
    },

    saveToBackend: async () => {
      const { mode, accentColor } = get();
      try {
        await kaosFetch("/api/settings", "", {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ theme: mode, accent_color: accentColor }),
        });
      } catch {}
    },
  };
});
