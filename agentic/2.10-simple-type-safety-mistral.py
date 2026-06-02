from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic import BaseModel, Field

class QueryResult(BaseModel):
    sentiment: str = Field(description="positive, negative, or neutral")
    confidence: float = Field(ge=0.0, le=1.0)
    summary: str = Field(max_length=200)

# This is the correct constructor for your version
model = OpenAIChatModel("mistral:7b")

agent = Agent(
    model=model,
    system_prompt="""
You MUST return ONLY valid JSON. 
No explanations. No markdown. No text outside the JSON object.
""",
    output_type=QueryResult,
)
# NOTE: The system_prompt has been added to work with local LLM models like Mistral
# NOTE: It is not required for OpenAI

# result = agent.run_sync("Summarize: 'The product works well but shipping was slow.'")
# print(result.output)

statements = [
    "Summarize: 'The product works well but shipping was slow.'",
    "Summarize: 'The product was aweful, but the shipping was awesome'",
    "Summarize: 'The product was OK, but nothing to write home about'"
]

results = []

for stmt in statements:
    run = agent.run_sync(stmt)
    results.append(run.output)

for i, r in enumerate(results, start=1):
    print(f"Result {i}:")
    print(f"  Original: {statements[i]}")
    print(f"  Sentiment: {r.sentiment}")
    print(f"  Confidence: {r.confidence}")
    print(f"  Summary: {r.summary}")