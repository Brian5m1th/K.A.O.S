import { describe, it, expect, vi, beforeEach } from "vitest";
import { useChatStore } from "@/application/stores/chat-store";
import { kaosFetch } from "@/infrastructure/http";

vi.mock("@/infrastructure/http", () => ({ kaosFetch: vi.fn() }));
const mockFetch = vi.mocked(kaosFetch);

function createSSEStream(chunks: string[]): ReadableStream {
  const enc = new TextEncoder();
  return new ReadableStream({
    async start(c) { for (const ch of chunks) c.enqueue(enc.encode(ch)); c.close(); },
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

  it("cancel should stop loading", () => {
    useChatStore.setState({ loading: true });
    useChatStore.getState().cancel();
    expect(useChatStore.getState().loading).toBe(false);
  });

  it("streamMessage should add user msg and stream", async () => {
    mockFetch.mockResolvedValue(new Response(createSSEStream([
      'data: {"choices":[{"delta":{"content":"Hi"}}]}\n\n',
      "data: [DONE]\n\n",
    ]), { status: 200, headers: { "Content-Type": "text/event-stream" } }));
    await useChatStore.getState().streamMessage("Hello");
    // user message is appended after existing messages
    expect(useChatStore.getState().messages[1].role).toBe("user");
  });

  it("streamMessage should handle error", async () => {
    mockFetch.mockRejectedValue(new TypeError("fail"));
    await useChatStore.getState().streamMessage("Hello");
    expect(useChatStore.getState().loading).toBe(false);
    const lastMsg = useChatStore.getState().messages.slice(-1)[0];
    expect(lastMsg.text).toContain("offline");
  });
});