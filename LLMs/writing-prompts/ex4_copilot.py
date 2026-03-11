#!/usr/bin/env python

import json
from dotenv import load_dotenv
from Copilot import Copilot

# Load environment variables from .env file
load_dotenv('lab.env')

client = Copilot()

"""
Apply Prompts to a Product Recommendation Chatbot
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

user_query = "I need a tablet for digital art under $500, I'm an artist who values screen quality."

# Prompt template: user_query + additional context
chatbot_prompt = f"{user_query} Recommend a product with good performance."
chatbot_response = generate_response(chatbot_prompt)
print(f"User Query: {user_query}")
print(f"Response: {chatbot_response}")