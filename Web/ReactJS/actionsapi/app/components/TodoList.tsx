"use client";

import { toggleTodo } from "../actions";

export default function TodoList({ todos }) {
  return (
    <ul className="space-y-2">
      {todos.map(todo => (
        <li key={todo.id} className="flex items-center gap-2">
          <form action={toggleTodo.bind(null, todo.id)}>
            <input
              type="checkbox"
              defaultChecked={todo.completed}
              onChange={() => {}}
            />
          

          <span className={todo.completed ? "line-through text-gray-500" : ""}>
            {todo.title}
          </span>
          </form>
        </li>
      ))}
    </ul>
  );
}
