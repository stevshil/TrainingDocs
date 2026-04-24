import React, { useState } from "react";
import { type Person } from "../types/Person";
import "../styles/Form.css";

interface PersonFormProps {
  initial?: Person;
  submitLabel: string;
  onSubmit: (person: Person) => void;
}

const PersonForm: React.FC<PersonFormProps> = ({
  initial,
  submitLabel,
  onSubmit,
}) => {
  const [name, setName] = useState(initial?.name ?? "");
  const [age, setAge] = useState(initial?.age.toString() ?? "");
  const [hobbies, setHobbies] = useState(initial?.hobbies.join(", ") ?? "");
  const [favouriteColour, setFavouriteColour] = useState(
    initial?.favouriteColour ?? ""
  );

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const parsedAge = Number(age);
    if (!name.trim() || Number.isNaN(parsedAge)) return;

    const person: Person = {
      name: name.trim(),
      age: parsedAge,
      hobbies: hobbies
        .split(",")
        .map((h) => h.trim())
        .filter(Boolean),
      favouriteColour: favouriteColour.trim(),
    };

    onSubmit(person);
  };

  return (
    <form className="form-card" onSubmit={handleSubmit}>
      <div className="form-row">
        <label>Name</label>
        <input
          type="text"
          value={name}
          required
          onChange={(e) => setName(e.target.value)}
          placeholder="Full name"
        />
      </div>

      <div className="form-row">
        <label>Age</label>
        <input
          type="number"
          value={age}
          required
          min={0}
          onChange={(e) => setAge(e.target.value)}
          placeholder="Age"
        />
      </div>

      <div className="form-row">
        <label>Hobbies</label>
        <input
          type="text"
          value={hobbies}
          onChange={(e) => setHobbies(e.target.value)}
          placeholder="Comma-separated (e.g. Reading, Cycling)"
        />
      </div>

      <div className="form-row">
        <label>Favourite colour</label>
        <input
          type="text"
          value={favouriteColour}
          onChange={(e) => setFavouriteColour(e.target.value)}
          placeholder="e.g. Blue"
        />
      </div>

      <div className="form-actions">
        <button type="submit" className="btn-primary">
          {submitLabel}
        </button>
      </div>
    </form>
  );
};

export default PersonForm;
