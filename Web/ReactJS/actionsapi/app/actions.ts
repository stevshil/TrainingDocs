// app/actions.ts
"use server";

import { db } from "../lib/db";
import { revalidatePath } from "next/cache";

export async function addTodo(formData: FormData) {
  const title = formData.get("title") as string;

  await db.todo.create({
    data: { title },
  });

  // 🔥 This forces page.tsx to re-fetch todos
  revalidatePath("/");
}
