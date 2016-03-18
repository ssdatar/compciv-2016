from os.path import join, basename
import csv

folder = 'tempdata'
start_year = 1950
end_year = 2014

csv_headers = ['name', 'gender' , 'ratio' , 'females', 'males', 'total']
output_csv = join(folder, 'wrangledbabynames.csv') #name of output csv

years = list(range(start_year, end_year)) #make a list of all years
years.append(end_year)

namesdict = {}
names_list = []

#loop through list to open respective year file
for year in years:
    thefilename = join(folder, 'yob' + str(year) + '.txt')
    print('PARSING', thefilename)

    with open(thefilename, 'r') as txtfile:
        for line in txtfile:
            name, gender, babies = line.split(',') #assign them to vars

            if not namesdict.get(name):     #if name is not in the list, add it
                namesdict[name] = {'M': 0, 'F': 0}
            namesdict[name][gender] += int(babies) #add baby counts

for name, babiescount in namesdict.items():
    temp = {'name': name, 'females': babiescount['F'], 'males': babiescount['M']}
    temp['total'] = babiescount['M'] + babiescount['F']

    #If female number > male number, set gender as F, else M
    if temp['females'] >= temp['males']:
        temp['gender'] = 'F'
        temp['ratio'] = round(100 * temp['females'] / temp['total']) #calculate gender ratio
    else:
        temp['gender'] = 'M'
        temp['ratio'] = round(100 * temp['males'] / temp['total'])

    names_list.append(temp)

#Function to sort descending
def desc_sort(xdict):
    return (-xdict['total'], xdict['name'])

#sort descending
sorted_names = sorted(names_list, key=desc_sort)

#Write the output file
with open(output_csv, 'w') as csv_out:
    writer = csv.DictWriter(csv_out, fieldnames=csv_headers)
    writer.writeheader()

    #Write each row
    for row in sorted_names:
        writer.writerow(row)
