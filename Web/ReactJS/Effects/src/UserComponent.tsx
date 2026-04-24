import { useEffect, useState } from "react";

export default function UserComponent() {
  const [user, setUser] = useState<{ name: string } | null>(null);

  useEffect(() => {
    // Simulate fetching data
    const fetchUser = async () => {
      const response = await new Promise<{ name: string }>((resolve) =>
        setTimeout(() => resolve({ name: "Alice" }), 1000)
      );
      setUser(response);
    };

    fetchUser();
  }, []); // Empty dependency array = run once on mount

  return (
    <div>
      <h2>User Info</h2>
      {user ? <p>Name: {user.name}</p> : <p>Loading...</p>}
    </div>
  );
}
