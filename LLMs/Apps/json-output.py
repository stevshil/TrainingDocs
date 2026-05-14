from dotenv import load_dotenv
from openai import OpenAI

load_dotenv('lab.env')
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "user", "content": "Extract the name and age from: 'Sarah is 32 years old.'"}
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "PersonInfo",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "age": {"type": "integer"}
                },
                "required": ["name", "age"]
            }
        }
    }
)

print(response.choices[0].message.content)
