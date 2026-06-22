import { useState, useRef, useCallback } from "react";
import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";
import { Paperclip, Play, RefreshCw } from "lucide-react";

interface Props {
  onSend: (text: string, files?: File[]) => void;
  loading: boolean;
  activeModel?: string;
}

export function ChatInput({ onSend, loading, activeModel }: Props) {
  const [text, setText] = useState("");
  const [attachedFiles, setAttachedFiles] = useState<File[]>([]);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleSubmit = useCallback(
    (e: React.FormEvent) => {
      e.preventDefault();
      if (!text.trim() && attachedFiles.length === 0) return;
      onSend(text.trim(), attachedFiles.length > 0 ? attachedFiles : undefined);
      setText("");
      setAttachedFiles([]);
    },
    [text, attachedFiles, onSend],
  );

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="border-t border-border-subtle bg-surface/60 backdrop-blur-md p-3 flex flex-col gap-2"
    >
      {attachedFiles.length > 0 && (
        <div className="flex gap-2 p-1 overflow-x-auto">
          {attachedFiles.map((f, i) => (
            <span
              key={i}
              className="text-xs bg-bg-active text-text-muted px-2 py-1 rounded border border-border-subtle"
            >
              {f.name}
            </span>
          ))}
        </div>
      )}
      <div className="flex items-center gap-2">
        <input
          type="file"
          multiple
          ref={fileInputRef}
          className="hidden"
          onChange={(e) =>
            e.target.files && setAttachedFiles(Array.from(e.target.files))
          }
        />
        <Button
          type="button"
          variant="subtle"
          size="sm"
          onClick={() => fileInputRef.current?.click()}
          title="Upload Documents (PDF, TXT, MD)"
        >
          <Paperclip className="h-4 w-4" />
        </Button>

        <Input
          value={text}
          onChange={(e) => setText(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder={
            loading
              ? "Waiting for response..."
              : `Command IA acting on ${activeModel || "local"}... (Use / for templates)`
          }
          disabled={loading}
          className="bg-canvas border-border-subtle h-10 text-sm focus-visible:border-accent-primary"
        />

        <Button
          type="submit"
          variant="primary"
          size="sm"
          className="h-10 px-4"
          isLoading={loading}
          disabled={loading || (!text.trim() && attachedFiles.length === 0)}
        >
          {loading ? <RefreshCw className="h-3.5 w-3.5 animate-spin" /> : <Play className="h-3.5 w-3.5 fill-current" />}
        </Button>
      </div>
    </form>
  );
}
