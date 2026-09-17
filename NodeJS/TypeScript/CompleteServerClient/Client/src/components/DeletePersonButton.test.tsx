import { cleanup, fireEvent, render, screen, waitFor, within } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import DeletePersonButton from "./DeletePersonButton";
import HobbyList from "./HobbyList";
import { PeopleProvider } from "../context/PeopleContext";

afterEach(cleanup);

const person = { _id: "abc123", name: "Steve", hobbies: ["Tennis"] };

function renderButton() {
  return render(
    <PeopleProvider>
      <DeletePersonButton person={person} />
    </PeopleProvider>,
  );
}

describe("DeletePersonButton", () => {
  it("asks for confirmation before deleting", async () => {
    const fetchMock = vi.fn().mockResolvedValue(new Response("[]"));
    vi.stubGlobal("fetch", fetchMock);
    renderButton();

    expect(screen.queryByRole("dialog")).toBeNull();
    fireEvent.click(screen.getByRole("button", { name: "Delete Steve" }));

    const dialog = screen.getByRole("dialog");
    expect(within(dialog).getByText(/cannot be undone/)).toBeTruthy();
    // Only the initial people fetch has run; nothing was deleted yet.
    expect(fetchMock).toHaveBeenCalledTimes(1);
  });

  it("cancelling closes the dialog without calling the API", async () => {
    const fetchMock = vi.fn().mockResolvedValue(new Response("[]"));
    vi.stubGlobal("fetch", fetchMock);
    renderButton();

    fireEvent.click(screen.getByRole("button", { name: "Delete Steve" }));
    fireEvent.click(screen.getByRole("button", { name: "Cancel" }));

    await waitFor(() => expect(screen.queryByRole("dialog")).toBeNull());
    expect(fetchMock).toHaveBeenCalledTimes(1);
  });

  it("confirming sends a DELETE request", async () => {
    const fetchMock = vi.fn()
      .mockResolvedValueOnce(new Response("[]"))
      .mockResolvedValueOnce(new Response(null, { status: 204 }));
    vi.stubGlobal("fetch", fetchMock);
    renderButton();

    fireEvent.click(screen.getByRole("button", { name: "Delete Steve" }));
    fireEvent.click(within(screen.getByRole("dialog")).getByRole("button", { name: "Delete" }));

    await waitFor(() => expect(fetchMock).toHaveBeenCalledTimes(2));
    expect(fetchMock.mock.calls[1][0]).toBe("/peoplejson/abc123");
    expect(fetchMock.mock.calls[1][1].method).toBe("DELETE");
    await waitFor(() => expect(screen.queryByRole("dialog")).toBeNull());
  });

  it("keeps the dialog open and reports API failures", async () => {
    vi.stubGlobal("fetch", vi.fn()
      .mockResolvedValueOnce(new Response("[]"))
      .mockResolvedValueOnce(new Response(JSON.stringify({ error: "Person not found" }), { status: 404 })));
    renderButton();

    fireEvent.click(screen.getByRole("button", { name: "Delete Steve" }));
    fireEvent.click(within(screen.getByRole("dialog")).getByRole("button", { name: "Delete" }));

    expect((await screen.findByRole("alert")).textContent).toBe("Person not found");
    expect(screen.getByRole("dialog")).toBeTruthy();
  });

  it("removes the row from the table after a successful delete", async () => {
    vi.stubGlobal("fetch", vi.fn()
      .mockResolvedValueOnce(new Response(JSON.stringify([
        { _id: "abc123", name: "Steve", hobbies: ["Tennis"] },
        { _id: "def456", name: "Elena", hobbies: ["Swimming"] },
      ])))
      .mockResolvedValueOnce(new Response(null, { status: 204 })));

    render(
      <PeopleProvider>
        <HobbyList />
      </PeopleProvider>,
    );

    expect(await screen.findByText("Steve")).toBeTruthy();
    fireEvent.click(screen.getByRole("button", { name: "Delete Steve" }));
    fireEvent.click(within(screen.getByRole("dialog")).getByRole("button", { name: "Delete" }));

    await waitFor(() => expect(screen.queryByText("Steve")).toBeNull());
    expect(screen.getByText("Elena")).toBeTruthy();
    expect(screen.getByText(/1 person/)).toBeTruthy();
  });
});
