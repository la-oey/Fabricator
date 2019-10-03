from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor, ElsAffil
from elsapy.elsdoc import FullDoc, AbsDoc
from elsapy.elssearch import ElsSearch
import json
import csv
import time
    
## Load configuration
con_file = open("config.json")
config = json.load(con_file)
con_file.close()

## Initialize client
client = ElsClient(config['apikey'])
client.inst_token = config['insttoken']

# record start time
start_time = time.clock()

# ScienceDirect (full-text) document example using DOI
with open('extract_2013.csv','w', encoding='utf-8') as file:
    fieldnames = ['doi', 'title', 'text']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    doi_list = []
    middle = [f"{i:02}" for i in range(13)]
    last = [f"{i:03}" for i in range(1000)]
    # generate potential doi list
    for m in middle:
        for l in last:
            doi_list.append("2013." + m + "." + l)

    # loop through doi list
    for doi_str in doi_list:
        full_doi = '10.1016/j.cognition.' + doi_str
        doi_doc = FullDoc(doi = full_doi)
        # check if has content
        if doi_doc.read(client):
            doi = full_doi
            title = doi_doc.title
            text = doi_doc.data["originalText"] # ['scopus-eid', 'originalText', 'scopus-id', 'pubmed-id', 'coredata', 'objects', 'link']
            writer.writerow({'doi': doi, 'title': title , 'text': text}) # , 'text': text

# record end time
end_time = time.clock()
minute_time = (end_time - start_time) / 60.0
print("The execution time is" + " %s minutes." % minute_time)
