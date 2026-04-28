"use client";

import { useOptimistic } from "react";
import { addTodo } from "../actions";

export type Todo = { id: string; title: string };

export function TodoList({ todos }: { todos: Todo[] }) {
  const [optimisticTodos, addOptimistic] = useOptimistic<Todo[], string>(
    todos,
    (state, title) => [...state, { id: crypto.randomUUID(), title }]
  );

  async function handleAction(formData: FormData) {
    const title = formData.get("title") as string;
    addOptimistic(title);
    await addTodo(formData);
  }

  return (
    <>
      <ul>
        {optimisticTodos.map(t => (
          <li key={t.id}>{t.title}</li>
        ))}
      </ul>

      <form action={handleAction}>
        <input name="title" required />
        <button type="submit">Add</button>
      </form>
    </>
  );
}
