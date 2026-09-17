import { describe, expect, it, vi } from "vitest";
import { del, get, post, put } from "./http";

function mockFetch(response: Response) {
  const fetchMock = vi.fn().mockResolvedValue(response);
  vi.stubGlobal("fetch", fetchMock);
  return fetchMock;
}

describe("http wrapper", () => {
  it("sends GET requests without a body", async () => {
    const fetchMock = mockFetch(new Response('{"ok":true}'));
    await expect(get("/peoplejson")).resolves.toEqual({ ok: true });

    const [url, init] = fetchMock.mock.calls[0];
    expect(url).toBe("/peoplejson");
    expect(init.method).toBe("GET");
    expect(init.body).toBeUndefined();
    expect(init.headers.Accept).toBe("application/json");
    expect(init.headers["Content-Type"]).toBeUndefined();
  });

  it("serialises bodies for POST and PUT", async () => {
    const postMock = mockFetch(new Response('{"_id":"1"}', { status: 201 }));
    await expect(post("/people", { name: "Ada" })).resolves.toEqual({ _id: "1" });
    expect(postMock.mock.calls[0][1]).toMatchObject({
      method: "POST",
      body: JSON.stringify({ name: "Ada" }),
    });
    expect(postMock.mock.calls[0][1].headers["Content-Type"]).toBe("application/json");

    const putMock = mockFetch(new Response('{"_id":"1"}'));
    await put("/people/1", { name: "Grace" });
    expect(putMock.mock.calls[0][1]).toMatchObject({
      method: "PUT",
      body: JSON.stringify({ name: "Grace" }),
    });
  });

  it("supports DELETE and empty 204 responses", async () => {
    const fetchMock = mockFetch(new Response(null, { status: 204 }));
    await expect(del("/people/1")).resolves.toBeUndefined();
    expect(fetchMock.mock.calls[0][1].method).toBe("DELETE");
  });

  it("throws on error responses and forwards abort signals and headers", async () => {
    mockFetch(new Response("Nope", { status: 500 }));
    await expect(get("/peoplejson")).rejects.toThrow("HTTP 500");

    const fetchMock = mockFetch(new Response("[]"));
    const controller = new AbortController();
    await get("/peoplejson", { signal: controller.signal, headers: { "X-Test": "1" } });
    expect(fetchMock.mock.calls[0][1].signal).toBe(controller.signal);
    expect(fetchMock.mock.calls[0][1].headers["X-Test"]).toBe("1");
  });
});
