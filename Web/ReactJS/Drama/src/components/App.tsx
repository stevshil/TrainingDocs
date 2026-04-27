// App.tsx
import React from "react";
import { createResource } from "./resource";
import { fetchUserSlow } from "./fetchUserSlow";
import { User } from "./User";
import { LoadingFallback } from "./LoadingFallback";

export default function App() {
  const [resource, setResource] = React.useState(() =>
    createResource(fetchUserSlow())
  );

  const [isPending, startTransition] = React.useTransition();

  const reload = () => {
    // Force immediate suspension
    setResource(null as any);

    startTransition(() => {
      const newResource = createResource(fetchUserSlow());
      setResource(newResource);
    });
  };

  return (
    <div>
      <button
        onClick={reload}
        disabled={isPending}
        style={{ margin: 20, padding: "8px 16px" }}
      >
        {isPending ? "Reloading…" : "Reload User"}
      </button>

      <React.Suspense fallback={<LoadingFallback />}>
        {resource && <User resource={resource} />}
      </React.Suspense>
    </div>
  );
}
