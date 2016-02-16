from os.path import basename
from operator import itemgetter

url = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
textfile = basename(url)

names = {}

#sort list first by length of name, then by number of names
def longest_names(x):
	return[len(x[0]), x[1]]

with open('tempdata/' + textfile, 'r') as baby_file:
	for line in baby_file:
		name, sex, babies = line.strip().split(',')

		if names.get(name):
			names[name] += int(babies)
		else:
			names[name] = int(babies)

#make a filtered dictionary with only those names with >2000
filtered_dict = {key: value for (key, value) in names.items() if value >= 2000}

filtered_list = []

#convert filtered dictionary to list of lists
for (k, v) in filtered_dict.items():
	filtered_list.append([k,v])

#sort list first by length of name, then by number of names
a = sorted(filtered_list, key=longest_names, reverse=True)

for i in range(10):
	print(a[i][0], str(a[i][1]).rjust(24 - len(a[i][0])))