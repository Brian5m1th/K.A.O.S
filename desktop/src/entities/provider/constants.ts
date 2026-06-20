import type { ProviderConfig, ProviderName } from "./types";

export const PROVIDER_ORDER: ProviderName[] = [
  "ollama",
  "openai",
  "anthropic",
  "google",
];

export const PROVIDER_LABELS: Record<ProviderName, string> = {
  ollama: "Ollama (Local)",
  openai: "OpenAI",
  anthropic: "Anthropic Claude",
  google: "Google Gemini",
};

export const DEFAULT_CONFIG: ProviderConfig = {
  ollama: { url: "http://localhost:11434", apiKey: "", model: "qwen3:14b", fastModel: "" },
  openai: { url: "https://api.openai.com/v1", apiKey: "", model: "gpt-4o", fastModel: "" },
  anthropic: {
    url: "https://api.anthropic.com",
    apiKey: "",
    model: "claude-sonnet-4-20250514",
    fastModel: "",
  },
  google: {
    url: "https://generativelanguage.googleapis.com",
    apiKey: "",
    model: "gemini-2.0-flash",
    fastModel: "",
  },
};

export const TEST_ENDPOINTS: Record<ProviderName, (base: string) => string> = {
  ollama: (base) => `${base}/api/tags`,
  openai: (base) => `${base}/models`,
  anthropic: (base) => base,
  google: (base) => `${base}/models`,
};
