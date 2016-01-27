import os

fname = os.path.join('tempdata', 'tragedies', 'hamlet')
hamlet = open(fname, 'r')

for line in range(5):
	print(hamlet.readline().strip())
hamlet.close()