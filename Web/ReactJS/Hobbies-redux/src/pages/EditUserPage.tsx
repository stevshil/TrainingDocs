import React from "react";
import { useParams, useNavigate } from "react-router";
import { useDispatch, useSelector } from "react-redux";
import type { RootState, AppDispatch } from "../store/store";
import { updatePerson, deletePerson } from "../store/peopleSlice";
import PersonForm from "../components/PersonForm";

const EditUserPage: React.FC = () => {
  const { name } = useParams();
  const navigate = useNavigate();
  const dispatch = useDispatch<AppDispatch>();

  const person = useSelector((state: RootState) =>
    state.people.list.find((p) => p.name === name)
  );

  if (!person) {
    return <p>User not found.</p>;
  }

  const handleUpdate = (updated: any) => {
    dispatch(updatePerson({ originalName: person.name, updated }));
    navigate("/");
  };

  const handleDelete = () => {
    if (window.confirm(`Delete ${person.name}?`)) {
      dispatch(deletePerson(person.name));
      navigate("/");
    }
  };

  return (
    <section>
      <h1>Manage user</h1>
      <PersonForm initial={person} submitLabel="Save changes" onSubmit={handleUpdate} />
      <button className="btn-danger" onClick={handleDelete}>
        Delete user
      </button>
    </section>
  );
};

export default EditUserPage;
