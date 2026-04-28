export interface User {
  username: string;
  password: string;
}

export const users: User[] = [
  { username: "alice", password: "password123" },
  { username: "bob", password: "secret456" },
  { username: "charlie", password: "qwerty789" }
];
