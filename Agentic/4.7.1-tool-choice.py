from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIChatModel
import sqlite3

# Choose a tool-capable model; if you keep "mistral:7b" expect worse tool-calling.
# model = OpenAIChatModel("mistral:7b")
model = OpenAIChatModel("qwen2.5:7b-instruct")
# Installed with ollama pull qwen2.5:7b-instruct
# OpenAI models run the code returned from the database.

DB_PATH = "mobile_store.db"

system_prompt="""
Default is tool is calculate_tool, unless you are asked about mobile products.

If the question cannot be answered with pure arithmetic then ALWAYS use run_sql.

Use run_sql for mobile products.

Only use the following TABLENAME(COLUMN NAMES) schema;
- Products (product_id,model,manufacturer,name,price_net,tax_rate,product_code,release_date,stock_quantity)
- Customers (customer_id,first_name,last_name,email,phone,address)
- Orders (order_id,customer_id,order_date)
- OrderItems (order_item_id,order_id,product_id,quantity,price_net_at_purchase,tax_rate_at_purchase)

ALL column names MUST be fully qualified.
"""

class CalculationInput(BaseModel):
    price: float = Field(gt=0, description="Unit price before tax.")
    quantity: int = Field(gt=0, description="Number of items.")
    tax_rate: float = Field(ge=0, le=1, description="Tax rate as a decimal (e.g. 0.08 for 8%).")

agent = Agent(
    model=model,
    tools=[],
    retries=3,
    system_prompt=system_prompt,
)

@agent.tool
def calculate_total(ctx: RunContext, params: CalculationInput) -> float:
    """Calculate the total price including tax."""
    subtotal = params.price * params.quantity
    total = subtotal * (1 + params.tax_rate)
    return round(total, 2)

@agent.tool
def run_sql(ctx: RunContext, sql: str) -> list[dict]:
    """Execute SQL query"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    columns = [col[0] for col in cur.description] if cur.description else []
    result = [dict(zip(columns, row)) for row in rows]
    conn.close()
    return result


if __name__ == "__main__":
    # Pure math → calculate_total
    result = agent.run_sync("What is the total cost for 5 items at $29.99 each with 8% tax?")
    print(result.output)  # e.g. "The total cost is $161.95."

    # DB question → run_sql
    result = agent.run_sync("Which mobile product generated the most revenue including tax?")
    print(result.output)  # e.g. "The iPhone 15 128GB generated the most revenue, with $1,950.40 in total."
