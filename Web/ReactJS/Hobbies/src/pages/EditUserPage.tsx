import React, { useMemo } from "react";
import { useParams } from "react-router";
import { type Person } from "../types/Person";
import PersonForm from "../components/PersonForm";

interface EditUserPageProps {
  people: Person[];
  onUpdate: (originalName: string, updated: Person) => void;
  onDelete: (name: string) => void;
}

// const EditUserPage: React.FC<EditUserPageProps> = ({
//   people,
//   onUpdate,
//   onDelete,
// }) => {
function EditUserPage({ people, onUpdate, onDelete }: EditUserPageProps) {

  const { name } = useParams<{ name: string }>();

  const person = useMemo(
    () =>
      people.find(
        (p) => p.name === (name ? decodeURIComponent(name) : name)
      ),
    [people, name]
  );

  if (!person) {
    return (
      <section>
        <h1>User not found</h1>
        <p>
          The selected user does not exist. Return to the home page and choose a
          valid name.
        </p>
      </section>
    );
  }

  const handleUpdate = (updated: Person) => {
    onUpdate(person.name, updated);
  };

  const handleDelete = () => {
    if (window.confirm(`Delete ${person.name}? This cannot be undone.`)) {
      onDelete(person.name);
    }
  };

  return (
    <section>
      <h1>Manage user</h1>
      <p>Update or remove the selected person from the system.</p>
      <PersonForm
        initial={person}
        submitLabel="Save changes"
        onSubmit={handleUpdate}
      />
      <button className="btn-danger" onClick={handleDelete}>
        Delete user
      </button>
    </section>
  );
};

export default EditUserPage;
