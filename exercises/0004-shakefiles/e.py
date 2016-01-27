import os

name = os.path.join('tempdata', 'tragedies', 'hamlet')
hamlet = open(name, 'r')

line_num = 0

for line in hamlet:
	line_num += 1
hamlet.close()

print(name, 'has', line_num, "lines")
