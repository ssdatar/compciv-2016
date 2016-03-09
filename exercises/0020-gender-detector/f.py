from os.path import join, basename
from glob import glob

folder = 'tempdata'
files = glob(join(folder, '*.txt')) #find all txt files, get all file names

names_count = {}

for year in range (1950, 2015, 5):
    names_count = {}
    txtfile = join(folder, 'yob' + str(year) + '.txt')

    total = 0
    unique_count = {'F': 0, 'M': 0}
    year_unique = 0

    with open(txtfile, 'r') as fname:
        for line in fname:
            name, gender, babies = line.split(',')

            if not names_count.get(name):
                names_count[name] = {'M': 0, 'F': 0}

            names_count[name][gender] += int(babies)

    total_names= len(names_count.keys())
    total_babies = 0

    for i in names_count.values():
        temp = i['M'] + i['F']
        total_babies += temp

    print(year)
    print("Total:", round(total_babies / total_names), 'babies per name')

    for gd in ['M', 'F']:
        babyct = 0
        namect = 0
        for v in names_count.values():
            if v[gd] > 0:
                babyct += v[gd]
                namect += 1
        print("    %s:" % gd, round(babyct / namect), 'babies per name')