from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic import BaseModel, Field, ValidationError
from pydantic_ai.exceptions import ModelAPIError
from calc_tool import calculate_total
from db_tool_better import run_sql
from dotenv import load_dotenv

load_dotenv("./lab.env")

TOOL_REGISTRY = {
    "run_sql": run_sql,
    "calculate_total": calculate_total,
}

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

You MUST return ONLY valid JSON matching the QueryResult schema.
Do not add any text, markdown, explanation, or wrapper tokens.
"""

judge_prompt="""
Evaluate the response for accuracy and relevance.

ENSURE you use the input_value as the result.
IGNORE any escape sequences.
"""

class QueryResult(BaseModel):
    statement: str
    confidence: float = Field(ge=0.0, le=1.0)
    tool_used: str

class JudgeResult(BaseModel):
    accuracy: str = Field(description="accurate, inaccurate, or partially accurate")
    relevance: str = Field(description="relevant, irrelevant, or partially relevant")


fallback_query_result = QueryResult(
    statement="Unable to provide a response at this time.",
    confidence=0.0,
    tool_used="None"
)

fallback_judge_result = JudgeResult(
    accuracy="inaccurate",
    relevance="irrelevant"
)

def run_with_fallback(agent, prompt, fallback_data):
    try:
        result = agent.run_sync(prompt)
        return result
    except ValidationError:
        print("Using fallback response")
        return fallback_data
    except ModelAPIError as e:
        # This is the exception raised when max retries exceeded
        print(f"Error Type: {type(e).__name__}\nMessage: {str(e)}\nFallback Used: True")
        return fallback_data

agent = Agent(
    model=model,
    tools=[calculate_total,run_sql],
    retries=3,
    system_prompt=system_prompt,
    output_type=QueryResult,
    model_settings={"response_format": "json"},
)

def run_judge_agent(prompt, tools, fallback):
    judge_agent = Agent(
        model = model,
        system_prompt = judge_prompt,
        retries=3,
        output_type=JudgeResult,
        model_settings={"response_format": "json"},
        tools=tools
    )
    return run_with_fallback(judge_agent,prompt,fallback)

if __name__ == "__main__":
    # Pure math → calculate_total
    # result = agent.run_sync("What is the total cost for 5 items at $29.99 each with 8% tax?")
    # print(result.output)  # e.g. "The total cost is $161.95."

    # # DB question → run_sql
    # result = agent.run_sync("Which mobile product generated the most revenue including tax?")
    # print(result.output)  # e.g. "The iPhone 15 128GB generated the most revenue, with $1,950.40 in total."

    # result = agent.run_sync("Which mobile product was the least successful?")
    # print(result.output)

    result = run_with_fallback(agent, "Which mobile product was the least successful?", fallback_query_result)

    print(f"Output: {result.output.statement}")
    print(f"Tool Used: {result.output.tool_used}")
    print(f"Confidence: {result.output.confidence}")

    tool_fn = TOOL_REGISTRY.get(result.output.tool_used)
    result_for_judge = run_judge_agent(
        f"Tool Used: {result.output.tool_used}\nTool Statement: {result.output.statement}\nTool Confidence: {result.output.confidence}", 
        [tool_fn] if tool_fn else [],
        fallback_judge_result)
    print(result_for_judge.output)