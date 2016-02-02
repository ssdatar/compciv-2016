from os.path import basename
import string

url = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
filename = basename(url)

got_file = open('tempdata/' + filename, 'r')

mydict = {'M': {}, 'F': {} }

for line in got_file:
	name, sex, babies = line.strip().split(',')
	last_letter = name[-1]

	if last_letter in mydict[sex]:
		mydict[sex][last_letter] += int(babies)
	else:
		mydict[sex][last_letter] = int(babies)

print("letter", "F".rjust(11), "M".rjust(6))
print("-" * 25)

for letter in string.ascii_lowercase:
	print(letter, str(mydict['F'][letter]).rjust(15), str(mydict['M'][letter]).rjust(7))

