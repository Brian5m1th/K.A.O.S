import { useState, useRef, useCallback, useEffect } from "react";
import type { Message, ToolCall } from "@/entities/message/types";
import { kaosFetch } from "@/shared/api/kaos-client";
import { useSystemStore } from "@/shared/lib/stores";

export function useChatStream(serverUrl: string, apiKey: string) {
  const [messages, setMessages] = useState<Message[]>([
    { role: "assistant", text: "KAOS initialized. How can I help you?" },
  ]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const abortRef = useRef<AbortController | null>(null);

  const streamMessage = useCallback(
    async (input: string, model?: string) => {
      if (!input.trim() || loading) return;

      const userMsg: Message = { role: "user", text: input.trim() };

      setMessages((prev) => [...prev, userMsg]);
      setLoading(true);
      setError(null);

      abortRef.current = new AbortController();

      try {
        const cleanUrl = serverUrl.replace(/\/+$/, "");

        const response = await kaosFetch(
          `${cleanUrl}/v1/chat/completions`,
          apiKey,
          {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              model: model || "kaos",
              messages: [
                ...messages.filter((m) => m.role !== "tool" || !m.text),
                userMsg,
              ].map((m) => ({
                role: m.role === "tool" ? "assistant" : m.role,
                content: m.text,
              })),
              stream: true,
            }),
            signal: abortRef.current.signal,
          },
        );

        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }

        const reader = response.body?.getReader();
        if (!reader) throw new Error("No reader available");

        const decoder = new TextDecoder();
        let buffer = "";
        let assistantText = "";

        // Create a placeholder for the assistant response
        setMessages((prev) => [...prev, { role: "assistant", text: "" }]);

        const processLine = (line: string) => {
          if (!line || !line.startsWith("data: ")) return;
          const data = line.slice(6);

          if (data === "[DONE]") return;

          try {
            const parsed = JSON.parse(data);
            const content = parsed.choices?.[0]?.delta?.content || "";
            const toolCallsDelta = parsed.choices?.[0]?.delta?.tool_calls;

            if (content) {
              buffer += content;
              assistantText += content;

              // Flush buffer periodically for smooth rendering
              if (buffer.length > 4 || content.includes("\n")) {
                setMessages((prev) => {
                  const updated = [...prev];
                  const last = updated[updated.length - 1];
                  if (last?.role === "assistant") {
                    updated[updated.length - 1] = {
                      ...last,
                      text: last.text + buffer,
                    };
                  }
                  return updated;
                });
                buffer = "";
              }
            }

            if (toolCallsDelta) {
              const toolCall: ToolCall = {
                name: toolCallsDelta.function?.name || "unknown",
                arguments: JSON.stringify(toolCallsDelta.function?.arguments || {}),
                output: "",
              };
              setMessages((prev) => {
                const updated = prev.slice(0, -1); // Remove empty assistant
                updated.push({ role: "tool", text: "", toolCall });
                updated.push({ role: "assistant", text: "" });
                return updated;
              });
            }
          } catch {
            // Skip malformed JSON lines
          }
        };

        while (true) {
          const { done, value } = await reader.read();
          if (done) break;

          const chunk = decoder.decode(value, { stream: true });
          const lines = chunk.split("\n");
          for (const line of lines) {
            processLine(line);
          }
        }

        // Flush remaining buffer
        if (buffer) {
          setMessages((prev) => {
            const updated = [...prev];
            const last = updated[updated.length - 1];
            if (last?.role === "assistant") {
              updated[updated.length - 1] = {
                ...last,
                text: last.text + buffer,
              };
            }
            return updated;
          });
          buffer = "";
        }

        // Update system store with response metadata
        const runtime = useSystemStore.getState().runtime;
        if (runtime.activeModel !== model) {
          useSystemStore.getState().setRuntime({ activeModel: model || "kaos" });
        }
      } catch (err: unknown) {
        if (err instanceof Error && err.name === "AbortError") {
          return; // User cancelled
        }
        const errorMsg =
          err instanceof Error ? err.message : "Connection failed";
        setError(errorMsg);
        setMessages((prev) => [
          ...prev,
          {
            role: "assistant",
            text: `Server unreachable. You're now in offline mode — previous responses are still available.`,
          },
        ]);
      } finally {
        setLoading(false);
        abortRef.current = null;
      }
    },
    [serverUrl, apiKey, messages, loading],
  );

  const cancel = useCallback(() => {
    abortRef.current?.abort();
  }, []);

  useEffect(() => {
    return () => {
      abortRef.current?.abort();
    };
  }, []);

  return { messages, loading, error, streamMessage, cancel };
}
