import { AddPerson } from "./components/AddPerson";
import { PeopleList } from "./components/PeopleList";
import { PeopleProvider } from "./context/PeopleContext";

export default function App() {
  return (
    <PeopleProvider>
      <main className="app">
        <h1>People</h1>
        <AddPerson />
        <PeopleList />
      </main>
    </PeopleProvider>
  );
}
