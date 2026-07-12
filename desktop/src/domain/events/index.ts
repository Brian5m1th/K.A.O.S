/**
 * Domain Events
 *
 * Typed event definitions for the internal event bus.
 * These describe state changes and user actions within the desktop app.
 *
 * TODO: Populate with specific event types as the FSD migration progresses.
 */

export interface DomainEvent {
  type: string;
  payload: unknown;
  timestamp: string;
}
