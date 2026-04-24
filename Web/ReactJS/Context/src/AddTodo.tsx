import { useContext, useState } from "react";
import { Context } from "./Context";

export default function AddTodo() {
  const ctx = useContext(Context);
  const [text, setText] = useState("");

  if (!ctx) return null;

  const { dispatch } = ctx;

  const handleAdd = () => {
    if (!text.trim()) return;
    dispatch({ type: "add", text });
    setText("");
  };

  return (
    <>
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="New todo"
      />
      <button onClick={handleAdd}>Add</button>
    </>
  );
}
