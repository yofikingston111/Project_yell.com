import os
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.yell.com/ucs/UcsSearchAction.do?'

params = {

    'keywords': 'hotels',
    'location': 'New York',
    'scrambleSeed': '196465982',
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
base_url = 'https://www.yell.com/'
result = []

res = requests.get(url, params=params, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
try:
    os.mkdir('json_result')
except FileExistsError:
    pass

# scraping proccess
headers_contents = soup.find_all('div', 'row businessCapsule--mainRow')

for content in headers_contents:
    title = content.find('h2', 'businessCapsule--name text-h2').text
    classification = content.find('span', 'businessCapsule--classification').text
    telephone = content.find('span', 'business--telephoneNumber').text
    link_web = base_url + content.find('div', 'businessCapsule--titSpons').find('a')['href']

    # final data
    final_data = {
        'title': title,
        'classification': classification,
        'telephone': telephone,
        'link web': link_web,
    }
    print(final_data)
    result.append(final_data)
print('jumlah datanya adalah', len(result))

try:
    os.mkdir('json_result')
except FileExistsError:
    pass
with open('json_result/final_data.json', 'w+') as json_data:
    json.dump(result, json_data)
print('json created')

# create csv
df = pd.DataFrame(result)
df.to_csv('yell_data.csv', index=False)
df.to_excel('yell_data.xlsx', index=False)

# data created
print('Data Created Succes')