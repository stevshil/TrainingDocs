import React from "react";
import { useDispatch } from "react-redux";
import { addPerson } from "../store/peopleSlice";
import { type AppDispatch } from "../store/store";
import PersonForm from "../components/PersonForm";
import { useNavigate } from "react-router";

const NewUserPage: React.FC = () => {
  const dispatch = useDispatch<AppDispatch>();
  const navigate = useNavigate();

  const handleAdd = (person: any) => {
    dispatch(addPerson(person));
    navigate("/");
  };

  return (
    <section>
      <h1>Add new user</h1>
      <PersonForm submitLabel="Create user" onSubmit={handleAdd} />
    </section>
  );
};

export default NewUserPage;
