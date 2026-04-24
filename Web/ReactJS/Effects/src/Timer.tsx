// This pattern is extremely common but easy to get wrong without cleanup.
import { useEffect, useState } from "react";

export default function Timer() {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    const id = setInterval(() => {
      setSeconds((s) => s + 1);
    }, 1000);

    // Cleanup interval on unmount
    return () => clearInterval(id);
  }, []);

  return <p>Timer: {seconds}s</p>;
}
