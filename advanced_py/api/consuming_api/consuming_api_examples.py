# Python Consuming API Example
import requests

def fetch_random_joke():
    """Fetches a random joke from the JokeAPI."""
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        joke_data = response.json()
        if not joke_data["error"]:
            print("Here's a random joke for you:")
            print(joke_data["joke"])
        else:
            print("Sorry, I couldn't fetch a joke at the moment.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_random_joke()
