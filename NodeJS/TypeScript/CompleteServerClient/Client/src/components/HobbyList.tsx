import { useState } from "react";
import DeletePersonButton from "./DeletePersonButton";
import PersonDetails from "./PersonDetails";
import { usePeople } from "../context/usePeople";
import { listHobbies, type Person } from "../Types/Person";

export default function HobbyList() {
  const { state, reload } = usePeople();
  const [selected, setSelected] = useState<Person | null>(null);

  if (state.status === "loading") {
    return (
      <p role="status" className="rounded-xl bg-blue-100 p-6 text-blue-950">
        Loading people...
      </p>
    );
  }

  if (state.status === "error") {
    return (
      <div role="alert" className="rounded-xl border border-red-200 bg-red-50 p-6">
        <h2 className="font-semibold text-red-900">Unable to load people</h2>
        <p className="mt-2 text-red-800">{state.message}</p>
        <p className="mt-2 text-sm text-red-800">
          Check that the API is running at http://localhost:3000/peoplejson.
        </p>
        <button
          type="button"
          onClick={reload}
          className="mt-4 cursor-pointer rounded-lg bg-blue-700 px-4 py-2 font-semibold text-white hover:bg-blue-800 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-700"
        >
          Try again
        </button>
      </div>
    );
  }

  return (
    <>
      <div className="overflow-x-auto rounded-xl border border-blue-200 shadow-sm">
        <table className="w-full border-collapse text-left">
          <caption className="bg-white px-6 py-4 text-left text-sm text-slate-600">
            {state.people.length} {state.people.length === 1 ? "person" : "people"} - select a row
            to see details
          </caption>
          <thead className="bg-blue-950 text-white">
            <tr>
              <th scope="col" className="px-6 py-4 font-semibold">Name</th>
              <th scope="col" className="px-6 py-4 font-semibold">Hobbies</th>
              <th scope="col" className="px-6 py-4 text-right font-semibold">Actions</th>
            </tr>
          </thead>
          <tbody>
            {state.people.map((person) => (
              <tr
                key={person._id}
                className="cursor-pointer odd:bg-blue-700 odd:text-white even:bg-blue-100 even:text-blue-950 hover:outline-2 hover:-outline-offset-2 hover:outline-blue-950"
                onClick={() => setSelected(person)}
              >
                <th scope="row" className="px-6 py-4 font-medium">
                  <button
                    type="button"
                    // Keyboard users reach the details view through this button.
                    onClick={(event) => {
                      event.stopPropagation();
                      setSelected(person);
                    }}
                    aria-label={`View details for ${person.name}`}
                    className="cursor-pointer underline-offset-4 hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-current"
                  >
                    {person.name}
                  </button>
                </th>
                <td className="px-6 py-4">
                  {listHobbies(person).join(", ") || "No hobbies listed"}
                </td>
                <td className="px-6 py-4 text-right" onClick={(event) => event.stopPropagation()}>
                  <DeletePersonButton person={person} />
                </td>
              </tr>
            ))}
            {state.people.length === 0 && (
              <tr className="bg-blue-100 text-blue-950">
                <td colSpan={3} className="px-6 py-8 text-center">
                  No people found.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

      {selected && <PersonDetails person={selected} onClose={() => setSelected(null)} />}
    </>
  );
}
