import { cleanup, fireEvent, render, screen, waitFor } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import AddPersonForm from "./AddPersonForm";
import { PeopleProvider } from "../context/PeopleContext";

afterEach(cleanup);

function renderForm() {
  return render(
    <PeopleProvider>
      <AddPersonForm />
    </PeopleProvider>,
  );
}

function fillIn(label: string, value: string) {
  fireEvent.change(screen.getByLabelText(label), { target: { value } });
}

describe("AddPersonForm", () => {
  it("posts a new person with comma separated hobbies and clears the form", async () => {
    const fetchMock = vi.fn()
      .mockResolvedValueOnce(new Response("[]"))
      .mockResolvedValueOnce(
        new Response(JSON.stringify({ _id: "1", name: "Ada", hobbies: ["Chess", "Cycling"] }), {
          status: 201,
        }),
      );
    vi.stubGlobal("fetch", fetchMock);
    renderForm();

    fillIn("Name", "  Ada  ");
    fillIn("Hobbies", "Chess, , Cycling ");
    fireEvent.click(screen.getByRole("button", { name: "Add person" }));

    await waitFor(() => expect(fetchMock).toHaveBeenCalledTimes(2));
    const [url, init] = fetchMock.mock.calls[1];
    expect(url).toBe("/peoplejson");
    expect(init.method).toBe("POST");
    expect(JSON.parse(init.body)).toEqual({ name: "Ada", hobbies: ["Chess", "Cycling"] });

    await waitFor(() => expect((screen.getByLabelText("Name") as HTMLInputElement).value).toBe(""));
    expect((screen.getByLabelText("Hobbies") as HTMLInputElement).value).toBe("");
  });

  it("validates the name before calling the API", async () => {
    const fetchMock = vi.fn().mockResolvedValue(new Response("[]"));
    vi.stubGlobal("fetch", fetchMock);
    renderForm();

    fireEvent.click(screen.getByRole("button", { name: "Add person" }));

    expect((await screen.findByRole("alert")).textContent).toBe("Please enter a name.");
    expect(fetchMock).toHaveBeenCalledTimes(1);
  });

  it("surfaces the API error message and keeps the input", async () => {
    vi.stubGlobal("fetch", vi.fn()
      .mockResolvedValueOnce(new Response("[]"))
      .mockResolvedValueOnce(
        new Response(JSON.stringify({ error: "A non-empty 'name' is required" }), { status: 400 }),
      ));
    renderForm();

    fillIn("Name", "Ada");
    fireEvent.click(screen.getByRole("button", { name: "Add person" }));

    expect((await screen.findByRole("alert")).textContent).toBe("A non-empty 'name' is required");
    expect((screen.getByLabelText("Name") as HTMLInputElement).value).toBe("Ada");
  });
});
