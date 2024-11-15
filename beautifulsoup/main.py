import requests
from bs4 import BeautifulSoup


# url = 'https://books.toscrape.com/'
url = 'https://crawler-test.com/'

response = requests.get(url)

# print response code
print(response.status_code)

# print codes html 
# print(response.text)

# page_html is a value to have html code website
page_html = response.text

# prettify can be show code by struct
soup = BeautifulSoup(markup=page_html, features='html.parser')
print(soup.prettify())