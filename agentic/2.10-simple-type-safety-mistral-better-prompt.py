from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic import BaseModel, Field

class QueryResult(BaseModel):
    sentiment: str = Field(description="positive, negative, or neutral")
    confidence: float = Field(ge=0.0, le=1.0)
    summary: str = Field(max_length=200)

# This is the correct constructor for your version
model = OpenAIChatModel("mistral:7b")

# Set up the agent to use Mistral:7b
agent = Agent(
    model=model,
    system_prompt="""
If your first attempt is invalid JSON, FIX IT and output valid JSON.
Do not output the invalid attempt.

You MUST return ONLY a JSON object with exactly these fields:

{
  "sentiment": "positive" | "negative" | "neutral",
  "confidence": number between 0 and 1,
  "summary": string
}

Rules:
- Extract on the "arguments" value
- No lists.
- No tool calls.
- No markdown.
- No text before or after the JSON.
- No explanations.
- If unsure, choose "neutral".
""",
    output_type=QueryResult,
)
# NOTE: The system_prompt has been added to work with local LLM models like Mistral
# NOTE: It is not required for OpenAI
# NOTE: Mistral is running through Ollama for free usage and needs to be told to focus on returning JSON.

statements = [
    "Summarize: 'The product works well but shipping was slow.'",
    "Summarize: 'The product was aweful, but the shipping was awesome'",
    "Summarize: 'The product was OK, but nothing to write home about'"
]

results = []

# Store the results of each statement
for stmt in statements:
    run = agent.run_sync(stmt)
    results.append(run.output)

# Iterate over the results, with r containing the result.
for i, r in enumerate(results, start=1):
    print(f"Result {i}:")
    print(f"  Original: {statements[i-1]}")
    print(f"  Sentiment: {r.sentiment}")
    print(f"  Confidence: {r.confidence}")
    print(f"  Summary: {r.summary}")