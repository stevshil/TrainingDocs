from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from calc_tool import calculate_total
from db_tool import run_sql

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

agent = Agent(
    model=model,
    tools=[calculate_total,run_sql],
    retries=3,
    system_prompt=system_prompt,
)

if __name__ == "__main__":
    # Pure math → calculate_total
    result = agent.run_sync("What is the total cost for 5 items at $29.99 each with 8% tax?")
    print(result.output)  # e.g. "The total cost is $161.95."

    # DB question → run_sql
    result = agent.run_sync("Which mobile product generated the most revenue including tax?")
    print(result.output)  # e.g. "The iPhone 15 128GB generated the most revenue, with $1,950.40 in total."
