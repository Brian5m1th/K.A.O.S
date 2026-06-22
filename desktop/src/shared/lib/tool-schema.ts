export type ToolStatus = "pending" | "running" | "success" | "error";

export interface ToolEvent {
  id: string;
  name: string;
  status: ToolStatus;
  arguments?: unknown;
  output?: unknown;
  error?: string;
  startedAt: number;
  completedAt?: number;
}

export type ToolEventType =
  | "tool:start"
  | "tool:complete"
  | "tool:error"
  | "tool:progress";

export function createToolEvent(
  name: string,
  args?: unknown,
): ToolEvent {
  return {
    id: crypto.randomUUID?.() || `${Date.now()}-${Math.random().toString(36).slice(2, 9)}`,
    name,
    status: "pending",
    arguments: args,
    startedAt: Date.now(),
  };
}

export function completeToolEvent(
  event: ToolEvent,
  output: unknown,
): ToolEvent {
  return {
    ...event,
    status: "success",
    output,
    completedAt: Date.now(),
  };
}

export function failToolEvent(
  event: ToolEvent,
  error: string,
): ToolEvent {
  return {
    ...event,
    status: "error",
    error,
    completedAt: Date.now(),
  };
}
