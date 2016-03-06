from os.path import join, basename
import csv

folder = 'tempdata'
year = 2014
thefilename = join(folder, 'yob' + str(year) + '.txt')

csv_headers = ['year', 'name', 'gender' , 'ratio' , 'females', 'males', 'total']
output_csv = join(folder, 'wrangled2014.csv')

namesdict = {}

with open(thefilename, 'r') as txtfile:
    for line in txtfile:
        name, gender, babies = line.split(',')
        if not namesdict.get(name):
            namesdict[name] = {'M': 0, 'F': 0}
        namesdict[name][gender] += int(babies)

names_list = []

for item in namesdict:
    temp = {}
    temp['year'] = year
    temp['name'] = item
    temp['females'] = namesdict[item]['F']
    temp['males'] = namesdict[item]['M']
    temp['total'] = temp['females'] + temp['males']

    if temp['females'] >= temp['males']:
        temp['gender'] = 'F'
        temp['ratio'] = round(100 * temp['females'] / temp['total'])
    else:
        temp['gender'] = 'M'
        temp['ratio'] = round(100 * temp['males'] / temp['total'])

    names_list.append(temp)

def desc_sort(xdict):
    return (-xdict['total'], xdict['name'])

sorted_names = sorted(names_list, key=desc_sort)

with open(output_csv, 'w') as csv_out:
    writer = csv.DictWriter(csv_out, fieldnames=csv_headers)
    writer.writeheader()

    for row in sorted_names:
        writer.writerow(row)

