import requests
from bs4 import BeautifulSoup
import re


# =setup====================================================================
url = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'

response = requests.get(url=url)

content = BeautifulSoup(response.text, 'html.parser')

episodes = []

