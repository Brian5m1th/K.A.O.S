import { describe, it, expect, vi, beforeEach } from "vitest";
import { useAgentStore } from "@/shared/lib/stores/agent-store";
import { kaosFetch } from "@/shared/api/kaos-client";

vi.mock("@/shared/api/kaos-client", () => ({ kaosFetch: vi.fn() }));
const mockFetch = vi.mocked(kaosFetch);
const cfg = { id: "a1", name: "Agent", model: "gpt-4", systemPrompt: "Test", temperature: 0.7, topP: 1 };

describe("Agent Store", () => {
  beforeEach(() => { useAgentStore.setState({ agents: {} }); mockFetch.mockReset(); });

  it("register should add agent with idle status", () => {
    useAgentStore.getState().register(cfg);
    expect(useAgentStore.getState().agents["a1"].status).toBe("idle");
  });

  it("unregister should remove agent", () => {
    useAgentStore.getState().register(cfg);
    useAgentStore.getState().unregister("a1");
    expect(useAgentStore.getState().agents["a1"]).toBeUndefined();
  });

  it("updateConfig should partial merge", () => {
    useAgentStore.getState().register(cfg);
    useAgentStore.getState().updateConfig("a1", { temperature: 0.2 });
    expect(useAgentStore.getState().agents["a1"].config.temperature).toBe(0.2);
  });

  it("setError should set error status", () => {
    useAgentStore.getState().register(cfg);
    useAgentStore.getState().setError("a1", "fail");
    expect(useAgentStore.getState().agents["a1"].status).toBe("error");
    expect(useAgentStore.getState().agents["a1"].error).toBe("fail");
  });

  it("start should call API and set running", async () => {
    useAgentStore.getState().register(cfg);
    mockFetch.mockResolvedValue(new Response(null, { status: 200 }));
    await useAgentStore.getState().start("a1");
    expect(mockFetch).toHaveBeenCalledWith(expect.stringContaining("/start"), undefined, expect.anything());
    expect(useAgentStore.getState().agents["a1"].status).toBe("running");
  });

  it("start should set error on failure", async () => {
    useAgentStore.getState().register(cfg);
    mockFetch.mockRejectedValue(new Error("fail"));
    await useAgentStore.getState().start("a1");
    expect(useAgentStore.getState().agents["a1"].status).toBe("error");
  });

  it("pause should update status", async () => {
    useAgentStore.getState().register(cfg);
    mockFetch.mockResolvedValue(new Response(null, { status: 200 }));
    await useAgentStore.getState().pause("a1");
    expect(useAgentStore.getState().agents["a1"].status).toBe("paused");
  });
});
