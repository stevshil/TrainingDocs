# providers/interface.py
# ---------------------------------------------------------
# This interface defines the abstraction for all product
# providers. Both cache and database providers implement
# this interface, allowing the Factory Method to return
# either one interchangeably.
# ---------------------------------------------------------

from typing import Optional
from models import Product

class ProductProvider:
    """Interface for all product providers."""

    async def __call__(self, product_id: int) -> Optional[Product]:
        raise NotImplementedError
