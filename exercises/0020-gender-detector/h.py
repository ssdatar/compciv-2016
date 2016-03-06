import csv

answer = []

with open('tempdata/wrangled2014.csv') as csv_in:
	reader = csv.reader(csv_in)
	next(reader, None) #skip the header row

	for row in reader:
		name, gender, ratio = row[1:4]
		total = row[-1]
		output = [name, gender, ratio, total] #get the required values

		if int(ratio) <= 60:          #if <= 60, add to list of lists
			answer.append(output)

for i in range(5):
    align = 11 - len(answer[i][0])
    print(answer[i][0], answer[i][1].rjust(align), answer[i][2], answer[i][3])