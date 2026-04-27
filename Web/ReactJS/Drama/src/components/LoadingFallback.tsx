// LoadingFallback.tsx
import React from "react";

export function LoadingFallback() {
  const [timer, setTimer] = React.useState(0);

  React.useEffect(() => {
    const interval = setInterval(() => {
      setTimer((t) => t + 0.1);
    }, 100);

    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ padding: 20, fontFamily: "sans-serif" }}>
      <div style={{ fontSize: 20, marginBottom: 10 }}>Loading…</div>
      <div style={{ opacity: 0.7 }}>{timer.toFixed(1)} seconds</div>
    </div>
  );
}
