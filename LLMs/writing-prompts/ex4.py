#!/usr/bin/env python

from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('lab.env')

client = OpenAI()

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
Now that you've experimented with different prompt variations, let's apply what you've learned to build a better product recommendation chatbot. You'll create a **prompt template**—a reusable pattern that combines user input with additional context to generate high-quality recommendations.
"""

# New user query
user_query = "I need a tablet for digital art under $500, I'm an artist who values screen quality."

# Prompt template: user_query + additional context
chatbot_prompt = f"{user_query} Recommend a product with good performance."
chatbot_response = generate_response(chatbot_prompt)
print(f"User Query: {user_query}")
print(f"Response: {chatbot_response}")
