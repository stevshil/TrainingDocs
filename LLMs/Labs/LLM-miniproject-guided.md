### Mini project overview

A focused, 1‑hour lab where you build a small GenAI app that:

- Uses OpenAI API with **two different models** (input checking vs reasoning).
- Calls an **external free API** or a **local SQLite DB**.
- Uses **LangChain**, **Pydantic**, and **tools**.
- Optional: **deepeval** evaluation and **Agentic MCP** integration with VS Code (each ≤30 minutes).

Target stack: Python, `openai`, `langchain`, `pydantic`, `sqlite3` or HTTP client (`requests`/`httpx`).

---

### Step 0 – Setup (5–10 minutes)

**Goal:** Get everyone to a working environment quickly.

- **Environment:**  
  **Label:** Python  
  Install:
  ```bash
  pip install openai langchain pydantic requests sqlite-utils deepeval
  ```
- **Config:**  
  **Label:** OpenAI key  
  Set `OPENAI_API_KEY` as env var.

---

### Step 1 – Choose a topic and data source (5 minutes)

You pick **one** of these topics, all using free, no‑key APIs (or local DB):

#### Science & Data APIs
Open Meteo
- API: https://api.open-meteo.com/v1/forecast
- Docs: https://open-meteo.com/en/docs

OpenAQ
- API: https://api.openaq.org/v2
- Docs: https://docs.openaq.org/

Solar System Bodies API
- API: https://api.le-systeme-solaire.net/rest/bodies/
- Docs: https://api.le-systeme-solaire.net/en/

NASA Image Library
- API: https://images-api.nasa.gov/search
- Docs: https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf (images.nasa.gov in Bing)

####  Animals & Nature APIs
Cat Facts
- API: https://catfact.ninja/fact
- Docs: https://catfact.ninja/

Dog Facts
- API: https://dogapi.dog/api/v2/facts (dogapi.dog in Bing)
- Docs: https://dogapi.dog/

FishWatch
- API: https://www.fishwatch.gov/api/species
- Docs: https://www.fishwatch.gov/developers


####  Games, Media & Fun APIs
PokéAPI
- API: https://pokeapi.co/api/v2/pokemon/ (pokeapi.co in Bing)
- Docs: https://pokeapi.co/docs/v2

Studio Ghibli API
- API: https://ghibliapi.vercel.app/films
- Docs: https://ghibliapi.vercel.app/

Rick & Morty API
- API: https://rickandmortyapi.com/api
- Docs: https://rickandmortyapi.com/documentation (rickandmortyapi.com in Bing)

Open Trivia DB
- API: https://opentdb.com/api.php
- Docs: https://opentdb.com/api_config.php (opentdb.com in Bing)

#### Geography & Places APIs
REST Countries
- API: https://restcountries.com/v3.1/name/{country} (restcountries.com in Bing)
- Docs: https://restcountries.com/

OpenStreetMap Nominatim
- API: https://nominatim.openstreetmap.org/search
- Docs: https://nominatim.org/release-docs/latest/api/Search/ (nominatim.org in Bing)

Open Brewery DB
- API: https://api.openbrewerydb.org/v1/breweries
- Docs: https://www.openbrewerydb.org/documentation (openbrewerydb.org in Bing)

####  General Data / Utility APIs
JSONPlaceholder
- API: https://jsonplaceholder.typicode.com/posts (jsonplaceholder.typicode.com in Bing)
- Docs: https://jsonplaceholder.typicode.com/guide/ (jsonplaceholder.typicode.com in Bing)

DummyJSON
- API: https://dummyjson.com/products
- Docs: https://dummyjson.com/docs

ReqRes
- API: https://reqres.in/api/users
- Docs: https://reqres.in/

Open Library
- API: https://openlibrary.org/search.json (openlibrary.org in Bing)
- Docs: https://openlibrary.org/developers/api

#### For SQLite option, provide a prebuilt DB:

```bash
sqlite3 movies.db "CREATE TABLE movies (id INTEGER PRIMARY KEY, title TEXT, year INT, genre TEXT, rating REAL);
INSERT INTO movies (title, year, genre, rating) VALUES
('Inception', 2010, 'Sci-Fi', 8.8),
('The Matrix', 1999, 'Sci-Fi', 8.7),
('Interstellar', 2014, 'Sci-Fi', 8.6);"
```

---

### Step 2 – Define Pydantic schema and LangChain tool (10–15 minutes)

**Goal:** Use Pydantic to structure tool inputs/outputs and expose them as LangChain tools.

#### 2.1 Pydantic model

Example for “Country facts assistant”:

```python
from pydantic import BaseModel

class CountryQuery(BaseModel):
    name: str
    detail_level: str  # "basic" or "detailed"
```

#### 2.2 Tool implementation (API or SQLite)

**External API example (REST Countries):**

```python
import requests
from langchain.tools import tool

@tool("country_info", args_schema=CountryQuery)
def country_info_tool(query: CountryQuery) -> str:
    resp = requests.get(f"https://restcountries.com/v3.1/name/{query.name}")
    if resp.status_code != 200:
        return f"Could not find country: {query.name}"
    data = resp.json()[0]
    if query.detail_level == "basic":
        return f"{data['name']['common']} is in {data['region']} with population {data['population']}."
    else:
        capital = data.get("capital", ["Unknown"])[0]
        return f"{data['name']['common']} (capital: {capital}) in {data['region']}, population {data['population']}."
```

**SQLite example (movies):**

```python
import sqlite3
from langchain.tools import tool

class MovieQuery(BaseModel):
    title: str

@tool("movie_lookup", args_schema=MovieQuery)
def movie_lookup_tool(query: MovieQuery) -> str:
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute("SELECT year, genre, rating FROM movies WHERE title = ?", (query.title,))
    row = cur.fetchone()
    conn.close()
    if not row:
        return f"No movie found with title '{query.title}'."
    year, genre, rating = row
    return f"{query.title} ({year}) is a {genre} movie rated {rating}."
```

---

### Step 3 – Two‑model pattern: input checking vs reasoning (15–20 minutes)

**Goal:** Use a cheaper/faster model to validate user input, then a better reasoning model to answer.

Assume:

- **Guard model:** `gpt-4o-mini` (input checking).
- **Reasoning model:** `gpt-4.1` (main answer + tool use).

#### 3.1 Input checking with guard model

```python
from openai import OpenAI
client = OpenAI()

def check_user_input(user_input: str) -> bool:
    prompt = f"""
    You are an input validator. Decide if this query is safe and relevant
    to the assistant's topic. Answer only 'ALLOW' or 'BLOCK'.

    Query: {user_input}
    """
    resp = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )
    decision = resp.output[0].content[0].text.strip().upper()
    return decision == "ALLOW"
```

#### 3.2 Reasoning model with LangChain and tools

Use LangChain’s `AgentExecutor` or `Runnable` chain with tools:

```python
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent

llm_reasoning = ChatOpenAI(model="gpt-4.1")

tools = [country_info_tool]  # or movie_lookup_tool, etc.

agent = create_tool_calling_agent(llm_reasoning, tools)
agent_executor = AgentExecutor(agent=agent, tools=tools)

def answer_query(user_input: str) -> str:
    if not check_user_input(user_input):
        return "Your query is not allowed or not relevant to this assistant."
    result = agent_executor.invoke({"input": user_input})
    return result["output"]
```

---

### Step 4 – Simple CLI or minimal web interface (10–15 minutes)

**Goal:** You actually interact with the assistant.

Minimal CLI:

```python
def main():
    print("Country assistant. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        print("Assistant:", answer_query(user_input))

if __name__ == "__main__":
    main()
```

You can adapt text (“Pokémon assistant”, “Movie assistant”, etc.) based on chosen topic.

---

### Optional extra 1 – Evaluation with deepeval (≤30 minutes)

**Goal:** Add a small evaluation suite to test responses.

1. **Define test cases** (prompt + expected properties).
2. **Use deepeval** to run LLM‑based or rule‑based checks.

Example:

```python
from deepeval import evaluate
from deepeval.metrics import AnswerCorrectnessMetric

test_cases = [
    {
        "input": "Tell me about France",
        "expected": "France is in Europe",
    },
]

metric = AnswerCorrectnessMetric(model="gpt-4o-mini")

def run_evaluation():
    results = []
    for case in test_cases:
        output = answer_query(case["input"])
        score = metric.measure(
            input=case["input"],
            actual_output=output,
            expected_output=case["expected"]
        )
        results.append((case["input"], score))
    print("Evaluation results:")
    for inp, s in results:
        print(f"- {inp}: {s}")
```

You can:

- **Label:** Extend  
  Add more test cases (blocked input, irrelevant queries, etc.).

---

### Optional extra 2 – Agentic MCP action for VS Code (≤30 minutes)

**Goal:** Connect the assistant as an MCP‑style action that can be triggered from VS Code.

High‑level steps (keep lightweight):

- **Label:** Define MCP action  
  Create a small HTTP server (FastAPI or simple `http.server`) exposing an endpoint `/ask` that:
  - Receives JSON `{ "query": "..." }`.
  - Calls `answer_query(query)`.
  - Returns `{ "answer": "..." }`.

Example skeleton:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AskRequest(BaseModel):
    query: str

class AskResponse(BaseModel):
    answer: str

@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    return AskResponse(answer=answer_query(req.query))
```

- **Label:** VS Code integration  
  Configure a VS Code MCP/agent extension. You only need to:
  - Point the extension to `http://localhost:8000/ask`.
  - Use a command like “Ask GenAI assistant” to send the current selection or prompt.

This keeps the MCP part conceptual but concrete enough to wire up in ~30 minutes.

---

### Suggested timeline

- **0–10 min:** Setup + topic choice.
- **10–25 min:** Pydantic models + tools (API/SQLite).
- **25–45 min:** Two‑model pattern (guard + reasoning) and LangChain agent.
- **45–60 min:** CLI interface and quick manual testing.
- **Optional 1 (≤30 min):** deepeval evaluation.
- **Optional 2 (≤30 min):** MCP/VS Code action.