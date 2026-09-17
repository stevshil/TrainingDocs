import { cleanup, fireEvent, render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import PersonDetails from "./PersonDetails";

afterEach(cleanup);

const person = { _id: "abc123", name: "Steve", hobbies: ["Tennis", "Motorbike"] };

describe("PersonDetails", () => {
  it("shows the person's details in a modal dialog", () => {
    render(<PersonDetails person={person} onClose={() => {}} />);

    const dialog = screen.getByRole("dialog");
    expect(dialog.getAttribute("aria-modal")).toBe("true");
    expect(screen.getByRole("heading", { name: "Steve" })).toBeTruthy();
    expect(screen.getByText("Hobbies (2)")).toBeTruthy();
    expect(screen.getByText("Tennis")).toBeTruthy();
    expect(screen.getByText("abc123")).toBeTruthy();
  });

  it("falls back to a placeholder for a legacy single hobby and no hobbies", () => {
    render(<PersonDetails person={{ _id: "1", name: "Peter", hobby: "Reading" }} onClose={() => {}} />);
    expect(screen.getByText("Reading")).toBeTruthy();
    cleanup();

    render(<PersonDetails person={{ _id: "2", name: "Elena" }} onClose={() => {}} />);
    expect(screen.getByText("No hobbies listed")).toBeTruthy();
  });

  it("closes via the button, the backdrop and Escape", () => {
    const onClose = vi.fn();
    const { container } = render(<PersonDetails person={person} onClose={onClose} />);

    fireEvent.click(screen.getByRole("button", { name: "Close" }));
    expect(onClose).toHaveBeenCalledTimes(1);

    fireEvent.click(container.firstElementChild!);
    expect(onClose).toHaveBeenCalledTimes(2);

    fireEvent.keyDown(document, { key: "Escape" });
    expect(onClose).toHaveBeenCalledTimes(3);
  });

  it("ignores clicks inside the dialog panel", () => {
    const onClose = vi.fn();
    render(<PersonDetails person={person} onClose={onClose} />);

    fireEvent.click(screen.getByRole("dialog"));
    expect(onClose).not.toHaveBeenCalled();
  });
});
