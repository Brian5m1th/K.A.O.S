import { describe, it, expect, vi, beforeEach } from "vitest";
import { useConversationStore } from "@/shared/lib/stores/conversation-store";
import { kaosFetch } from "@/infrastructure/http";

vi.mock("@/infrastructure/http", () => ({ kaosFetch: vi.fn() }));
const mockFetch = vi.mocked(kaosFetch);
const session = { sessionId: "s1", userId: "u1", startedAt: "2025-01-01T00:00:00Z", lastMessageAt: "2025-01-01T01:00:00Z", messageCount: 5, workflowTypes: ["chat"], totalTokens: 100 };
const resp = { conversations: [session], total: 1, page: 1, limit: 20 };

describe("Conversation Store", () => {
  beforeEach(() => {
    useConversationStore.setState({ sessions: [], loading: false, total: 0, currentPage: 1 });
    mockFetch.mockReset();
  });

  it("should start empty", () => {
    const s = useConversationStore.getState();
    expect(s.sessions).toEqual([]);
    expect(s.total).toBe(0);
  });

  it("fetchSessions should populate state", async () => {
    mockFetch.mockResolvedValue(new Response(JSON.stringify(resp), { status: 200 }));
    await useConversationStore.getState().fetchSessions("u1");
    expect(useConversationStore.getState().sessions).toHaveLength(1);
    expect(useConversationStore.getState().total).toBe(1);
  });

  it("fetchSessions should skip empty userId", async () => {
    await useConversationStore.getState().fetchSessions("");
    expect(mockFetch).not.toHaveBeenCalled();
  });

  it("deleteSession should remove and update total", async () => {
    useConversationStore.setState({ sessions: [session], total: 1 });
    mockFetch.mockResolvedValue(new Response(null, { status: 200 }));
    await useConversationStore.getState().deleteSession("s1", "u1");
    expect(useConversationStore.getState().sessions).toHaveLength(0);
    expect(useConversationStore.getState().total).toBe(0);
  });

  it("clearSessions should reset everything", () => {
    useConversationStore.setState({ sessions: [session], total: 1, currentPage: 3 });
    useConversationStore.getState().clearSessions();
    expect(useConversationStore.getState().sessions).toEqual([]);
    expect(useConversationStore.getState().currentPage).toBe(1);
  });
});
