/**
 * InferenceStore — Desktop store for LLM model inference.
 *
 * Supports 5 providers (ollama, airllm, openai, gemini, claude)
 * via a single REST API. The Desktop never knows which framework
 * implements each provider.
 *
 * API: POST /api/inference/invoke
 *      POST /api/inference/stream (SSE)
 *      GET  /api/inference/models
 *      GET  /api/inference/health
 */

import { create } from "zustand";
import { kaosFetch } from "@/infrastructure";

interface InferenceResult {
  content: string;
  provider: string;
  model: string;
  tokens_used: number;
  latency_ms: number;
}

interface ModelList {
  [provider: string]: string[];
}

interface InferenceState {
  loading: boolean;
  error: string | null;
  lastResult: InferenceResult | null;
  models: ModelList;

  invoke: (messages: Array<{ role: string; content: string }>, provider?: string, model?: string, serverUrl?: string) => Promise<InferenceResult | null>;
  fetchModels: (serverUrl?: string) => Promise<ModelList>;
  streamInference: (messages: Array<{ role: string; content: string }>, provider?: string, serverUrl?: string, onChunk?: (chunk: string) => void) => Promise<void>;
}

const DEFAULT_URL = "http://localhost:8000";

export const useInferenceStore = create<InferenceState>((set) => ({
  loading: false,
  error: null,
  lastResult: null,
  models: {},

  invoke: async (messages, provider = "ollama", model, serverUrl = DEFAULT_URL) => {
    set({ loading: true, error: null });
    try {
      const res = await kaosFetch(`${serverUrl}/api/inference/invoke`, "", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages, provider, model }),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      const result: InferenceResult = {
        content: data.content,
        provider: data.provider,
        model: data.model,
        tokens_used: data.tokens_used,
        latency_ms: data.latency_ms,
      };
      set({ loading: false, lastResult: result });
      return result;
    } catch (e) {
      set({ loading: false, error: String(e) });
      return null;
    }
  },

  fetchModels: async (serverUrl = DEFAULT_URL) => {
    try {
      const res = await kaosFetch(`${serverUrl}/api/inference/models`, "");
      if (!res.ok) return {};
      const data = await res.json();
      set({ models: data });
      return data;
    } catch {
      return {};
    }
  },

  streamInference: async (messages, provider = "ollama", serverUrl = DEFAULT_URL, onChunk) => {
    set({ loading: true, error: null });
    try {
      const res = await fetch(`${serverUrl}/api/inference/stream`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages, provider }),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const reader = res.body?.getReader();
      const decoder = new TextDecoder();
      if (!reader) throw new Error("No response body");

      let buffer = "";
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split("\n");
        buffer = lines.pop() || "";
        for (const line of lines) {
          if (line.startsWith("data: ") && line !== "data: [DONE]") {
            try {
              const parsed = JSON.parse(line.slice(6));
              onChunk?.(parsed.content);
            } catch { /* skip malformed */ }
          }
        }
      }
      set({ loading: false });
    } catch (e) {
      set({ loading: false, error: String(e) });
    }
  },
}));
