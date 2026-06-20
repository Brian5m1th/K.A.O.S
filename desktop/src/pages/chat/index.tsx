import { useChatStream } from "@/features/ask-ai/hooks/useChatStream";
import { ChatInput } from "@/features/ask-ai/ui/ChatInput";
import { MessageBubble } from "@/entities/message/ui/MessageBubble";
import { ScrollArea } from "@/shared/ui/scroll-area";
import { Badge } from "@/shared/ui/badge";
import { Button } from "@/shared/ui/button";
import { Separator } from "@/shared/ui/separator";

interface Props {
  serverUrl: string;
  apiKey: string;
  onDisconnect: () => void;
}

export default function ChatPage({ serverUrl, apiKey, onDisconnect }: Props) {
  const { messages, loading, error, streamMessage } = useChatStream(
    serverUrl,
    apiKey,
  );

  return (
    <div className="flex h-full flex-col">
      {error && (
        <div className="bg-warning/10 border-b border-warning/20 px-4 py-2 text-center text-sm text-warning">
          Offline mode — server connection lost
        </div>
      )}

      <div className="flex items-center justify-between border-b border-zinc-800 px-4 py-2">
        <div className="flex items-center gap-2">
          <span className="text-sm font-semibold text-zinc-100">Chat</span>
          {loading && (
            <Badge variant="info">Generating...</Badge>
          )}
        </div>
        <Button
          onClick={onDisconnect}
          variant="danger"
          size="sm"
        >
          Disconnect
        </Button>
      </div>

      <ScrollArea className="flex-1 px-4 py-3">
        <div className="flex flex-col">
          {messages.map((msg, i) => (
            <MessageBubble
              key={i}
              message={msg}
              isLast={i === messages.length - 1}
            />
          ))}
        </div>
      </ScrollArea>

      <Separator />

      <ChatInput onSend={streamMessage} loading={loading} />
    </div>
  );
}
