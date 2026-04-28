"use client";

import { addTodo } from "../actions";

export function TodoForm() {
  return (
    <form action={addTodo}>
      <input name="title" required />
      <button type="submit">Add</button>
    </form>
  );
}
