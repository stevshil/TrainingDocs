#!/usr/bin/env python

import json
import os
from datetime import date

import requests
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from lab.env file
load_dotenv("lab.env")

provider = os.getenv("AI_PROVIDER", "openai").lower()
f1data = [] # Cache for F1 API responses
f1data_usage = [] # Track usage of cached vs API data

if provider == "ollama": # Set up to use a local Ollama model
    length_limit = 256
    ai_model = os.getenv("AI_MODEL", "mistral:7b") # Which model to use from Ollama
    ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434").rstrip("/") # The API url for Ollama
    if not ollama_url.endswith("/v1"):
        ollama_url = f"{ollama_url}/v1"
    client = OpenAI(
        api_key="ollama",
        base_url=ollama_url,
    )
elif provider == "openai":
    length_limit = 50
    ai_model = os.getenv("AI_MODEL", "gpt-5.4-mini") # Model to use from OpenAI
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"]) # Your API key to use the model
else:
    raise ValueError("AI_PROVIDER must be either 'openai' or 'ollama'.")

messages=[]

# Jolpica is the community-maintained, Ergast-compatible F1 API that is kept up to date each season
F1_API_BASE = "https://api.jolpi.ca/ergast/f1"

# The tool function that will retrieve F1 data from the API, using cached data if available
# This function could be placed in a separate file and imported, to make it cleaner
def fetch_f1_data(endpoint: str = "current") -> str:
    """
    Retrieve Formula 1 data (results, standings, schedules, etc.) from the
    Jolpica F1 API, which includes historic data as well as the latest season.
    """
    cache_key = endpoint.strip("/")
    today = date.today().isoformat()
    cached_data = next(
        (
            item["data"]
            for item in f1data
            if item["endpoint"] == cache_key and item["date"] == today # Check if cached data is for the current day
        ),
        None,
    )
    if cached_data is not None:
        f1data_usage.append(f"f1data cache ({cache_key})")
        return cached_data

    try:
        url = f"{F1_API_BASE}/{cache_key}.json"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        f1data.append({"endpoint": cache_key, "date": today, "data": response.text})
        f1data_usage.append(f"API ({cache_key})")
        return response.text
    except Exception as e:
        return f"Error retrieving F1 data: {e}"

# Tool definition so the model can decide when to call the API for live/up to date info
# This is the line that would make the LLM aware of the available tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "fetch_f1_data",
            "description": (
                "Fetch Formula 1 data (race results, driver/constructor standings, "
                "schedules) from the Jolpica F1 API, including the current/latest "
                "season. Use this for anything requiring up to date or specific data."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "endpoint": {
                        "type": "string",
                        "description": (
                            "Ergast-style API path, e.g. 'current/last/results', "
                            "'current/driverStandings', 'current/constructorStandings', "
                            "'current/circuits/silverstone/results', or '2024/circuits'. "
                            "Do not include '.json'."
                        ),
                    }
                },
                "required": ["endpoint"],
            },
        },
    }
]

available_functions = {"fetch_f1_data": fetch_f1_data}

# Ollama requires increased tokens for reasoning, where as open AI would be ok with 50
def get_response(messages, model=ai_model, max_length=length_limit):
    """
    Generate a response using the chat completions API, calling the F1 data
    tool if the model requests it.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice="required" if provider == "ollama" else "auto",
            max_completion_tokens=max_length
            # max_tokens=max_length
        )
        reply = response.choices[0].message

        while reply.tool_calls:
            messages.append(reply)
            for tool_call in reply.tool_calls:
                function = available_functions.get(tool_call.function.name)
                args = json.loads(tool_call.function.arguments or "{}")
                result = function(**args) if function else "Unknown tool requested."
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result,
                })
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                tools=tools,
                tool_choice="auto",
                max_completion_tokens=max_length
            )
            reply = response.choices[0].message

        return reply.content
    except Exception as e:
        print(f"Error generating response: {e}")
        return None

def build_history(id,message, model=ai_model, max_output=256):
    global messages, f1data_usage
    if len(messages) == 0:
        # messages.append({"role": "system", "content": "You are a helpful assistant."})
        messages.append({"role": "system", "content": "You are a Formula 1 expert, with historic and up to date knowledge."})
        messages.append({"role": "developer", "content": "Ensure ehtical and responsible use of the assistant."})
        messages.append({"role": "developer", "content": "Always include the actual date of a race when it is available in the data."})
        messages.append({"role": "developer", "content": "Answer the latest user question directly. For current-season facts, call fetch_f1_data and base the answer only on its result. For the British Grand Prix winner, use endpoint 'current/circuits/silverstone/results'. Do not give a generic overview unless the user asks for one."})
    
    if len(messages) > 10:
        # Have the AI model summarize the conversation to keep it concise
        summary_prompt = "Summarize the conversation so far in a concise manner."
        new_messages = messages[:4]
        conversation = json.dumps(messages[4:], default=str)
        new_messages.append({
            "role": "user",
            "content": f"{summary_prompt}\n\nConversation:\n{conversation}",
        })
        summary = get_response(new_messages, model=model, max_length=max_output)
        if summary is not None:
            messages = messages[:4]  # Keep the system and developer messages
            messages.append({"role": "assistant", "content": summary})

    f1data_usage = []
    messages.append({"role": "user", "content": message})
    response = get_response(messages, model=model, max_length=max_output)
    if response is not None:
        messages.append({"role": "assistant", "content": response})

    # Write full history to log for later review, or to DB, instead of the terminal
    with open("chat_log.log","a") as fh:
        data_source = ", ".join(f1data_usage) or "not used"
        fh.write(f"ID: {id} - F1 DATA: {data_source} - MESSAGES: {messages}\n")

def is_safe(prompt: str) -> bool:
    # Ollama's OpenAI-compatible API does not implement /moderations.
    if provider == "ollama":
        return True

    # Ensure that the prompt is safe before sending it to the model
    result = client.moderations.create(
        model="omni-moderation-latest",
        input=prompt
    )
    flagged = result.results[0].flagged
    # print(flagged) # True would result in the prompt being considered unsafe
    return not flagged

if __name__ == "__main__":
    allids=[]
    try:
        with open("chat_id_log.log","r") as rh:
            allids = [line.strip() for line in rh.readlines()]
        id = int(allids[-1])+1
        print(f"ID: {id}")
    except:
        id = 1
        print(f"from except ID: {id}")
    allids.append(id)
    with open("chat_id_log.log","w") as wh:
        cleanids = [x for x in allids if x and str(x).strip()]
        wh.write("\n".join(map(str,cleanids)))

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting chat. Goodbye!")
            break
        if is_safe(user_input):
            build_history(id,user_input)
            print(f"Assistant: {messages[-1]['content']}\n")
        else:
            print("Your prompt is not considers appropriate.")        