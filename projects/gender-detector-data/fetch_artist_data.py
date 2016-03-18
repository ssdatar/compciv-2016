import requests
from os import makedirs
from os.path import basename, join

DATA_DIR = 'tempdata'
makedirs(DATA_DIR, exist_ok=True)

source_url = 'https://data.sfgov.org/api/views/mxvq-mfs5/rows.csv'

print("Downloading", source_url)
resp = requests.get(source_url)
data_file_path = join(DATA_DIR, 'artists.csv')

with open(data_file_path, 'w') as fname:
	fname.write(resp.text)
	print("Wrote", len(resp.text), "to", data_file_path)