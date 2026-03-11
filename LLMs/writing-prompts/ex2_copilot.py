#!/usr/bin/env python

import json
from dotenv import load_dotenv
from Copilot import Copilot

# Load environment variables from .env file
load_dotenv('lab.env')

client = Copilot()

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
            {"role": "system", "content": "You are a helpful product recommendation assistant."},
            {"role": "user", "content": prompt}
        ]
        
        response = client.completions(
            messages=messages,
            max_tokens=max_length,
            model="gpt-4.1-mini"
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating response: {e}")
        return None

# Test the generate_response function
# print(generate_response("Recommend a product for me."))
# Better prompt
# print(generate_response("Recommend a coffee machine for me."))
import sys
print(generate_response(sys.argv[1]))