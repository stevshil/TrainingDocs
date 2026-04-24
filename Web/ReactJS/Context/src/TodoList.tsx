import { useContext } from "react";
import { Context } from "./Context";

export default function TodoList() {
  const ctx = useContext(Context);
  if (!ctx) return null;

  const { todos, dispatch } = ctx;

  return (
    <center>
      <table border="3px">
        <thead>
          <tr><th>Task</th><th>Status</th></tr>
        </thead>
        <tbody>
          {todos.map(t => (
            <tr key={t.id}>
              <td>{t.text}</td>
              <td>
                <input type="checkbox" checked={t.completed} onChange={() => dispatch({ type: "toggle", id: t.id })}
                />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </center>
  );
}
