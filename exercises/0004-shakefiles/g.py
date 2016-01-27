from os.path import join
from glob import glob

path = join('tempdata', 'tragedies', '*')
tragedy = glob(path)

for fname in tragedy:
	current = open(fname, 'r')
	current_lines = current.readlines()
	current.close()
	current_length = len(current_lines)

	print(fname, "has", current_length, "lines")

	start = current_length - 5

	for line_num in range(start, current_length):
		line = current_lines[line_num]
		print(str(line_num + 1) + ": " + line.strip())

