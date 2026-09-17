import type { NewPerson } from "./NewPerson";
import type { PeopleState } from "./PeopleState";
import type { Person } from "./Person";

export interface PeopleContextValue {
  state: PeopleState;
  reload: () => void;
  addPerson: (person: NewPerson) => Promise<Person>;
  removePerson: (id: string) => Promise<void>;
}
