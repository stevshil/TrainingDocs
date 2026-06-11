# main.py
# ---------------------------------------------------------
# FastAPI entry point.
# - Build a Deps instance
# - Pass it into agent.run(..., deps=deps)
# - Extract result.data (the tool's return value)
# ---------------------------------------------------------

from fastapi import FastAPI, HTTPException

from agent import agent, Deps, product_from_output
from providers.cache_provider import CacheProvider
from providers.db_provider import DatabaseProvider
from models import Product

app = FastAPI()

deps = Deps(
    cache=CacheProvider(ttl_seconds=120),
    db=DatabaseProvider("mobile_store.db"),
)

@app.get("/products/{product_id}", response_model=Product)
async def fetch_product(product_id: int):
    prompt = f"Fetch product {product_id}."

    result = await agent.run(prompt, deps=deps)

    product = product_from_output(result.output)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product

