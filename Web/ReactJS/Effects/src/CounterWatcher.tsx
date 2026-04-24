// This runs every time a specific state value changes.
import { useEffect, useState } from "react";

export default function CounterWatcher() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    console.log("Count changed:", count);
  }, [count]); // Runs whenever count updates

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount((c) => c + 1)}>Increment</button>
    </div>
  );
}
