# Python Web Scraping Example with BeautifulSoup
# To run this example:
# 1. Install the required packages: pip install -r requirements.txt
# 2. Run the script: python web_scraping_examples.py

import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    """Scrapes quotes from quotes.toscrape.com."""
    url = "http://quotes.toscrape.com"
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            text = quote.find("span", class_="text").get_text()
            author = quote.find("small", class_="author").get_text()
            print(f'"{text}" - {author}')

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    scrape_quotes()
