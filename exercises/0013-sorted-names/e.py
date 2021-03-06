from os.path import basename

url = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
textfile = basename(url)

baby_list = []

#function to sort by baby count. This function is called in sorted method
def sort_by_number(x):
	return x[1]

#calculate percentages, given a percentage bracket
def percent_bracket(start, end, array):
	bracket_babies = 0
	for i in range(start-1, end):
		bracket_babies += array[i][1]
	percent = (bracket_babies/total_babies) * 100
	print('Names', str(start), 'to', str(end) + ':', round(percent,1))

total_babies = 0

#open file, read contents, make a list of all babies
with open('tempdata/' + textfile, 'r') as baby_file:
	for line in baby_file:
		name, sex, babies = line.strip().split(',')
		row = [name, int(babies)]
		total_babies += int(babies)
		baby_list.append(row)

#sorted the list of baby names in descending order
a = sorted(baby_list, key=sort_by_number, reverse=True)

#print results
percent_bracket(1, 10, a)
percent_bracket(11, 100, a)
percent_bracket(101, 1000, a)
percent_bracket(10001, len(a), a)


