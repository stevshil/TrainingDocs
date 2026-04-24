import React from "react";
import { Link } from "react-router";
import { type Person } from "../types/Person";
import "../styles/HomePage.css";

interface HomePageProps {
  people: Person[];
}

// const HomePage: React.FC<HomePageProps> = ({ people }) => {
function HomePage({ people }: HomePageProps) {
  return (
    <section className="home">
      <div className="home-intro">
        <h1>People Manager</h1>
        <p>
          This internal tool lets you maintain a curated list of people with
          their age, hobbies, and favourite colour.
        </p>
        <p>
          Only the people listed below can be selected for modification or
          deletion. Select a name to manage their details.
        </p>
      </div>

      <div className="home-list-card">
        <h2>Available people</h2>
        {people.length === 0 ? (
          <p className="muted">No people yet. Add a new user to get started.</p>
        ) : (
          <ul className="people-list">
            {people.map((person) => (
              <li key={person.name} className="people-list-item">
                <span className="person-name">{person.name}</span>
                <Link
                  to={`/edit/${encodeURIComponent(person.name)}`}
                  className="link-inline"
                >
                  Manage
                </Link>
              </li>
            ))}
          </ul>
        )}
      </div>
    </section>
  );
};

export default HomePage;
