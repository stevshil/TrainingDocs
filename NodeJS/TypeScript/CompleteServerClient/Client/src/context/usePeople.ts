import { useContext } from "react";
import { PeopleContext } from "./PeopleContext";
import type { PeopleContextValue } from "../Types/PeopleContextValue";

export function usePeople(): PeopleContextValue {
  const context = useContext(PeopleContext);

  if (!context) {
    throw new Error("usePeople must be used within a PeopleProvider.");
  }

  return context;
}
