import { createContext, PropsWithChildren, useContext, useMemo, useState } from "react";

type Person = {
  id: number;
  name: string;
};

type PeopleContextValue = {
  people: Person[];
  addPerson: (name: string) => void;
};

const PeopleContext = createContext<PeopleContextValue | undefined>(undefined);

export function PeopleProvider({ children }: PropsWithChildren) {
  const [people, setPeople] = useState<Person[]>([
    { id: 1, name: "Ada Lovelace" },
    { id: 2, name: "Grace Hopper" },
  ]);

  function addPerson(name: string) {
    const trimmedName = name.trim();

    if (!trimmedName) {
      return;
    }

    setPeople((currentPeople) => [
      ...currentPeople,
      {
        id: Date.now(),
        name: trimmedName,
      },
    ]);
  }

  const value = useMemo(() => ({ people, addPerson }), [people]);

  return <PeopleContext.Provider value={value}>{children}</PeopleContext.Provider>;
}

export function usePeople() {
  const context = useContext(PeopleContext);

  if (!context) {
    throw new Error("usePeople must be used inside PeopleProvider");
  }

  return context;
}
