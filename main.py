from bs4 import BeautifulSoup
import requests
import csv 
from datetime import datetime


URL = "https://en.wikipedia.org/wiki/COVID-19_vaccine"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')



#gets vaccinated info

vaxx_dist = soup.find("div", {"id": "covid19-container"})
body = vaxx_dist.tbody
trs = body.find_all('tr')
rows = trs[2].find_all('td')


#print("Monde: ", row[0].a.string)

day = datetime.today().strftime('%Y-%m-%d')

#for row in rows:

countries = []

index = 2
with open('database.csv', 'a', newline='') as csvfile:
	writer = csv.writer(csvfile)
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


with open('cases.csv', 'a', newline='') as csvfile:
	writer = csv.writer(csvfile)

with open('output.csv', 'a', newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow("\n")	

	

for tr in trs:
	td = trs[index].find_all('td')
	th = trs[index].find_all('th')
	deaths = td[0].string
	cases = td[1].string
	country = th[1].a.string
	print(country, deaths, cases)
	index = index + 1
	with open('cases.csv' ,'a', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow([day, country, cases, deaths])

	for a in countries:
		with open('cases.csv', 'a', newline='') as csvfile:
			writer = csv.writer(csvfile)
			if country == a:
				with open('database.csv', 'r', newline='') as csvfile:
					reader = csv.DictReader(csvfile)
					reader1 = csv.reader(csvfile)
					for row in reader:
						if row['country'] == country:
							vaccinated = row['vaccinated']
							percentage = row['percentage']

							fout = [day, a, deaths, cases, vaccinated, percentage]
							print(vaccinated)
							with open("output.csv", "a+") as fhandle:
								writer = csv.writer(fhandle)
								writer.writerow(fout)
								break


						



