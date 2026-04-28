"use server";

import { db } from "../lib/db";
import { revalidatePath } from "next/cache";

export async function addTodo(formData: FormData) {
  const title = formData.get("title") as string;
  const completed = formData.get("completed") === "on";

  await db.todo.create({
    data: { title, completed },
  });

  revalidatePath("/");
}

export async function toggleTodo(id: string) {
  const todos = await db.todo.findMany();
  const todo = todos.find(t => t.id === id);

  if (!todo) return;

  todo.completed = !todo.completed;

  revalidatePath("/");
}
