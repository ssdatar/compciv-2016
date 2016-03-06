from os.path import join
import csv

folder = 'tempdata'
thefile = join(folder, 'wrangledbabynames.csv')

input_names = ['Michael', 'Kelly', 'Kanye', 'THOR', 'casey', 'Arya','ZZZblahblah']
answer = []

for name in input_names:
    with open(thefile, 'r') as csv_in:
        for line in csv_in:
            temp = line.strip().split(',')
            result = {}

            #Check if name is there
            if name.lower() == temp[0].lower():
                #if yes, store results in result dict
                result = {'name': name, 
                          'gender': temp[1],
                          'ratio': temp[2],
                          'males': temp[4],
                          'females': temp[3],
                          'total': temp[5]}
                #append to master list and break out of loop
                answer.append(result)
                break
        
    #if nothing found, then append this to master list
    if not len(result):
        result = {'name': name, 
                      'gender': 'NA',
                      'ratio': None,
                      'males': None,
                      'females': None,
                      'total': 0}
        answer.append(result)

boys = 0
girls = 0
na = 0

boy_count = 0
girl_count = 0

for i in answer:
    print(i['name'],i['gender'], i['ratio'])
    if i['gender'] == 'F':
        girls += 1
        girl_count += int(i['females'])
        boy_count += int(i['males'])
    
    elif i['gender'] == 'M':
        boys += 1
        girl_count += int(i['females'])
        boy_count += int(i['males'])

    else:
        na += 1
print('Total:')
print('F:', girls, 'M:', boys, 'NA:', na)
print('females:', girl_count, 'males:', boy_count)