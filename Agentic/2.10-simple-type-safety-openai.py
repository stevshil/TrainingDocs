import os
from pydantic import BaseModel, Field
from pydantic_ai import Agent
class QueryResult(BaseModel):
    """Schema the agent must populate. Pydantic validates each field."""
    sentiment: str = Field(description="positive, negative, or neutral")
    confidence: float = Field(ge=0.0, le=1.0)
    summary: str = Field(max_length=200)

agent = Agent(
    os.getenv('AI_MODEL', 'openai:gpt-5.4-mini'),
    output_type=QueryResult,
    # constrain + validate the model's output
)

result = agent.run_sync("Summarize: 'The product works well but shipping was slow.'")

print(result.output.sentiment, result.output.confidence)
# Pydantic raises ValidationError if confidence > 1.0 or summary >200 chars,
# and Pydantic AI re-prompts the model to fix the response.