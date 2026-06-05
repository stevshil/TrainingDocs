from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIChatModel

model = OpenAIChatModel("mistral:7b")

agent = Agent(
    model = model
)

# Validation
class CalculationInput(BaseModel):
    price: float = Field(gt=0)
    quantity: int = Field(gt=0)
    tax_rate: float = Field(ge=0, le=1)

# Definition
@agent.tool
def calculate_total(ctx: RunContext, params: CalculationInput) -> float:
    """Calculate the total price including tax."""

    subtotal = params.price * params.quantity
    total = subtotal * (1 + params.tax_rate)
    return round(total, 2)

    # Imagine if you're writing your tool to interface with office products, or other APIs

# Execution
result = agent.run_sync('What is the total cost for 5 items at $29.99 each with 8% tax?')
print(result.output)
# The agent will call calculate_total(29.99, 5, 0.08)
# Output: "The total cost is $161.95"