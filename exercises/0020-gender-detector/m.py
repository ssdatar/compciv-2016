import csv
import json
from os.path import join

folder = 'tempdata'
thefile = join(folder, 'wrangledbabynames.csv')

output_json = join(folder, 'wrangledbabynames.json')
namesdict = {}
answer = []

with open(thefile, 'r') as csv_in:
	csv_len = len(thefile)
	with open(output_json, 'w') as json_out:
		reader = csv.reader(csv_in)
		next(reader, None)

		for row in reader:
			name,gender,ratio,females,males,total = row
			namesdict = {'name': name,
			             'gender': gender,
			             'ratio': int(ratio),
			             'females': int(females),
			             'males': int(males),
			             'total': int(total)}
			answer.append(namesdict)
			json_out.write(json.dumps(namesdict, json_out, indent=4))
			json_out.write(',\n')
			# json_out.write('\n')

csv_chars = 0
json_chars = 0
with open(thefile, 'r') as csv_in:
	for line in csv_in:
		csv_chars += len(line)

with open(output_json, 'r') as jsonfile:
	for line in jsonfile:
		json_chars += len(line)

print('CSV has', str(csv_chars), 'characters')
print('JSON has', str(json_chars), 'characters')
print('JSON requires', round(json_chars/csv_chars, 1), 'times more characters than CSV')