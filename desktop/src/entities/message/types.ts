export interface ToolCall {
  name: string;
  arguments: string;
  output: string;
}

export interface Message {
  role: "user" | "assistant" | "tool";
  text: string;
  toolCall?: ToolCall;
  thinking?: boolean;
}
