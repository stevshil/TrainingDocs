import { usePeople } from "../context/PeopleContext";

export function PeopleList() {
  const { people } = usePeople();

  return (
    <section className="card">
      <h2>People list</h2>
      {people.length === 0 ? (
        <p>No people yet.</p>
      ) : (
        <ul>
          {people.map((person) => (
            <li key={person.id}>{person.name}</li>
          ))}
        </ul>
      )}
    </section>
  );
}
