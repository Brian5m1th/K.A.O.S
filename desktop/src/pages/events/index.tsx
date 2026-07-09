import { useState, useEffect, useRef } from "react";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/shared/ui/card";
import { Button } from "@/shared/ui/button";
import { Badge } from "@/shared/ui/badge";
import { Play, Pause, Trash2, ShieldAlert, Cpu, Database, Info, GitBranch } from "lucide-react";
import { useAuthStore } from "@/application";

interface EventLog {
  id: string;
  source: "agent" | "system" | "database" | "webhook";
  type: string;
  message: string;
  timestamp: string;
}

const INITIAL_EVENTS: EventLog[] = [
  { id: "1", source: "system", type: "system:init", message: "Workspace K.A.O.S inicializado com sucesso no backend.", timestamp: new Date(Date.now() - 600000).toLocaleTimeString() },
  { id: "2", source: "database", type: "db:qdrant_sync", message: "Sincronização com banco vetorial Qdrant concluída. 142 fragmentos atualizados.", timestamp: new Date(Date.now() - 500000).toLocaleTimeString() },
  { id: "3", source: "agent", type: "agent:chat_reply", message: "Agente 'kaos-architect' gerou resposta para conversa a7c10490.", timestamp: new Date(Date.now() - 400000).toLocaleTimeString() },
  { id: "4", source: "webhook", type: "webhook:n8n_trigger", message: "Disparo automático enviado com sucesso para webhook n8n 'backup-vault'.", timestamp: new Date(Date.now() - 300000).toLocaleTimeString() },
];

export default function EventsPage() {
  const [events, setEvents] = useState<EventLog[]>(INITIAL_EVENTS);
  const [paused, setPaused] = useState(false);

  const serverUrl = useAuthStore((s) => s.serverUrl);
  const pausedRef = useRef(paused);

  useEffect(() => {
    pausedRef.current = paused;
  }, [paused]);

  useEffect(() => {
    const cleanUrl = serverUrl.replace(/\/+$/, "");
    const eventSource = new EventSource(`${cleanUrl}/api/observability/events/stream`);

    eventSource.onmessage = (event) => {
      if (pausedRef.current) return;
      if (event.data) {
        try {
          const parsed = JSON.parse(event.data);
          setEvents((prev) => [parsed, ...prev].slice(0, 100));
        } catch (e) {
          console.error("Failed to parse EventBus event:", e);
        }
      }
    };

    eventSource.onerror = (err) => {
      console.error("EventSource failed:", err);
    };

    return () => {
      eventSource.close();
    };
  }, [serverUrl]);

  const handleClear = () => {
    setEvents([]);
  };

  const getSourceIcon = (source: string) => {
    switch (source) {
      case "agent":
        return <Cpu className="h-3.5 w-3.5 text-accent-neon" />;
      case "database":
        return <Database className="h-3.5 w-3.5 text-warning" />;
      case "webhook":
        return <GitBranch className="h-3.5 w-3.5 text-accent-primary" />;
      default:
        return <Info className="h-3.5 w-3.5 text-text-dim" />;
    }
  };

  return (
    <div className="flex h-full flex-col gap-4 p-4">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-base font-semibold text-text-primary">Event Explorer</h1>
          <p className="text-xs text-text-muted mt-0.5">
            Timeline de eventos e disparos do EventBus do K.A.O.S em tempo real.
          </p>
        </div>
        <div className="flex items-center gap-2">
          <Button variant="subtle" size="sm" onClick={() => setPaused(!paused)}>
            {paused ? (
              <>
                <Play className="h-3.5 w-3.5 mr-1.5" />
                Resume Stream
              </>
            ) : (
              <>
                <Pause className="h-3.5 w-3.5 mr-1.5" />
                Pause Stream
              </>
            )}
          </Button>
          <Button variant="danger" size="sm" onClick={handleClear}>
            <Trash2 className="h-3.5 w-3.5 mr-1.5" />
            Clear
          </Button>
        </div>
      </div>

      <Card className="flex-1 flex flex-col border border-border-subtle bg-surface-raised/35 overflow-hidden">
        <CardHeader className="pb-2 border-b border-border-subtle">
          <CardTitle className="text-xs font-semibold text-text-muted uppercase tracking-wider">
            Live Stream logs
          </CardTitle>
        </CardHeader>
        <CardContent className="flex-1 overflow-y-auto p-4 space-y-3 font-mono text-xs scrollbar-thin bg-canvas/30">
          {events.length === 0 ? (
            <div className="h-full flex items-center justify-center text-text-dim">
              Aguardando eventos do sistema...
            </div>
          ) : (
            events.map((evt) => (
              <div
                key={evt.id}
                className="flex items-start justify-between border-b border-border-subtle/50 pb-2 hover:bg-surface-hover/20 px-1 rounded transition-colors"
              >
                <div className="flex items-start gap-3 min-w-0">
                  <div className="bg-bg-active p-1.5 rounded-lg shrink-0 mt-0.5">
                    {getSourceIcon(evt.source)}
                  </div>
                  <div className="min-w-0">
                    <div className="flex items-center gap-2">
                      <span className="text-[11px] font-bold text-text-primary uppercase">
                        {evt.type}
                      </span>
                      <Badge variant="neutral" className="text-[9px] scale-95 py-0 px-1 font-mono uppercase tracking-wider">
                        {evt.source}
                      </Badge>
                    </div>
                    <p className="text-[11px] text-text-muted mt-1 leading-snug break-words">
                      {evt.message}
                    </p>
                  </div>
                </div>
                <span className="text-[10px] text-text-dim shrink-0">{evt.timestamp}</span>
              </div>
            ))
          )}
        </CardContent>
      </Card>
    </div>
  );
}
