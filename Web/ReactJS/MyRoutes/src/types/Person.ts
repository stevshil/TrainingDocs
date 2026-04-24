// Define the structure of a Person
export interface Person {
  name: string;
  age: number;
  hobby: string;
}

export function searchPeople<K extends keyof Person>(
  people: Person[],
  key: K,
  query: Person[K]
): Person[] {
  return people.filter((person) => {
    const value = person[key];

    // If the field is a string, allow partial match
    if (typeof value === "string" && typeof query === "string") {
      return value.toLowerCase().includes(query.toLowerCase());
    }

    // If the field is a number, require exact match
    if (typeof value === "number" && typeof query === "number") {
      return value === query;
    }

    return false;
  });
};
