// User.tsx
import type { UserData } from "./fetchUserSlow";

export function User({ resource }: { resource: { read(): UserData } }) {
  const user = resource.read();

  return (
    <div style={{ padding: 20, fontFamily: "sans-serif" }}>
      <h2>{user.name}</h2>
      <p>Email: {user.email}</p>
    </div>
  );
}
