import { useState, useRef, useCallback } from "react";
import { Button } from "@/shared/ui/button";
import { Textarea } from "@/shared/ui/textarea";

interface Props {
  onSend: (message: string) => void;
  loading: boolean;
}

export function ChatInput({ onSend, loading }: Props) {
  const [input, setInput] = useState("");
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const handleSend = useCallback(() => {
    if (!input.trim() || loading) return;
    onSend(input.trim());
    setInput("");
    textareaRef.current?.focus();
  }, [input, loading, onSend]);

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="flex items-end gap-2 border-t border-zinc-800 bg-zinc-950/80 px-4 py-3">
      <Textarea
        ref={textareaRef}
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder={loading ? "Waiting for response..." : "Type a message..."}
        disabled={loading}
        className="min-h-[40px] max-h-[120px]"
        rows={1}
      />
      <Button
        onClick={handleSend}
        disabled={loading || !input.trim()}
        isLoading={loading}
        variant="primary"
        size="md"
        className="shrink-0"
      >
        Send
      </Button>
    </div>
  );
}
