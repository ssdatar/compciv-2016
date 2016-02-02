from os.path import basename
import string

url = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
filename = basename(url)

got_file = open('tempdata/' + filename, 'r')

letter_count = {}

for line in got_file:
	name, sex, babies = line.strip().split(',')
	last_letter = name[-1]

	if last_letter in letter_count:
		letter_count[last_letter] += int(babies)
	else:
		letter_count[last_letter] = int(babies)

for letter in string.ascii_lowercase:
	print(letter +':', letter_count[letter])

