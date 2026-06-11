# providers/cache_provider.py
# ---------------------------------------------------------
# In-memory cache provider implementing ProductProvider.
#
# The Factory Method may return this provider if the product
# is already cached. The service does not know or care that
# this is a cache — it only sees the interface.
# ---------------------------------------------------------

import time
from typing import Dict, Optional
from models import Product
from providers.interface import ProductProvider

class CacheProvider(ProductProvider):
    """In-memory cache implementing ProductProvider."""

    def __init__(self, ttl_seconds: int = 60):
        # TTL controls how long cached entries remain valid
        self.ttl = ttl_seconds
        self._cache: Dict[int, tuple[float, Product]] = {}

    async def __call__(self, product_id: int) -> Optional[Product]:
        """Return cached product if present and not expired."""
        entry = self._cache.get(product_id)
        if not entry:
            return None

        timestamp, product = entry

        # Expire old entries
        if time.time() - timestamp > self.ttl:
            del self._cache[product_id]
            return None

        return product

    def set(self, product_id: int, product: Product):
        """Store product in cache with timestamp."""
        self._cache[product_id] = (time.time(), product)
