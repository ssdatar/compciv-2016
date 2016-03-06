import csv

master_data = []

with open('tempdata/wrangled2014.csv') as csv_in:
	reader = csv.reader(csv_in)
	next(reader, None) #skip the header row

	for row in reader:
		name, gender, ratio = row[1:4]
		total = row[-1]
		output = {}
		
        #get the required values
		output['name'] = name
		output['gender'] = gender
		output['ratio'] = int(ratio)
		output['total'] = int(total)

		if int(total) >= 100:          #if >= 100, add to list of dictionaries
			master_data.append(output)

print('Popular names in 2014 with gender ratio less than or equal to:')
for genderratio in (60, 70, 80, 90, 99):
	count = 0
	for data in master_data:
		if data['ratio'] <= genderratio:
			count += 1
	print(' ', str(genderratio) + '%:', str(count) + '/' + str(len(master_data)))