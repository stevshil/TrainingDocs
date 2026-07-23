import sqlite3
from pydantic_ai import Agent, RunContext

# This version improves the PyDoc for the agent to understand why to use this tool.

DB_PATH = "mobile_store.db"

def run_sql(ctx: RunContext, sql: str) -> list[dict]:
    """
Execute SQL query against the mobile information database.

ONLY USE THESE TABLES AND COLUMNS from the Database schema:
Products (product_id, model, manufacturer, name, price_net, tax_rate, product_code, release_date, stock_quantity)
Customers (customer_id, first_name, last_name, email, phone, address)
Orders (order_id, customer_id, order_date)
OrderItems (order_item_id, order_id, product_id, quantity, price_net_at_purchase, tax_rate_at_purchase)

Table aliases:
p = Products
c = Customers
o = Orders
oi = OrderItems

STRICT RULES:
- NEVER invent column names.
- NEVER abbreviate column names.
- ALWAYS fully qualify columns.
- ALWAYS join tables correctly.
- ALWAYS compute revenue using:
  oi.quantity * oi.price_net_at_purchase * (1 + oi.tax_rate_at_purchase)
- ALWAYS ensure only valid SQL is passed as sql variable to cur.execute(sql)
- NEVER output the SQL query itself, only the final answer.
- ONLY use columns and aliases from the database schema.
- NEVER make up your own columns or table names, use only what you've been told here.
- ALL SQL statements must conform to SQLite3 syntax.

EXAMPLE OUTPUT:
The iPhone 15 128GB generated the most revenue, with $1,950.40 in total.

Must return valid JSON.
"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    columns = [col[0] for col in cur.description] if cur.description else []
    result = [dict(zip(columns, row)) for row in rows]
    conn.close()
    return result