import { describe, it, expect, vi, beforeEach } from "vitest";
import { useAuthStore } from "@/application/stores/auth-store";
import { kaosFetch } from "@/infrastructure/http";

vi.mock("@/infrastructure/http", () => ({
  kaosFetch: vi.fn(),
}));

const mockKaosFetch = vi.mocked(kaosFetch);

describe("Auth Store", () => {
  beforeEach(() => {
    useAuthStore.setState({
      accessToken: null, refreshToken: null, maskedKey: "",
      user: null, serverUrl: "http://localhost:8000",
      configured: false, checking: true, error: null,
    });
    mockKaosFetch.mockReset();
  });

  it("should start with no tokens and checking true", () => {
    const s = useAuthStore.getState();
    expect(s.accessToken).toBeNull();
    expect(s.checking).toBe(true);
  });

  it("clearError should reset error", () => {
    useAuthStore.setState({ error: "err" });
    useAuthStore.getState().clearError();
    expect(useAuthStore.getState().error).toBeNull();
  });

  it("checkSetupStatus should query parallel endpoints", async () => {
    mockKaosFetch
      .mockResolvedValueOnce(new Response(JSON.stringify({ configured: false, has_users: false }), { status: 200 }))
      .mockResolvedValueOnce(new Response(JSON.stringify({ has_key: true, masked: "sk-***" }), { status: 200 }));
    await useAuthStore.getState().checkSetupStatus();
    expect(useAuthStore.getState().checking).toBe(false);
    expect(useAuthStore.getState().maskedKey).toBeTruthy();
  });

  it("login should store tokens on success", async () => {
    mockKaosFetch.mockResolvedValue(new Response(JSON.stringify({
      access_token: "jwt-a", refresh_token: "jwt-r",
      user: { id: "1", name: "T", email: "t@t.com", role: "admin" },
    }), { status: 200 }));
    await useAuthStore.getState().login("t@t.com", "pw");
    expect(useAuthStore.getState().accessToken).toBe("jwt-a");
    expect(useAuthStore.getState().user?.name).toBe("T");
  });

  it("login should handle backend error", async () => {
    mockKaosFetch.mockResolvedValue(new Response(JSON.stringify({ detail: "Invalid" }), { status: 401 }));
    await useAuthStore.getState().login("t@t.com", "bad");
    expect(useAuthStore.getState().error).toBe("Invalid");
  });

  it("login should handle network error", async () => {
    mockKaosFetch.mockRejectedValue(new TypeError("Network error"));
    await useAuthStore.getState().login("t@t.com", "pw");
    expect(useAuthStore.getState().error).toBe("Cannot reach the backend server");
  });

  it("register should store tokens and set configured", async () => {
    mockKaosFetch.mockResolvedValue(new Response(JSON.stringify({
      access_token: "jwt-a", refresh_token: "jwt-r",
      user: { id: "2", name: "New", email: "n@t.com", role: "user" },
    }), { status: 200 }));
    await useAuthStore.getState().register("New", "n@t.com", "pw");
    expect(useAuthStore.getState().configured).toBe(true);
  });

  it("refreshAccessToken should update tokens", async () => {
    useAuthStore.setState({ refreshToken: "old-r", accessToken: "old-a" });
    mockKaosFetch.mockResolvedValue(new Response(JSON.stringify({ access_token: "new-a", refresh_token: "new-r" }), { status: 200 }));
    await useAuthStore.getState().refreshAccessToken();
    expect(useAuthStore.getState().accessToken).toBe("new-a");
  });

  it("refreshAccessToken should clear auth on failure", async () => {
    useAuthStore.setState({ accessToken: "a", user: { id: "1", name: "T", email: "t@t.com", role: "user" } });
    mockKaosFetch.mockRejectedValue(new Error("fail"));
    await useAuthStore.getState().refreshAccessToken();
    expect(useAuthStore.getState().accessToken).toBeNull();
    expect(useAuthStore.getState().user).toBeNull();
  });

  it("logout should clear all auth data", () => {
    useAuthStore.setState({ accessToken: "t", refreshToken: "r", user: { id: "1", name: "T", email: "t@t.com", role: "user" } });
    useAuthStore.getState().logout();
    expect(useAuthStore.getState().accessToken).toBeNull();
    expect(useAuthStore.getState().user).toBeNull();
  });
});
