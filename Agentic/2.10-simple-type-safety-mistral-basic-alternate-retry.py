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

# Alternative to using retries in the Agent constructor.
count=1
prompt="Summarize: 'The product works well but shipping was slow.'"
while count <= 2:
    try:
        result = agent.run_sync(prompt)
        print(result.output)
        break
    except Exception as e:
        print(f"Exception: {e} {str(result)}")
        prompt+=result
    count+=1