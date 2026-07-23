# Set up OpenAI response generation function
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
import re

# Load environment variables from .env file
load_dotenv('lab.env')

client = OpenAI()

def fetch_f1_results(year):
    url = f"https://www.formula1.com/en/results/{year}/races"
    html = requests.get(url).text
    return html

def parse_race_winners(html):
    soup = BeautifulSoup(html, "html.parser")
    results = []

    for row in soup.select("tr"):
        cols = row.find_all("td")
        if len(cols) >= 3:
            race = cols[0].get_text(strip=True)
            date = cols[1].get_text(strip=True)
            winner = cols[2].get_text(strip=True)
            team = cols[3].get_text(strip=True)
            laps = cols[4].get_text(strip=True)
            time = cols[5].get_text(strip=True)
            results.append({"race": race, "date": date, "winner": winner, "team": team, "laps": laps, "time": time})

    return results

# OpenAI version to extract year from prompt
# def extract_year_from_prompt(prompt):
#     current_year = datetime.now().year

#     messages = [
#         {
#             "role": "system",
#             "content": (
#                 "Extract the Formula 1 season year mentioned in the user prompt. "
#                 f"Return ONLY the 4-digit year. If no year is mentioned, assume {current_year}."
#             )
#         },
#         {"role": "user", "content": prompt}
#     ]

#     response = client.chat.completions.create(
#         model="gpt-4.1-mini",
#         messages=messages,
#         max_tokens=10
#     )

#     return response.choices[0].message.content.strip()

# Free Ollama and Mistral to extract year from prompt
def extract_year_from_prompt(prompt, model="mistral:7b"):
    current_year = datetime.now().year

    messages = [
        {
            "role": "system",
            "content": (
                "Extract the Formula 1 season year mentioned in the user prompt. "
                f"Return ONLY the 4-digit year. If no year is mentioned, assume {current_year}."
                "Do NOT return any other text or explanation, just the year."
            )
        },
        {"role": "user", "content": prompt}
    ]

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": model,
            "messages": messages,
            "stream": False
        }
    ).json()

    print(response)
    return re.findall(r'\d{4}', response["message"]["content"].strip())[0]

def generate_response(prompt, max_length=100):
    extracted_year = extract_year_from_prompt(prompt)

    if not extracted_year.isdigit():
        return f"Could not determine the year from your question: {prompt}"

    year = int(extracted_year)

    # ---------------------------
    # NEW: Branch based on year
    # ---------------------------
    if year >= 2024:
        # Use real scraped data
        html = fetch_f1_results(year)
        winners = parse_race_winners(html)

        messages = [
            {"role": "system", "content": "You are a helpful F1 results assistant."},
            {"role": "system", "content": f"Here are the official {year} race winners:\n{winners}"},
            {"role": "user", "content": prompt}
        ]

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages,
            max_tokens=max_length
        )
        try:
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating response: {e}")
            return None

    else:
        # ---------------------------
        # NEW: Use model’s internal knowledge
        # ---------------------------
        messages = [
            {"role": "system", "content": "You are a helpful F1 historian assistant."},
            {"role": "user", "content": prompt}
        ]

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages,
            max_tokens=max_length
        )
        try:
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating response: {e}")
            return None

# Test the generate_response function
test_prompt = input("Ask a formula 1 question: ")
# test_prompt = "who won the 2026 spanish grand prix"
test_response = generate_response(test_prompt, max_length=50)
# html=fetch_f1_results(2026)
# print(parse_race_winners(html))
# print(f"Test prompt: {test_prompt}")
print(f"Response: {test_response}\n")