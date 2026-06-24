import { create } from "zustand";
import { kaosFetch } from "@/shared/api/kaos-client";

export interface ConversationSession {
  sessionId: string;
  userId: string;
  startedAt: string;
  lastMessageAt: string;
  messageCount: number;
  workflowTypes: string[];
  totalTokens: number;
}

interface ConversationState {
  sessions: ConversationSession[];
  loading: boolean;
  total: number;
  currentPage: number;

  fetchSessions: (userId: string, page?: number) => Promise<void>;
  deleteSession: (sessionId: string, userId: string) => Promise<void>;
  clearSessions: () => void;
}

export const useConversationStore = create<ConversationState>((set) => ({
  sessions: [],
  loading: false,
  total: 0,
  currentPage: 1,

  fetchSessions: async (userId: string, page = 1) => {
    if (!userId) return;
    set({ loading: true });
    try {
      const res = await kaosFetch(
        `/api/conversations?user_id=${encodeURIComponent(userId)}&page=${page}&limit=20`
      );
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      set({
        sessions: data.conversations || [],
        total: data.total || 0,
        currentPage: page,
        loading: false,
      });
    } catch (err) {
      console.error("[conversation-store] fetchSessions failed:", err);
      set({ loading: false });
    }
  },

  deleteSession: async (sessionId: string, userId: string) => {
    try {
      const res = await kaosFetch(
        `/api/conversations/${sessionId}?user_id=${encodeURIComponent(userId)}`,
        "",
        { method: "DELETE" }
      );
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      set((state) => ({
        sessions: state.sessions.filter((s) => s.sessionId !== sessionId),
        total: state.total - 1,
      }));
    } catch (err) {
      console.error("[conversation-store] deleteSession failed:", err);
    }
  },

  clearSessions: () => {
    set({ sessions: [], total: 0, currentPage: 1 });
  },
}));
