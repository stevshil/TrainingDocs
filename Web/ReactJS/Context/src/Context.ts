import { createContext } from "react";
import type { Todo } from "./Todo";
import type { TodoAction } from "./todoReducer";

export const Context = createContext<{
  todos: Todo[];
  dispatch: React.Dispatch<TodoAction>;
} | null>(null);
