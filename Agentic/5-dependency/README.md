# Mobile Store API — Factory Method + RunContext DI (Pydantic AI)

This project demonstrates a clean, extensible architecture using:

- **FastAPI** for the API layer  
- **Pydantic AI** for dependency injection via RunContext  
- **Factory Method pattern** to select providers at runtime  
- **Cache + SQLite providers** implementing a shared interface  

The system retrieves product data using a **cache-first strategy**, implemented through a Factory Method.

---

## Architecture Overview

```
FastAPI → Agent → RunContext → Factory → Provider → Product
```

### Why RunContext?

`RunContext` is created automatically by the Pydantic AI agent.  
It provides:

- Dependency injection (`ctx.deps`)
- Model metadata
- Execution context
- Usage tracking

You never instantiate it manually.

---

## Project Structure

```
./
│
├── models.py
├── providers/
│   ├── interface.py
│   ├── cache_provider.py
│   ├── db_provider.py
│   └── factory.py
├── service.py
├── agent.py
└── main.py
```

---

## Running the API

Install dependencies:

```bash
pip install fastapi uvicorn pydantic-ai
```

Start the server:

```bash
uvicorn main:app --reload
```

Test:

```
http://127.0.0.1:8000/products/1
```

---

## Extending the Factory

To add a new provider:

1. Implement `ProductProvider`
2. Add it to `deps` in `agent.py`
3. Update the factory logic

No changes required in:

- `ProductService`
- FastAPI endpoints
- Pydantic models