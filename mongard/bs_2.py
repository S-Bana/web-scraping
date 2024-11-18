import requests
from bs4 import BeautifulSoup


url = 'https://www.wikipedia.org/'

response = requests.get(url=url)

content = BeautifulSoup(response.text, 'html.parser')

# print source code html
# print(content)

# =find====================================================================
# find a value and return first one
# print(content.find('h1'))

# find a value and return all
# print(content.find_all('h1'))
# print(content.findAll('h1'))

# find two or more than values and return first one
# print(content.find(['h1','h2']))

# find two or more than values and return first one
# print(content.find_all(['h1','h2']))

# =find_Attribute==========================================================

# find a value and return first one, in result get attribute
print(content.find('h1').attrs)