from bs4 import BeautifulSoup
import requests
import csv 
import os
import math
from datetime import datetime, timedelta, date

global day

####
countries = list()

with open('nha.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		country = row['Countries']
		countries.append(country)

doable1 = False
doable2 = False


day = datetime.today().strftime('%Y-%m-%d')

def prevision():
	global doable1
	global doable2
	global f_country
	foundcountry = None
	os.remove('results.csv')
	with open('results.csv', 'w') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['country', 'results', 'percentage'])
	f_country = ['0']
	with open('output3.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		since = "2021-02-14"
		try:
			for row in reader:
				for a in countries:
					
					if a == row['country'] and since == row['day']:
						x2 = row['day']
						y2 = row['percentage']
						foundcountry = row['country']

						y2strip = y2.strip("%")
						
						date = x2.split("-")
						day2 = int(date[2])
						month1 = int(date[1])
						x2 = (month1 * 30) + day2


						f_country = []
						f_country.append(foundcountry)

						doable2 = True
						with open('output.csv') as csvfile:
							reader = csv.DictReader(csvfile)
							for row1 in reader:
								
							 
								if row1['country'] == foundcountry and day == row1['day']:
									
									x1 = row1['day'] 
									y1 = row1['percentage']
									y1strip = y1.strip("%")
									date = x1.split("-")
									day1 = int(date[2])
									month2 = int(date[1])
									doable1 = True
									if doable1 == True and doable2 == True:
										try:
											#print(a)
											x1 = (month2 * 30) + day1
											#print(y1strip, "y1strip")
											#print(y2strip, "y2strip")
											slope = (float(y1strip) - float(y2strip)) / (x1 - x2)
											#print(slope)
											model = slope * (x1 - x2 - float(y1strip)) 
											result = ((float(y1strip) - float(y2strip) - 100) / slope)
											#print(a)
											#print(int(result))
											with open('results.csv', 'a') as csvfile:
												writer = csv.writer(csvfile)
												writer.writerow([row1['country'], result, y1])
										except:
											pass
									doable1 = False
									doable2 = False

		except Exception as e:
			print(e)
			pass
			

def results():
	global day

	with open('results.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		print("Date:", day)
		for row in reader:

			percentage = row['percentage']
			
			dayssince = day.split("-")
			result = math.sqrt(float(row['results']) ** 2)
			delta = timedelta(result)
			offset = delta + date(int(dayssince[0]), int(dayssince[1]), int(dayssince[2]))
			prevision = offset.strftime('%Y-%m-%d')
			print(row['country'], "previsão pra conclusão da vacinação:", prevision, "-", percentage)

prevision()										
results()
