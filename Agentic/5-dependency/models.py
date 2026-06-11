# models.py
# ---------------------------------------------------------
# Pydantic models define the structure of data returned
# from providers and exposed through the API.
#
# These models remain unchanged regardless of DI or
# architectural patterns — they are pure data containers.
# ---------------------------------------------------------

from pydantic import BaseModel

class Product(BaseModel):
    product_id: int
    model: str
    manufacturer: str
    name: str
    price_net: float
    tax_rate: float
    product_code: str
    release_date: str
    stock_quantity: int
