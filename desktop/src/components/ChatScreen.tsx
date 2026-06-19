import { useState, useRef, useEffect } from "react";

interface Props {
  serverUrl: string;
  onDisconnect: () => void;
}

interface Message {
  role: "user" | "assistant";
  text: string;
}

export default function ChatScreen({ serverUrl, onDisconnect }: Props) {
  const [messages, setMessages] = useState<Message[]>([
    { role: "assistant", text: "KAOS initialized. How can I help you?" },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [offline, setOffline] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim() || loading) return;

    const userMsg: Message = { role: "user", text: input.trim() };
    setMessages((prev) => [...prev, userMsg]);
    setInput("");
    setLoading(true);

    try {
      const resp = await fetch(`${serverUrl.replace(/\/+$/, "")}/v1/chat/completions`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          model: "kaos",
          messages: messages.concat(userMsg).map((m) => ({
            role: m.role,
            content: m.text,
          })),
          stream: false,
        }),
      });

      if (resp.ok) {
        const data = await resp.json();
        const reply = data.choices?.[0]?.message?.content || "No response";
        setMessages((prev) => [...prev, { role: "assistant", text: reply }]);
      } else {
        throw new Error(`HTTP ${resp.status}`);
      }
    } catch {
      setOffline(true);
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "Server unreachable. You're now in offline mode — previous responses are still available.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div style={{ height: "100%", display: "flex", flexDirection: "column" }}>
      {offline && (
        <div style={{
          padding: "8px 16px",
          background: "#ff9800",
          color: "#000",
          textAlign: "center",
          fontSize: "13px",
        }}>
          Offline mode — server connection lost
        </div>
      )}

      <div style={{ flex: 1, overflow: "auto", padding: "16px" }}>
        {messages.map((msg, i) => (
          <div key={i} style={{
            marginBottom: "12px",
            display: "flex",
            justifyContent: msg.role === "user" ? "flex-end" : "flex-start",
          }}>
            <div style={{
              maxWidth: "70%",
              padding: "10px 14px",
              borderRadius: "12px",
              background: msg.role === "user" ? "#1976d2" : "#333",
              color: "#e0e0e0",
              whiteSpace: "pre-wrap",
            }}>
              {msg.text}
            </div>
          </div>
        ))}
        <div ref={bottomRef} />
      </div>

      <div style={{
        padding: "12px 16px",
        borderTop: "1px solid #333",
        display: "flex",
        gap: "8px",
      }}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder={loading ? "Waiting for response..." : "Type a message..."}
          disabled={loading}
          style={{
            flex: 1,
            padding: "10px",
            borderRadius: "6px",
            border: "1px solid #555",
            background: "#2a2a2a",
            color: "#e0e0e0",
          }}
        />
        <button
          onClick={sendMessage}
          disabled={loading || !input.trim()}
          style={{
            padding: "10px 20px",
            borderRadius: "6px",
            border: "none",
            background: loading ? "#555" : "#1976d2",
            color: "white",
            cursor: loading ? "not-allowed" : "pointer",
          }}
        >
          Send
        </button>
        <button
          onClick={onDisconnect}
          title="Disconnect and return to setup"
          style={{
            padding: "10px",
            borderRadius: "6px",
            border: "none",
            background: "#f44336",
            color: "white",
            cursor: "pointer",
          }}
        >
          Disconnect
        </button>
      </div>
    </div>
  );
}
