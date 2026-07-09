import { describe, it, expect, vi, beforeEach } from "vitest";
import { useChatStore } from "@/shared/lib/stores/chat-store";
import { kaosFetch } from "@/shared/api/kaos-client";

vi.mock("@/shared/api/kaos-client", () => ({ kaosFetch: vi.fn() }));
const mockFetch = vi.mocked(kaosFetch);

function mockSSE(chunks: string[]): ReadableStream {
  const enc = new TextEncoder();
  return new ReadableStream({
    async start(c) { for (const ch of chunks) { c.enqueue(enc.encode(ch)); } c.close(); },
  });
}

describe("Chat Store", () => {
  beforeEach(() => {
    useChatStore.setState({
      messages: [{ role: "assistant", text: "Welcome" }],
      loading: false, error: null, activeModel: "kaos",
    });
    mockFetch.mockReset();
  });

  it("should initialize with welcome message", () => {
    expect(useChatStore.getState().messages).toHaveLength(1);
    expect(useChatStore.getState().loading).toBe(false);
  });

  it("setActiveModel should change model", () => {
    useChatStore.getState().setActiveModel("gpt-4");
    expect(useChatStore.getState().activeModel).toBe("gpt-4");
  });

  it("setMessages should replace all", () => {
    const msgs = [{ role: "user" as const, text: "Hi" }];
    useChatStore.getState().setMessages(msgs);
    expect(useChatStore.getState().messages).toEqual(msgs);
  });

  it("clearMessages should reset to welcome", () => {
    useChatStore.setState({ messages: [{ role: "user", text: "X" }] });
    useChatStore.getState().clearMessages();
    expect(useChatStore.getState().messages[0].text).toContain("Welcome");
  });

  it("cancel should stop loading", () => {
    useChatStore.setState({ loading: true });
    useChatStore.getState().cancel();
    expect(useChatStore.getState().loading).toBe(false);
  });

  it("streamMessage should add user msg and stream response", async () => {
    mockFetch.mockResolvedValue(new Response(mockSSE([
      'data: {"choices":[{"delta":{"content":"Hi"}}]}\n\n',
      "data: [DONE]\n\n",
    ]), { status: 200, headers: { "Content-Type": "text/event-stream" } }));
    await useChatStore.getState().streamMessage("Hello");
    expect(useChatStore.getState().messages[0].role).toBe("user");
    expect(useChatStore.getState().loading).toBe(false);
  });

  it("streamMessage should handle network error", async () => {
    mockFetch.mockRejectedValue(new TypeError("fail"));
    await useChatStore.getState().streamMessage("Hello");
    expect(useChatStore.getState().loading).toBe(false);
    expect(useChatStore.getState().messages.at(-1)!.text).toContain("offline");
  });
});
