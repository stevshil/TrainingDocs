import { useReducer } from "react";
import { Context } from "./Context";
import { todoinit } from "./todoinit";
import { todoReducer } from "./todoReducer";
import TodoList from "./TodoList";
import AddTodo from "./AddTodo";

export default function App() {
  const [todos, dispatch] = useReducer(todoReducer, todoinit);

  return (
    <Context.Provider value={{ todos, dispatch }}>
      <div className="App">
        <h3>ToDo App</h3>
        <TodoList />
        <AddTodo />
      </div>
    </Context.Provider>
  );
}
