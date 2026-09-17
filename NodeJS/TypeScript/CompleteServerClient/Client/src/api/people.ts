import { del, get, post } from "./http";
import type { NewPerson } from "../Types/NewPerson";
import { isPerson, isPersonList, type Person } from "../Types/Person";

// Vite forwards these requests to http://localhost:3000.
export const PEOPLE_URL = "/peoplejson";

const UNEXPECTED_FORMAT = "The people API returned an unexpected data format.";

export async function fetchPeople(signal?: AbortSignal): Promise<Person[]> {
  const data = await get<unknown>(PEOPLE_URL, { signal });

  if (!isPersonList(data)) {
    throw new Error(UNEXPECTED_FORMAT);
  }

  return data;
}

export async function createPerson(person: NewPerson, signal?: AbortSignal): Promise<Person> {
  const data = await post<unknown>(PEOPLE_URL, person, { signal });

  if (!isPerson(data)) {
    throw new Error(UNEXPECTED_FORMAT);
  }

  return data;
}

export async function deletePerson(id: string, signal?: AbortSignal): Promise<void> {
  await del(`${PEOPLE_URL}/${encodeURIComponent(id)}`, { signal });
}
