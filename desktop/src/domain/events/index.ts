/**
 * Domain Events
 *
 * Typed event definitions for the internal event bus.
 * These describe state changes and user actions within the desktop app.
 *
 * FSD Migration: Event types will be added here during FSD refactoring.
 * See IMPLEMENTATION_GRAPH.md W4.5 for migration status.
 */

export interface DomainEvent {
  type: string;
  payload: unknown;
  timestamp: string;
}
