// This pattern is essential for avoiding memory leaks.
import { useEffect, useState } from "react";

export default function WindowWidth() {
  const [width, setWidth] = useState(window.innerWidth);

  useEffect(() => {
    const handleResize = () => setWidth(window.innerWidth);

    window.addEventListener("resize", handleResize);

    // Cleanup runs when component unmounts
    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  return <p>Window width: {width}px</p>;
}
