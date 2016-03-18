import requests
from os import makedirs
from os.path import basename, join
import csv
import re

DATA_DIR = 'tempdata'
DATA_FILE_NAME = 'artists.csv'
DATA_FILE_PATH = join(DATA_DIR, DATA_FILE_NAME)

wrangled_dir = 'wrangled'
makedirs(wrangled_dir, exist_ok=True)
wrangled_file = 'wrangled_data.csv'
wrangled_data_path = join(wrangled_dir, wrangled_file)

with open(DATA_FILE_PATH, 'r') as infile:
	readCSV = csv.reader(infile)
	headers = next(readCSV)

	with open (wrangled_data_path, 'w') as outfile:
		writeCSV = csv.writer(outfile)
		writeCSV.writerow(headers)

		for row in readCSV:
			if 'Individual Artist Commission' in row[1]:
				row[2] = re.findall('\w+', row[2])[0]
				row[2] = int(row[2])
				writeCSV.writerow(row)


