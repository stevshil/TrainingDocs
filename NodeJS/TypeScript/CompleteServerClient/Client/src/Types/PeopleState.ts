import type { Person } from "./Person";

export type PeopleState =
  | { status: "loading" }
  | { status: "success"; people: Person[] }
  | { status: "error"; message: string };
