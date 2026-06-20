export interface ProviderFields {
  url: string;
  apiKey: string;
  model: string;
}

export type ProviderName = "ollama" | "openai" | "anthropic" | "google";

export type ProviderConfig = Record<ProviderName, ProviderFields>;

export type StatusMap = Partial<Record<ProviderName, string>>;
