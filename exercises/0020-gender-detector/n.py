from os.path import join
import json
from zoofoo import detect_gender

input_names = ['Michael', 'Kelly', 'Kanye', 'THOR', 'casey', 'Arya','ZZZblahblah']
answer = []

for name in input_names:
  answer.append(detect_gender(name))
    
boys = 0
girls = 0
na = 0

boy_count = 0
girl_count = 0

for i in answer:
    print(i['name'],i['gender'], i['ratio'])
    if i['gender'] == 'F':
        girls += 1                      #count gender
        girl_count += int(i['females']) #count girls
        boy_count += int(i['males'])    #count boys
    
    elif i['gender'] == 'M':
        boys += 1                       #count gender                  
        girl_count += int(i['females']) #count girls
        boy_count += int(i['males'])    #count boys

    else:
        na += 1 #count na
print('Total:')
print('F:', girls, 'M:', boys, 'NA:', na)
print('females:', girl_count, 'males:', boy_count)