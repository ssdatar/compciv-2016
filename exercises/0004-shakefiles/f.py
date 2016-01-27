import os

name = os.path.join('tempdata', 'tragedies', 'romeoandjuliet')
rnj = open(name, 'r')
line_num = 0

for i in range(4766 - 5): 
    line_num += 1
    rnj.readline()

for line in rnj:
    line_num += 1
    the_line = str(line_num) + ": " + line.strip()
    print(the_line) 
    
rnj.close()