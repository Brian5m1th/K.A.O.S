import { useEffect, useRef, useCallback } from "react";

interface WebSocketOptions {
  url: string;
  onMessage: (data: unknown) => void;
  onError?: (error: Event) => void;
  onOpen?: () => void;
  reconnectInterval?: number;
  maxRetries?: number;
}

export function useWebSocket({
  url,
  onMessage,
  onError,
  onOpen,
  reconnectInterval = 3000,
  maxRetries = 5,
}: WebSocketOptions) {
  const wsRef = useRef<WebSocket | null>(null);
  const retriesRef = useRef(0);
  const mountedRef = useRef(true);

  const connect = useCallback(() => {
    if (!mountedRef.current || retriesRef.current >= maxRetries) return;

    try {
      const ws = new WebSocket(url);

      ws.onopen = () => {
        retriesRef.current = 0;
        onOpen?.();
      };

      ws.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          onMessage(data);
        } catch {
          // Non-JSON messages are ignored
        }
      };

      ws.onerror = (error) => {
        onError?.(error);
      };

      ws.onclose = () => {
        if (mountedRef.current) {
          retriesRef.current++;
          setTimeout(connect, reconnectInterval);
        }
      };

      wsRef.current = ws;
    } catch {
      // WebSocket not available, will be handled by parent with fallback
    }
  }, [url, onMessage, onError, onOpen, reconnectInterval, maxRetries]);

  useEffect(() => {
    mountedRef.current = true;
    connect();

    return () => {
      mountedRef.current = false;
      wsRef.current?.close();
    };
  }, [connect]);

  const send = useCallback((data: unknown) => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify(data));
    }
  }, []);

  return { send, isConnected: () => wsRef.current?.readyState === WebSocket.OPEN };
}
