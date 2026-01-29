# Python Web Automation Example with Selenium
# To run this example:
# 1. Install the required packages: pip install -r requirements.txt
# 2. Download the appropriate webdriver for your browser (e.g., chromedriver for Chrome).
#    Make sure the webdriver is in your PATH or specify the path to it.
# 3. Run the script: python selenium_example.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def search_on_google():
    """Performs a search on Google and prints the titles of the results."""
    # The following line assumes you have chromedriver in your PATH
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.google.com")

        # Find the search box element and enter a search query
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium with Python")
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load
        time.sleep(2)

        # Print the titles of the search results
        results = driver.find_elements(By.CSS_SELECTOR, "h3")
        for result in results:
            print(result.text)

    finally:
        driver.quit()

if __name__ == "__main__":
    search_on_google()
