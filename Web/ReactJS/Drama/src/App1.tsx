import { Suspense, useState, useTransition, lazy } from "react";

const SlowList = lazy(() => import("./SlowList"));

export default function App() {
  const [query, setQuery] = useState("");
  const [search, setSearch] = useState("");
  const [isPending, startTransition] = useTransition();

  function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
    const value = e.target.value;
    setQuery(value); // urgent update (typing)

    startTransition(() => {
      setSearch(value); // non‑urgent update (slow list)
    });
  }

  return (
    <div style={{ padding: 20 }}>
      <h1>Suspense + Transition Example</h1>

      <input
        value={query}
        onChange={handleChange}
        placeholder="Type to search..."
      />

      {isPending && <p style={{ color: "orange" }}>Updating results…</p>}

      <Suspense fallback={<p>Loading list…</p>}>
        <SlowList query={search} />
      </Suspense>
    </div>
  );
}
