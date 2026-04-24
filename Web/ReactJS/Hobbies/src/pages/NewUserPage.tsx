import React from "react";
import PersonForm from "../components/PersonForm";
import { type Person } from "../types/Person";

interface NewUserPageProps {
  onAdd: (person: Person) => void;
}

// const NewUserPage: React.FC<NewUserPageProps> = ({ onAdd }) => {
function NewUserPage( { onAdd }: NewUserPageProps ) {
  return (
    <section>
      <h1>Add new user</h1>
      <p>
        Capture a new person’s details. Once saved, they will appear on the home
        page and can be managed there.
      </p>
      <PersonForm submitLabel="Create user" onSubmit={onAdd} />
    </section>
  );
};

export default NewUserPage;
