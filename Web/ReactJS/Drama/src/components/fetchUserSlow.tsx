// api.ts
export type UserData = {
  id: number;
  name: string;
  email: string;
};

function delay(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export async function fetchUserSlow(): Promise<UserData> {
  await delay(2000); // slow down by 2 seconds
  const res = await fetch("https://jsonplaceholder.typicode.com/users/1");
  return res.json();
}
