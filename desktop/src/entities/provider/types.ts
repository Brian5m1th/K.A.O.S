export interface ProviderFields {
  url: string;
  apiKey: string;
  model: string;
  fastModel: string;
}

export type ProviderName = "ollama" | "openai" | "anthropic" | "google";

export type ProviderConfig = Record<ProviderName, ProviderFields>;

export type StatusMap = Partial<Record<ProviderName, string>>;

export interface ConfigResponse {
  [key: string]: unknown;
  _activeProvider: ProviderName;
  ollama: ProviderFields;
  openai: ProviderFields;
  anthropic: ProviderFields;
  google: ProviderFields;
}
