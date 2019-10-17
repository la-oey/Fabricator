from bs4 import BeautifulSoup
import requests
import csv
import re
import time

"""
# creat urls
urls_2004, urls_2005, urls_2006, urls_2007, urls_2008 = [], [], [], [], []
years = [f"{i:04}" for i in range(2004, 2009)]
# 2004
dois_2004 = [f"{i:05}" for i in range(655, 769)]
for doi in dois_2004:
    urls_2004.append('http://journals.sagepub.com/doi/full-xml/10.1111/j.0956-7976.2004.' + doi + '.x')

# 2005
dois = [f"{i:05}" for i in range(771, 812)]
dois2 = [f"{i:05}" for i in range(1524, 1669)]
dois3 = [f"{i:05}" for i in range(1578, 1654)]
dois4 = [f"{i:05}" for i in range(1656, 1669)]
for doi in dois:
    urls_2005.append('http://journals.sagepub.com/doi/full-xml/10.1111/j.0956-7976.2005.' + doi + '.x')
for doi2 in dois2:
    urls_2005.append('http://journals.sagepub.com/doi/full-xml/10.1111/j.0956-7976.2005.' + doi2 + '.x')
for doi3 in dois3:
    urls_2005.append('http://journals.sagepub.com/doi/full-xml/10.1111/j.1467-9280.2005.' + doi3 + '.x')
for doi4 in dois4:
    urls_2005.append('http://journals.sagepub.com/doi/full-xml/10.1111/j.1467-9280.2005.' + doi4 + '.x')
for doi5 in dois5:
    urls_2009.append('http://journals.sagepub.com/doi/full-xml/10.1177/0956797609' + doi5)

# 2006
dois6 = [f"{i:05}" for i in range(1669, 1826)]
dois7 = [f"{i:05}" for i in range(1827, 1836)]
dois_2006 = dois6 + dois7
for doi in dois_2006:
    urls_2006.append('http://journals.sagepub.com/doi/full-xml/10.1111/j.1467-9280.2006.' + doi + '.x')

# 2007
dois8 = [f"{i:05}" for i in range(1837, 1971)]
dois9 = [f"{i:05}" for i in range(1972, 2034)]
dois_2007 = dois8 + dois9
for doi in dois_2007:
    urls_2007.append('http://journals.sagepub.com/doi/full-xml/10.1111/j.1467-9280.2007.' + doi + '.x')

# 2008
dois10 = [f"{i:05}" for i in range(2036, 2242)]
dois11 = [f"{i:05}" for i in range(2243, 2259)]
dois12 = [f"{i:05}" for i in range(2260, 2263)]
dois13 = [f"{2264:05}"]
dois_2008 = dois10 + dois11 + dois12 + dois13
for doi in dois_2008:
    urls_2008.append('http://journals.sagepub.com/doi/full-xml/10.1111/j.1467-9280.2008.' + doi + '.x')

# dictionary
dic = {"2008": urls_2008, "2007": urls_2007, "2006": urls_2006, "2005": urls_2005, "2004": urls_2004}


for year in years:
    # record start time
    start_time = time.clock()

    with open('psychScience_' + year + '.csv','w', encoding='utf-8') as csv_file:
            fieldnames = ['doi', 'author', 'date', 'title', 'subtitle', 'text']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            # loop through url list
            for url in dic[year]:
                response = requests.get(url)
                # check if has content
                if response:
                    try:
                        doi = url
                        soup = BeautifulSoup(response.text, 'html.parser')
                        # title
                        title = soup.find('title-group').find('article-title').get_text()
                        sub = soup.find('title-group').find('subtitle')
                        sub_title = ""
                        if sub:
                            sub_title = sub.get_text()
                        # author
                        first = soup.find('contrib-group').findAll('given-names')
                        last = soup.find('contrib-group').findAll('surname')
                        name = [i.text + " " + j.text for i, j in zip(first, last)]
                        # date
                        month = soup.find('pub-date').find('month').get_text()
                        year = soup.find('pub-date').find('year').get_text()
                        date = year + "/" + format(int(month), '02d')
                        texts = response.text
                        writer.writerow({'doi': doi, 'author': "; ".join(name), 'date': date, 'title': title , 'subtitle': sub_title, 'text': texts}) # , 'text': text
                    except:
                        continue

    # record end time
    end_time = time.clock()
    minute_time = (end_time - start_time) / 60.0
    print("The execution time is" + " %s minutes." % minute_time)

"""

doi_2010 = [f"{i:06}" for i in range(350000, 400000)]
urls_2010 = []
for doi in doi_2010:
    urls_2010.append('http://journals.sagepub.com/doi/full-xml/10.1177/0956797610' + doi)

# record start time
start_time = time.clock()


with open('psychScience_2010.csv','w', encoding='utf-8') as csv_file:
        fieldnames = ['doi', 'author', 'date', 'title', 'subtitle', 'text']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for url in urls_2010:
        # loop through url list
            response = requests.get(url)
            # check if has content
            if response:
                try:
                    doi = url
                    soup = BeautifulSoup(response.text, 'html.parser')
                    # title
                    title = soup.find('title-group').find('article-title').get_text()
                    sub = soup.find('title-group').find('subtitle')
                    sub_title = ""
                    if sub:
                        sub_title = sub.get_text()
                    # author
                    first = soup.find('contrib-group').findAll('given-names')
                    last = soup.find('contrib-group').findAll('surname')
                    name = [i.text + " " + j.text for i, j in zip(first, last)]
                    # date
                    month = soup.find('pub-date').find('month').get_text()
                    year = soup.find('pub-date').find('year').get_text()
                    date = year + "/" + format(int(month), '02d')
                    texts = response.text
                    writer.writerow({'doi': doi, 'author': "; ".join(name), 'date': date, 'title': title , 'subtitle': sub_title, 'text': texts}) # , 'text': text
                except:
                    continue

# record end time
end_time = time.clock()
minute_time = (end_time - start_time) / 60.0
print("The execution time is" + " %s minutes." % minute_time)