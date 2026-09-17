export interface HttpRequestOptions {
  signal?: AbortSignal;
  headers?: Record<string, string>;
}
