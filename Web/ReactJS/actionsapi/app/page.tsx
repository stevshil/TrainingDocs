import { db } from "../lib/db";
import TodoList from "./components/TodoList";
import TodoForm from "./components/TodoForm";
import { addTodo } from "./actions";

export default async function Page() {
  const todos = await db.todo.findMany();

  return (
    <main className="p-4 space-y-6">
      <TodoList todos={todos} />
      <TodoForm action={addTodo} />
    </main>
  );
}
