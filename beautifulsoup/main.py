import requests
from bs4 import BeautifulSoup

# url = 'https://books.toscrape.com/'
url = 'https://crawler-test.com/'

response = requests.get(url)

print(response.status_code)