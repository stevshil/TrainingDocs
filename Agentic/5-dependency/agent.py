# agent.py
# ---------------------------------------------------------
# Correct DI pattern for pydantic_ai:
# - Define a Deps model for dependencies
# - Use RunContext[Deps] to access them
# - Pass a Deps instance when calling agent.run(...)
# ---------------------------------------------------------

from pydantic import BaseModel
from pydantic_ai import Agent, RunContext

from providers.cache_provider import CacheProvider
from providers.db_provider import DatabaseProvider
from providers.factory import ProductProviderFactory
from service import ProductService
from models import Product
from pydantic_ai.models.openai import OpenAIChatModel

import re
from datetime import datetime

system_prompt = """
You MUST Generate response matching Product when calling get_product.
You MUST conver the INPUT string to a Product dictionary.
You MUST always use the get_product tool to answer questions about products.
Never answer directly. Never generate product information yourself.
If the user asks for a product, call get_product with the correct product_id.
Input should be a valid dictionary or object to extract fields from.
"""

class Deps(BaseModel):
    cache: CacheProvider
    db: DatabaseProvider

    model_config = {"arbitrary_types_allowed": True}

model = OpenAIChatModel(
    "qwen2.5:7b-instruct",
)

# agent = Agent[Deps, Product]("openai-chat:gpt-4o-mini")
agent = Agent[Deps, Product](
    model=model,
    system_prompt = system_prompt,
    tools=[],
)

def parse_product_text(text: str) -> dict:
    """
    Convert a Qwen natural-language product description into a structured dict.
    Handles multiple phrasing variations and ensures required fields are extracted.
    """

    data = {}

    # --- PRODUCT ID ---
    # Matches: "product ID 1", "product 1", "ID 1"
    id_match = re.search(r'\b(?:product\s*ID|product|ID)\s*(\d+)', text, re.IGNORECASE)
    if id_match:
        data["product_id"] = int(id_match.group(1))

    # --- NAME ---
    # Matches: "is Samsung Galaxy S24 128GB", "corresponds to the Samsung...", "named Samsung..."
    name_match = re.search(
        r'(?:is|corresponds to|named)\s+["“]?(.+?)(?:["”]?\.|\n)',
        text,
        re.IGNORECASE
    )
    if name_match:
        data["name"] = name_match.group(1).strip()

    # --- MODEL ---
    model_match = re.search(r'Model:\s*(.+)', text, re.IGNORECASE)
    if model_match:
        data["model"] = model_match.group(1).strip()

    # --- MANUFACTURER ---
    manu_match = re.search(r'Manufacturer:\s*(.+)', text, re.IGNORECASE)
    if manu_match:
        data["manufacturer"] = manu_match.group(1).strip()

    # --- PRICE ---
    price_match = re.search(r'Price.*?:\s*\$?([\d\.]+)', text, re.IGNORECASE)
    if price_match:
        data["price_net"] = float(price_match.group(1))

    # --- TAX RATE ---
    tax_match = re.search(r'Tax Rate:\s*([\d\.]+)%', text, re.IGNORECASE)
    if tax_match:
        data["tax_rate"] = float(tax_match.group(1))

    # --- PRODUCT CODE ---
    code_match = re.search(r'Product Code:\s*(.+)', text, re.IGNORECASE)
    if code_match:
        data["product_code"] = code_match.group(1).strip()

    # --- RELEASE DATE ---
    date_match = re.search(r'Release Date:\s*(.+)', text, re.IGNORECASE)
    if date_match:
        raw_date = date_match.group(1).strip()
        try:
            data["release_date"] = datetime.strptime(raw_date, "%B %d, %Y").strftime("%Y-%m-%d")
        except ValueError:
            data["release_date"] = raw_date  # fallback

    # --- STOCK QUANTITY ---
    stock_match = re.search(r'Stock Quantity:\s*(\d+)', text, re.IGNORECASE)
    if stock_match:
        data["stock_quantity"] = int(stock_match.group(1))

    return data

def product_from_output(output):
    """
    Accepts either:
    - a Product instance (already structured)
    - a string (LLM hallucinated description)

    Returns a Product instance.
    """
    if isinstance(output, Product):
        return output

    if isinstance(output, str):
        data = parse_product_text(output)
        return Product(**data)

    raise TypeError(f"Unsupported output type: {type(output)}")


@agent.tool
async def get_product(ctx: RunContext[Deps], product_id: int) -> Product | None:
    cache = ctx.deps.cache
    db = ctx.deps.db

    factory = ProductProviderFactory(cache, db)
    service = ProductService(factory)

    return await service.get_product(product_id)

