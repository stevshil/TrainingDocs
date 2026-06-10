from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from calc_tool import calculate_total
from db_tool_better import run_sql
from dotenv import load_dotenv

load_dotenv("./lab.env")

# Choose a tool-capable model; if you keep "mistral:7b" expect worse tool-calling.
# model = OpenAIChatModel("mistral:7b")
model = OpenAIChatModel("qwen2.5:7b-instruct")
# Installed with ollama pull qwen2.5:7b-instruct
# OpenAI models run the code returned from the database.

DB_PATH = "mobile_store.db"

system_prompt="""
You MUST use run_sql for ANY question involving:
- products
- mobile devices
- revenue
- tax
- prices
- quantities
- orders
- customers
- stock
- sales
- totals derived from database values

NEVER use calculate_total for anything involving the mobile database.

Only use calculate_total for simple arithmetic when NO database information is required.
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

    result = agent.run_sync("Which mobile product was the least successful?")
    print(result.output)