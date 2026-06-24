import { useCallback, useEffect, useState } from "react";
import { useChatStore, useAuthStore, useConversationStore } from "@/shared/lib/stores";
import { ModelSelector } from "@/features/ask-ai/ui/ModelSelector";
import { ChatInput } from "@/features/ask-ai/ui/ChatInput";
import { MessageBubble } from "@/entities/message/ui/MessageBubble";
import { ScrollArea } from "@/shared/ui/scroll-area";
import { Badge } from "@/shared/ui/badge";
import { Button } from "@/shared/ui/button";
import { Separator } from "@/shared/ui/separator";
import { kaosFetch } from "@/shared/api/kaos-client";
import { Square, Loader2, MessageSquare, Plus, Trash2, History } from "lucide-react";

interface ProviderOption {
  id: string;
  name: string;
  models: string[];
}

function formatRelativeTime(dateStr: string): string {
  const now = Date.now();
  const d = new Date(dateStr).getTime();
  const diffMs = now - d;
  const diffMin = Math.floor(diffMs / 60000);
  if (diffMin < 1) return "now";
  if (diffMin < 60) return `${diffMin}m`;
  const diffHr = Math.floor(diffMin / 60);
  if (diffHr < 24) return `${diffHr}h`;
  const diffDay = Math.floor(diffHr / 24);
  if (diffDay < 30) return `${diffDay}d`;
  return new Date(dateStr).toLocaleDateString();
}

function HistorySidebar({
  userId,
  onSelectSession,
  onNewChat,
}: {
  userId: string;
  onSelectSession: (sessionId: string) => void;
  onNewChat: () => void;
}) {
  const sessions = useConversationStore((s) => s.sessions);
  const loading = useConversationStore((s) => s.loading);
  const total = useConversationStore((s) => s.total);
  const fetchSessions = useConversationStore((s) => s.fetchSessions);
  const deleteSession = useConversationStore((s) => s.deleteSession);

  useEffect(() => {
    if (userId) fetchSessions(userId);
  }, [userId, fetchSessions]);

  return (
    <div className="flex w-64 shrink-0 flex-col border-r border-border-subtle bg-surface-raised">
      {/* Header */}
      <div className="flex items-center justify-between border-b border-border-subtle px-3 py-2.5">
        <div className="flex items-center gap-1.5 text-xs font-semibold text-text-primary">
          <History className="h-3.5 w-3.5" />
          History
        </div>
        <button
          onClick={onNewChat}
          className="flex items-center gap-1 rounded-md bg-primary px-2 py-1 text-[11px] text-white hover:bg-primary/90 transition-colors"
          title="New conversation"
        >
          <Plus className="h-3 w-3" />
          New
        </button>
      </div>

      {/* Session list */}
      <ScrollArea className="flex-1">
        {loading && sessions.length === 0 ? (
          <div className="flex items-center justify-center py-8">
            <Loader2 className="h-4 w-4 animate-spin text-text-dim" />
          </div>
        ) : sessions.length === 0 ? (
          <div className="px-3 py-6 text-center text-xs text-text-dim">
            <MessageSquare className="mx-auto mb-2 h-5 w-5 opacity-40" />
            No conversations yet
          </div>
        ) : (
          <div className="py-1">
            {sessions.map((session) => (
              <div
                key={session.sessionId}
                className="group flex items-center gap-1 px-2 py-1.5 hover:bg-surface-hover cursor-pointer transition-colors rounded-sm mx-1"
                onClick={() => onSelectSession(session.sessionId)}
              >
                <MessageSquare className="h-3 w-3 shrink-0 text-text-dim" />
                <div className="min-w-0 flex-1">
                  <div className="truncate text-xs text-text-primary">
                    {session.workflowTypes.join(", ") || "Chat"}
                  </div>
                  <div className="text-[10px] text-text-dim">
                    {session.messageCount} msgs · {formatRelativeTime(session.lastMessageAt)}
                  </div>
                </div>
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    deleteSession(session.sessionId, userId);
                  }}
                  className="shrink-0 rounded p-0.5 text-text-dim opacity-0 group-hover:opacity-100 hover:bg-error/10 hover:text-error transition-all"
                  title="Delete session"
                >
                  <Trash2 className="h-3 w-3" />
                </button>
              </div>
            ))}
            {total > sessions.length && (
              <button
                onClick={() => fetchSessions(userId, Math.ceil(sessions.length / 20) + 1)}
                className="w-full px-3 py-2 text-[11px] text-primary hover:text-primary/80 transition-colors"
              >
                Load more ({total - sessions.length} remaining)
              </button>
            )}
          </div>
        )}
      </ScrollArea>

      {/* Footer */}
      <div className="border-t border-border-subtle px-3 py-2 text-[10px] text-text-dim">
        {total > 0 ? `${total} session${total > 1 ? "s" : ""}` : "No history"}
      </div>
    </div>
  );
}

export default function ChatPage() {
  const serverUrl = useAuthStore((s) => s.serverUrl);
  const userId = useAuthStore((s) => s.user?.id || "");

  const messages = useChatStore((s) => s.messages);
  const loading = useChatStore((s) => s.loading);
  const error = useChatStore((s) => s.error);
  const streamMessage = useChatStore((s) => s.streamMessage);
  const cancel = useChatStore((s) => s.cancel);
  const clearMessages = useChatStore((s) => s.clearMessages);
  const activeModel = useChatStore((s) => s.activeModel);
  const setActiveModel = useChatStore((s) => s.setActiveModel);

  const [showSidebar, setShowSidebar] = useState(true);
  const [providers, setProviders] = useState<ProviderOption[]>([]);
  const [selectedProvider, setSelectedProvider] = useState("ollama");
  const [defaultModel, setDefaultModel] = useState("kaos");
  const [fastModel, setFastModel] = useState("");
  const [fastMode, setFastMode] = useState(false);
  const [providersLoading, setProvidersLoading] = useState(true);

  const fetchProviders = useCallback(async () => {
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

        const active = data.activeProvider || "ollama";
        setSelectedProvider(active);

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
  }, [serverUrl, activeModel, setActiveModel]);

  useEffect(() => {
    fetchProviders();
  }, [fetchProviders]);

  const handleSend = (input: string) => {
    streamMessage(input, activeModel, serverUrl, "");
  };

  const handleNewChat = () => {
    clearMessages();
  };

  const handleSelectSession = (_sessionId: string) => {
    // TODO: Load session messages from API and populate chat-store
    // For now, just start a new chat
    clearMessages();
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
    <div className="flex h-full">
      {/* History sidebar */}
      {showSidebar && (
        <HistorySidebar
          userId={userId}
          onSelectSession={handleSelectSession}
          onNewChat={handleNewChat}
        />
      )}

      {/* Main chat area */}
      <div className="flex flex-1 flex-col">
        {error && (
          <div className="bg-warning/10 border-b border-warning/20 px-4 py-2 text-center text-sm text-warning">
            Offline mode — server connection lost
          </div>
        )}

        <div className="flex items-center justify-between border-b border-border-subtle px-4 py-2">
          <div className="flex items-center gap-2">
            {/* Toggle sidebar */}
            <button
              onClick={() => setShowSidebar(!showSidebar)}
              className="rounded-md p-1 text-text-dim hover:bg-surface-hover transition-colors"
              title={showSidebar ? "Hide history" : "Show history"}
            >
              <History className="h-4 w-4" />
            </button>

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
    </div>
  );
}
