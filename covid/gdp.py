from bs4 import BeautifulSoup
import requests
import csv 
from datetime import datetime


URL = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')



#gets vaccinated info

main = soup.find("table", {"class": "wikitable"})



body = main.tbody

data = body.find_all('tr')

items = data[1].table.tbody


trs = items.find_all('tr')

with open("economyrank.csv", 'a+', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow('"\n"')

for tr in trs:
    value = tr.find_all('td')
    for values in value:
        country = value[1].a.string
        economyrank = value[2].string
        economyrankposition = value[0].string
        print(country)
        print(economyrank)
        print(economyrankposition)
        with open("economyrank.csv", 'a+', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([country, economyrank, economyrankposition])
            break
       