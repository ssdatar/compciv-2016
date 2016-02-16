from os.path import basename
from operator import itemgetter

url = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
textfile = basename(url)

boys = []
girls = []

def check_for_letter(element, letter):
	return letter.lower() in element or letter.upper() in element

def print_x_times(array, count):
	for i in range(count):
		name_length = len(array[i][0])
		print(str(i+1) + '.', array[i][0], str(array[i][2]).rjust(24 - name_length - 3))

with open('tempdata/' + textfile, 'r') as baby_file:
	for line in baby_file:
		name, sex, babies = line.strip().split(',')
		row = [name, sex, babies]
		
		if row[1] == 'F':
			if check_for_letter(row[0], 'x'):
				girls.append(row)
		else:
			if check_for_letter(row[0], 'x'):
				boys.append(row)

print('Female')
print_x_times(girls, 5)

print('Male')
print_x_times(boys, 5)