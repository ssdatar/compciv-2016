import csv
from os.path import join
from gender import detect_gender

WRANGLED_FOLDER = 'wrangled'
WRANGLED_FILE = 'wrangled_data.csv'
WRANGLED_FILE_PATH = join(WRANGLED_FOLDER, WRANGLED_FILE)

CLASSIFIED_FILE = 'classified_data.csv'
CLASSIFIED_FILE_PATH = join(WRANGLED_FOLDER, CLASSIFIED_FILE)

def extract_usable_name(fullname):
	return fullname.split(' ')[0]

with open(WRANGLED_FILE_PATH, 'r') as artist_csv:
	reader = csv.reader(artist_csv)
	headers = next(reader)
	headers.extend(['gender', 'usable_name', 'ratio'])

	with open(CLASSIFIED_FILE_PATH, 'w') as classified_csv:
		writer = csv.writer(classified_csv)
		writer.writerow(headers)

		for row in reader:
			full_name = row[0]
			usable_name = extract_usable_name(full_name)
			name_result = detect_gender(usable_name)
			gender = name_result['gender']
			ratio = name_result['ratio']
			row.extend([gender, usable_name, ratio])
			writer.writerow(row)


