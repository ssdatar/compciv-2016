from os.path import basename

url = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
filename = basename(url)

got_file = open('tempdata/' + filename, 'r')

girl_count = 0 
boy_count = 0

for line in got_file:
	name, sex, babies = line.strip().split(',')
	if sex == 'F': 
		girl_count += int(babies)
	elif sex == 'M':
		boy_count += int(babies)

print("F:", girl_count)
print("M:", boy_count)

