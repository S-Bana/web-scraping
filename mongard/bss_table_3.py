import requests
from bs4 import BeautifulSoup
import re

import pandas as pd
# =setup====================================================================
url = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'

response = requests.get(url=url)

print(response.status_code)

content = BeautifulSoup(response.text, 'html.parser')

episodes = []

# =get_tables===============================================================
# find all 'tables' that class name = 'wikiepisodetable'
ep_tables = content.find_all('table', class_='wikiepisodetable')

for table in ep_tables[:-1]:
    headers = []
    rows = table.find_all('tr')

    print('='*90)

    for header in table.find('tr').find_all('th'):
        # print(header.text)
        headers.append(header.text)
    
    print('*'*90)

    
    data = []
    for row in table.find_all('tr')[1:]:
        values = []
        for col in row.find_all(['th', 'td']):
            # print(col.text)
            values.append(col.text)
        
        data.append(values)

        # print('-'*90)
    
    df = pd.DataFrame(data=data, columns=headers)
    print(df)
    #     if values:
    #         episode_dict = {}

    #         for i in range(len(values)):
    #             episode_dict[headers[i]] = values[i]
    #             episodes.append(episode_dict)


# for ep in episodes:
#     print(ep)



