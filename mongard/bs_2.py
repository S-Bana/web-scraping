import requests
from bs4 import BeautifulSoup
import re


# =setup====================================================================
# url = 'https://www.wikipedia.org/'
url = 'https://en.wikipedia.org/wiki/Linus_Torvalds'

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

# find a value and return all
# print(content.find_all('h2', limit=5))

# find two or more than values and return first one
# print(content.find(['h1','h2']))

# find two or more than values and return first one
# print(content.find_all(['h1','h2']))


# =find_something==========================================================
# find a value and return first one, in result get attribute, text , ...
# print(content.find('h1').attrs)

# print(content.find('h1').text)

# print(content.find(attrs={"title":"Alan Emtage"}))


# =find_something_&_filter_it==========================================================
# return text from first 'h1'
# print(content.find('h1').text)

# number of 'h2' in source code html
# print(len(content.find_all('h2')))

# find first 'h2' and get from it , parameter 'id'
# print(content.find('h2').get('id'))


# =find_by_search=====================================================================
# find value , that start by 'd'
# print(content.find(re.compile('^d')))


# =select=====================================================================
# return 'li' chiled 'a',that 'title="Ed Krol"'
print(content.select('li > a[title="Ed Krol"]'))

