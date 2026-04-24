import React, { Suspense, useState, useTransition, lazy } from "react";
import Spinner from "./Spinner";

const SlowList = lazy(() => import("./SlowList"));

export default function App() {
  const [query, setQuery] = useState("");
  const [search, setSearch] = useState("");
  const [isPending, startTransition] = useTransition();

  function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
    const value = e.target.value;
    setQuery(value);

    startTransition(() => {
      setSearch(value);
    });
  }

  return (
    <div style={{ padding: 20 }}>
      <h1>Suspense + Transition + Spinner</h1>

      <input
        value={query}
        onChange={handleChange}
        placeholder="Type to search..."
      />

      <div style={{ height: 30, marginTop: 10 }}>
        {isPending && (
          <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
            <Spinner />
            <span style={{ color: "orange" }}>Updating results…</span>
          </div>
        )}
      </div>

      <Suspense fallback={<Spinner />}>
        <SlowList query={search} />
      </Suspense>
    </div>
  );
}
