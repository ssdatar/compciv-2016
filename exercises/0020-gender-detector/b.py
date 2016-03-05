from os.path import join, basename
from glob import glob
import re

folder = 'tempdata'
files = glob(join(folder, '*.txt')) #find all txt files, get all file names

required_years = []
counts = [0, 0]

for filename in files:
	year = re.findall('\d+', filename) #extract year of filename
	year = int(year[0])					#convert returned list to int
	
	if year >= 1950:
		required_years.append(filename)

for fname in required_years:
	babyfile = open(fname, 'r')

	for line in babyfile:
		name, gender, babies = line.split(',')
		
		if gender == 'F':
			counts[0] += int(babies)
		
		if gender == 'M':
			counts[1] += int(babies)

print('F:', str(counts[0]).rjust(6),
      'M:', str(counts[1]).rjust(6))

f_to_m = round(100 * counts[0] / counts[1])
print ('F/M baby ratio:', f_to_m)



