export async function kaosFetch(
  url: string,
  apiKey: string,
  options: RequestInit = {},
): Promise<Response> {
  const headers = new Headers(options.headers);
  headers.set("X-API-Key", apiKey);
  return fetch(url, { ...options, headers });
}
