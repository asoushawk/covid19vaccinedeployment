from bs4 import BeautifulSoup
import requests
import csv 
import os
from datetime import datetime



URL = "https://en.wikipedia.org/wiki/COVID-19_vaccine"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')



#gets vaccinated info

vaxx_dist = soup.find("div", {"id": "covid19-container"})
body = vaxx_dist.tbody
trs = body.find_all('tr')
rows = trs[2].find_all('td')



day = datetime.today().strftime('%Y-%m-%d')



os.remove('database.csv')

countries = []

index = 2
with open('database.csv', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['day', 'country', 'vaccinated', 'percentage"'])
	writer.writerow("\n")


try:
	for tr in trs:
		td = trs[index].find_all('td')
		country = td[0].a.string
		vaccinated = td[1].string
		percentage = td[2].string
		countries.append(country)
		print(country, "-", vaccinated, "vacinados", percentage, "% população")
		index = index + 1
		with open('database.csv', 'a+', newline='') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow([day, country, vaccinated, percentage])
except:
	pass



######################################

URL = "https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')



vaxx_dist = soup.find("div", {"id": "covid19-container"})
day = datetime.today().strftime('%Y-%m-%d')
body = vaxx_dist.tbody
trs = body.find_all('tr')
index = 2

with open ('output.csv', 'a', newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow('\n')


	
try:
	for tr in trs:
		td = trs[index].find_all('td')
		th = trs[index].find_all('th')
		deaths = td[0].string
		cases = td[1].string
		country = th[1].a.string
		#print(country, deaths, cases)
		index = index + 1
		with open('cases.csv' ,'a', newline='') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow([day, country, cases, deaths])
		for a in countries:
			if country == a:
				with open('database.csv', 'r', newline='') as csvfile:
					reader = csv.DictReader(csvfile)
					for row in reader:
						if row['country'] == country:
							vaccinated = row['vaccinated']
							percentage = row['percentage"']
							with open("nha.csv") as csvfile:
								reader = csv.DictReader(csvfile)
								for row1 in reader:
									nhacountry = row1['Countries']
									if nhacountry == 'United States of America':
										nhacountry = 'United States'	
									if a == nhacountry:
										expenditure = row1['2018']
										with open("economyrank.csv") as csvfile1:
											reader = csv.DictReader(csvfile1)
											for row2 in reader:
												if row2['country'] == country:
													economyrank = row2['economyrank']
													economyrankposition = row2['economyrankposition']
													fout = [day, a, deaths, cases, vaccinated, percentage, expenditure, economyrank, economyrankposition]
													with open("output.csv", "a+") as fhandle:
														writer = csv.writer(fhandle)
														writer.writerow(fout)

except:
	pass


										
				 					

							


						



