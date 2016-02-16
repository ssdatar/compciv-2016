from os.path import basename
from operator import itemgetter

url = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
textfile = basename(url)

#open file
baby_file = open('tempdata/' + textfile, 'r')
baby_list = []

#read file contents and make a list of each row of data
for line in baby_file:
	name, sex, babies = line.strip().split(',')
	temp = [name, sex, int(babies)]
	baby_list.append(temp)

#sort by baby count descending
answer = sorted(baby_list, key=itemgetter(2), reverse=True)

for i in range(10):
	answer[i][2] = str(answer[i][2])
	print(str(i+1) + '.',','.join(answer[i]))
