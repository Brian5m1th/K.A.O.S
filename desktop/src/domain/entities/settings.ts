/**
 * Settings Entity — user and system configuration.
 */

export type ProviderType = "ollama" | "openai" | "anthropic" | "gemini" | "airllm";

export interface ProviderSetting {
  name: ProviderType;
  apiUrl?: string;
  apiKey?: string;
  model?: string;
  isActive: boolean;
}

export interface SystemSetting {
  key: string;
  value: string;
  category: "general" | "inference" | "storage" | "observability";
}

export interface UserPreferences {
  theme: "light" | "dark" | "system";
  language: string;
  defaultModel?: string;
  autoIndexVault: boolean;
}
