from bs4 import BeautifulSoup
import csv
import re


with open('fabricatedPapers.csv', 'w', encoding='utf-8') as csv_file:
	fieldnames = ['year publish', 'year retract', 'authors', 'title', 'journal']
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	writer.writeheader()
	db = open('RetractionWatchDatabase_SOC.htm', 'rb')
	soup = BeautifulSoup(db, 'html.parser')
	
	for paper in soup.find_all('tr', attrs={'class':'mainrow'}):
		
		# find title
		title = paper.find('span', attrs={'class':'rTitleNotIE'}).get_text()
		# print(title)

		# find journal
		journal = paper.find('span', attrs={'class':"rJournal"})\
			     .find('span', attrs={'class':"rJournal"}).get_text()[:-4]
		# print(journal)
		
		# find year_published and year_retracted
		year_text = paper.get_text(" ")
		year_published = re.findall(r'(\d+/\d+/\d+)', year_text)[-2][-4:]
		year_retracted = re.findall(r'(\d+/\d+/\d+)', year_text)[-1][-4:]
		# print(year_published, year_retracted)

		# find author
		authors = []
		for author in paper.find_all('a', attrs={'class':'authorLink'}):
			authors.append(author.get_text())
		# print(authors)

		writer.writerow({'year publish': year_published, 'year retract': year_retracted, 'authors': authors, 'title': title, 'journal': journal})
	
	"""
	for t in soup.find_all('span', attrs={'class':'rTitleNotIE'}):
	    print(t.get_text())
	# print(title)

	for temp in soup.find_all('span', attrs={'class':"rJournal"}):
		for j in temp.find_all('span', attrs={'class':"rJournal"}):
			print(j.get_text()[:-4])
	# print(journal)


	year = pass
	authors = pass

	title = soup.find('span', attrs={'class':'rTitleNotIE'}).get_text()
	print(title)
	# journal = pass

	for i in db.rows():
		writer.writerow({'year': year, 'authors': authors, 'title': title, 'journal': journal})
	"""
	
	csv_file.close()
	db.close()
