import requests

url = 'https://www.wikipedia.org/'

response = requests.get(url=url)

# list all function
print(dir(response))

# status code
print(response.status_code)

# source code website
# print(response.text)