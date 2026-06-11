# service.py
# ---------------------------------------------------------
# The service uses the Factory Method to obtain the correct
# provider for each request. It does not know whether the
# provider is a cache, database, or something else entirely.
# ---------------------------------------------------------

from typing import Optional
from models import Product
from providers.factory import ProductProviderFactory
from providers.cache_provider import CacheProvider

class ProductService:
    """Service using a Factory Method to obtain providers."""

    def __init__(self, factory: ProductProviderFactory):
        self.factory = factory

    async def get_product(self, product_id: int) -> Optional[Product]:
        """Retrieve product using provider chosen by the factory."""
        provider = await self.factory.create(product_id)
        product = await provider(product_id)

        # If DB provider was used, write-through to cache
        if product and not isinstance(provider, CacheProvider):
            self.factory.cache.set(product_id, product)

        return product
