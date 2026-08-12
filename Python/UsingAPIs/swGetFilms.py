#!/usr/bin/env python

import requests

def get_films():
    url = "https://swapi.info/api/films"
    response = requests.get(url)
    response.raise_for_status()   # fail fast on HTTP errors
    return response.json()

if __name__ == "__main__":
    films = get_films()
    for film in films:
        print(f"{film['episode_id']}: {film['title']} ({film['release_date']})")
