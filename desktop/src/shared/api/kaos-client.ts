let getAccessTokenFn: (() => string | null) | null = null;
let getServerUrlFn: (() => string) | null = null;

export function setAccessTokenProvider(fn: () => string | null) {
  getAccessTokenFn = fn;
}

export function setServerUrlProvider(fn: () => string) {
  getServerUrlFn = fn;
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

  // Prepends serverUrl if relative path is provided
  let finalUrl = url;
  if (url.startsWith("/")) {
    const serverUrl = getServerUrlFn ? getServerUrlFn() : "http://localhost:8000";
    finalUrl = `${serverUrl.replace(/\/$/, "")}${url}`;
  }

  return fetch(finalUrl, { ...options, headers });
}
