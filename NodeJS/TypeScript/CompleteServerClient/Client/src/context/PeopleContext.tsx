import { createContext, useCallback, useEffect, useMemo, useState, type ReactNode } from "react";
import { createPerson, deletePerson, fetchPeople } from "../api/people";
import type { NewPerson } from "../Types/NewPerson";
import type { PeopleContextValue } from "../Types/PeopleContextValue";
import type { PeopleState } from "../Types/PeopleState";
import type { Person } from "../Types/Person";

export const PeopleContext = createContext<PeopleContextValue | undefined>(undefined);

const byName = (a: Person, b: Person) => a.name.localeCompare(b.name);

export function PeopleProvider({ children }: { children: ReactNode }) {
  const [state, setState] = useState<PeopleState>({ status: "loading" });
  const [request, setRequest] = useState(0);

  const reload = useCallback(() => setRequest((current) => current + 1), []);

  // Keep the loaded list in sync locally so the table updates without a refetch.
  const addPerson = useCallback(async (person: NewPerson) => {
    const created = await createPerson(person);

    setState((current) =>
      current.status === "success"
        ? { status: "success", people: [...current.people, created].sort(byName) }
        : current,
    );

    return created;
  }, []);

  const removePerson = useCallback(async (id: string) => {
    await deletePerson(id);

    setState((current) =>
      current.status === "success"
        ? { status: "success", people: current.people.filter((person) => person._id !== id) }
        : current,
    );
  }, []);

  useEffect(() => {
    const controller = new AbortController();
    setState({ status: "loading" });

    async function loadPeople() {
      try {
        const people = await fetchPeople(controller.signal);
        if (!controller.signal.aborted) {
          setState({ status: "success", people });
        }
      } catch (error) {
        if (!controller.signal.aborted) {
          setState({
            status: "error",
            message: error instanceof Error ? error.message : "Unable to load people.",
          });
        }
      }
    }

    void loadPeople();
    return () => controller.abort();
  }, [request]);

  const value = useMemo<PeopleContextValue>(
    () => ({ state, reload, addPerson, removePerson }),
    [state, reload, addPerson, removePerson],
  );

  return <PeopleContext.Provider value={value}>{children}</PeopleContext.Provider>;
}
