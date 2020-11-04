import csv
import json

csv_file_path = '../data/sample_map.csv'
json_file_path = '{}.json'.format(csv_file_path[:-4])

data = {}
with open(csv_file_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for rows in csv_reader:
        id = rows['ID']
        data[id] = rows['Name']

with open(json_file_path, 'w') as json_file:
    json_file.write(json.dumps(data, indent=4))
