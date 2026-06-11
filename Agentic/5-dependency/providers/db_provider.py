# providers/db_provider.py
# ---------------------------------------------------------
# SQLite-backed provider implementing ProductProvider.
#
# The Factory Method returns this provider when the cache
# does not contain the requested product.
# ---------------------------------------------------------

import sqlite3
from typing import Optional
from models import Product
from providers.interface import ProductProvider

class DatabaseProvider(ProductProvider):
    """SQLite-backed provider implementing ProductProvider."""

    def __init__(self, db_path: str = "mobile_store.db"):
        self.db_path = db_path

    async def __call__(self, product_id: int) -> Optional[Product]:
        """Fetch product from SQLite by ID."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT product_id, model, manufacturer, name, price_net, tax_rate,
                   product_code, release_date, stock_quantity
            FROM Products
            WHERE product_id = ?
        """, (product_id,))

        row = cursor.fetchone()
        conn.close()

        if not row:
            return None

        return Product(
            product_id=row[0],
            model=row[1],
            manufacturer=row[2],
            name=row[3],
            price_net=row[4],
            tax_rate=row[5],
            product_code=row[6],
            release_date=row[7],
            stock_quantity=row[8],
        )
