from os.path import basename

url = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
filename = basename(url)

got_file = open('tempdata/' + filename, 'r')

boy_babies = []
girl_babies = []
baby_count = []

for line in got_file:
	name, sex, babies = line.strip().split(',')
	if sex == 'F': 
		girl_babies.append(name)
		baby_count.append(babies)
	else:
		boy_babies.append(name)
		baby_count.append(babies)

boy_babies = (boy_babies)[0:5]
girl_babies = (girl_babies)[0:5]

print("Top baby girl names")
for i in range(5):
	print(str(i + 1) + ".", girl_babies[i], baby_count[i])

print('')

print("Top baby boy names")
for i in range(5):
	print(str(i + 1) + ".", boy_babies[i], baby_count[i])

