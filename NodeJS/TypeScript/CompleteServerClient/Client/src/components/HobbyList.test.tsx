import { cleanup, fireEvent, render, screen, waitFor } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import HobbyList from "./HobbyList";
import { PeopleProvider } from "../context/PeopleContext";

afterEach(cleanup);

function renderHobbyList() {
  return render(
    <PeopleProvider>
      <HobbyList />
    </PeopleProvider>,
  );
}

describe("HobbyList", () => {
  it("renders context data with both hobby formats and alternating row classes", async () => {
    const fetchMock = vi.fn().mockResolvedValue(
      new Response(JSON.stringify([
        { _id: "1", name: "Steve", hobbies: ["Tennis", "Motorbike"] },
        { _id: "2", name: "Peter", hobby: "Reading" },
        { _id: "3", name: "Elena" },
      ])),
    );
    vi.stubGlobal("fetch", fetchMock);
    renderHobbyList();

    expect(screen.getByRole("status").textContent).toBe("Loading people...");
    expect(await screen.findByText("Steve")).toBeTruthy();
    expect(screen.getByText("Tennis, Motorbike")).toBeTruthy();
    expect(screen.getByText("Reading")).toBeTruthy();
    expect(screen.getByText("No hobbies listed")).toBeTruthy();
    expect(fetchMock).toHaveBeenCalledWith("/peoplejson", expect.objectContaining({
      method: "GET",
      signal: expect.any(AbortSignal),
    }));
    for (const row of screen.getAllByRole("row").slice(1)) {
      expect(row.className).toContain("odd:bg-blue-700");
      expect(row.className).toContain("even:bg-blue-100");
    }
  });

  it("opens the details dialog when a row is clicked", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(
      new Response(JSON.stringify([{ _id: "1", name: "Steve", hobbies: ["Tennis"] }])),
    ));
    renderHobbyList();

    const row = (await screen.findByText("Steve")).closest("tr")!;
    fireEvent.click(row);

    const dialog = screen.getByRole("dialog");
    expect(dialog.getAttribute("aria-label")).toBe("Steve");
    fireEvent.click(screen.getByRole("button", { name: "Close" }));
    await waitFor(() => expect(screen.queryByRole("dialog")).toBeNull());
  });

  it("does not open details when the delete button in a row is clicked", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(
      new Response(JSON.stringify([{ _id: "1", name: "Steve", hobbies: ["Tennis"] }])),
    ));
    renderHobbyList();

    fireEvent.click(await screen.findByRole("button", { name: "Delete Steve" }));

    expect(screen.getByRole("dialog").getAttribute("aria-label")).toBe("Delete person");
  });

  it("shows an empty state", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(new Response("[]")));
    renderHobbyList();
    expect(await screen.findByText("No people found.")).toBeTruthy();
  });

  it("reports HTTP failures and reloads through the context", async () => {
    const fetchMock = vi.fn()
      .mockResolvedValueOnce(new Response("Unavailable", { status: 503 }))
      .mockResolvedValueOnce(new Response("[]"));
    vi.stubGlobal("fetch", fetchMock);
    renderHobbyList();
    expect((await screen.findByRole("alert")).textContent).toContain("HTTP 503");
    fireEvent.click(screen.getByRole("button", { name: "Try again" }));
    expect(await screen.findByText("No people found.")).toBeTruthy();
    expect(fetchMock).toHaveBeenCalledTimes(2);
  });

  it("reports network failures", async () => {
    vi.stubGlobal("fetch", vi.fn().mockRejectedValue(new TypeError("Failed to fetch")));
    renderHobbyList();
    expect((await screen.findByRole("alert")).textContent).toContain("Failed to fetch");
  });

  it("rejects malformed API data", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(new Response('[{"name":42}]')));
    renderHobbyList();
    expect((await screen.findByRole("alert")).textContent).toContain("unexpected data format");
  });

  it("requires a PeopleProvider", () => {
    const consoleError = vi.spyOn(console, "error").mockImplementation(() => {});
    expect(() => render(<HobbyList />)).toThrowError(/PeopleProvider/);
    consoleError.mockRestore();
  });
});
