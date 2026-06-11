# providers/factory.py
# ---------------------------------------------------------
# This is the Factory Method.
#
# It decides which provider to return based on runtime
# conditions. The service does not know which provider
# it receives — only that it implements ProductProvider.
# ---------------------------------------------------------

from providers.cache_provider import CacheProvider
from providers.db_provider import DatabaseProvider
from providers.interface import ProductProvider

class ProductProviderFactory:
    """Factory Method: chooses which provider to return."""

    def __init__(self, cache: CacheProvider, db: DatabaseProvider):
        self.cache = cache
        self.db = db

    async def create(self, product_id: int) -> ProductProvider:
        """Return cache provider if product is cached, else DB provider."""
        cached = await self.cache(product_id)
        if cached:
            return self.cache

        return self.db
