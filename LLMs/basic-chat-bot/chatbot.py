#!/usr/bin/env python

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from lab.env file
load_dotenv('lab.env')

client = OpenAI()

messages=[]

def get_response(messages, model='gpt-4.1-mini', max_length=50):
    """
    Generate a response using the chat completions API
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_length
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating response: {e}")
        return None

def build_history(message, model='gpt-4.1-mini', max_output=50):
    if len(messages) == 0:
        messages.append({"role": "system", "content": "You are a helpful assistant."})
        messages.append({"role": "developer", "content": "Ensure ehtical and responsible use of the assistant."})

    messages.append({"role": "user", "content": message})
    messages.append({"role": "assistant", "content": get_response(messages, model=model, max_length=max_output)})

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting chat. Goodbye!")
            break
        build_history(user_input)
        print(f"Assistant: {messages[-1]['content']}\n")