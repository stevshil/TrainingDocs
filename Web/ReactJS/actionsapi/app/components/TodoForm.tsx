"use client";

export default function TodoForm({ action }) {
  return (
    <form action={action} className="space-y-2">
      <input
        type="text"
        name="title"
        placeholder="New todo"
        required
        className="border p-2"
      />

      <label className="flex items-center gap-2">
        <input type="checkbox" name="completed" />
        Completed
      </label>

      <button type="submit" className="bg-blue-600 text-white px-4 py-2">
        Add Todo
      </button>
    </form>
  );
}
