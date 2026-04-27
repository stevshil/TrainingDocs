import React from "react";

type UserData = {
  id: number;
  name: string;
  email: string;
};

// Utility: delay for N milliseconds
function delay(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// Fetch with artificial delay
async function fetchUserSlow(): Promise<UserData> {
  await delay(2000); // ← slow down by 2 seconds
  const res = await fetch("https://jsonplaceholder.typicode.com/users/");
  return res.json();
}

export default function User() {
  const [user, setUser] = React.useState<UserData | null>(null);
  const [loading, setLoading] = React.useState<boolean>(true);
  const [timer, setTimer] = React.useState<number>(0);

  // Suspense-like manual fetch
  React.useEffect(() => {
    let cancelled = false;

    fetchUserSlow().then((data) => {
      if (!cancelled) {
        setUser(data);
        setLoading(false);
      }
    });

    return () => {
      cancelled = true;
    };
  }, []);

  // Animated loading timer
  React.useEffect(() => {
    if (!loading) {
      setTimer(0);
      return;
    }

    const interval = setInterval(() => {
      setTimer((t) => t + 0.1);
    }, 100);

    return () => clearInterval(interval);
  }, [loading]);

  if (loading) {
    return (
      <div style={{ fontFamily: "sans-serif", padding: 20 }}>
        <div style={{ fontSize: 20, marginBottom: 10 }}>Loading…</div>
        <div style={{ fontSize: 14, opacity: 0.7 }}>
          {timer.toFixed(1)} seconds
        </div>
      </div>
    );
  }

  if (user?.email) {
    return (
        <div style={{ fontFamily: "sans-serif", padding: 20 }}>
        <h2>{user?.name}</h2>
        <p>Email: {user?.email}</p>
        </div>
    );
  } else {
    return (
        <div style={{ fontFamily: "sans-serif", padding: 20 }}>
            No user found!
        </div>
    )
  }
}
