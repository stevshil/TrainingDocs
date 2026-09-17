import Modal from "./Modal";
import { listHobbies, type Person } from "../Types/Person";

interface PersonDetailsProps {
  person: Person;
  onClose: () => void;
}

export default function PersonDetails({ person, onClose }: PersonDetailsProps) {
  const hobbies = listHobbies(person);

  return (
    <Modal title={person.name} onClose={onClose}>
      <dl className="mt-4 space-y-4">
        <div>
          <dt className="text-sm font-medium text-slate-500">Name</dt>
          <dd className="text-slate-900">{person.name}</dd>
        </div>

        <div>
          <dt className="text-sm font-medium text-slate-500">
            Hobbies ({hobbies.length})
          </dt>
          <dd className="text-slate-900">
            {hobbies.length > 0 ? (
              <ul className="mt-1 flex flex-wrap gap-2">
                {hobbies.map((hobby) => (
                  <li
                    key={hobby}
                    className="rounded-full bg-blue-100 px-3 py-1 text-sm text-blue-950"
                  >
                    {hobby}
                  </li>
                ))}
              </ul>
            ) : (
              "No hobbies listed"
            )}
          </dd>
        </div>

        <div>
          <dt className="text-sm font-medium text-slate-500">ID</dt>
          <dd className="font-mono text-sm break-all text-slate-700">{person._id}</dd>
        </div>
      </dl>

      <button
        type="button"
        onClick={onClose}
        className="mt-6 cursor-pointer rounded-lg bg-blue-700 px-4 py-2 font-semibold text-white hover:bg-blue-800 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-700"
      >
        Close
      </button>
    </Modal>
  );
}
