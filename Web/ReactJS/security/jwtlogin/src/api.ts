export const API_URL = "http://localhost:3000";

export async function login(username: string, password: string) {
  const res = await fetch(`${API_URL}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });

  if (!res.ok) throw new Error("Invalid login");

  return res.json();
}

export async function fetchUsers(token: string) {
  const res = await fetch(`${API_URL}/users`, {
    headers: { Authorization: `Bearer ${token}` }
  });

  if (!res.ok) throw new Error("Unauthorized");

  return res.json();
}
