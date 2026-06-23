import { create } from "zustand";
import { kaosFetch } from "@/shared/api/kaos-client";

const SERVER_URL = "http://localhost:8000";

type ThemeMode = "dark" | "light" | "kaos-blue" | "purple" | "terminal";

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
  },
  light: {
    "--bg-canvas": "#ffffff",
    "--bg-surface": "#f4f4f5",
    "--bg-active": "#e4e4e7",
    "--text-primary": "#18181b",
    "--text-muted": "#71717a",
    "--text-dim": "#a1a1aa",
    "--border-subtle": "#e4e4e7",
  },
  "kaos-blue": {
    "--bg-canvas": "#0c0f1a",
    "--bg-surface": "#1a1f35",
    "--bg-active": "#252b45",
    "--text-primary": "#e8edff",
    "--text-muted": "#8892c0",
    "--text-dim": "#5d6785",
    "--border-subtle": "#252b45",
  },
  purple: {
    "--bg-canvas": "#130c1a",
    "--bg-surface": "#241a35",
    "--bg-active": "#322545",
    "--text-primary": "#f0e8ff",
    "--text-muted": "#9888c0",
    "--text-dim": "#6d5d85",
    "--border-subtle": "#322545",
  },
  terminal: {
    "--bg-canvas": "#0d1a0d",
    "--bg-surface": "#1a2e1a",
    "--bg-active": "#244224",
    "--text-primary": "#00ff41",
    "--text-muted": "#00cc33",
    "--text-dim": "#008a22",
    "--border-subtle": "#244224",
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
        const res = await kaosFetch(`${SERVER_URL}/api/settings`, "");
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
        await kaosFetch(`${SERVER_URL}/api/settings`, "", {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ theme: mode, accent_color: accentColor }),
        });
      } catch {}
    },
  };
});
