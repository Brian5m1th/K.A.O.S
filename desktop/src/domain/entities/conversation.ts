/**
 * Conversation Entity — core domain object for chat sessions.
 */

export interface ConversationMessage {
  id: string;
  sessionId: string;
  role: "user" | "assistant" | "system";
  content: string;
  workflowType?: string;
  tokensUsed?: number;
  modelUsed?: string;
  provider?: string;
  createdAt: string;
}

export interface ConversationSession {
  id: string;
  userId: string;
  startedAt: string;
  lastMessageAt: string;
  messageCount: number;
  workflowTypes: string[];
  totalTokens: number;
}
