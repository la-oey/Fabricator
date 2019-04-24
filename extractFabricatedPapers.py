from bs4 import BeautifulSoup
import csv
import re


with open('fabricatedPapers.csv', 'w') as csv_file:
	fieldnames = ['year', 'authors', 'title', 'journal']
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	writer.writeheader()
	db = open('RetractionWatchDatabase_SOC.htm', 'rb')
	soup = BeautifulSoup(db, 'html.parser')
	for t in soup.find_all('span', attrs={'class':'rTitleNotIE'}):
		print(t.get_text())

	csv_file.close()
	db.close()
