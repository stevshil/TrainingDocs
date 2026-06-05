#!/usr/bin/env python

import os
from pydantic import BaseModel, Field, field_validator, ValidationError
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai import Agent

product_data="""
ProLite XB3294UHSCP-B1
32” 4K VA panel with USB-C connection (95W), KVM Switch and PiP/PbP

The ProLite XB3294UHSCP-B1 is a 32 inch 4K monitor designed to give you more space, sharper detail, and smoother workflows.

Its VA panel with Ultra HD resolution and a 3000:1 contrast ratio delivers crisp, vibrant visuals. A brightness of 350cd/m², 2ms response time, and Adaptive Sync ensure everything stays smooth and clear, whether you're creating content or working with data.

USB-C (95W Power Delivery), HDMI, DisplayPort, and a built-in KVM switch make it easy to manage multiple devices while powering your laptop. PiP (Picture-in-Picture) and PbP (Picture-by-Picture) modes let you view content from two sources at the same time for more efficient multitasking.

The three side borderless design helps you stay focused and supports seamless multi-monitor setups. The height adjustable stand, built-in speakers, and headphone jack provide comfort and convenience throughout your day.

Certified with TCO, TÜV-GS and EPEAT Silver, it’s a smart, sustainable choice for any modern workspace.
"""

class ProductReview(BaseModel):
    rating: int = Field(ge=1, le=5)
    review_text: str
    recommend: bool

    @field_validator('review_text')
    @classmethod
    def review_text_length(cls, v):
        if len(v) < 50:
            raise ValueError('Review must be at least 50 characters.')
        return v

def run_with_fallback(agent, prompt, fallback_data):
    try:
        result = agent.run_sync(prompt)
        return result.output
    except ValidationError:
        print("Using fallback response")
        return fallback_data

fallback_data = ProductReview(
    # The next 2 lines will cause a validation error on Fallback.
    # rating = 0, # Less than 1
    # review_text = "Review unavailable", # Less than 50 characters
    rating = 1,
    review_text = "No review could be generated for this product at this time.",
    recommend = False
)

# model = OpenAIChatModel("gpt-oss:20b")
model = OpenAIChatModel("mistral:7b")

agent = Agent(
    model = model,
    output_type=ProductReview,
    retries=3,
    system_prompt="""
You are an expert in computer monitors, and can provide truthful reviews given a product overview.

You MUST output ONLY a JSON object with exactly these fields:

{
  "rating": number between 1 and 5,
  "review_text": string,
  "recommend": bool
}

Rules:
- Extract on the "arguments" value
- No markdown.
- No lists.
- No tool calls.
- No explanations.
- No text before or after the JSON.
- Never escape braces.
- Never prefix braces with backslashes.
- If your first attempt is invalid JSON, output a NEW corrected JSON object.
"""
)

# We're now using retries in the agent
result = run_with_fallback(agent, f'Review this product: {product_data}', fallback_data)
print()
review = result
print(f"Review: {review.review_text}\nRating: {review.rating} out of 5\nRecommend: {review.recommend}")