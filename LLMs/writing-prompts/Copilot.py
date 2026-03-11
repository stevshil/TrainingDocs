#!/usr/bin/env python

import os
import requests
import json
from dotenv import load_dotenv

from types import SimpleNamespace
import json

# Convert the JSON into an object, so we can still process as normal
def to_object(data):
    if isinstance(data, dict):
        return SimpleNamespace(**{k: to_object(v) for k, v in data.items()})
    if isinstance(data, list):
        return [to_object(item) for item in data]
    return data


class Copilot:
    def __init__(self, env_file="lab.env"):
        load_dotenv(env_file)
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.url = "https://models.inference.ai.azure.com/chat/completions"

        if not self.github_token:
            raise ValueError("GITHUB_TOKEN not found in environment variables.")

    def completions(self, messages, max_tokens=100, model="gpt-4.1-mini"):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.github_token}"
        }

        data = {
            "model": model,
            "messages": messages
        }

        response = requests.post(self.url, headers=headers, json=data)
        return to_object(response.json())


if __name__ == "__main__":
    client = Copilot()

    messages = [
        {"role": "system", "content": "You are a helpful product recommendation assistant."},
        {"role": "user", "content": "What is the capital of England"}
    ]

    model = "gpt-4.1-mini"
    max_length = 100

    data = client.completions(messages, max_length, model)
    print(data.choices[0].message.content)
  
