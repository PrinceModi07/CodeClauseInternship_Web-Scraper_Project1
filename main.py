import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://timesofindia.indiatimes.com/"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the website
soup = BeautifulSoup(response.content, "html.parser")

# Find all the headline elements on the page
headlines = soup.find_all("figcaption")

# Extract the text from each headline element
for headline in headlines:
    print(headline.text.strip())