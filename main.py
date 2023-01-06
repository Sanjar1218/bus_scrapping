from bs4 import BeautifulSoup
import json

with open('bus_list.html', 'r') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

column = soup.find('div', class_='first-column info-wrapper clearfix')

buses = column.find('div', attrs={'id': 'agency-lines'}).ul

all_links = []

for li in buses.find_all('li'):
    link = li.a['href']
    stop_name = li.a.find('div', class_='line-title-wrapper').strong.text.replace('в†’', 'to')

    all_links.append({'name': stop_name, 'link':link})

with open('bus_links.json', 'w') as f:
    json.dump(all_links, f, indent=4, separators=(',', ':'))