import { useState, useRef, useCallback, useEffect } from "react";
import type { Message } from "@/entities/message/types";
import { kaosFetch } from "@/shared/api/kaos-client";

export function useChatStream(serverUrl: string, apiKey: string) {
  const [messages, setMessages] = useState<Message[]>([
    { role: "assistant", text: "KAOS initialized. How can I help you?" },
  ]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const tokenBuffer = useRef("");
  const frameTimer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const messagesRef = useRef<Message[]>(messages);

  messagesRef.current = messages;

  const flushBuffer = useCallback(() => {
    if (!tokenBuffer.current) return;

    setMessages((prev) => {
      const last = prev[prev.length - 1];
      if (last?.role === "assistant") {
        const updated = [...prev];
        updated[updated.length - 1] = {
          ...last,
          text: last.text + tokenBuffer.current,
        };
        return updated;
      }
      return [...prev, { role: "assistant", text: tokenBuffer.current }];
    });

    tokenBuffer.current = "";
    frameTimer.current = null;
  }, []);

  const streamMessage = useCallback(
    async (input: string, model?: string) => {
      if (!input.trim() || loading) return;

      const userMsg: Message = { role: "user", text: input.trim() };

      setMessages((prev) => [...prev, userMsg]);
      setLoading(true);
      setError(null);

      try {
        const cleanUrl = serverUrl.replace(/\/+$/, "");

        const currentMessages = messagesRef.current
          .filter((m) => m.role !== "assistant" || m.text)
          .concat(userMsg);

        setMessages((prev) => [...prev, { role: "assistant", text: "" }]);

        const response = await kaosFetch(
          `${cleanUrl}/v1/chat/completions`,
          apiKey,
          {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              model: model || "kaos",
              messages: currentMessages.map((m) => ({
                role: m.role,
                content: m.text,
              })),
              stream: false,
            }),
          },
        );

        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();
        const reply = data.choices?.[0]?.message?.content || "No response";

        setMessages((prev) => {
          const updated = [...prev];
          updated[updated.length - 1] = {
            role: "assistant",
            text: reply,
          };
          return updated;
        });
      } catch (err) {
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
      }
    },
    [serverUrl, apiKey, loading],
  );

  useEffect(() => {
    return () => {
      if (frameTimer.current) clearTimeout(frameTimer.current);
    };
  }, []);

  return { messages, loading, error, streamMessage };
}
