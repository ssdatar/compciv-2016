from os.path import join, basename
from glob import glob
import re

folder = 'tempdata'
files = glob(join(folder, '*.txt')) #find all txt files, get all file names

required_years = []
counts = {'M': set(), 'F': set()}

for filename in files:
	year = re.findall('\d+', filename) #extract year of filename
	year = int(year[0])					#convert returned list to int
	
	if year >= 1950:
		required_years.append(filename)

for fname in required_years:
	babyfile = open(fname, 'r')

	for line in babyfile:
		name, gender, babies = line.split(',')
		counts[gender].add(name)

males = len(counts['M'])
females = len(counts['F'])

print('F:', str(females).rjust(6), 'M: ', str(males).rjust(6))
f_to_m = 100 * len(counts['F']) / len(counts['M'])
print('F/M name ratio: ', round(f_to_m))

