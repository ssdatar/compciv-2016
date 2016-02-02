from os.path import basename

url = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
filename = basename(url)

got_file = open('tempdata/' + filename, 'r')
got_baby_count = 0

for line in got_file:
	got_baby_count += int(line.split(',')[2])
print("There are", got_baby_count, "babies whose names were recorded in 2014.")
