import React from "react";
import { useSelector } from "react-redux";
import { type RootState } from "../store/store";
import { Link } from "react-router";
import "../styles/HomePage.css";

const HomePage: React.FC = () => {
  const people = useSelector((state: RootState) => state.people.list);

  return (
    <section className="home">
      <div className="home-intro">
        <h1>People Manager</h1>
        <p>
          This internal tool lets you maintain a curated list of people with
          their age, hobbies, and favourite colour.
        </p>
      </div>

      <div className="home-list-card">
        <h2>Available people</h2>
        <ul className="people-list">
          {people.map((p) => (
            <li key={p.name} className="people-list-item">
              <span className="person-name">{p.name}</span>
              <Link to={`/edit/${encodeURIComponent(p.name)}`} className="link-inline">
                Manage
              </Link>
            </li>
          ))}
        </ul>
      </div>
    </section>
  );
};

export default HomePage;
