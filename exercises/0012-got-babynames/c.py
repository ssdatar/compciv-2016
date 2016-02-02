from os.path import basename

url = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
filename = basename(url)

got_file = open('tempdata/' + filename, 'r')
khaleesi_count = [0, 0]

for line in got_file:
	name, sex, babies = line.strip().split(',')
	if name == "Daenerys":
		khaleesi_count[0] += int(babies)

	elif "Khalees" in name or "Khaless" in name:
		khaleesi_count[1] += int(babies)

print("Daenerys:", khaleesi_count[0])
print("Khaleesi:", khaleesi_count[1])
