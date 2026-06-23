let getAccessTokenFn: (() => string | null) | null = null;

export function setAccessTokenProvider(fn: () => string | null) {
  getAccessTokenFn = fn;
}

export async function kaosFetch(
  url: string,
  _fallbackKey: string = "",
  options: RequestInit = {},
): Promise<Response> {
  const headers = new Headers(options.headers);

  // Auto-detect auth from store (JWT preferred, API key fallback)
  const accessToken = getAccessTokenFn ? getAccessTokenFn() : null;
  if (accessToken) {
    headers.set("Authorization", `Bearer ${accessToken}`);
  } else if (_fallbackKey) {
    headers.set("X-API-Key", _fallbackKey);
  }

  headers.set("Content-Type", "application/json");
  return fetch(url, { ...options, headers });
}
