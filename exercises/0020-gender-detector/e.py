from os.path import join, basename
from glob import glob

names_count = {}
girls = 0
boys  = 0

with open('tempdata/yob2014.txt', 'r') as file_2014:
    for line in file_2014:
        name, gender, babies = line.split(',')
        
        if not names_count.get(name):
            names_count[name] = [0, 0]

        if gender == 'F':
            names_count[name][0] += int(babies)
            girls += int(babies)

        else:
            names_count[name][1] += int(babies)
            boys += int(babies)

unique_count = {'M': 0, 'F': 0}

for i in names_count:
    if names_count[i][0] > 0:
        unique_count['F'] += 1
    if names_count[i][1] > 0:
        unique_count['M'] += 1

print('Total: ', len(names_count), 'unique names for ', boys + girls, ' babies')
print('    M: ', unique_count['M'], 'unique names for ', boys, ' babies')
print('    F: ', unique_count['F'], 'unique names for ', girls, ' babies')
