import csv
import json
from os.path import join

folder = 'tempdata'
thefile = join(folder, 'wrangledbabynames.csv')

output_json = join(folder, 'wrangledbabynames.json')
namesdict = {}
answer = []

with open(thefile, 'r') as csv_in:
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
        json_data = json.dumps(answer, indent=2)
        json_out.write(json_data)

csv_chars = 0
json_chars = 0
with open(thefile, 'r') as csv_in:
    csv_chars = len(csv_in.read())

with open(output_json, 'r') as jsonfile:
    json_chars += len(jsonfile.read())

chars_more = (json_chars - csv_chars) / csv_chars

print('CSV has', str(csv_chars), 'characters')
print('JSON has', str(json_chars), 'characters')
print('JSON requires', round(chars_more, 1), 'times more characters than CSV')