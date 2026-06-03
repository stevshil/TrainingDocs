import asyncio
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic import BaseModel, Field

class QueryResult(BaseModel):
    confidence: float = Field(ge=0.0, le=1.0)
    explanation: str = Field(max_length=400)

# This is the correct constructor for your version
model = OpenAIChatModel("mistral:7b")

agent = Agent(
    model=model,
    output_type=QueryResult,
    system_prompt="""
You are an expert on neural networks, and you can answer any questions, but you always back it up with a rating.

If your first attempt is not valid JSON EXACTLY matching the schema,
discard it completely and output a NEW corrected JSON object.

Never output the invalid attempt.
Never explain the correction.
Never output anything except the final JSON object.

You MUST return ONLY a JSON object with exactly these fields:

{
  "confidence": number between 0 and 1,
  "explanation": string
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
)

async def run_agent():
    result = await agent.run("Explain neural networks'")
    return result.output

# Run the async function
x = 0
while x < 4:
    try:
        output = asyncio.run(run_agent())
        break
    except:
        if x == 0:
            print("Thinking",end="")
        print(".",end="")

    x=x+1

print()

print(f"{output.explanation}\n\nAccuracy of Statement: {float(output.confidence)*100}%")
