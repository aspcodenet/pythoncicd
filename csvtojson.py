import json
import csv
import os

with open('./profiles1.csv', newline='',encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

    

with open('./data.json', 'w') as jsonfile:
    json.dump(data, jsonfile)    