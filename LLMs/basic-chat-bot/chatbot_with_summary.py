#!/usr/bin/env python

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from lab.env file
load_dotenv('lab.env')

client = OpenAI()

messages=[]

def get_response(messages, model='gpt-5.4-mini', max_length=50):
    """
    Generate a response using the chat completions API
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_completion_tokens=max_length
            # max_tokens=max_length
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating response: {e}")
        return None

def build_history(id,message, model='gpt-5.4-mini', max_output=150):
    global messages
    if len(messages) == 0:
        # messages.append({"role": "system", "content": "You are a helpful assistant."})
        messages.append({"role": "system", "content": "You are a Formula 1 expert, with historic and up to date knowledge."})
        messages.append({"role": "developer", "content": "Ensure ehtical and responsible use of the assistant."})
    
    if len(messages) > 10:
        # Have the AI model summarize the conversation to keep it concise
        summary_prompt = "Summarize the conversation so far in a concise manner."
        new_messages = messages[:2]
        new_messages.append({"role": "user", "content": summary_prompt})
        summary = get_response(messages[2:], model=model, max_length=max_output)
        messages = messages[:2]  # Keep only the system and developer messages
        messages.append({"role": "assistant", "content": summary})  # Add the summary as the assistant's message
        # Replace the conversation history with the summary

    messages.append({"role": "user", "content": message})
    messages.append({"role": "assistant", "content": get_response(messages, model=model, max_length=max_output)})
    print(f"MESSAGES: {messages}")

    # Write history to log for later review, or to DB    
    with open("chat_log.log","a") as fh:
        fh.write(f"ID: {id} - {messages}\n")

def is_safe(prompt: str) -> bool:
    result = client.moderations.create(
        model="omni-moderation-latest",
        input=prompt
    )
    flagged = result.results[0].flagged
    print(flagged)
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