// Useful for things like previous values, counters, or tracking state without triggering UI updates.
import { useRef, useState } from "react";

export default function ClickCounter() {
  const [count, setCount] = useState(0);
  const clickRef = useRef(0);

  const handleClick = () => {
    clickRef.current += 1; // does NOT cause re-render
    setCount((c) => c + 1); // does cause re-render
  };

  return (
    <div>
      <p>Rendered count: {count}</p>
      <p>Ref count (no re-render): {clickRef.current}</p>
      <button onClick={handleClick}>Click</button>
    </div>
  );
}
