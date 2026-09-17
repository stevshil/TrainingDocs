import { useState, type SubmitEventHandler } from "react";
import { usePeople } from "../context/PeopleContext";

export function AddPerson() {
  const [name, setName] = useState("");
  const { addPerson } = usePeople();

  const handleSubmit: SubmitEventHandler<HTMLFormElement> = (event) => {
    event.preventDefault();
    addPerson(name);
    setName("");
  };

  return (
    <form className="card" onSubmit={handleSubmit}>
      <label htmlFor="person-name">Person name</label>
      <div className="row">
        <input
          id="person-name"
          value={name}
          onChange={(event) => setName(event.target.value)}
          placeholder="Enter a name"
        />
        <button type="submit">Add person</button>
      </div>
    </form>
  );
}
