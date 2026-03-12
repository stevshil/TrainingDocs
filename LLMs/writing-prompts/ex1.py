#!/usr/bin/env python

from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('../lab.env')

client = OpenAI()

"""
OpenAI set up and response generation
"""
# Set up OpenAI response generation function
def generate_response(prompt, max_length=100):
    """
    Generate a response using OpenAI's chat completions API
    """
    try:
        messages = [
            # To return JSON message format in response at least 1 message must contain JSON.
            {"role": "system", "content": "You are a helpful product recommendation assistant. Returning JSON output."},
            # {"role": "system", "content": "You are a helpful product recommendation assistant."},
            {"role": "user", "content": prompt}
        ]
        
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages,
            max_tokens=max_length,
            # Uncomment below if you want JSON formatted messages
            response_format={"type": "json_object"}
        )
        print(f"RESPONSE: {response}")
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating response: {e}")
        return None

# Test the generate_response function
test_prompt = "What is the capital of France?"
test_response = generate_response(test_prompt, max_length=50)
print(f"Test prompt: {test_prompt}")
print(f"Response: {test_response}\n")