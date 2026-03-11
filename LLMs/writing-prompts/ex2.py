#!/usr/bin/env python

from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('lab.env')

client = OpenAI()

"""
Write and Test a Baseline Prompt
"""
# Set up OpenAI response generation function
def generate_response(prompt, max_length=100):
    """
    Generate a response using OpenAI's chat completions API
    """
    try:
        messages = [
            {"role": "system", "content": "You are a helpful product recommendation assistant."},
            {"role": "user", "content": prompt}
        ]
        
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages,
            max_tokens=max_length
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating response: {e}")
        return None

"""
Start with a simple, generic prompt for recommending a product. This baseline will help you understand how minimal prompts perform before adding specificity, tone, and context.

Use the `generate_response()` function with a very basic prompt like "Recommend a product for me." Observe the response—is it specific enough? Does it provide actionable recommendations? Think about what information is missing that would help the model give better recommendations.
"""

# Test the generate_response function
print(generate_response("Recommend a product for me."))
