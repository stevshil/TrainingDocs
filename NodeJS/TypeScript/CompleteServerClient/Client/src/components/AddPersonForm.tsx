import { useState } from "react";
import { usePeople } from "../context/usePeople";

export default function AddPersonForm() {
  const { addPerson } = usePeople();
  const [name, setName] = useState("");
  const [hobbies, setHobbies] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [saving, setSaving] = useState(false);

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();

    if (name.trim() === "") {
      setError("Please enter a name.");
      return;
    }

    setSaving(true);
    setError(null);

    try {
      await addPerson({
        name: name.trim(),
        hobbies: hobbies
          .split(",")
          .map((hobby) => hobby.trim())
          .filter((hobby) => hobby !== ""),
      });
      setName("");
      setHobbies("");
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : "Unable to add this person.");
    } finally {
      setSaving(false);
    }
  }

  return (
    <form
      onSubmit={handleSubmit}
      aria-labelledby="add-person-heading"
      className="mb-6 rounded-xl border border-blue-200 bg-white p-6 shadow-sm"
    >
      <h2 id="add-person-heading" className="text-lg font-semibold text-slate-900">
        Add a person
      </h2>

      <div className="mt-4 grid gap-4 sm:grid-cols-2">
        <div>
          <label htmlFor="person-name" className="block text-sm font-medium text-slate-700">
            Name
          </label>
          <input
            id="person-name"
            value={name}
            onChange={(event) => setName(event.target.value)}
            placeholder="Ada"
            className="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2 focus-visible:border-blue-700 focus-visible:outline-2 focus-visible:outline-blue-700"
          />
        </div>

        <div>
          <label htmlFor="person-hobbies" className="block text-sm font-medium text-slate-700">
            Hobbies
          </label>
          <input
            id="person-hobbies"
            value={hobbies}
            onChange={(event) => setHobbies(event.target.value)}
            placeholder="Chess, Cycling"
            aria-describedby="hobbies-hint"
            className="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2 focus-visible:border-blue-700 focus-visible:outline-2 focus-visible:outline-blue-700"
          />
          <p id="hobbies-hint" className="mt-1 text-xs text-slate-500">
            Separate multiple hobbies with commas.
          </p>
        </div>
      </div>

      {error && (
        <p role="alert" className="mt-4 text-sm font-medium text-red-700">
          {error}
        </p>
      )}

      <button
        type="submit"
        disabled={saving}
        className="mt-4 cursor-pointer rounded-lg bg-blue-700 px-4 py-2 font-semibold text-white hover:bg-blue-800 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-700 disabled:cursor-not-allowed disabled:bg-slate-400"
      >
        {saving ? "Adding..." : "Add person"}
      </button>
    </form>
  );
}
