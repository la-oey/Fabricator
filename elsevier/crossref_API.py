from bs4 import BeautifulSoup
import requests
import csv
import re
import time

# creat 2004 urls
urls = []
dois = [f"{i:05}" for i in range(771, 812)]
dois2 = [f"{i:05}" for i in range(1524, 1578)]
dois3 = [f"{i:05}" for i in range(1578, 1654)]
dois4 = [f"{i:05}" for i in range(1656, 1669)]
dois5 = [f"{i:06}" for i in range(350000, 400000)]
"""
for doi in dois:
    urls.append('http://journals.sagepub.com/doi/full-xml/10.1111/j.0956-7976.2005.' + doi + '.x')
for doi2 in dois2:
    urls.append('http://journals.sagepub.com/doi/full-xml/10.1111/j.0956-7976.2005.' + doi2 + '.x')
for doi3 in dois3:
    urls.append('http://journals.sagepub.com/doi/full-xml/10.1111/j.1467-9280.2005.' + doi3 + '.x')
for doi4 in dois4:
    urls.append('http://journals.sagepub.com/doi/full-xml/10.1111/j.1467-9280.2005.' + doi4 + '.x')"""
for doi5 in dois5:
    urls.append('http://journals.sagepub.com/doi/full-xml/10.1177/0956797609' + doi5)

# record start time
start_time = time.clock()

with open('psychScience_2009.csv','w', encoding='utf-8') as csv_file:
        fieldnames = ['doi', 'title', 'subtitle', 'text']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # loop through url list
        for url in urls:
            response = requests.get(url)
            # check if has content
            if response:
                try:
                    doi = url
                    soup = BeautifulSoup(response.text, 'html.parser')
                    title = soup.find('title-group').find('article-title').get_text()
                    sub = soup.find('title-group').find('subtitle')
                    sub_title = ""
                    if sub:
                        sub_title = sub.get_text()
                    texts = response.text
                    writer.writerow({'doi': doi, 'title': title , 'subtitle': sub_title, 'text': texts}) # , 'text': text
                except:
                    continue

# record end time
end_time = time.clock()
minute_time = (end_time - start_time) / 60.0
print("The execution time is" + " %s minutes." % minute_time)