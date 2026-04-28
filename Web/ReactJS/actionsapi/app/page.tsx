// app/page.tsx
import { TodoList } from "./components/TodoList";
import { Todo } from "./components/TodoList";
import { db } from "../lib/db"; // optional, depending on your setup

export default async function Page() {
  // Example: fetch todos from your DB
  const todos: Todo[] = await db.todo.findMany();

  return (
    <main style={{ padding: 24 }}>
      <h1>Todos</h1>
      <TodoList todos={todos} />
    </main>
  );
}
