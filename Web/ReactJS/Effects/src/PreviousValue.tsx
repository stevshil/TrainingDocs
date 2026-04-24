import { useEffect, useRef, useState } from "react";

export default function PreviousValue() {
  const [value, setValue] = useState("");
  const prevValueRef = useRef<string>("");

  useEffect(() => {
    prevValueRef.current = value;
  }, [value]);

  return (
    <div>
      <input
        value={value}
        onChange={(e) => setValue(e.target.value)}
        placeholder="Type something"
      />
      <p>Current: {value}</p>
      <p>Previous: {prevValueRef.current}</p>
    </div>
  );
}
