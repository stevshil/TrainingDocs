# People & Hobbies

A React + TypeScript app using Vite and Tailwind CSS. Displays names and hobbies
in a responsive table with alternating blue and light-blue rows. People can be
added, inspected, and deleted.

## Features

- **Add a person** with a name and comma-separated hobbies.
- **View details** by clicking a row (or the name button for keyboard users).
- **Delete a person** from any row, guarded by a confirmation dialog.

## Project structure

```text
src/
  App.tsx                         Page layout and provider wiring
  api/http.ts                     GET/POST/PUT/DELETE fetch wrapper
  api/people.ts                   People endpoint calls built on the wrapper
  components/AddPersonForm.tsx    Create form
  components/DeletePersonButton.tsx  Delete with confirmation
  components/HobbyList.tsx        The people/hobbies table
  components/Modal.tsx            Shared modal shell
  components/PersonDetails.tsx    Details dialog for one person
  context/PeopleContext.tsx       Loads people, shares state and actions
  context/usePeople.ts            Hook for consuming the context
  Types/                          One interface or type per file
```

Components read data and actions through `usePeople()` rather than fetching
directly, so the request logic lives in one place. Adding or deleting updates
the loaded list in place, avoiding a full refetch. Use the `http` wrapper for
any new API calls:

```ts
import { get, post, put, del } from "./api/http";

const people = await get<Person[]>("/peoplejson");
await post("/people", { name: "Ada", hobbies: ["Chess"] });
await put("/people/1", { name: "Grace" });
await del("/people/1");
```

## Run locally

1. Start the people API at `http://localhost:3000/peoplejson`.
   For the adjacent SimpleServer project, run `npm run peopledev` from that
   directory with its MongoDB instance available.
2. From this directory:

   ```sh
   npm install
   npm run dev
   ```

3. Open `http://localhost:5173`.

The app requests `/peoplejson`; Vite proxies it to
`http://localhost:3000/peoplejson`, so no backend CORS changes are needed.
Both `hobbies` arrays and a single `hobby` string are supported:

```json
[
  { "_id": "1", "name": "Steve", "hobbies": ["Tennis", "Motorbike"] },
  { "_id": "2", "name": "Peter", "hobby": "Reading" }
]
```

Loading, empty results, invalid responses, and request failures have visible
states. Failed requests can be retried.

## Validate and build

```sh
npm test
npm run build
npm run preview
```

The production build is written to `dist`. Vite's preview server also proxies
the API locally. When deploying `dist` to a production host, configure that host
to forward `/peoplejson` to your backend; the Vite proxy is not bundled into the
static files.
