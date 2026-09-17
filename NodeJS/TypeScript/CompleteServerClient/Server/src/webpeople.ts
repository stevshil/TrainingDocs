import express from "express";
import { MongoClient, Collection, ObjectId, OptionalId } from "mongodb";
import { Person } from "../Types/Person";

const mongoUrl = process.env.MONGO_URL ?? "mongodb://127.0.0.1:27017";
const port = Number(process.env.PORT ?? 3000);

const client = new MongoClient(mongoUrl);
const people: Collection<Person> = client.db("people").collection<Person>("hobbies");

const app = express();
app.use(express.json());

// Documents store hobbies either as an array (hobbies) or a single string (hobby).
const listHobbies = (person: Person): string =>
  (person.hobbies ?? (person.hobby ? [person.hobby] : [])).join(", ");

// Accepts either "hobbies": ["a", "b"] or "hobby": "a" and normalises to an array.
const readHobbies = (body: { hobbies?: unknown; hobby?: unknown }): string[] | undefined => {
  if (Array.isArray(body.hobbies)) {
    return body.hobbies.filter((hobby): hobby is string => typeof hobby === "string");
  }
  if (typeof body.hobby === "string") {
    return [body.hobby];
  }
  return undefined;
};

const toObjectId = (id: string): ObjectId | null =>
  ObjectId.isValid(id) ? new ObjectId(id) : null;

app.get("/people", async (_req, res) => {
  try {
    const persons = await people.find().sort({ name: 1 }).toArray();

    const rows = persons.map(person => `
        <tr>
          <td>${person.name}</td>
          <td>${listHobbies(person)}</td>
        </tr>`).join("\n");

    const table = `<table>
        <thead>
          <tr><th>Name</th><th>Hobbies</th></tr>
        </thead>
        <tbody>${rows}</tbody>
      </table>`;

    res.type("html").send(table);
  } catch (error) {
    console.error("Failed to fetch people:", error);
    res.status(500).type("text").send("Failed to fetch people");
  }
});

// create an endpoint to fetch all people but return json
app.get("/peoplejson", async (_req, res) => {
  try {
    const persons = await people.find().sort({ name: 1 }).toArray();
    res.json(persons);
  } catch (error) {
    console.error("Failed to fetch people:", error);
    res.status(500).json({ error: "Failed to fetch people" });
  }
});

// Fetch a single person by id.
app.get("/peoplejson/:id", async (req, res) => {
  const id = toObjectId(req.params.id);
  if (!id) {
    res.status(400).json({ error: "Invalid id" });
    return;
  }

  try {
    const person = await people.findOne({ _id: id });
    if (!person) {
      res.status(404).json({ error: "Person not found" });
      return;
    }
    res.json(person);
  } catch (error) {
    console.error("Failed to fetch person:", error);
    res.status(500).json({ error: "Failed to fetch person" });
  }
});

// Create a new person.
app.post("/peoplejson", async (req, res) => {
  const { name } = req.body ?? {};
  if (typeof name !== "string" || name.trim() === "") {
    res.status(400).json({ error: "A non-empty 'name' is required" });
    return;
  }

  try {
    const person = { name: name.trim(), hobbies: readHobbies(req.body ?? {}) ?? [] };
    const result = await people.insertOne(person as OptionalId<Person>);
    res.status(201).json({ _id: result.insertedId, ...person });
  } catch (error) {
    console.error("Failed to create person:", error);
    res.status(500).json({ error: "Failed to create person" });
  }
});

// Replace an existing person.
app.put("/peoplejson/:id", async (req, res) => {
  const id = toObjectId(req.params.id);
  if (!id) {
    res.status(400).json({ error: "Invalid id" });
    return;
  }

  const { name } = req.body ?? {};
  if (typeof name !== "string" || name.trim() === "") {
    res.status(400).json({ error: "A non-empty 'name' is required" });
    return;
  }

  try {
    // Replacing drops the legacy 'hobby' field so updated documents share one shape.
    const person = { name: name.trim(), hobbies: readHobbies(req.body ?? {}) ?? [] };
    const updated = await people.findOneAndReplace(
      { _id: id },
      person,
      { returnDocument: "after" }
    );

    if (!updated) {
      res.status(404).json({ error: "Person not found" });
      return;
    }
    res.json(updated);
  } catch (error) {
    console.error("Failed to update person:", error);
    res.status(500).json({ error: "Failed to update person" });
  }
});

// Delete a person.
app.delete("/peoplejson/:id", async (req, res) => {
  const id = toObjectId(req.params.id);
  if (!id) {
    res.status(400).json({ error: "Invalid id" });
    return;
  }

  try {
    const result = await people.deleteOne({ _id: id });
    if (result.deletedCount === 0) {
      res.status(404).json({ error: "Person not found" });
      return;
    }
    res.status(204).end();
  } catch (error) {
    console.error("Failed to delete person:", error);
    res.status(500).json({ error: "Failed to delete person" });
  }
});

app.use((_req, res) => {
  res.status(404).type("text").send("Really not Found");
});

const start = async (): Promise<void> => {
  await client.connect();
  app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/people`);
    console.log(`Server running at http://localhost:${port}/peoplejson`);
  });
};

start().catch(error => {
  console.error("Failed to start server:", error);
  process.exit(1);
});
