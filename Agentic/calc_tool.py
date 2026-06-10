from pydantic import BaseModel, Field
from pydantic_ai import RunContext

class CalculationInput(BaseModel):
    price: float = Field(gt=0, description="Unit price before tax.")
    quantity: int = Field(gt=0, description="Number of items.")
    tax_rate: float = Field(ge=0, le=1, description="Tax rate as a decimal (e.g. 0.08 for 8%).")

def calculate_total(ctx: RunContext, params: CalculationInput) -> float:
    """
Calculate the total price including tax.
The calculation requires a price, quantity and the tax rate as a percentage (e.g., 0.08 for 8% tax).
"""
    subtotal = params.price * params.quantity
    total = subtotal * (1 + params.tax_rate)
    return round(total, 2)
