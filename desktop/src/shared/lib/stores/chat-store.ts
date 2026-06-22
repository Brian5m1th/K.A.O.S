import { create } from "zustand";
import type { Message } from "@/entities/message/types";
import { kaosFetch } from "@/shared/api/kaos-client";
import { eventBus } from "@/shared/lib/event-bus";
import { createToolEvent, completeToolEvent, failToolEvent } from "@/shared/lib/tool-schema";
import type { ToolCall } from "@/entities/message/types";

interface ChatState {
  messages: Message[];
  loading: boolean;
  error: string | null;
  activeModel: string;

  streamMessage: (input: string, model?: string, serverUrl?: string, apiKey?: string) => Promise<void>;
  cancel: () => void;
  clearMessages: () => void;
  setActiveModel: (model: string) => void;
}

let abortController: AbortController | null = null;

export const useChatStore = create<ChatState>((set, get) => ({
  messages: [{ role: "assistant", text: "KAOS initialized. How can I help you?" }],
  loading: false,
  error: null,
  activeModel: "kaos",

  setActiveModel: (activeModel) => set({ activeModel }),

  clearMessages: () =>
    set({ messages: [{ role: "assistant", text: "KAOS initialized. How can I help you?" }] }),

  cancel: () => {
    abortController?.abort();
    abortController = null;
    set({ loading: false });
  },

  streamMessage: async (input, model, serverUrl = "http://localhost:8000", apiKey = "") => {
    const { messages, loading } = get();
    if (!input.trim() || loading) return;

    const userMsg: Message = { role: "user", text: input.trim() };

    set((s) => ({
      messages: [...s.messages, userMsg],
      loading: true,
      error: null,
    }));

    abortController = new AbortController();
    const usedModel = model || get().activeModel;

    eventBus.emit({ type: "chat:stream-start", payload: { model: usedModel } });

    try {
      const cleanUrl = serverUrl.replace(/\/+$/, "");

      const response = await kaosFetch(`${cleanUrl}/v1/chat/completions`, apiKey, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          model: usedModel,
          messages: [
            ...messages.filter((m) => m.role !== "tool" || !m.text),
            userMsg,
          ].map((m) => ({
            role: m.role === "tool" ? "assistant" : m.role,
            content: m.text,
          })),
          stream: true,
        }),
        signal: abortController.signal,
      });

      if (!response.ok) throw new Error(`HTTP ${response.status}`);

      const reader = response.body?.getReader();
      if (!reader) throw new Error("No reader available");

      const decoder = new TextDecoder();
      let buffer = "";
      let fullText = "";

      set((s) => ({ messages: [...s.messages, { role: "assistant", text: "" }] }));

      const flushBuffer = () => {
        if (!buffer) return;
        set((s) => {
          const updated = [...s.messages];
          const last = updated[updated.length - 1];
          if (last?.role === "assistant") {
            updated[updated.length - 1] = { ...last, text: last.text + buffer };
          }
          return { messages: updated };
        });
        buffer = "";
      };

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value, { stream: true });
        const lines = chunk.split("\n");

        for (const line of lines) {
          if (!line || !line.startsWith("data: ")) continue;
          const data = line.slice(6);
          if (data === "[DONE]") continue;

          try {
            const parsed = JSON.parse(data);
            const content = parsed.choices?.[0]?.delta?.content || "";
            const toolCallsDelta = parsed.choices?.[0]?.delta?.tool_calls;

            if (content) {
              buffer += content;
              fullText += content;
              eventBus.emit({ type: "chat:stream-token", payload: { token: content } });
              if (buffer.length > 4 || content.includes("\n")) flushBuffer();
            }

            if (toolCallsDelta) {
              flushBuffer();
              const toolEvent = createToolEvent(
                toolCallsDelta.function?.name || "unknown",
                toolCallsDelta.function?.arguments,
              );
              const toolCall: ToolCall = {
                name: toolEvent.name,
                arguments: JSON.stringify(toolEvent.arguments),
                output: "",
              };
              set((s) => {
                const updated = s.messages.slice(0, -1);
                updated.push({ role: "tool", text: "", toolCall });
                updated.push({ role: "assistant", text: "" });
                return { messages: updated };
              });
              eventBus.emit({ type: "tool:start", payload: toolEvent });
            }
          } catch {
            // Skip malformed lines
          }
        }
      }

      flushBuffer();
      eventBus.emit({ type: "chat:stream-end", payload: { fullText } });
      set({ activeModel: usedModel });
    } catch (err: unknown) {
      if (err instanceof Error && err.name === "AbortError") return;
      const msg = err instanceof Error ? err.message : "Connection failed";
      set({ error: msg });
      eventBus.emit({ type: "chat:error", payload: { message: msg } });
      set((s) => ({
        messages: [
          ...s.messages,
          { role: "assistant", text: "Server unreachable. You're now in offline mode." },
        ],
      }));
    } finally {
      set({ loading: false });
      abortController = null;
    }
  },
}));
