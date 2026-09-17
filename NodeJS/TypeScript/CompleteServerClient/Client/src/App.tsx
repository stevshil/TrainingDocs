import AddPersonForm from "./components/AddPersonForm";
import HobbyList from "./components/HobbyList";
import { PeopleProvider } from "./context/PeopleContext";

export default function App() {
  return (
    <main className="min-h-screen bg-slate-50 px-4 py-12 text-slate-900 sm:px-8">
      <section className="mx-auto max-w-4xl" aria-labelledby="people-heading">
        <header className="mb-6">
          <p className="text-sm font-semibold uppercase tracking-widest text-blue-700">
            People directory
          </p>
          <h1 id="people-heading" className="mt-2 text-3xl font-bold">
            People &amp; Hobbies
          </h1>
          <p className="mt-2 text-slate-600">
            Discover the people in your community and what they enjoy.
          </p>
        </header>

        <PeopleProvider>
          <AddPersonForm />
          <HobbyList />
        </PeopleProvider>
      </section>
    </main>
  );
}
