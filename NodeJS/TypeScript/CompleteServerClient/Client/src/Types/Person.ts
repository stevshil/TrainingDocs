export interface Person {
  _id: string;
  name: string;
  hobbies?: string[];
  hobby?: string;
}

export function isPerson(value: unknown): value is Person {
  if (typeof value !== "object" || value === null) return false;

  return (
    "_id" in value &&
    typeof value._id === "string" &&
    "name" in value &&
    typeof value.name === "string" &&
    (!("hobbies" in value) ||
      (Array.isArray(value.hobbies) &&
        value.hobbies.every((hobby: unknown) => typeof hobby === "string"))) &&
    (!("hobby" in value) || typeof value.hobby === "string")
  );
}

export function isPersonList(value: unknown): value is Person[] {
  return Array.isArray(value) && value.every(isPerson);
}

// Documents store hobbies either as an array (hobbies) or a single string (hobby).
export function listHobbies(person: Person): string[] {
  return person.hobbies ?? (person.hobby ? [person.hobby] : []);
}
