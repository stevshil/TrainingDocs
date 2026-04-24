import React, { useState } from "react";
import { Routes, Route, useNavigate } from "react-router";
import { type Person } from "./types/Person";
import Layout from "./components/Layout";
import HomePage from "./pages/HomePage";
import NewUserPage from "./pages/NewUserPage";
import EditUserPage from "./pages/EditUserPage";
import {People} from './data/People';

// const App: React.FC = () => {
function App() {
  const [people, setPeople] = useState<Person[]>(People);

  const navigate = useNavigate();

  const addPerson = (person: Person) => {
    setPeople((prev) => [...prev, person]);
    navigate("/");
  };

  const updatePerson = (originalName: string, updated: Person) => {
    setPeople((prev) =>
      prev.map((p) => (p.name === originalName ? updated : p))
    );
    navigate("/");
  };

  const deletePerson = (name: string) => {
    setPeople((prev) => prev.filter((p) => p.name !== name));
    navigate("/");
  };

  return (
    <Layout>
      <Routes>
        <Route
          path="/"
          element={<HomePage people={people} />}
        />
        <Route
          path="/new"
          element={<NewUserPage onAdd={addPerson} />}
        />
        <Route
          path="/edit/:name"
          element={
            <EditUserPage
              people={people}
              onUpdate={updatePerson}
              onDelete={deletePerson}
            />
          }
        />
      </Routes>
    </Layout>
  );
};

export default App;
