from bs4 import BeautifulSoup
import requests
import json

url = 'https://moovitapp.com/index/en/public_transit-lines-Samarkand-6104-1936108'

r = requests.get(url)

with open('bus_list.html', 'w', encoding='UTF8') as f:
    f.write(r.text)