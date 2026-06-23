import { create } from "zustand";
import { kaosFetch } from "@/shared/api/kaos-client";

const DEFAULT_SERVER_URL = "http://localhost:8000";

interface User {
  id: string;
  name: string;
  email: string;
  role: string;
}

interface AuthState {
  accessToken: string | null;
  refreshToken: string | null;
  maskedKey: string;
  user: User | null;
  serverUrl: string;
  configured: boolean;
  checking: boolean;
  error: string | null;

  checkSetupStatus: () => Promise<void>;
  register: (name: string, email: string, password: string) => Promise<void>;
  login: (email: string, password: string) => Promise<void>;
  refreshAccessToken: () => Promise<void>;
  logout: () => void;
  clearError: () => void;
}

export const useAuthStore = create<AuthState>((set, get) => ({
  accessToken: null,
  refreshToken: null,
  maskedKey: "",
  user: null,
  serverUrl: DEFAULT_SERVER_URL,
  configured: false,
  checking: true,
  error: null,

  clearError: () => set({ error: null }),

  checkSetupStatus: async () => {
    set({ checking: true });
    try {
      const [setupRes, keyRes] = await Promise.allSettled([
        kaosFetch(`${DEFAULT_SERVER_URL}/auth/setup-status`, ""),
        kaosFetch(`${DEFAULT_SERVER_URL}/auth/key`, ""),
      ]);

      if (setupRes.status === "fulfilled" && setupRes.value.ok) {
        const data = await setupRes.value.json();
        set({ configured: data.configured ?? false, checking: false });
      } else {
        set({ configured: false, checking: false });
      }

      if (keyRes.status === "fulfilled" && keyRes.value.ok) {
        const data = await keyRes.value.json();
        set({ maskedKey: data.masked || "" });
      }
    } catch {
      set({ configured: false, checking: false });
    }
  },

  register: async (name, email, password) => {
    set({ error: null });
    try {
      const res = await kaosFetch(
        `${DEFAULT_SERVER_URL}/auth/register`,
        "",
        {
          method: "POST",
          body: JSON.stringify({ name, email, password }),
        },
      );
      const data = await res.json();
      if (!res.ok) {
        set({ error: data.detail || "Registration failed" });
        return;
      }
      set({
        accessToken: data.access_token,
        refreshToken: data.refresh_token,
        user: data.user,
        configured: true,
      });
    } catch {
      set({ error: "Cannot reach the backend server" });
    }
  },

  login: async (email, password) => {
    set({ error: null });
    try {
      const res = await kaosFetch(
        `${DEFAULT_SERVER_URL}/auth/login`,
        "",
        {
          method: "POST",
          body: JSON.stringify({ email, password }),
        },
      );
      const data = await res.json();
      if (!res.ok) {
        set({ error: data.detail || "Login failed" });
        return;
      }
      set({
        accessToken: data.access_token,
        refreshToken: data.refresh_token,
        user: data.user,
      });
    } catch {
      set({ error: "Cannot reach the backend server" });
    }
  },

  refreshAccessToken: async () => {
    const { refreshToken } = get();
    if (!refreshToken) {
      set({ accessToken: null, user: null });
      return;
    }
    try {
      const res = await kaosFetch(
        `${DEFAULT_SERVER_URL}/auth/refresh`,
        "",
        {
          method: "POST",
          body: JSON.stringify({ refresh_token: refreshToken }),
        },
      );
      if (!res.ok) {
        set({ accessToken: null, refreshToken: null, user: null });
        return;
      }
      const data = await res.json();
      set({
        accessToken: data.access_token,
        refreshToken: data.refresh_token,
        user: data.user,
      });
    } catch {
      set({ accessToken: null, refreshToken: null, user: null });
    }
  },

  logout: () => {
    set({
      accessToken: null,
      refreshToken: null,
      user: null,
    });
  },
}));
