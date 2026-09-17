import type { HttpRequestOptions } from "../Types/HttpRequestOptions";

// The API reports failures as { "error": "..." }; fall back to the status code.
async function readErrorMessage(response: Response): Promise<string> {
  const fallback = `The people API returned HTTP ${response.status}.`;

  try {
    const text = await response.text();
    if (!text) return fallback;

    const body: unknown = JSON.parse(text);
    if (typeof body === "object" && body !== null && "error" in body && typeof body.error === "string") {
      return body.error;
    }
  } catch {
    // Non-JSON error bodies are not useful to show, so keep the fallback.
  }

  return fallback;
}

async function request<T>(
  method: "GET" | "POST" | "PUT" | "DELETE",
  url: string,
  body?: unknown,
  options: HttpRequestOptions = {},
): Promise<T> {
  const hasBody = body !== undefined;

  const response = await fetch(url, {
    method,
    signal: options.signal,
    headers: {
      Accept: "application/json",
      ...(hasBody ? { "Content-Type": "application/json" } : {}),
      ...options.headers,
    },
    ...(hasBody ? { body: JSON.stringify(body) } : {}),
  });

  if (!response.ok) {
    throw new Error(await readErrorMessage(response));
  }

  // 204 responses and empty bodies have nothing to parse.
  if (response.status === 204) {
    return undefined as T;
  }

  const text = await response.text();
  return (text ? JSON.parse(text) : undefined) as T;
}

export function get<T = unknown>(url: string, options?: HttpRequestOptions) {
  return request<T>("GET", url, undefined, options);
}

export function post<T = unknown>(url: string, body?: unknown, options?: HttpRequestOptions) {
  return request<T>("POST", url, body, options);
}

export function put<T = unknown>(url: string, body?: unknown, options?: HttpRequestOptions) {
  return request<T>("PUT", url, body, options);
}

export function del<T = unknown>(url: string, options?: HttpRequestOptions) {
  return request<T>("DELETE", url, undefined, options);
}

export const http = { get, post, put, delete: del };
