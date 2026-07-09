import { describe, it, expect, beforeEach, vi } from "vitest";
import {
  kaosFetch,
  setAccessTokenProvider,
  setServerUrlProvider,
} from "@/infrastructure/http";

describe("kaos-client", () => {
  beforeEach(() => {
    setAccessTokenProvider(() => null);
    setServerUrlProvider(() => "http://localhost:8000");
    vi.mocked(fetch).mockReset();
  });

  describe("setAccessTokenProvider", () => {
    it("should register a token provider", () => {
      const provider = vi.fn(() => "token-123");
      setAccessTokenProvider(provider);
      expect(provider).not.toHaveBeenCalled(); // lazy evaluation
    });
  });

  describe("setServerUrlProvider", () => {
    it("should register a server URL provider", () => {
      const provider = vi.fn(() => "http://custom:8000");
      setServerUrlProvider(provider);
      expect(provider).not.toHaveBeenCalled();
    });
  });

  describe("kaosFetch", () => {
    it("should inject Authorization header when token is available", async () => {
      setAccessTokenProvider(() => "my-jwt-token");
      vi.mocked(fetch).mockResolvedValue(new Response(null, { status: 200 }));

      await kaosFetch("/api/data");

      expect(fetch).toHaveBeenCalledTimes(1);
      const [url, options] = vi.mocked(fetch).mock.calls[0];
      expect(url).toBe("http://localhost:8000/api/data");
      const headers = new Headers(options?.headers);
      expect(headers.get("Authorization")).toBe("Bearer my-jwt-token");
      expect(headers.get("Content-Type")).toBe("application/json");
    });

    it("should inject X-API-Key when fallback key is provided and no token", async () => {
      setAccessTokenProvider(() => null);
      vi.mocked(fetch).mockResolvedValue(new Response(null, { status: 200 }));

      await kaosFetch("/api/data", "fallback-key-123");

      expect(fetch).toHaveBeenCalledTimes(1);
      const [, options] = vi.mocked(fetch).mock.calls[0];
      const headers = new Headers(options?.headers);
      expect(headers.get("X-API-Key")).toBe("fallback-key-123");
      expect(headers.get("Content-Type")).toBe("application/json");
    });

    it("should not inject auth headers when no token and no fallback", async () => {
      setAccessTokenProvider(() => null);
      vi.mocked(fetch).mockResolvedValue(new Response(null, { status: 200 }));

      await kaosFetch("/api/data");

      const [, options] = vi.mocked(fetch).mock.calls[0];
      const headers = new Headers(options?.headers);
      expect(headers.get("Authorization")).toBeNull();
      expect(headers.get("X-API-Key")).toBeNull();
      expect(headers.get("Content-Type")).toBe("application/json");
    });

    it("should preserve existing custom headers", async () => {
      vi.mocked(fetch).mockResolvedValue(new Response(null, { status: 200 }));

      await kaosFetch("/api/data", undefined, {
        headers: { "X-Custom": "value123" },
      });

      const [, options] = vi.mocked(fetch).mock.calls[0];
      const headers = new Headers(options?.headers);
      expect(headers.get("X-Custom")).toBe("value123");
      expect(headers.get("Content-Type")).toBe("application/json");
    });

    it("should not modify absolute URLs", async () => {
      vi.mocked(fetch).mockResolvedValue(new Response(null, { status: 200 }));

      await kaosFetch("https://external.api.com/route");

      const [url] = vi.mocked(fetch).mock.calls[0];
      expect(url).toBe("https://external.api.com/route");
    });

    it("should fallback to default server URL when provider is not set", async () => {
      setServerUrlProvider(() => "http://localhost:8000");
      vi.mocked(fetch).mockResolvedValue(new Response(null, { status: 200 }));

      await kaosFetch("/test");

      const [url] = vi.mocked(fetch).mock.calls[0];
      expect(url).toBe("http://localhost:8000/test");
    });

    it("should pass through options like method and body", async () => {
      vi.mocked(fetch).mockResolvedValue(new Response(null, { status: 200 }));
      const body = JSON.stringify({ key: "value" });

      await kaosFetch("/api/submit", undefined, {
        method: "POST",
        body,
      });

      const [, options] = vi.mocked(fetch).mock.calls[0];
      expect(options?.method).toBe("POST");
      expect(options?.body).toBe(body);
    });

    it("should return the raw Response object", async () => {
      const response = new Response(JSON.stringify({ ok: true }), { status: 200 });
      vi.mocked(fetch).mockResolvedValue(response);

      const result = await kaosFetch("/api/data");
      expect(result).toBe(response);
    });

    it("should propagate fetch errors", async () => {
      const error = new TypeError("Network error");
      vi.mocked(fetch).mockRejectedValue(error);

      await expect(kaosFetch("/api/data")).rejects.toThrow("Network error");
    });
  });
});