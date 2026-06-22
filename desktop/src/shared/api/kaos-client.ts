import { useAuthStore } from "@/shared/lib/stores";

export async function kaosFetch(
  url: string,
  _fallbackKey: string = "",
  options: RequestInit = {},
): Promise<Response> {
  const headers = new Headers(options.headers);

  // Auto-detect auth from store (JWT preferred, API key fallback)
  const { accessToken } = useAuthStore.getState();
  if (accessToken) {
    headers.set("Authorization", `Bearer ${accessToken}`);
  } else if (_fallbackKey) {
    headers.set("X-API-Key", _fallbackKey);
  }

  headers.set("Content-Type", "application/json");
  return fetch(url, { ...options, headers });
}
