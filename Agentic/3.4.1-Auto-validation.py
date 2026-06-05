#!/usr/bin/env python

import os
from pydantic import BaseModel, Field
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

# model = OpenAIChatModel("gpt-oss:20b")
model = OpenAIChatModel("mistral:7b")

agent = Agent(
    model = model,
    output_type=ProductReview,
    system_prompt="""
You are an expert in computer monitors, and can provide truthful reviews given a product overview.

If your first attempt is not valid JSON EXACTLY matching the schema,
discard it completely and output a NEW corrected JSON object.

Never output the invalid attempt.
Never explain the correction.
Never output anything except the final JSON object.

You MUST return ONLY a JSON object with exactly these fields:

{
  "rating": number between 1 and 5,
  "review": string
  "recommend": bool
}

Rules:
- Extract on the "arguments" value
- No lists.
- No tool calls.
- No markdown.
- No text before or after the JSON.
- No explanations.
"""
)

# The agent will ensure the output matches this schema
x = 0
while x < 4:
    try: # Prevent Mistral crashing out
        result = agent.run_sync(f'Review this product: {product_data}')
        break
    except Exception as e:
        # print(f"Exception: {e}")
        if x == 0:
            print("Thinking",end="")
        print(".",end="")

print()
review = result.output
print(f"Review: {review.review_text}\nRating: {review.rating} out of 5\nRecommend: {review.recommend}")