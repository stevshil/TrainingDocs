import os
import requests
from dotenv import load_dotenv

# Load token from lab.env
load_dotenv("lab.env")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

API_URL = "https://models.inference.ai.azure.com/chat/completions"

def generate_response(prompt, max_length=100):
    """
    Generate a response using Copilot's GitHub Models chat completions API.
    """
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {GITHUB_TOKEN}"
        }

        payload = {
            "model": "gpt-4.1-mini",
            "messages": [
                {"role": "system", "content": "You are a helpful product recommendation assistant."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": max_length
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()

        data = response.json()
        return data["choices"][0]["message"]["content"]

    except Exception as e:
        print(f"Error generating response: {e}")
        return None


# Test the function
test_prompt = "What is the capital of France?"
test_response = generate_response(test_prompt, max_length=50)

print(f"Test prompt: {test_prompt}")
print(f"Response: {test_response}\n")
