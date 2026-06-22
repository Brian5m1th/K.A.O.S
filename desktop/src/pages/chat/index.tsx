import { useEffect, useState } from "react";
import { useChatStore } from "@/shared/lib/stores";
import { useAuthStore } from "@/shared/lib/stores";
import { ModelSelector } from "@/features/ask-ai/ui/ModelSelector";
import { ChatInput } from "@/features/ask-ai/ui/ChatInput";
import { MessageBubble } from "@/entities/message/ui/MessageBubble";
import { ScrollArea } from "@/shared/ui/scroll-area";
import { Badge } from "@/shared/ui/badge";
import { Button } from "@/shared/ui/button";
import { Separator } from "@/shared/ui/separator";
import { kaosFetch } from "@/shared/api/kaos-client";
import { Square, Loader2 } from "lucide-react";

interface ProviderOption {
  id: string;
  name: string;
  models: string[];
}

export default function ChatPage() {
  const serverUrl = useAuthStore((s) => s.serverUrl);

  const messages = useChatStore((s) => s.messages);
  const loading = useChatStore((s) => s.loading);
  const error = useChatStore((s) => s.error);
  const streamMessage = useChatStore((s) => s.streamMessage);
  const cancel = useChatStore((s) => s.cancel);
  const activeModel = useChatStore((s) => s.activeModel);
  const setActiveModel = useChatStore((s) => s.setActiveModel);

  // Providers state
  const [providers, setProviders] = useState<ProviderOption[]>([]);
  const [selectedProvider, setSelectedProvider] = useState("ollama");
  const [defaultModel, setDefaultModel] = useState("kaos");
  const [fastModel, setFastModel] = useState("");
  const [fastMode, setFastMode] = useState(false);
  const [providersLoading, setProvidersLoading] = useState(true);

  // Fetch providers on mount
  useEffect(() => {
    const fetchProviders = async () => {
      try {
        const res = await kaosFetch(`${serverUrl}/api/providers`, "");
        if (res.ok) {
          const data = await res.json();
          const mapped: ProviderOption[] = (data.providers || []).map((p: any) => ({
            id: p.id,
            name: p.name,
            models: p.models || [],
          }));
          setProviders(mapped);

          // Set active provider
          const active = data.activeProvider || "ollama";
          setSelectedProvider(active);

          // Set default model from active provider
          const activeProvider = mapped.find((p: ProviderOption) => p.id === active);
          if (activeProvider?.models?.length) {
            const defaultM = activeProvider.models[0];
            setDefaultModel(defaultM);
            setFastModel(activeProvider.models.length > 1 ? activeProvider.models[1] : "");
            if (!activeModel) setActiveModel(defaultM);
          }
        }
      } catch {
        // Backend offline — keep defaults
      } finally {
        setProvidersLoading(false);
      }
    };
    fetchProviders();
  }, [serverUrl, activeModel, setActiveModel]);

  const handleSend = (input: string) => {
    streamMessage(input, activeModel, serverUrl, "");
  };

  const handleProviderChange = (providerId: string) => {
    setSelectedProvider(providerId);
    setFastMode(false);
  };

  const handleModelChange = (model: string) => {
    setActiveModel(model);
    if (fastMode && model === defaultModel) setFastMode(false);
  };

  const handleFastModeToggle = (active: boolean) => {
    setFastMode(active);
  };

  return (
    <div className="flex h-full flex-col">
      {error && (
        <div className="bg-warning/10 border-b border-warning/20 px-4 py-2 text-center text-sm text-warning">
          Offline mode — server connection lost
        </div>
      )}

      <div className="flex items-center justify-between border-b border-border-subtle px-4 py-2">
        <div className="flex items-center gap-2">
          <span className="text-sm font-semibold text-text-primary">Chat</span>
          {providersLoading ? (
            <div className="flex items-center gap-1.5 text-xs text-text-dim">
              <Loader2 className="h-3 w-3 animate-spin" />
              Loading providers...
            </div>
          ) : (
            <ModelSelector
              currentModel={activeModel}
              defaultModel={defaultModel}
              fastModel={fastModel}
              fastMode={fastMode}
              providers={providers}
              selectedProvider={selectedProvider}
              onProviderChange={handleProviderChange}
              onModelChange={handleModelChange}
              onFastModeToggle={handleFastModeToggle}
            />
          )}
          {loading && (
            <>
              <Badge variant="info">Generating...</Badge>
              <button
                onClick={cancel}
                className="ml-1 flex items-center gap-1 rounded-md bg-error/10 px-2 py-0.5 text-[11px] text-error hover:bg-error/20 transition-colors"
              >
                <Square className="h-2.5 w-2.5 fill-current" />
                Stop
              </button>
            </>
          )}
        </div>
        <Button
          onClick={() => cancel()}
          variant="danger"
          size="sm"
          disabled={loading}
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

      <ChatInput onSend={handleSend} loading={loading} activeModel={activeModel || defaultModel} />
    </div>
  );
}
