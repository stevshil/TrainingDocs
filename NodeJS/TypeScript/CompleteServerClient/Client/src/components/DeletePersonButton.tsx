import { useState } from "react";
import Modal from "./Modal";
import { usePeople } from "../context/usePeople";
import type { Person } from "../Types/Person";

export default function DeletePersonButton({ person }: { person: Person }) {
  const { removePerson } = usePeople();
  const [confirming, setConfirming] = useState(false);
  const [deleting, setDeleting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  function close() {
    setConfirming(false);
    setError(null);
  }

  async function handleDelete() {
    setDeleting(true);
    setError(null);

    try {
      await removePerson(person._id);
      setConfirming(false);
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : "Unable to delete this person.");
    } finally {
      setDeleting(false);
    }
  }

  return (
    <>
      <button
        type="button"
        onClick={() => setConfirming(true)}
        aria-label={`Delete ${person.name}`}
        className="cursor-pointer rounded-lg border border-current px-3 py-1 text-sm font-semibold hover:bg-red-700 hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-current"
      >
        Delete
      </button>

      {confirming && (
        <Modal title="Delete person" onClose={close}>
          <p className="mt-4 text-slate-700">
            Delete <span className="font-semibold">{person.name}</span>? This cannot be undone.
          </p>

          {error && (
            <p role="alert" className="mt-4 text-sm font-medium text-red-700">
              {error}
            </p>
          )}

          <div className="mt-6 flex justify-end gap-3">
            <button
              type="button"
              onClick={close}
              className="cursor-pointer rounded-lg border border-slate-300 px-4 py-2 font-semibold text-slate-700 hover:bg-slate-100 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-slate-500"
            >
              Cancel
            </button>
            <button
              type="button"
              onClick={handleDelete}
              disabled={deleting}
              className="cursor-pointer rounded-lg bg-red-700 px-4 py-2 font-semibold text-white hover:bg-red-800 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-red-700 disabled:cursor-not-allowed disabled:bg-slate-400"
            >
              {deleting ? "Deleting..." : "Delete"}
            </button>
          </div>
        </Modal>
      )}
    </>
  );
}
