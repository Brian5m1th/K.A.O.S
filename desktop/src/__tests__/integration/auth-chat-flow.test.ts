import { describe, it, expect, vi, beforeEach } from "vitest";
import { useChatStore } from "@/shared/lib/stores/chat-store";
import { useAuthStore } from "@/shared/lib/stores/auth-store";
import { kaosFetch } from "@/shared/api/kaos-client";

vi.mock("@/shared/api/kaos-client", () => ({ kaosFetch: vi.fn() }));
const mockFetch = vi.mocked(kaosFetch);

describe("Integration: Auth -> Chat Flow", () => {
  beforeEach(() => {
    useAuthStore.setState({ accessToken: null, user: null, configured: false, checking: false, error: null, serverUrl: "http://localhost:8000", refreshToken: null, maskedKey: "" });
    useChatStore.setState({ messages: [{ role: "assistant", text: "Welcome" }], loading: false, error: null, activeModel: "kaos" });
    mockFetch.mockReset();
  });

  it("should login, then chat, then logout", async () => {
    // Login
    mockFetch.mockResolvedValueOnce(new Response(JSON.stringify({
      access_token: "jwt-token", refresh_token: "jwt-refresh",
      user: { id: "1", name: "User", email: "u@t.com", role: "user" },
    }), { status: 200 }));
    await useAuthStore.getState().login("u@t.com", "pass");
    expect(useAuthStore.getState().accessToken).toBe("jwt-token");

    // Chat stream
    const enc = new TextEncoder();
    const stream = new ReadableStream({
      async start(c) { c.enqueue(enc.encode('data: {"choices":[{"delta":{"content":"Reply"}}]}\n\n')); c.enqueue(enc.encode("data: [DONE]\n\n")); c.close(); },
    });
    mockFetch.mockResolvedValueOnce(new Response(stream, { status: 200, headers: { "Content-Type": "text/event-stream" } }));
    await useChatStore.getState().streamMessage("Hello");
    expect(useChatStore.getState().messages[0].role).toBe("user");

    // Logout
    useAuthStore.getState().logout();
    expect(useAuthStore.getState().accessToken).toBeNull();
    expect(mockFetch.mock.calls[0][0]).toContain("/auth/login");
  });
});
