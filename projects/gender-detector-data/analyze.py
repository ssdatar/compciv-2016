from os.path import join
import csv

classified_folder = 'wrangled'
classified_csv = 'classified_data.csv'
classified_path = join(classified_folder, classified_csv)

grants_total = { 'M': 0, 'F': 0, 'NA': 0 }
counts = {'M': 0, 'F': 0, 'NA': 0 }

# Analyze gender distribution of grants
with open(classified_path, 'r') as csv_in:
	reader = csv.DictReader(csv_in)
	print("---------------------------------------------")
	print('Analyzing gender distribution of grants...')

	for row in reader:
		gender = row['gender']
		grant = row['Grant Amount']
		grants_total[gender] += int(grant)
		counts[gender] += 1

grants_million = {}
grants_million['M'] = round(grants_total['M'] / 1000000, 2)
grants_million['F'] = round(grants_total['F'] / 1000000, 2)

print('Since 2004,', counts['M'], 'men have got $' + 
	   str(grants_million['M']), 'million in grants')
print('Since 2004,', counts['F'], 'women have got $' + 
	   str(grants_million['F']), 'million in grants')

print('Average grant amount for men', round(grants_total['M'] / counts['M']), 
	  'dollars')
print('Average grant amount for women', round(grants_total['F'] / counts['F']),
	  'dollars')

# Analyze yearly distribution of grants

grants_per_year = {}

with open(classified_path, 'r') as csv_in:
	reader = csv.DictReader(csv_in)
	print("---------------------------------------------")
	print('Analyzing yearly distribution of grants...')

	for row in reader:
		year = int(row['Grant Fiscal Year'][6:10]) #extract year from the date
		
		if not grants_per_year.get(year):
			grants_per_year[year] = { 'M': 0, 'F': 0, 'NA': 0 }
		gender = row['gender']
		grant = int(row['Grant Amount'])
		grants_per_year[year][gender] += grant

for year in grants_per_year:
	print('\n')
	print('In the year', year)
	print('Men got', grants_per_year[year]['M'], 'dollars')
	print('Women got', grants_per_year[year]['F'], 'dollars')
	print('Grant gender ratio', 
          round(grants_per_year[year]['M'] / grants_per_year[year]['F'], 2))
	print('\n')

# Analyze gender distribution of types of grants
focus = {}

with open(classified_path, 'r') as csv_in:
	reader = csv.DictReader(csv_in)
	print("---------------------------------------------")
	print('Analyzing gender distribution of types of grants...')

	for row in reader:
		grant_focus = row['Community Focus Combined'].replace('\n', ' ')

		if not focus.get(grant_focus):
			focus[grant_focus] = {'M':0, 'F':0, 'NA': 0 }
		gender = row['gender']
		grant = int(row['Grant Amount'])
		focus[grant_focus][gender] += grant

# Analyze gender distribution of who took up LGBT projects

lgbt_men = 0
lgbt_women = 0

for f in focus:
	if 'L/G/B' in f:
		if not focus[f]['M']:
			lgbt_men += 1
		if not focus[f]['F']:
			lgbt_women += 1

	print('Grant focus was:', f)
	print('Amount received by men for this focus:', focus[f]['M'])
	print('Amount received by women for this focus:', focus[f]['F'])
	print('\n')

print('Number of men who took up LGBT projects', lgbt_men)
print('Number of women who took up LGBT projects', lgbt_women)