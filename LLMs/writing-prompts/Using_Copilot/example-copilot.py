import requests, os
from dotenv import load_dotenv


url = "https://models.inference.ai.azure.com/chat/completions"
load_dotenv('lab.env')
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {GITHUB_TOKEN}"
}

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "user", "content": "Explain quantum computing simply."}
    ]
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
